// 1Dproj_delphi.C
// ROOT macro to produce 1-D DeltaPhi projections for J/psi flow analysis
// in pPb collisions.
//
// This macro targets a single pT bin (ipt = 3, i.e. 4.5--6.0 GeV/c) and
// merges all 8 mass bins.  For each mass bin the 2-D (DeltaEta, DeltaPhi)
// histograms are projected onto the DeltaPhi axis with the requirement
// |DeltaEta| > 1.  The per-mass-bin contributions are then summed,
// weighted by the number of J/psi triggers, to obtain inclusive Signal,
// Mixing, and Correlation 1-D DeltaPhi distributions.  A Fourier
// decomposition C(DeltaPhi) = A * [1 + 2*V2*cos(2*DeltaPhi)] is fitted
// to the correlation.
//
// Input ROOT file directory structure (as produced by RaghuV0Ana.cc):
//   RAGHUV0/SigMix/hobs_sig_c2_jpsi_vs_ch_pT_<ipt>_mass_<imass>
//   RAGHUV0/SigMix/hobs_mix_c2_jpsi_vs_ch_pT_<ipt>_mass_<imass>
//   RAGHUV0/Ntrigg/hntrg_obs_jpsiks_pT_<ipt>_mass_<imass>
//
// Usage (from ROOT prompt or root -l -b -q):
//   root -l -b -q '1Dproj_delphi.C+("input.root","output_1Dproj_delphi.root")'
//   (The '+' triggers ACLiC compilation; otherwise load and call manually:)
//   root -l 1Dproj_delphi.C
//   root [0] OneDproj_delphi("input.root","output_1Dproj_delphi.root")
//
// pT bins:  [0.2,1.8,3.0,4.5,6.0,8.0,10.0] --> ipt=3 is [4.5,6.0] GeV/c
// Mass bins (edges): [2.5933,2.7023,2.8172,2.9331,3.0379,3.1367,3.2448,3.3676,3.4960]
//                    --> 8 bins, indices 0-7
// ============================================================================

#include "TFile.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TCanvas.h"
#include "TF1.h"
#include "TStyle.h"
#include "TLegend.h"
#include "TPaveText.h"
#include "TMath.h"
#include "TLatex.h"

#include <iostream>
#include <cmath>

// ---------------------------------------------------------------------------
// Helper: project 2-D histogram onto DeltaPhi axis applying |DeltaEta|>1 cut
// ---------------------------------------------------------------------------
TH1D* ProjectDeltaPhi(TH2D* h2d, const char* name, double etaCut = 1.0) {
    if (!h2d) return nullptr;

    TAxis* xax = h2d->GetXaxis(); // DeltaEta axis
    int binLo1 = 1;
    int binHi1 = xax->FindBin(-etaCut - 1e-9);     // Eta < -etaCut
    int binLo2 = xax->FindBin(+etaCut + 1e-9);     // Eta > +etaCut
    int binHi2 = xax->GetNbins();

    // Project the two |DeltaEta|>1 sideband slices and add them
    TH1D* h_neg = h2d->ProjectionY(Form("%s_neg", name), binLo1, binHi1, "e");
    TH1D* h_pos = h2d->ProjectionY(Form("%s_pos", name), binLo2, binHi2, "e");

    h_neg->Add(h_pos);
    h_neg->SetName(name);

    delete h_pos;
    return h_neg;
}

