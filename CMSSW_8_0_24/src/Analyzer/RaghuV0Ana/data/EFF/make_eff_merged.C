#include <TFile.h>
#include <TH3D.h>
#include <TDirectory.h>
#include <TAxis.h>
#include <TString.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <stdexcept>

using std::cout;
using std::endl;
using std::string;
using std::vector;

#include <iomanip>

// Print one (ix,iy) line across all z-bins of a TH3
static void printZProfile(const TH3D* h, int ix, int iy, const char* tag) {
  if (!h) { std::cout << "[printZProfile] null hist for " << tag << "\n"; return; }
  auto* zax = h->GetZaxis();
  std::cout << "\n== " << tag
            << "  (ix=" << ix << ", iy=" << iy << ") ==\n";
  for (int iz=1; iz<=zax->GetNbins(); ++iz) {
    double low  = zax->GetBinLowEdge(iz);
    double high = zax->GetBinUpEdge(iz);
    double c    = h->GetBinContent(ix,iy,iz);
    double e    = h->GetBinError(ix,iy,iz);
    std::cout << "  z" << std::setw(2) << iz
              << " [" << low << "," << high << "]: "
              << "C=" << c << ", E=" << e << "\n";
  }
}

// Convenience: choose (ix,iy) by physics values (pT, η)
static std::pair<int,int> binByValues(const TH3D* h, double pt, double eta) {
  int ix = h->GetXaxis()->FindBin(pt);
  int iy = h->GetYaxis()->FindBin(eta);
  return {ix, iy};
}

// Quick numeric check that merged z3 equals (old z3 + old z4) with errors in quadrature
static void checkMergeAt(const TH3D* hIn, const TH3D* hMerged, int ix, int iy, const char* tag) {
  if (!hIn || !hMerged) return;
  if (hIn->GetZaxis()->GetNbins() < 4 || hMerged->GetZaxis()->GetNbins() < 3) return;

  double c3  = hIn->GetBinContent(ix,iy,3);
  double e3  = hIn->GetBinError  (ix,iy,3);
  double c4  = hIn->GetBinContent(ix,iy,4);
  double e4  = hIn->GetBinError  (ix,iy,4);
  double sum = c3 + c4;
  double esum= std::hypot(e3, e4);

  double cm  = hMerged->GetBinContent(ix,iy,3);
  double em  = hMerged->GetBinError  (ix,iy,3);

  std::cout << "\n-- Merge check (" << tag << ", ix="<<ix<<", iy="<<iy<<") --\n"
            << "  old z3+z4: C=" << sum << "  E=" << esum << "\n"
            << "  new z3  : C=" << cm  << "  E=" << em   << "\n";
}


// Helper: extract bin edges from a TAxis into a std::vector<double>
static vector<double> axisEdges(const TAxis* ax) {
  int nb = ax->GetNbins();
  vector<double> edges; edges.reserve(nb+1);
  for (int i=1;i<=nb;i++) edges.push_back(ax->GetBinLowEdge(i));
  edges.push_back(ax->GetBinUpEdge(nb));
  return edges;
}

// Create an empty TH3D with given X,Y edges copied from src and new Z edges
static TH3D* makeEmptyWithNewZ(const TH3D* src,
                               const vector<double>& zEdgesNew,
                               const string& name,
                               const string& title)
{
  // X, Y from src
  vector<double> xEdges = axisEdges(src->GetXaxis());
  vector<double> yEdges = axisEdges(src->GetYaxis());

  auto* h = new TH3D(name.c_str(), title.c_str(),
                     (int)xEdges.size()-1, xEdges.data(),
                     (int)yEdges.size()-1, yEdges.data(),
                     (int)zEdgesNew.size()-1, zEdgesNew.data());
  h->Sumw2(); // ensure errors are stored
  return h;
}