// ---------------------------------------------------------------------------
// Main macro function
// ---------------------------------------------------------------------------
void OneDproj_delphi(const char* inputFile  = "input.root",
                     const char* outputFile = "output_1Dproj_delphi.root") {

    // ---- style ---------------------------------------------------------------
    gStyle->SetOptStat(0);
    gStyle->SetOptTitle(1);
    gStyle->SetPadLeftMargin(0.15);
    gStyle->SetPadBottomMargin(0.12);
    gStyle->SetTitleFont(42,"xyz");
    gStyle->SetLabelFont(42,"xyz");
    gStyle->SetTitleSize(0.05,"xyz");
    gStyle->SetLabelSize(0.04,"xyz");

    // ---- pT and mass bin configuration ----------------------------------------
    const int ipt       = 3;                          // pT bin index [4.5--6.0 GeV/c]
    const int nmassbins = 8;                          // mass bin indices 0-7
    const double ptLow  = 4.5, ptHigh = 6.0;

    const double massEdge[9] = {2.5933, 2.7023, 2.8172, 2.9331,
                                 3.0379, 3.1367, 3.2448, 3.3676, 3.4960};

    // ---- open input file -------------------------------------------------------
    TFile* f = TFile::Open(inputFile, "READ");
    if (!f || f->IsZombie()) {
        std::cerr << "ERROR: cannot open " << inputFile << std::endl;
        return;
    }
    std::cout << "Opened input file: " << inputFile << std::endl;

    // ---- containers for merged 1-D histograms ---------------------------------
    TH1D* hSig_merged  = nullptr;
    TH1D* hMix_merged  = nullptr;
    double totalTriggers = 0.0;

    // ---- loop over mass bins, project and accumulate --------------------------
    std::cout << "\n========================================" << std::endl;
    std::cout << "Processing pT bin " << ipt
              << " [" << ptLow << "-" << ptHigh << " GeV/c]" << std::endl;
    std::cout << "========================================" << std::endl;

    for (int imass = 0; imass < nmassbins; ++imass) {
        std::cout << "\n  Mass bin " << imass << " ["
                  << massEdge[imass] << " - " << massEdge[imass+1] << " GeV/c^2]:"
                  << std::endl;

        // Load histograms
        TH2D* hsig = (TH2D*)f->Get(
            Form("RAGHUV0/SigMix/hobs_sig_c2_jpsi_vs_ch_pT_%d_mass_%d", ipt, imass));
        TH2D* hmix = (TH2D*)f->Get(
            Form("RAGHUV0/SigMix/hobs_mix_c2_jpsi_vs_ch_pT_%d_mass_%d", ipt, imass));
        TH1D* hntrg = (TH1D*)f->Get(
            Form("RAGHUV0/Ntrigg/hntrg_obs_jpsiks_pT_%d_mass_%d", ipt, imass));

        if (!hsig || !hmix || !hntrg) {
            std::cout << "    Warning: Could not load histograms for pT="
                      << ipt << " mass=" << imass << " -- skipping." << std::endl;
            continue;
        }

        // Trigger count is stored in bin 1 of the trigger histogram
        double nTrg = hntrg->GetBinContent(1);
        std::cout << "    Triggers = " << nTrg << std::endl;

        if (nTrg <= 0.0) {
            std::cout << "    Warning: zero triggers -- skipping mass bin." << std::endl;
            continue;
        }

        // Project 2D --> 1D DeltaPhi with |DeltaEta|>1
        TH1D* hSig_proj = ProjectDeltaPhi(
            hsig,
            Form("hSig_pT%d_mass%d_proj", ipt, imass), 1.0);
        TH1D* hMix_proj = ProjectDeltaPhi(
            hmix,
            Form("hMix_pT%d_mass%d_proj", ipt, imass), 1.0);

        if (!hSig_proj || !hMix_proj) {
            std::cout << "    Warning: projection failed -- skipping." << std::endl;
            continue;
        }

        // Normalise each projection by its own trigger count
        hSig_proj->Scale(1.0 / nTrg);
        hMix_proj->Scale(1.0 / nTrg);

        // Accumulate into merged histograms (weighted by trigger count)
        if (!hSig_merged) {
            hSig_merged = (TH1D*)hSig_proj->Clone("hSig_merged");
            hSig_merged->Scale(nTrg);
            hMix_merged = (TH1D*)hMix_proj->Clone("hMix_merged");
            hMix_merged->Scale(nTrg);
        } else {
            hSig_proj->Scale(nTrg);
            hMix_proj->Scale(nTrg);
            hSig_merged->Add(hSig_proj);
            hMix_merged->Add(hMix_proj);
        }
        totalTriggers += nTrg;

        delete hSig_proj;
        delete hMix_proj;
    }

    if (!hSig_merged || !hMix_merged || totalTriggers <= 0.0) {
        std::cerr << "ERROR: No valid mass bins found. Check histogram names." << std::endl;
        f->Close();
        return;
    }

    // Divide by total triggers to get the final per-trigger yields
    hSig_merged->Scale(1.0 / totalTriggers);
    hMix_merged->Scale(1.0 / totalTriggers);

    std::cout << "\n  Total triggers used = " << totalTriggers << std::endl;

    // ---- Compute correlation C(DeltaPhi) = Sig / Mix -------------------------
    // Normalise the mixing histogram so that its average bin content equals 1.
    // This makes C(DeltaPhi) dimensionless and centred around ~1.
    double mixIntegral = hMix_merged->Integral();
    int    mixNbins    = hMix_merged->GetNbinsX();
    if (mixIntegral > 0.0 && mixNbins > 0)
        hMix_merged->Scale(static_cast<double>(mixNbins) / mixIntegral);

    // Divide bin by bin; propagate errors independently (not binomial)
    TH1D* hCorr = (TH1D*)hSig_merged->Clone("hCorr_merged");
    hCorr->SetTitle(Form("Correlation C(#Delta#phi) pT [%.1f-%.1f] |#Delta#eta|>1 (all mass bins);#Delta#phi (rad);C(#Delta#phi)", ptLow, ptHigh));
    hCorr->Divide(hMix_merged);   // hCorr = hSig_merged / hMix_merged

    // ---- Fourier fit: C(DeltaPhi) = A * [1 + 2*V2*cos(2*DeltaPhi)] ----------
    double phiLow = hCorr->GetXaxis()->GetXmin();
    double phiHigh = hCorr->GetXaxis()->GetXmax();

    TF1* fitFunc = new TF1("fitFourier",
                           "[0]*(1 + 2*[1]*cos(2*x))",
                           phiLow, phiHigh);
    fitFunc->SetParName(0, "A");
    fitFunc->SetParName(1, "V_{2}^{eff}");
    fitFunc->SetParameter(0, 1.0);                 // initial value for A (~1 for normalised corr.)
    fitFunc->SetParameter(1, 0.05);                // small initial v2
    fitFunc->SetLineColor(kRed+1);
    fitFunc->SetLineWidth(2);

    std::cout << "\n  Fitting C(DeltaPhi) with A*(1+2*V2*cos(2*DeltaPhi)) ..." << std::endl;
    hCorr->Fit("fitFourier", "RNQ");
    hCorr->Fit("fitFourier", "RQ");   // second pass to converge

    double V2eff     = fitFunc->GetParameter(1);
    double V2eff_err = fitFunc->GetParError(1);
    double A_fit     = fitFunc->GetParameter(0);
    double chi2ndf   = (fitFunc->GetNDF() > 0) ?
                       fitFunc->GetChisquare() / fitFunc->GetNDF() : 0.0;

    std::cout << "  Fit result: V2_eff = " << V2eff
              << " +/- " << V2eff_err
              << "  (chi2/ndf = " << chi2ndf << ")" << std::endl;

    // ---- Cosmetics -----------------------------------------------------------
    hSig_merged->SetTitle(
        Form("Signal #Delta#phi projection  pT [%.1f-%.1f] |#Delta#eta|>1;#Delta#phi (rad);dN/d#Delta#phi (per trigger)", ptLow, ptHigh));
    hSig_merged->SetLineColor(kBlue+1);
    hSig_merged->SetMarkerColor(kBlue+1);
    hSig_merged->SetMarkerStyle(20);
    hSig_merged->SetMarkerSize(0.8);

    hMix_merged->SetTitle(
        Form("Mixing #Delta#phi projection  pT [%.1f-%.1f] |#Delta#eta|>1;#Delta#phi (rad);dN/d#Delta#phi (per trigger)", ptLow, ptHigh));
    hMix_merged->SetLineColor(kGreen+2);
    hMix_merged->SetMarkerColor(kGreen+2);
    hMix_merged->SetMarkerStyle(21);
    hMix_merged->SetMarkerSize(0.8);

    hCorr->SetLineColor(kBlack);
    hCorr->SetMarkerColor(kBlack);
    hCorr->SetMarkerStyle(20);
    hCorr->SetMarkerSize(0.8);

    // ---- Canvases ------------------------------------------------------------
    // Canvas 1: Signal
    TCanvas* cSig = new TCanvas("cSig",
        Form("Signal DeltaPhi pT[%.1f-%.1f]", ptLow, ptHigh), 700, 600);
    cSig->SetLeftMargin(0.15);
    hSig_merged->Draw("E1");

    // Canvas 2: Mixing
    TCanvas* cMix = new TCanvas("cMix",
        Form("Mixing DeltaPhi pT[%.1f-%.1f]", ptLow, ptHigh), 700, 600);
    cMix->SetLeftMargin(0.15);
    hMix_merged->Draw("E1");

    // Canvas 3: Correlation + fit
    TCanvas* cCorr = new TCanvas("cCorr",
        Form("Correlation DeltaPhi pT[%.1f-%.1f]", ptLow, ptHigh), 700, 600);
    cCorr->SetLeftMargin(0.15);
    hCorr->Draw("E1");
    fitFunc->Draw("same");

    // Annotation box
    TPaveText* pt = new TPaveText(0.55, 0.65, 0.90, 0.88, "NDC");
    pt->SetFillColor(0);
    pt->SetBorderSize(1);
    pt->SetTextFont(42);
    pt->SetTextSize(0.035);
    pt->AddText("pPb  #sqrt{s_{NN}} = 8.16 TeV");
    pt->AddText(Form("%.1f < p_{T}^{J/#psi} < %.1f GeV/c", ptLow, ptHigh));
    pt->AddText("|#Delta#eta| > 1, all mass bins");
    pt->AddText(Form("V_{2}^{eff} = %.4f #pm %.4f", V2eff, V2eff_err));
    pt->AddText(Form("#chi^{2}/ndf = %.2f", chi2ndf));
    pt->Draw();

    TLegend* leg = new TLegend(0.18, 0.70, 0.50, 0.88);
    leg->SetFillColor(0);
    leg->SetBorderSize(0);
    leg->SetTextFont(42);
    leg->SetTextSize(0.035);
    leg->AddEntry(hCorr,   "C(#Delta#phi) = Sig/Mix", "lep");
    leg->AddEntry(fitFunc, "A[1+2V_{2}cos(2#Delta#phi)]", "l");
    leg->Draw();

    // ---- Save to output ROOT file --------------------------------------------
    TFile* fout = TFile::Open(outputFile, "RECREATE");
    if (!fout || fout->IsZombie()) {
        std::cerr << "ERROR: cannot create output file " << outputFile << std::endl;
        f->Close();
        return;
    }

    TDirectory* dSig  = fout->mkdir("Signal");
    TDirectory* dMix  = fout->mkdir("Mixing");
    TDirectory* dCorr = fout->mkdir("Correlation");

    dSig->cd();
    hSig_merged->SetName(Form("hSig_dphi_pT%d_allMass", ipt));
    hSig_merged->Write();
    cSig->Write("cSig");

    dMix->cd();
    hMix_merged->SetName(Form("hMix_dphi_pT%d_allMass", ipt));
    hMix_merged->Write();
    cMix->Write("cMix");

    dCorr->cd();
    hCorr->SetName(Form("hCorr_dphi_pT%d_allMass", ipt));
    hCorr->Write();
    fitFunc->Write("fitFourier");
    cCorr->Write("cCorr");

    fout->cd();
    // Summary histogram with fit result
    TH1D* hV2summary = new TH1D("hV2eff_summary",
        Form("V_{2}^{eff}  pT [%.1f-%.1f];mass bin;V_{2}^{eff}", ptLow, ptHigh),
        1, 0.5, 1.5);
    hV2summary->SetBinContent(1, V2eff);
    hV2summary->SetBinError(1, V2eff_err);
    hV2summary->Write();

    fout->Close();
    f->Close();

    std::cout << "\nOutput saved to: " << outputFile << std::endl;
    std::cout << "Directories in output file: Signal, Mixing, Correlation" << std::endl;
}

// The ROOT macro entry point when loading via `root -l 1Dproj_delphi.C`.
// Since C++ identifiers cannot start with a digit, the file-level entry point
// is named OneDproj_delphi().  Call it directly after loading:
//   root -l 1Dproj_delphi.C
//   root [0] OneDproj_delphi("in.root","out.root")