// Merge centrality z-bins: [0,20],[20,60],[60,100],[100,160] -> [0,20],[20,60],[60,160]
static TH3D* mergeCentrality3Z(const TH3D* hIn,
                               const string& outName,
                               const string& outTitle)
{
  if (!hIn) throw std::runtime_error("mergeCentrality3Z: input histogram is null");

  // Build new Z edges for 3 bins as specified
  vector<double> zEdgesNew = {0.0, 20.0, 60.0, 100.0, 160.0};

  // Sanity on original Z edges (we won't hard-fail if different, but we map by range)
  vector<double> zEdgesOld = axisEdges(hIn->GetZaxis());
  if (zEdgesOld.size()-1 < 3) {
    throw std::runtime_error("Expected at least 3 z-bins in the input histogram.");
  }

  TH3D* hOut = makeEmptyWithNewZ(hIn, zEdgesNew, outName, outTitle);

  const int nx = hIn->GetXaxis()->GetNbins();
  const int ny = hIn->GetYaxis()->GetNbins();
  const int nz = hIn->GetZaxis()->GetNbins();

  // Triple loop with explicit bin-index mapping for Z:
  // if z-bin is within [0,20] -> new z=1
  // within (20,60] -> new z=2
  // everything >=60 -> new z=3
  for (int ix=1; ix<=nx; ++ix) {
    for (int iy=1; iy<=ny; ++iy) {
      for (int iz=1; iz<=nz; ++iz) {
        double content = hIn->GetBinContent(ix,iy,iz);
        double err     = hIn->GetBinError(ix,iy,iz);
        if (content==0.0 && err==0.0) continue;

        double zLow  = hIn->GetZaxis()->GetBinLowEdge(iz);
        double zHigh = hIn->GetZaxis()->GetBinUpEdge(iz);

	//int izNew = 1;
	
        int izNew = 4; // default to merged-high bin
        if (zHigh <= 20.0)        izNew = 1;
        else if (zHigh <= 60.0)   izNew = 2;
	else if (zHigh <= 100.0)   izNew = 3;
        else                      izNew = 4;
	
        // Accumulate contents and errors in quadrature
        double oldC = hOut->GetBinContent(ix,iy,izNew);
        double oldE = hOut->GetBinError(ix,iy,izNew);
        double newC = oldC + content;
        double newE = std::sqrt(oldE*oldE + err*err);

        hOut->SetBinContent(ix,iy,izNew, newC);
        hOut->SetBinError  (ix,iy,izNew, newE);
      }
    }
  }

  return hOut;
}

// Safe histogram fetch with directory and name
template<typename H>
static H* fetchHist(TDirectory* dir, const char* name) {
  if (!dir) return nullptr;
  TObject* obj = dir->Get(name);
  if (!obj) return nullptr;
  return dynamic_cast<H*>(obj);
}

// Build efficiency = (eff_eta)/(Gen_eta) 
static TH3D* makeEfficiency(const TH3D* hRecoMerged, const TH3D* hGenMerged,
                            const string& name, const string& title)
{
  if (!hRecoMerged || !hGenMerged) throw std::runtime_error("Null input to makeEfficiency");
  TH3D* hEff = (TH3D*)hRecoMerged->Clone(name.c_str());
  hEff->SetTitle(title.c_str());
  hEff->Sumw2();
  hEff->Divide(hRecoMerged, hGenMerged, 1.0, 1.0);
  return hEff;
}

void make_eff_merged(const char* infile="eff_dca1_dauFinal.root",
                     const char* outfile="Eff_OO_2025_lm_dr0p03_dpt0p05_ks_dr0p03_dpt0p04_DCA1_cos999_dr0p3_ef.root")
{
  // Open input
  TFile fin(infile, "READ");
  if (fin.IsZombie()) {
    throw std::runtime_error(TString::Format("Failed to open input file: %s", infile).Data());
  }

  // Folders
  TDirectory* dKs = fin.GetDirectory("RAGHUV0/GenReco");
  TDirectory* dLm = fin.GetDirectory("RAGHUV0/GenReco_lm");
  if (!dKs) { throw std::runtime_error("Folder 'GenReco' not found"); }
  if (!dLm) { throw std::runtime_error("Folder 'GenReco_lm' not found"); }

  // === Ks: get 3D histograms ===
  TH3D* ksGen3D = fetchHist<TH3D>(dKs, "Gen_rap");
  TH3D* ksRec3D = fetchHist<TH3D>(dKs, "eff_rap");
 
  if (!ksGen3D) { throw std::runtime_error("In GenReco: 'Gen_rap' (TH3D) not found"); }
  if (!ksRec3D) { throw std::runtime_error("In GenReco: 'eff_rap' (TH3D) not found"); }

  TH3D* ksfake3D = fetchHist<TH3D>(dKs, "fake_rap");
  TH3D* ksReco3D = fetchHist<TH3D>(dKs, "Reco_rap");
 
  if (!ksfake3D) { throw std::runtime_error("In GenReco: 'fake_rap' (TH3D) not found"); }
  if (!ksReco3D) { throw std::runtime_error("In GenReco: 'Reco_rap' (TH3D) not found"); }

 
  // === Lambda: get 3D histograms ===
  
  TH3D* lmGen3D = fetchHist<TH3D>(dLm, "Gen_rap_lm");
  TH3D* lmRec3D = fetchHist<TH3D>(dLm, "eff_rap_lm");
  if (!lmGen3D) { throw std::runtime_error("In GenReco_lm: 'Gen_rap_lm' (TH3D) not found"); }
  if (!lmRec3D) { throw std::runtime_error("In GenReco_lm: 'eff_rap_lm' (TH3D) not found"); }

  TH3D* lmfake3D = fetchHist<TH3D>(dLm, "fake_rap_lm");
  TH3D* lmReco3D = fetchHist<TH3D>(dLm, "Reco_rap_lm");
  if (!lmfake3D) { throw std::runtime_error("In GenReco_lm: 'fake_rap_lm' (TH3D) not found"); }
  if (!lmReco3D) { throw std::runtime_error("In GenReco_lm: 'Reco_rap_lm' (TH3D) not found"); }
  
  // --- Merge centrality bins for Ks ---
  
  TH3D* ksGen3D_m = mergeCentrality3Z(ksGen3D, "Gen_rap_Ks_mergedZ",
                                      "Ks Gen; p_{T} [GeV]; #eta; centrality");
  TH3D* ksRec3D_m = mergeCentrality3Z(ksRec3D, "eff_rap_Ks_mergedZ",
                                      "Ks Reco/Eff; p_{T} [GeV]; #eta; centrality");

  TH3D* ksfake3D_m = mergeCentrality3Z(ksfake3D, "fake_rap_Ks_mergedZ",
				      "Ks fake; p_{T} [GeV]; #eta; centrality");

  TH3D* ksReco3D_m = mergeCentrality3Z(ksReco3D, "Reco_rap_Ks_mergedZ",
                                      "Ks Reco/Eff; p_{T} [GeV]; #eta; centrality");
				      
  // --- Make efficiency for Ks ---
  TH3D* ksEff3D   = makeEfficiency(ksRec3D_m, ksGen3D_m, "hEff_3D_ks",
                                   "Ks efficiency = eff_{eta} / Gen_{eta}");
  
  TH3D* ksFake3D   = makeEfficiency(ksfake3D_m, ksReco3D_m, "hfake_3D_ks",
                                   "Ks fake = fake_{eta} / Reco_{eta} ");
  
  
  
 
  
  // --- Merge centrality bins for Lambda ---
  TH3D* lmGen3D_m = mergeCentrality3Z(lmGen3D, "Gen_rap_Lm_mergedZ",
                                      "Lambda Gen; p_{T} [GeV]; #eta; centrality");
  TH3D* lmRec3D_m = mergeCentrality3Z(lmRec3D, "eff_rap_Lm_mergedZ",
                                      "Lambda Reco/Eff; p_{T} [GeV]; #eta; centrality");

  TH3D* lmfake3D_m = mergeCentrality3Z(lmfake3D, "fake_rap_Lm_mergedZ",
				       "Lm fake; p_{T} [GeV]; #eta; centrality");

  TH3D* lmReco3D_m = mergeCentrality3Z(lmReco3D, "Reco_rap_Lm_mergedZ",
				       "Lm Reco/Eff; p_{T} [GeV]; #eta; centrality");

  // --- Make efficiency for Lambda ---
  TH3D* lmEff3D   = makeEfficiency(lmRec3D_m, lmGen3D_m, "hEff_3D_lm",
                                   "Lambda efficiency = eff_{eta} / Gen_{eta}");

  TH3D* lmFake3D   = makeEfficiency(lmfake3D_m, lmReco3D_m, "hfake_3D_lm",
				     "Lm fake = fake_{eta} / Reco_{eta} ");
  
  // --- Merge centrality bins for Lambda ---
 
  // Choose a (pT, rap) point to inspect
  auto [ixKs, iyKs] = binByValues(ksGen3D, 1.0, 0.0);   // pT=1.0 GeV, eta=0
  printZProfile(ksGen3D,   ixKs, iyKs, "Ks Gen (INPUT)");
  printZProfile(ksGen3D_m, ixKs, iyKs, "Ks Gen (MERGED)");
  //checkMergeAt(ksGen3D, ksGen3D_m, ixKs, iyKs, "Ks Gen");

  printZProfile(ksRec3D,   ixKs, iyKs, "Ks EffNum (INPUT)");
  printZProfile(ksRec3D_m, ixKs, iyKs, "Ks EffNum (MERGED)");
  // checkMergeAt(ksRec3D, ksRec3D_m, ixKs, iyKs, "Ks EffNum");

 

  // Save outputs
  TFile fout(outfile, "RECREATE");
  if (fout.IsZombie()) {
    throw std::runtime_error(TString::Format("Failed to create output file: %s", outfile).Data());
  }

  // Organize output: keep simple top-level objects
  // ksGen3D_m->Write();
  //ksRec3D_m->Write();
  ksEff3D->Write();

  //ksfake3D_m->Write();
  //ksReco3D_m->Write();
  //ksFake3D->Write();

  //lmGen3D_m->Write();
  //lmRec3D_m->Write();
  lmEff3D->Write();

  //lmfake3D_m->Write();
  //lmReco3D_m->Write();
  //lmFake3D->Write();

  fout.Close();
  fin.Close();

  cout << "Wrote merged and efficiency histograms to: " << outfile << endl;
}

