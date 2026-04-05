// This code is for two cent bins 0-40% and 60%-80%
// removed SingleMuon selectiomn
//  recoVtx removed
// abs eta and phi taken
//1 march 2026
// Naming changed for Jpsi
//3rd March

// CMSSW include files
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/CaloTowers/interface/CaloTowerCollection.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/PatCandidates/interface/CompositeCandidate.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/RecoCandidate/interface/RecoChargedCandidate.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "FWCore/Utilities/interface/typelookup.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
// user include files
#include "Analyzer/RaghuV0Ana/interface/RaghuV0Ana.h"
#define M_PI 3.14159265358979323846

RaghuV0Ana::RaghuV0Ana(const edm::ParameterSet& iConfig) :

  trackTags_(consumes< edm::View< pat::PackedCandidate> >(iConfig.getParameter<edm::InputTag>("tracksSrc"))),
  packedCandToken_(consumes<pat::PackedCandidateCollection>(iConfig.getParameter<edm::InputTag>("packedCandidates"))),
  pc2trackAssocToken_(consumes<edm::Association<reco::TrackCollection>>(iConfig.getParameter<edm::InputTag>("trackAssociation"))),
  recoTracksToken_(consumes<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("recoTracksSrc"))),
  vtxTags_(consumes<std::vector<reco::Vertex>>(iConfig.getParameter<edm::InputTag>("vertexSrc"))),
  V0Src_jpsiSel_(consumes<pat::CompositeCandidateCollection>(iConfig.getParameter<edm::InputTag>("V0Src_jpsi"))),
  dbCent_(consumes<int>(iConfig.getUntrackedParameter<edm::InputTag>("dbCent"))),
  //=========================================================================================================
  pTmin_trg_(iConfig.getUntrackedParameter< std::vector< double > >("pTminTrk_trg")),
  pTmax_trg_(iConfig.getUntrackedParameter< std::vector< double > >("pTmaxTrk_trg")),
  pTmin_ass_(iConfig.getUntrackedParameter< std::vector< double > >("pTminTrk_ass")),
  pTmax_ass_(iConfig.getUntrackedParameter< std::vector< double > >("pTmaxTrk_ass")),
  pTmin_trg_jpsiSel_(iConfig.getUntrackedParameter< double >("pTminTrk_trg_jpsi")),
  pTmax_trg_jpsiSel_(iConfig.getUntrackedParameter< double >("pTmaxTrk_trg_jpsi")),
  pTmin_ass_jpsiSel_(iConfig.getUntrackedParameter< double >("pTminTrk_ass_jpsi")),
  pTmax_ass_jpsiSel_(iConfig.getUntrackedParameter< double >("pTmaxTrk_ass_jpsi")),

  bkgFactor(iConfig.getUntrackedParameter<unsigned int>("bkgFactor")),
  zminVtx_(iConfig.getUntrackedParameter<double>("zminVtx")),
  zmaxVtx_(iConfig.getUntrackedParameter<double>("zmaxVtx")),
  //==========================================================================================================
  dauNhitsmin_(iConfig.getUntrackedParameter<int>("dauNhitsMin")),
  mis_ph_range_(iConfig.getUntrackedParameter<double>("mis_ph_range")),
  dauPixelhitsmin_(iConfig.getUntrackedParameter<int>("dauPixelhitsMin")),
  
  pTmin_(iConfig.getUntrackedParameter<double>("ptMin")),
  pTmax_(iConfig.getUntrackedParameter<double>("ptMax")),
  pTmin_ch_(iConfig.getUntrackedParameter<double>("ptMin_ch")),
  pTmax_ch_(iConfig.getUntrackedParameter<double>("ptMax_ch")),
  Etamin_(iConfig.getUntrackedParameter<double>("EtaMin")),
  Etamax_(iConfig.getUntrackedParameter<double>("EtaMax")),
  Etamin_j(iConfig.getUntrackedParameter<double>("EtaMinJ")),
  Etamax_j(iConfig.getUntrackedParameter<double>("EtaMaxJ")),
  Rapmin_1(iConfig.getUntrackedParameter<double>("RapMin1")),
  Rapmax_1(iConfig.getUntrackedParameter<double>("RapMax1")),
  // mass window:
  mSigLow_(iConfig.getUntrackedParameter<double>("mSigLow")),
  mSigHigh_(iConfig.getUntrackedParameter<double>("mSigHigh")),
  
  mSB1Low_(iConfig.getUntrackedParameter<double>("mSB1Low")),
  mSB1High_(iConfig.getUntrackedParameter<double>("mSB1High")),
  
  mSB2Low_(iConfig.getUntrackedParameter<double>("mSB2Low")),
  mSB2High_(iConfig.getUntrackedParameter<double>("mSB2High")),
  //
  Massmin_jpsiSel_(iConfig.getUntrackedParameter<double>("MassMin_jpsi")),
  Massmax_jpsiSel_(iConfig.getUntrackedParameter<double>("MassMax_jpsi")),
  Chi2max_(iConfig.getUntrackedParameter<double>("Chi2Max")),
  ThetaXYZmin_(iConfig.getUntrackedParameter<double>("ThetaXYZMin")),
  //ThetaXYZmax_(iConfig.getUntrackedParameter<double>("ThetaXYZMax",999.)),
  DecaySigXYZmin_(iConfig.getUntrackedParameter<double>("DecayXYZMin")),
  //DecaySigXYZmax_(iConfig.getUntrackedParameter<double>("DecayXYZMax",9999999.)),
  DCAmax_(iConfig.getUntrackedParameter<double>("DCAMax")),
  
  //dau_costheta_(iConfig.getUntrackedParameter<double>("dau_costheta")),
  //dau_delpt_(iConfig.getUntrackedParameter<double>("dau_delpt")),
  
  dau_etaphi_(iConfig.getUntrackedParameter<double>("dau_etaphi")),
  del_R_(iConfig.getUntrackedParameter<double>("del_R")),
  binTable(iConfig.getUntrackedParameter< std::vector<double>>("binTable")),
  npt_binedge(iConfig.getUntrackedParameter< std::vector<double>>("npt_binedge")),
  nmass_jpsiSel_binedge(iConfig.getUntrackedParameter< std::vector<double>>("nmass_jpsi_binedge"))
{

  isMC_ = iConfig.getUntrackedParameter<bool>("isMC", false);
  if (isMC_) {
    tracks_ = consumes<reco::GenParticleCollection>(iConfig.getParameter<edm::InputTag>("tracks"));
  }
  evt_ = new DiHadronCorrelationEvt(pTmin_trg_.size(), pTmin_ass_.size());  
  usesResource("TFileService");
  TH1::SetDefaultSumw2();
  TH2::SetDefaultSumw2();
  //TH3::SetDefaultSumw2();
    
    edm::Service<TFileService> fs;
    TFileDirectory fGlobalHist  = fs->mkdir("QA_plots");
    hzvtx_          = fGlobalHist.make<TH1D>("hzvtx", "", 400 , -20, 20);
    hV0pT_jpsiSel_          = fGlobalHist.make<TH1D>("hV0pT_jpsi", "", 100 , 0.0, 10.0);
    hV0eta_jpsiSel_          = fGlobalHist.make<TH1D>("hV0eta_jpsi", "", 160 , Etamin_j, Etamax_j);
    hV0phi_jpsiSel_          = fGlobalHist.make<TH1D>("hV0phi_jpsi", "", 60 , -TMath::Pi(),  TMath::Pi());
    hV0rapidity_jpsiSel_     = fGlobalHist.make<TH1D>("hV0rapidity_jpsi", "", 100 , -2.5, 2.5);
    hpT_eta_          = fGlobalHist.make<TH2D>("hpT_eta", "", 160 , Etamin_j, Etamax_j,50 , 0.0, 10.0);
    hpT_rap_          = fGlobalHist.make<TH2D>("hpT_rap", "", 60 , -2.5, 2.5,50 , 0.0, 10.0);
    hbin_            = fGlobalHist.make<TH1I>("hbin", "", 200 , 0, 400);
    //hcent_bin        = fGlobalHist.make<TH1F>("hcent_bin distribution", "", 16, 0, 80);
    //hchi2_            = fGlobalHist.make<TH1F>("hchi2", "", 100, 0., 1.);
    // Histograms for ch_Hadrons
    hch_pt_       = fGlobalHist.make<TH1D>("hch_pt", "", 100, 0.3, 3.0);
    hch_eta_      = fGlobalHist.make<TH1D>("hch_eta", "", 96, -2.4, 2.4);
    hch_phi_      = fGlobalHist.make<TH1D>("hch_phi", "", 64, -TMath::Pi(), TMath::Pi());
    //hch_pt_eta_   = fGlobalHist.make<TH2D>("hch_pt_eta", "", 120, -2.4, 2.4, 100, 0.3, 3.0);
    //before selection histograms:
    hpT_jpsi_          = fGlobalHist.make<TH1D>("hpT_jpsi_wo", "", 100 , 0.0, 10.0);
    heta_jpsi_          = fGlobalHist.make<TH1D>("heta_jpsi_wo", "", 160 , Etamin_j, Etamax_j);
    hphi_jpsi_          = fGlobalHist.make<TH1D>("hphi_jpsi_wo", "", 60 , -TMath::Pi(),  TMath::Pi());
    hrapidity_jpsi_     = fGlobalHist.make<TH1D>("hrapidity_jpsi_wo", "", 100 , -2.5, 2.5);
    hvtxProv_jpsi_      = fGlobalHist.make<TH1D>("hvtxProv_wo_jpsi", "", 110 , -0.1, 1.0);
    hvtxProv_jpsiSel_   = fGlobalHist.make<TH1D>("hvtxProv_jpsi_Sel", "", 110 , -0.1, 1.0);
    //hpT_eta1_          = fGlobalHist.make<TH2D>("hpT_eta_wo_sel", "", 160 , Etamin_j, Etamax_j,50 , 0.0, 10.0);
    hpT_rap1_          = fGlobalHist.make<TH2D>("hpT_rap_wo_sel", "", 60 , -2.5, 2.5,50 , 0.0, 10.0);
    hpT_eta_mu          = fGlobalHist.make<TH2D>("hpT_eta_mu", "", 160 , -2.5, 2.5,200 , 0.0, 10.0);
    double nBins_deta = 32;
    double nBins_dphi = 32;

    double etaW = (4.0*2.4)/nBins_deta;
    double phiW = (2.0*TMath::Pi())/nBins_dphi;
    
    double eta_upedge = (2.0*2.4)+(etaW/2.0);
    double eta_lowedge = -(2.0*2.4)-(etaW/2.0);
    
    double phi_upedge = ((3.0*TMath::Pi()) - phiW)/2.0;
    double phi_lowedge = -(TMath::Pi() - phiW)/2.0;
    
    TFileDirectory fV0Hist  = fs->mkdir("V0_plots");
    hV0mass_wocut_jpsiSel_          = fV0Hist.make<TH1D>("hV0mass_jpsi", "", 90 ,2.6, 3.5);
    hmass_jpsi_          = fV0Hist.make<TH1D>("hV0mass_jpsi_woSel", "", 90 ,2.6, 3.5);
    nptbins = npt_binedge.size() - 1;
    // pPb mode: use only one inclusive multiplicity class (no centrality binning).
    //ncentbin_binedge = {0.0, 1.0};
    //ncentbins = 1;
    nmassbins_jpsiSel = nmass_jpsiSel_binedge.size() - 1;

    //jpsi_pT.resize(nptbins);
    hV0pTbin = fV0Hist.make<TH1D>("hV0pTbin", "", nptbins, &npt_binedge[0]);
    //hV0centbin = fV0Hist.make<TH1D>("hV0centbin", "", ncentbins, &ncentbin_binedge[0]);
    hV0massbin_jpsiSel = fV0Hist.make<TH1D>("hV0massbin_jpsi", "", nmassbins_jpsiSel, &nmass_jpsiSel_binedge[0]);

    TFileDirectory jpsipTHist = fs->mkdir("Jpsi_pT");
    //jpsi_pT.resize(ncentbins);
    //for (unsigned int ict = 0; ict < ncentbins; ++ict) {
      jpsi_pT.resize(nptbins);
      for (unsigned int ipt = 0; ipt < nptbins; ++ipt) {
	jpsi_pT[ipt] = jpsipTHist.make<TH1D>(Form("jpsi_pT_%d", ipt), Form("%1.1f < p_{T} < %1.1f GeV/c", npt_binedge[ipt], npt_binedge[ipt+1]), 90, 2.6, 3.5);
      }
      //}
    
    TFileDirectory ntrgHist = fs->mkdir("Ntrigg");
    //hevent_V0_CH.resize(ncentbins);
    //hntrg_ch.resize(ncentbins);
    //hntrg_ch_assoc.resize(ncentbins);
    //hntrg_obs_jpsiks.resize(ncentbins);
    //hntrg_bkg_jpsiks.resize(ncentbins);
    //for (unsigned int ict = 0; ict < ncentbins; ++ict) {
    hntrg_obs_jpsiks.resize(nptbins);
      //hntrg_bkg_jpsiks[ict].resize(nptbins);
      
      for (unsigned int ipt = 0; ipt < nptbins; ++ipt) {
	hntrg_obs_jpsiks[ipt].resize(nmassbins_jpsiSel);
	for (unsigned int imass = 0; imass < nmassbins_jpsiSel; ++imass) {
	  hntrg_obs_jpsiks[ipt][imass] = ntrgHist.make<TH1D>(Form("hntrg_obs_jpsiks_pT_%d_mass_%d", ipt, imass), Form("%1.1f < p_{T} < %1.1f GeV/c & mass bin %d", npt_binedge[ipt], npt_binedge[ipt+1], imass), 2 ,0., 2.);
	}      
      }
      
      hevent_V0_CH = ntrgHist.make<TH1D>("hevent_V0_CH", "J/#psi, K^{0}, Charged-hadrons", 3 ,0., 3.);
      hntrg_ch = ntrgHist.make<TH1D>("hntrg_ch", "0.3 < p_{T} < 3.0 GeV/c", 1 ,0., 1.);
      hntrg_ch_assoc = ntrgHist.make<TH1D>("hntrg_ch_assoc", "0.3 < p_{T} < 3.0 GeV/c", 400 ,0., 400.);
    

    TFileDirectory sigmixHist = fs->mkdir("SigMix");

//hobs_sig_c2_jpsiSel_vs_ch.resize(ncentbins);
//hobs_mix_c2_jpsiSel_vs_ch.resize(ncentbins);

//    hbkg_sig_c2_jpsiSel_vs_ch.resize(ncentbins);
//  hbkg_mix_c2_jpsiSel_vs_ch.resize(ncentbins);

//  hsig_c2_ch_vs_ch.resize(ncentbins);
//  hmix_c2_ch_vs_ch.resize(ncentbins);

//  for (unsigned int ict = 0; ict < ncentbins; ++ict) {
      hobs_sig_c2_jpsiSel_vs_ch.resize(nptbins);
      hobs_mix_c2_jpsiSel_vs_ch.resize(nptbins);

//    hbkg_sig_c2_jpsiSel_vs_ch[ict].resize(nptbins);
//    hbkg_mix_c2_jpsiSel_vs_ch[ict].resize(nptbins);
      

      for (unsigned int ipt = 0; ipt < nptbins; ++ipt) {
	hobs_sig_c2_jpsiSel_vs_ch[ipt].resize(nmassbins_jpsiSel);
	hobs_mix_c2_jpsiSel_vs_ch[ipt].resize(nmassbins_jpsiSel);
      
	for (unsigned int imass = 0; imass < nmassbins_jpsiSel; ++imass) {

	  hobs_sig_c2_jpsiSel_vs_ch[ipt][imass] = sigmixHist.make<TH2D>(Form("hobs_sig_c2_jpsi_vs_ch_pT_%d_mass_%d", ipt,imass), Form("hobs_sig_c2_jpsi_vs_ch_pT_%d_mass_%d", ipt, imass), nBins_deta+1, eta_lowedge, eta_upedge, nBins_dphi-1, phi_lowedge, phi_upedge);

	  hobs_mix_c2_jpsiSel_vs_ch[ipt][imass] = sigmixHist.make<TH2D>(Form("hobs_mix_c2_jpsi_vs_ch_pT_%d_mass_%d", ipt, imass), Form("hobs_mix_c2_jpsi_vs_ch_pT_%d_mass_%d", ipt, imass), nBins_deta+1, eta_lowedge, eta_upedge, nBins_dphi-1, phi_lowedge, phi_upedge);

	}

      }


      hsig_c2_ch_vs_ch = sigmixHist.make<TH2D>("hsig_c2_ch_vs_ch", "hsig_c2_ch_vs_ch", nBins_deta+1, eta_lowedge, eta_upedge, nBins_dphi-1, phi_lowedge, phi_upedge);
      hmix_c2_ch_vs_ch = sigmixHist.make<TH2D>("hmix_c2_ch_vs_ch", "hmix_c2_ch_vs_ch", nBins_deta+1, eta_lowedge, eta_upedge, nBins_dphi-1, phi_lowedge, phi_upedge);
}
    


RaghuV0Ana::~RaghuV0Ana()
{
  
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
  delete evt_; 
}

// ------------ method called for each event  ------------
void
RaghuV0Ana::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  zBestVtx1_ = -999.;
  ntrkoff = 0;
  centbin = -999;
  LoopV0Vertices(iEvent, iSetup);

  if(ntrkoff<185 || ntrkoff>250) return;
  //if(ntrkoff>35) return;
  //if(ntrkoff<0) return;
  hzvtx_->Fill(zBestVtx1_);
  hbin_->Fill(ntrkoff);
  evt_->run   = iEvent.id().run();
  evt_->event = iEvent.id().event();
  evt_->zvtx  = zBestVtx1_;
  evt_->ntrkOFF  = ntrkoff;
  evt_->cent = ntrkoff;
  
  evtVec_.push_back(*evt_);

  // ----- Reset evt container -----                                                                                                             
  evt_->reset();
}  
 

// ------------ method called once each job just before starting event loop  ------------
void
RaghuV0Ana::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
RaghuV0Ana::endJob()
{

  std::cout<< "Start sorting the events!" << std::endl;

  std::cout<< "Finish sorting the events!" << std::endl;
  
  std::cout<< "Total of " << evtVec_.size() << " events are selected!" << std::endl;
  
  std::cout<< "Start running correlation analysis!" << std::endl;

  unsigned int ievt = 0;
  for( unsigned int i = 0; i < evtVec_.size(); i++ )
    {      
      if( i % 100 == 0 ) std::cout << "Processing " << i << "th event" << std::endl;
      ievt = i;
      
      if (evtVec_[i].pVect_trg.size() == 0) std::cerr << "pVect_trg empty at i = " << i << std::endl;
      if (evtVec_[i].pVect_daup_trg.size() == 0) std::cerr << "pVect_daup_trg empty at i = " << i << std::endl;
      if (evtVec_[i].pVect_daun_trg.size() == 0) std::cerr << "pVect_daun_trg empty at i = " << i << std::endl;
      
      if (evtVec_[i].pVect_trg.empty() || evtVec_[i].pVect_daup_trg.empty() || evtVec_[i].pVect_daun_trg.empty()) {
	continue;  // skip this event safely //doubt1
      }
      
      unsigned int itrack = 0;
      unsigned int ntrack_trg = evtVec_[ievt].pVect_trg[itrack].size();
      //int ict = 0;

      //int ctbin = evtVec_[ievt].cent;
      //int ict = hV0centbin->FindBin(ctbin) - 1;   
      for( unsigned int n = 0; n < ntrack_trg; n++) {

	TVector3 pvector_n = (evtVec_[ievt].pVect_trg[itrack])[n];
	int id_n = (evtVec_[ievt].chgVect_trg[itrack])[n];
	double mass = (evtVec_[ievt].massVect_trg[itrack])[n];
	double pt_n = pvector_n.Pt();
	double eta_n = pvector_n.Eta();
	double phi_n = pvector_n.Phi();
	double ntrk_ch = (evtVec_[ievt].chgVect_ass[itrack])[n];
	
	int ipt = hV0pTbin->FindBin(pt_n) - 1;
	int imass = hV0massbin_jpsiSel->FindBin(mass) - 1;
	//std::cout<< " pt_n  :  "<< pt_n << std::endl;
	if (TMath::Abs(id_n) == 1){
	  if (pt_n < pTmin_ch_ || pt_n >= pTmax_ch_) continue;
	  if (eta_n < Etamin_ || eta_n >= Etamax_) continue;
	  //hch_pt_->Fill(pt_n); 
	  hntrg_ch->AddBinContent(1, 1);
	  hntrg_ch_assoc->Fill(ntrk_ch);
	}

	if (TMath::Abs(id_n) == 443) {
	if (pt_n < pTmin_trg_jpsiSel_ || pt_n >= pTmax_trg_jpsiSel_) continue;
	if(imass != -999 && ipt != -999)hntrg_obs_jpsiks[ipt][imass]->AddBinContent(1,1);
	}

	// ---- Daughter particles informations 
	TVector3 pvector_daup_n = (evtVec_[ievt].pVect_daup_trg[itrack])[n];
	TVector3 pvector_daun_n = (evtVec_[ievt].pVect_daun_trg[itrack])[n];
	
	// ---- Daughter no.1 : positive
	double pt_daup_n = pvector_daup_n.Pt();
	double eta_daup_n = pvector_daup_n.Eta();
	double phi_daup_n = pvector_daup_n.Phi();
	
	// ---- Daughter no.2 : negative
	double pt_daun_n = pvector_daun_n.Pt();
	double eta_daun_n = pvector_daun_n.Eta();
	double phi_daun_n = pvector_daun_n.Phi();
	
	// ---- associated track loop:: track loop 2
	for( unsigned int m = 0; m < ntrack_trg; m++) {
	  TVector3 pvector_m = (evtVec_[ievt].pVect_trg[itrack])[m];
	  int id_m = (evtVec_[ievt].chgVect_trg[itrack])[m];
	  
	  double pt_m = pvector_m.Pt();
	  double eta_m = pvector_m.Eta();
	  double phi_m = pvector_m.Phi();

	  if (TMath::Abs(id_m) == 443) continue;
	  if (TMath::Abs(id_m) == 1){
	    if (pt_m < pTmin_ch_ || pt_m >= pTmax_ch_) continue;
            if (eta_m < Etamin_ || eta_m >= Etamax_) continue;
          }
	  if(pt_n < pt_m) continue;
	  if (phi_daup_n == phi_m && eta_daup_n == eta_m && pt_daup_n == pt_m) continue;
	  if (phi_daun_n == phi_m && eta_daun_n == eta_m && pt_daun_n == pt_m) continue;
	  
	  double deltaPhi = (phi_n - phi_m);
	  double deltaEta = (eta_n - eta_m);
	  double deltaPhi2 = (phi_m - phi_n);
	  
	  if(deltaPhi> 1.5*TMath::Pi()){
	    deltaPhi = deltaPhi - 2.0*TMath::Pi();
	  }
	  else if(deltaPhi < -0.5*TMath::Pi()) {
	    deltaPhi = deltaPhi + 2.0*TMath::Pi();
	  }

	  if(deltaPhi2> 1.5*TMath::Pi()){
            deltaPhi2 = deltaPhi2 - 2.0*TMath::Pi();
          }
          else if(deltaPhi2 < -0.5*TMath::Pi()) {
            deltaPhi2 = deltaPhi2 + 2.0*TMath::Pi();
          }

	  if (TMath::Abs(id_n) == 443 && TMath::Abs(id_m) == 1){
	    hobs_sig_c2_jpsiSel_vs_ch[ipt][imass]->Fill( std::abs(deltaEta), deltaPhi, 0.25 );
            hobs_sig_c2_jpsiSel_vs_ch[ipt][imass]->Fill( -std::abs(deltaEta), deltaPhi, 0.25 );
            hobs_sig_c2_jpsiSel_vs_ch[ipt][imass]->Fill( std::abs(deltaEta), deltaPhi2, 0.25 );
            hobs_sig_c2_jpsiSel_vs_ch[ipt][imass]->Fill( -std::abs(deltaEta), deltaPhi2, 0.25 );
	  }//id 443 close 
	  if (TMath::Abs(id_n) == 1 && TMath::Abs(id_m) == 1){
	    hsig_c2_ch_vs_ch->Fill( std::abs(deltaEta), deltaPhi, 0.25 );
            hsig_c2_ch_vs_ch->Fill( -std::abs(deltaEta), deltaPhi, 0.25 );
            hsig_c2_ch_vs_ch->Fill( std::abs(deltaEta), deltaPhi2, 0.25 );
            hsig_c2_ch_vs_ch->Fill( -std::abs(deltaEta), deltaPhi2, 0.25 );
	  }
	}//end of associated track loop
      }//end of trigger track loop

      
      //~~~~~~~~~~~~ Mixing Correlation ~~~~~~~~~~~
      // bkgFactor = 5;

      unsigned int mixstart = ievt+1;
      unsigned int mixend   = (int)evtVec_.size();

      if(mixstart > (0.7*(evtVec_.size())))
        {
           mixstart = (0.4*(evtVec_.size()));
           mixend   = (int)evtVec_.size();
        }

       int nmix = 0;

       
       for( unsigned int jevt = mixstart; jevt < mixend; jevt++ ) {
	if(jevt == ievt) continue;

	if( evtVec_[ievt].run == evtVec_[jevt].run && evtVec_[ievt].event == evtVec_[jevt].event ) continue;

	double deltazvtx = evtVec_[ievt].zvtx-evtVec_[jevt].zvtx;
	//if(fabs(deltazvtx) > 0.5) continue;
	if(fabs(deltazvtx) > 2) continue;

	double deltantrkoff = evtVec_[ievt].ntrkOFF-evtVec_[jevt].ntrkOFF;
	//if(fabs(deltantrkoff) > 10) continue;
	unsigned int nsize_ievt_trg = evtVec_[ievt].pVect_trg[itrack].size();
	unsigned int nsize_jevt_trg = evtVec_[jevt].pVect_trg[itrack].size();
	//unsigned int nsize_jevt = evtVec_[jevt].pVect[itrack].size();
	
	if (nsize_ievt_trg ==0 || nsize_jevt_trg ==0) continue;

	for(unsigned int n = 0; n < nsize_ievt_trg; n++) {
	  TVector3 pvector_n = (evtVec_[ievt].pVect_trg[itrack])[n];
	  int id_n = (evtVec_[ievt].chgVect_trg[itrack])[n];
	  double mass = (evtVec_[ievt].massVect_trg[itrack])[n];
	  
	  double pt_n = pvector_n.Pt();
	  double eta_n = pvector_n.Eta();
	  double phi_n = pvector_n.Phi();

	  int ipt = hV0pTbin->FindBin(pt_n) - 1;
	  int imass = hV0massbin_jpsiSel->FindBin(mass) - 1;
	  if (TMath::Abs(id_n) == 1){
	    if (pt_n < pTmin_ch_ || pt_n >= pTmax_ch_) continue;
	    if (eta_n < Etamin_ || eta_n >= Etamax_) continue;
	  }
	  
	    if (TMath::Abs(id_n) == 443){
	    if (pt_n < pTmin_trg_jpsiSel_ || pt_n >= pTmax_trg_jpsiSel_) continue;

	  }
	  
	  // ---- Daughter particles informations
	  TVector3 pvector_daup_n = (evtVec_[ievt].pVect_daup_trg[itrack])[n];
	  TVector3 pvector_daun_n = (evtVec_[ievt].pVect_daun_trg[itrack])[n]; 

	  // ---- Daughter no.1 : positive
	  double pt_daup_n = pvector_daup_n.Pt();
	  double eta_daup_n = pvector_daup_n.Eta();
	  double phi_daup_n = pvector_daup_n.Phi();
	  
	  // ---- Daughter no.2 : negative
	  double pt_daun_n = pvector_daun_n.Pt();
	  double eta_daun_n = pvector_daun_n.Eta();
	  double phi_daun_n = pvector_daun_n.Phi();
	  
	  // ---- associated track loop:: track loop 2
	  for(unsigned int m = 0; m < nsize_jevt_trg; m++) {
	    TVector3 pvector_m = (evtVec_[jevt].pVect_trg[itrack])[m];
	    int id_m = (evtVec_[jevt].chgVect_trg[itrack])[m];
	    
	    double pt_m = pvector_m.Pt();
	    double eta_m = pvector_m.Eta();
	    double phi_m = pvector_m.Phi();

	    //associate pt cuts
	    if (TMath::Abs(id_m) == 443) continue; 
	    if (TMath::Abs(id_m) == 1){
	      if (pt_m < pTmin_ch_ || pt_m >= pTmax_ch_) continue;
              if(eta_m < Etamin_ || eta_m >= Etamax_) continue;
            }
	    if(pt_n < pt_m) continue;
	    if (phi_daup_n == phi_m && eta_daup_n == eta_m && pt_daup_n == pt_m) continue;
	    if (phi_daun_n == phi_m && eta_daun_n == eta_m && pt_daun_n == pt_m) continue; 
	    
	    double deltaPhi = (phi_n - phi_m);
	    double deltaEta = (eta_n - eta_m);
	    double deltaPhi2 = (phi_m - phi_n);
	    if(deltaPhi> 1.5*TMath::Pi()){
	      deltaPhi = deltaPhi - 2.0*TMath::Pi();
	    }
	    else if(deltaPhi < -0.5*TMath::Pi()) {
	      deltaPhi = deltaPhi + 2.0*TMath::Pi();
	    }
	    if(deltaPhi2> 1.5*TMath::Pi()){
              deltaPhi2 = deltaPhi2 - 2.0*TMath::Pi();
            }
            else if(deltaPhi2 < -0.5*TMath::Pi()) {
              deltaPhi2 = deltaPhi2 + 2.0*TMath::Pi();
            }
	    //if (TMath::Abs(id_n) == 443 && TMath::Abs(id_m) == 1 && mass > 2.94 && mass < 3.24){
	    if (TMath::Abs(id_n) == 443 && TMath::Abs(id_m) == 1 && (mass >= mSigLow_ && mass < mSigHigh_) ){
	      hobs_mix_c2_jpsiSel_vs_ch[ipt][imass]->Fill( std::abs(deltaEta), deltaPhi, 0.25 );
              hobs_mix_c2_jpsiSel_vs_ch[ipt][imass]->Fill( -std::abs(deltaEta), deltaPhi, 0.25 );
              hobs_mix_c2_jpsiSel_vs_ch[ipt][imass]->Fill( std::abs(deltaEta), deltaPhi2, 0.25 );
              hobs_mix_c2_jpsiSel_vs_ch[ipt][imass]->Fill( -std::abs(deltaEta), deltaPhi2, 0.25 );
	    }
	    else if (TMath::Abs(id_n) == 1 && TMath::Abs(id_m) == 1){
	      hmix_c2_ch_vs_ch->Fill( std::abs(deltaEta), deltaPhi, 0.25 );
              hmix_c2_ch_vs_ch->Fill( -std::abs(deltaEta), deltaPhi, 0.25 );
              hmix_c2_ch_vs_ch->Fill( std::abs(deltaEta), deltaPhi2, 0.25 );
              hmix_c2_ch_vs_ch->Fill( -std::abs(deltaEta), deltaPhi2, 0.25 );
	    }
	  }//end of associated track loop 
	}//end of trigger track loop
	nmix++;
	//if(nmix >= 5) break;
	if(nmix >= 20) break;
      }// end of mixing event loop
    }//end of the 1st event loop 
}
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
RaghuV0Ana::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//=========================================================================================================================
void
RaghuV0Ana::LoopV0Vertices(const edm::Event& iEvent,
				   const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std;
  using namespace reco;
  
  edm::Handle< reco::VertexCollection > vertices;
  iEvent.getByToken(vtxTags_, vertices);

  edm::Handle<pat::PackedCandidateCollection> packed;
  iEvent.getByToken(packedCandToken_, packed);

  edm::Handle<edm::Association<reco::TrackCollection>> pc2track;
  iEvent.getByToken(pc2trackAssocToken_, pc2track);

  edm::Handle<reco::TrackCollection> recoTracks;
  iEvent.getByToken(recoTracksToken_, recoTracks);

  const bool usePackedTracks = packed.isValid() && pc2track.isValid();
  if (!usePackedTracks && (!recoTracks.isValid() || recoTracks->empty())) {
    edm::LogError("RaghuV0Ana") << "Neither packed track inputs nor generalTracks are available.";
    return;
  }
  
  //if(!vertices->size())
  if (!vertices.isValid() || vertices->empty()) 
    {
      //std::cout<<"Invalid or empty vertex collection!"<<std::endl;
      return;
    }
  
  reco::VertexCollection recoVertices = *vertices;
  
  sort(recoVertices.begin(), recoVertices.end(), [](const reco::Vertex &a, const reco::Vertex &b){
      return a.tracksSize() > b.tracksSize();
    });


  unsigned int primaryvtx = 0;  
  for ( primaryvtx = 0; primaryvtx < recoVertices.size(); primaryvtx++ ) {
    if ( (!recoVertices[primaryvtx].isFake())
         && fabs(recoVertices[primaryvtx].z()) <= 25.
         && recoVertices[primaryvtx].position().Rho() <= 2.0) break;
  }

  //if(recoVertices.size() != 1) return;
   reco::Vertex const * pv = &recoVertices[primaryvtx];
 
  // std::cout << "recoVertices.size():" << pv->size() << std::endl;
  double zBestVtx_ = pv->z();
  if (zBestVtx_ < zminVtx_ || zBestVtx_ > zmaxVtx_ ) return;
  zBestVtx1_ = zBestVtx_;

  auto trackPassesBaseCuts = [&](const reco::Track* trk_ch) {
    if (!trk_ch) return false;
    const math::XYZPoint bestvtx(pv->x(), pv->y(), pv->z());
    const double dzvtx_ch = trk_ch->dz(bestvtx);
    const double dxyvtx_ch = trk_ch->dxy(bestvtx);
    const double dzerror_ch = std::sqrt(std::pow(trk_ch->dzError(), 2) + std::pow(pv->zError(), 2));
    const double dxyerror_ch = std::sqrt(std::pow(trk_ch->d0Error(), 2) + std::pow(pv->xError(), 2) + std::pow(pv->yError(), 2));
    const double pterror_ch = trk_ch->ptError();
    const double pt = trk_ch->pt();

    if (!trk_ch->quality(reco::TrackBase::highPurity)) return false;
    if (trk_ch->charge() == 0) return false;
    if (pt <= 0.0) return false;
    if (std::abs(pterror_ch) / pt >= 0.1) return false;
    if (dzerror_ch <= 0.0 || std::abs(dzvtx_ch / dzerror_ch) >= 3.0) return false;
    if (dxyerror_ch <= 0.0 || std::abs(dxyvtx_ch / dxyerror_ch) >= 3.0) return false;
    return true;
  };
  /*
  auto countOfflineTracks = [&]() {
    int count = 0;
    if (usePackedTracks) {
      for (size_t itrk = 0; itrk < packed->size(); ++itrk) {
        const pat::PackedCandidate& cand_ch = (*packed)[itrk];
        if (!cand_ch.hasTrackDetails()) continue;
        if (cand_ch.charge() == 0) continue;
        edm::Ref<pat::PackedCandidateCollection> candRef(packed, itrk);
        const reco::Track* trk_ch = (*pc2track)[candRef].get();
        if (!trackPassesBaseCuts(trk_ch)) continue;
        if (trk_ch->pt() <= 0.4) continue;
        count++;
      }
    } else {
      for (const auto& trk : *recoTracks) {
        if (!trackPassesBaseCuts(&trk)) continue;
        if (trk.pt() <= 0.4) continue;
        count++;
      }
    }
    return count;
  };
*/
  auto countOfflineTracks = [&]() {
  int count = 0;

  if (usePackedTracks) {

    for (size_t itrk = 0; itrk < packed->size(); ++itrk) {

      const pat::PackedCandidate& cand_ch = (*packed)[itrk];

      if (cand_ch.charge() == 0) continue;

      edm::Ref<pat::PackedCandidateCollection> candRef(packed, itrk);

      if ((*pc2track)[candRef].isNull()) continue;

      const reco::Track* trk_ch = (*pc2track)[candRef].get();

      if (!trackPassesBaseCuts(trk_ch)) continue;
      if (trk_ch->pt() <= 0.4) continue;

      count++;
    }

  } else {

    for (const auto& trk : *recoTracks) {

      if (!trackPassesBaseCuts(&trk)) continue;
      if (trk.pt() <= 0.4) continue;

      count++;
    }

  }

  return count;
};
  
  ntrkoff = countOfflineTracks();
  //if (ntrkoff <= 185 || ntrkoff > 250) return;
  //if (ntrkoff <= 0) return;

  centbin = ntrkoff;
  //  int icent = 0;
  
  
  edm::Handle< pat::CompositeCandidateCollection > V0s_jpsiSel;
  iEvent.getByToken(V0Src_jpsiSel_, V0s_jpsiSel);
  
  if (!V0s_jpsiSel.isValid()) {
    edm::LogError("RaghuV0Ana") << "pat::CompositeCandidate onia2MuMuPatGlbGlb not found.";
    return;
  }
  //edm::Handle< reco::VertexCompositeCandidateCollection > V0s_jpsiSel;
  //iEvent.getByToken(V0Src_jpsiSel_, V0s_jpsiSel)

  V0pt_vect.resize(0);
  V0eta_vect.resize(0);
  V0phi_vect.resize(0);
  V0id_vect.resize(0);
  V0mass_vect.resize(0);

  pdau_pt_vect.resize(0);
  pdau_eta_vect.resize(0);
  pdau_phi_vect.resize(0);
  pdau_chi2_vect.resize(0);

  ndau_pt_vect.resize(0);
  ndau_eta_vect.resize(0);
  ndau_phi_vect.resize(0);
  ndau_chi2_vect.resize(0);

  V0pt_vect_unmatch.resize(0);
  V0eta_vect_unmatch.resize(0);
  V0phi_vect_unmatch.resize(0);
  V0id_vect_unmatch.resize(0);
  V0mass_vect_unmatch.resize(0);

  pdau_pt_vect_unmatch.resize(0);
  pdau_eta_vect_unmatch.resize(0);
  pdau_phi_vect_unmatch.resize(0);
  pdau_chi2_vect_unmatch.resize(0);

  ndau_pt_vect_unmatch.resize(0);
  ndau_eta_vect_unmatch.resize(0);
  ndau_phi_vect_unmatch.resize(0);
  ndau_chi2_vect_unmatch.resize(0);

  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ jpsi ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  /*
    int nevent_jpsiSel = 0;
    const pat::CompositeCandidateCollection& recV0jpsiSel = *V0s_jpsiSel;

    for (pat::CompositeCandidateCollection::const_iterator recoV0sjpsiSel = recV0jpsiSel.begin();
         recoV0sjpsiSel != recV0jpsiSel.end(); ++recoV0sjpsiSel)
    {
      V0id_jpsiSel = 443;
      V0mass_jpsiSel     = recoV0sjpsiSel->mass();
      V0pt_jpsiSel       = recoV0sjpsiSel->pt();
      V0eta_jpsiSel      = recoV0sjpsiSel->eta();
      V0phi_jpsiSel      = recoV0sjpsiSel->phi();
      V0rapidity_jpsiSel = recoV0sjpsiSel->rapidity();

      double vtxProb = recoV0sjpsiSel->userFloat("vProb");
      if (vtxProb < 0.01) continue;

      // --- Daughter variables (safe defaults)
      pdau_chi2 = ndau_chi2 = -1;
      pTrkNHit = nTrkNHit = 0;
      pTrkPtError = nTrkPtError = -1;
      pTrkNPxLayer = nTrkNPxLayer = 0;
      pTrkDCASigXY = nTrkDCASigXY = -1;
      pTrkDCASigZ  = nTrkDCASigZ  = -1;
      pdau_pt = ndau_pt = 0.;
      pdau_eta = ndau_eta = 0.;
      pdau_phi = ndau_phi = 0.;

      //std::cout<< "Kinematics variables!" << std::endl;
      //std::cout<< "V0pt_jpsiSel:  "<<V0pt_jpsiSel<< "    V0eta_jpsiSel:  "<< V0eta_jpsiSel << "    V0rapidity_jpsiSel:  "<< V0rapidity_jpsiSel << "    V0mass_jpsiSel:  "<<V0mass_jpsiSel  << std::endl;
      
      // Access daughters
      const reco::Candidate* dau0 = recoV0sjpsiSel->daughter(0);
      const reco::Candidate* dau1 = recoV0sjpsiSel->daughter(1);
      if (!dau0 || !dau1) continue;

      // Opposite-sign requirement (early!)
      if (dau0->charge() * dau1->charge() >= 0) continue;

      // Keep daughter kinematics
      pdau_pt  = dau0->pt();  pdau_eta  = dau0->eta();  pdau_phi  = dau0->phi();
      ndau_pt  = dau1->pt();  ndau_eta  = dau1->eta();  ndau_phi  = dau1->phi();

      // Cast to PAT muons (define ONCE)
      const pat::Muon* mu0 = dynamic_cast<const pat::Muon*>(dau0);
      const pat::Muon* mu1 = dynamic_cast<const pat::Muon*>(dau1);
      if (!mu0 || !mu1) continue;

      // Single-muon acceptance
      //if (!passSingleMuonAcc(mu0->pt(), mu0->eta())) continue;
      //if (!passSingleMuonAcc(mu1->pt(), mu1->eta())) continue;

      // PF + SoftMuon ID
      if (!mu0->isPFMuon() || !mu1->isPFMuon()) continue;
      if (!mu0->isSoftMuon(*pv) || !mu1->isSoftMuon(*pv)) continue;

      // Helper to fill track info
      auto fillFromTrack = [&](const reco::Track* trkl, bool isPositive){
        if (!trkl) return;
        const math::XYZPoint bestvtx(pv->x(), pv->y(), pv->z());
        const double dz   = trkl->dz(bestvtx);
        const double dxy  = trkl->dxy(bestvtx);
        const double dzErr  = std::sqrt(trkl->dzError()*trkl->dzError() + pv->zError()*pv->zError());
        const double dxyErr = std::sqrt(trkl->dxyError()*trkl->dxyError()
                                        + pv->xError()*pv->xError() + pv->yError()*pv->yError());
        const double sigZ  = dzErr  > 0 ? std::abs(dz/dzErr)   : -1;
        const double sigXY = dxyErr > 0 ? std::abs(dxy/dxyErr) : -1;

        if (isPositive) {
          pdau_chi2 = trkl->normalizedChi2();
          pdau_pt_jpsiSel = trkl->pt();
          pdau_eta_jpsiSel = trkl->eta();
          pdau_phi_jpsiSel = trkl->phi();
          pTrkNHit = trkl->numberOfValidHits();
          pTrkPtError = trkl->ptError();
          pTrkNPxLayer = trkl->hitPattern().pixelLayersWithMeasurement();
          pTrkDCASigXY = sigXY;
          pTrkDCASigZ  = sigZ;
        } else {
          ndau_chi2 = trkl->normalizedChi2();
          ndau_pt_jpsiSel = trkl->pt();
          ndau_eta_jpsiSel = trkl->eta();
          ndau_phi_jpsiSel = trkl->phi();
          nTrkNHit_jpsiSel = trkl->numberOfValidHits();
          nTrkPtError = trkl->ptError();
          nTrkNPxLayer = trkl->hitPattern().pixelLayersWithMeasurement();
          nTrkDCASigXY = sigXY;
          nTrkDCASigZ  = sigZ;
        }
      };

      fillFromTrack(mu0->bestTrack(), mu0->charge() > 0);
      fillFromTrack(mu1->bestTrack(), mu1->charge() > 0);



      //std::cout<< "V0pt_jpsiSel:  "<<V0pt_jpsiSel<< "    V0eta_jpsiSel:  "<< V0eta_jpsiSel << "    V0rapidity_jpsiSel:  "<< V0rapidity_jpsiSel << "    V0mass_jpsiSel: "<<V0mass_jpsiSel  << std::endl;
      // Candidate-level cuts

  bool is_dcut = kTRUE;
      if (V0pt_jpsiSel < pTmin_ || V0pt_jpsiSel > pTmax_) continue;
      if (std::abs(V0rapidity_jpsiSel) < Rapmin_1 || std::abs(V0rapidity_jpsiSel) > Rapmax_1) continue;
      if (V0mass_jpsiSel < 2.70 || V0mass_jpsiSel > 3.45) continue;

      int ipt = hV0pTbin->FindBin(V0pt_jpsiSel) - 1;
      jpsi_pT[icent][ipt]->Fill(V0mass_jpsiSel);
      //std::cout<< "V0pt_jpsiSel:  "<<V0pt_jpsiSel<< "    V0eta_jpsiSel:  "<< V0eta_jpsiSel << "    V0rapidity_jpsiSel:  "<< V0rapidity_jpsiSel << "    V0mass_jpsiSel:  "<<V0mass_jpsiSel  << std::endl;
      
      hV0mass_wocut_jpsiSel_->Fill(V0mass_jpsiSel);
      hV0pT_jpsiSel_->Fill(V0pt_jpsiSel);
      hV0eta_jpsiSel_->Fill(V0eta_jpsiSel);
      hV0phi_jpsiSel_->Fill(V0phi_jpsiSel);
      hV0rapidity_jpsiSel_->Fill(V0rapidity_jpsiSel);
      hpT_eta_->Fill(V0eta_jpsiSel, V0pt_jpsiSel);
      hpT_rap_->Fill(V0rapidity_jpsiSel, V0pt_jpsiSel);

      int index1_jpsiSel = GetpTbin(V0pt_jpsiSel, is_dcut);
      if (index1_jpsiSel == -1) continue;

      AssignpTbins(V0pt_jpsiSel, V0eta_jpsiSel, V0phi_jpsiSel, V0id_jpsiSel, V0mass_jpsiSel,
                   pdau_pt_jpsiSel, pdau_eta_jpsiSel, pdau_phi_jpsiSel,
                   ndau_pt_jpsiSel, ndau_eta_jpsiSel, ndau_phi_jpsiSel,
                   index1_jpsiSel, is_dcut);

      nevent_jpsiSel++;
    }

    if (nevent_jpsiSel > 0)
      hevent_V0_CH[icent]->AddBinContent(1, 1);
*/
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ J/psi ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/*
int nevent_jpsiSel = 0;
const pat::CompositeCandidateCollection& recV0jpsiSel = *V0s_jpsiSel;

//if(recV0jpsiSel.size()>0)
//std::cout << "Total J/psi candidates in event: " << recV0jpsiSel.size() << std::endl;
 
for (auto recoV0sjpsiSel = recV0jpsiSel.begin();
     recoV0sjpsiSel != recV0jpsiSel.end(); ++recoV0sjpsiSel)
{

  // ---------------- Candidate basic info ----------------

  V0id_jpsiSel = 443;

  V0mass_jpsiSel     = recoV0sjpsiSel->mass();
  V0pt_jpsiSel       = recoV0sjpsiSel->pt();
  V0eta_jpsiSel      = recoV0sjpsiSel->eta();
  V0phi_jpsiSel      = recoV0sjpsiSel->phi();
  V0rapidity_jpsiSel = recoV0sjpsiSel->rapidity();

double vtxProb = recoV0sjpsiSel->userFloat("vProb");
  if (V0mass_jpsiSel < mSB1Low_ || V0mass_jpsiSel > mSB2High_) continue;
  if (V0pt_jpsiSel < 0.0 || V0pt_jpsiSel > 35.0) continue;
  
  //if (recoV0sjpsiSel->hasUserFloat("vProb")) vtxProb = recoV0sjpsiSel->userFloat("vProb");
  hpT_jpsi_->Fill(V0pt_jpsiSel);
  heta_jpsi_->Fill(V0eta_jpsiSel);
  hphi_jpsi_->Fill(V0phi_jpsiSel);
  hmass_jpsi_->Fill(V0mass_jpsiSel);
  hrapidity_jpsi_->Fill(V0rapidity_jpsiSel);
  hvtxProv_jpsi_->Fill(vtxProb);

  if (vtxProb < 0.01) continue;
  hvtxProv_jpsiSel_->Fill(vtxProb);

  // ---------------- Daughter access ----------------

  if (recoV0sjpsiSel->numberOfDaughters() != 2) continue;

  const reco::Candidate* dau0 = recoV0sjpsiSel->daughter(0);
  const reco::Candidate* dau1 = recoV0sjpsiSel->daughter(1);
  if (!dau0 || !dau1) continue;

  if (dau0->charge() * dau1->charge() >= 0) continue;

  const pat::Muon* mu0 = dynamic_cast<const pat::Muon*>(dau0);
  const pat::Muon* mu1 = dynamic_cast<const pat::Muon*>(dau1);
  if (!mu0 || !mu1) continue;

  // Trigger
  bool mu0_trig = !mu0->triggerObjectMatchesByPath("HLT_OxyL1SingleMuOpen_v*").empty();
  bool mu1_trig = !mu1->triggerObjectMatchesByPath("HLT_OxyL1SingleMuOpen_v*").empty();
  if (!(mu0_trig || mu1_trig)) continue;

  // Acceptance
  if (!passSingleMuonAcc(mu0->pt(), mu0->eta())) continue;
  if (!passSingleMuonAcc(mu1->pt(), mu1->eta())) continue;

  // Muon ID
  if (!mu0->isPFMuon() || !mu1->isPFMuon()) continue;
  if (!mu0->isSoftMuon(*pv) || !mu1->isSoftMuon(*pv)) continue;
  //
  // Reset variables
  double pdau_pt_jpsiSel = 0,  ndau_pt_jpsiSel = 0.;
  double pdau_eta_jpsiSel =0, ndau_eta_jpsiSel = 0.;
  double pdau_phi_jpsiSel =0, ndau_phi_jpsiSel = 0.;
  double pdau_chi2 = -1., ndau_chi2 = -1.;

  auto fillMuon = [&](const pat::Muon* mu) {
    if (!mu) return;

    bool isPositive = mu->charge() > 0;
    const reco::Track* trk = mu->bestTrack();

    if (isPositive) {
      pdau_pt_jpsiSel  = mu->pt();
      pdau_eta_jpsiSel = mu->eta();
      pdau_phi_jpsiSel = mu->phi();

      if (trk) {
        pdau_chi2 = trk->normalizedChi2();
      }
    } else {
      ndau_pt_jpsiSel  = mu->pt();
      ndau_eta_jpsiSel = mu->eta();
      ndau_phi_jpsiSel = mu->phi();

      if (trk) {
        ndau_chi2 = trk->normalizedChi2();
      }
    }
  };
  fillMuon(mu0);
  fillMuon(mu1);

  hpT_eta_mu->Fill(pdau_eta_jpsiSel, pdau_pt_jpsiSel);
  hpT_eta_mu->Fill(ndau_eta_jpsiSel, ndau_pt_jpsiSel);


  hpT_rap1_->Fill(V0rapidity_jpsiSel, V0pt_jpsiSel);
  if (V0mass_jpsiSel < 2.6 || V0mass_jpsiSel > 3.0) continue;
  if (V0pt_jpsiSel < pTmin_ || V0pt_jpsiSel > pTmax_) continue;
  if (std::abs(V0rapidity_jpsiSel) < Rapmin_1 || std::abs(V0rapidity_jpsiSel) > Rapmax_1) continue;

  hV0mass_wocut_jpsiSel_->Fill(V0mass_jpsiSel);
  hV0pT_jpsiSel_->Fill(V0pt_jpsiSel);
  hV0eta_jpsiSel_->Fill(V0eta_jpsiSel);
  hV0phi_jpsiSel_->Fill(V0phi_jpsiSel);
  hV0rapidity_jpsiSel_->Fill(V0rapidity_jpsiSel);

  hpT_eta_->Fill(V0eta_jpsiSel, V0pt_jpsiSel);
  hpT_rap_->Fill(V0rapidity_jpsiSel, V0pt_jpsiSel);

  bool is_dcut = kTRUE;
  int ipt = hV0pTbin->FindBin(V0pt_jpsiSel) - 1;
  jpsi_pT[ipt]->Fill(V0mass_jpsiSel);

  int index1_jpsiSel = GetpTbin(V0pt_jpsiSel, is_dcut);
  if (index1_jpsiSel == -1) continue;

  //  AssignpTbins(V0pt_jpsiSel, V0eta_jpsiSel, V0phi_jpsiSel, V0id_jpsiSel, V0mass_jpsiSel,             pdau_pt, pdau_eta, pdau_phi,               ndau_pt, ndau_eta, ndau_phi,               index1_jpsiSel, is_dcut);
AssignpTbins(V0pt_jpsiSel, V0eta_jpsiSel, V0phi_jpsiSel, V0id_jpsiSel, V0mass_jpsiSel,
             pdau_pt_jpsiSel, pdau_eta_jpsiSel, pdau_phi_jpsiSel,
             ndau_pt_jpsiSel, ndau_eta_jpsiSel, ndau_phi_jpsiSel,
             index1_jpsiSel, is_dcut);
  nevent_jpsiSel++;
}
*/
int nevent_jpsiSel = 0;
const pat::CompositeCandidateCollection& recV0jpsiSel = *V0s_jpsiSel;

//if(recV0jpsiSel.size()>0)
//std::cout << "Total J/psi candidates in event: " << recV0jpsiSel.size() << std::endl;
 
for (auto recoV0sjpsiSel = recV0jpsiSel.begin();
     recoV0sjpsiSel != recV0jpsiSel.end(); ++recoV0sjpsiSel)
{

  // ---------------- Candidate basic info ----------------

  V0id_jpsiSel = 443;

  V0mass_jpsiSel     = recoV0sjpsiSel->mass();
  V0pt_jpsiSel       = recoV0sjpsiSel->pt();
  V0eta_jpsiSel      = recoV0sjpsiSel->eta();
  V0phi_jpsiSel      = recoV0sjpsiSel->phi();
  V0rapidity_jpsiSel = recoV0sjpsiSel->rapidity();
  double vtxProb = -1;

  if (recoV0sjpsiSel->hasUserFloat("vProb")) vtxProb = recoV0sjpsiSel->userFloat("vProb");

  if (V0mass_jpsiSel < mSB1Low_ || V0mass_jpsiSel > mSB2High_) continue;
  if (V0pt_jpsiSel < 0.0 || V0pt_jpsiSel > 10.0) continue;

  hpT_jpsi_->Fill(V0pt_jpsiSel);
  heta_jpsi_->Fill(V0eta_jpsiSel);
  hphi_jpsi_->Fill(V0phi_jpsiSel);
  hmass_jpsi_->Fill(V0mass_jpsiSel);
  hrapidity_jpsi_->Fill(V0rapidity_jpsiSel);
  hvtxProv_jpsi_->Fill(vtxProb);
  if (vtxProb < 0.01) continue;
  hvtxProv_jpsiSel_->Fill(vtxProb);
  // ---------------- Daughter access ----------------

  if (recoV0sjpsiSel->numberOfDaughters() != 2) continue;

  const reco::Candidate* dau0 = recoV0sjpsiSel->daughter(0);
  const reco::Candidate* dau1 = recoV0sjpsiSel->daughter(1);
  //hpT_rap1_->Fill(V0rapidity_jpsiSel, V0pt_jpsiSel);   //  getting 16/20
  if (!dau0 || !dau1) continue;
  //hpT_rap1_->Fill(V0rapidity_jpsiSel, V0pt_jpsiSel); //  getting 16/20
  if (dau0->charge() * dau1->charge() >= 0) continue;
  //  hpT_rap1_->Fill(V0rapidity_jpsiSel, V0pt_jpsiSel);  //getting 11/20
  const pat::Muon* mu0 = dynamic_cast<const pat::Muon*>(dau0);
  const pat::Muon* mu1 = dynamic_cast<const pat::Muon*>(dau1);

  if (!mu0 || !mu1) continue;
  //hpT_rap1_->Fill(V0rapidity_jpsiSel, V0pt_jpsiSel);  //getting 11/20
  //if (abs(mu0->eta()) > 2.4) continue;
  //if (abs(mu1->eta()) > 2.4) continue;
  //std::cout << "pT : " << mu0->pt() << "pT : "<<mu1->pt() << std::endl;
  //if (abs(mu0->pt()) < 3.0) continue;
  //if (abs(mu1->pt()) < 3.0) continue;
  //std::cout <<  " After pT : " << mu0->pt() << "pT : "<<mu1->pt() << std::endl;
			       
  //if (!mu0->isPFMuon() || !mu1->isPFMuon()) continue;
  //hpT_rap1_->Fill(V0rapidity_jpsiSel, V0pt_jpsiSel);  //getting 1/20
  //if (!mu0->isSoftMuon(*pv) || !mu1->isSoftMuon(*pv)) continue;
  //hpT_rap1_->Fill(V0rapidity_jpsiSel, V0pt_jpsiSel);  //getting 1/20

  ///////////////
const math::XYZPoint vtxPoint(pv->x(), pv->y(), pv->z());

auto passMuonSel = [&](const pat::Muon* mu) -> bool {
  //if (!mu->isPFMuon()) return false;
  //if (!muon::isGoodMuon(*mu, muon::TMOneStationTight)) return false;
    reco::TrackRef itk = mu->innerTrack();
    if (itk.isNull()) return false;
    if (itk->hitPattern().trackerLayersWithMeasurement() <= 5) return false;
    if (itk->hitPattern().numberOfValidPixelHits()       <= 0) return false;
    if (!itk->quality(reco::TrackBase::highPurity))            return false;
    if (std::abs(itk->dxy(vtxPoint)) >= 0.3)                   return false;
    if (std::abs(itk->dz(vtxPoint))  >= 20.0)                  return false;
    if (mu->p() <= 3.0)                                        return false;  // total momentum
    if (std::abs(mu->eta()) >= 2.4)                            return false;
    return true;
};

if (!passMuonSel(mu0) || !passMuonSel(mu1)) continue;
 
  double pdau_pt = 0,  ndau_pt = 0.;
  double pdau_eta =0, ndau_eta = 0.;
  double pdau_phi =0, ndau_phi = 0.;
  double pdau_chi2 = -1., ndau_chi2 = -1.;

  auto fillMuon = [&](const pat::Muon* mu) {
    if (!mu) return;

    bool isPositive = mu->charge() > 0;
    const reco::Track* trk = mu->bestTrack();

    if (isPositive) {
      pdau_pt   = mu->pt();
      pdau_eta = mu->eta();
      pdau_phi = mu->phi();

      if (trk) {
        pdau_chi2 = trk->normalizedChi2();
      }
    } else {
      ndau_pt  = mu->pt();
      ndau_eta = mu->eta();
      ndau_phi = mu->phi();

      if (trk) {
        ndau_chi2 = trk->normalizedChi2();
      }
    }
  };

  fillMuon(mu0);
  fillMuon(mu1);
  //hpT_rap1_->Fill(V0rapidity_jpsiSel, V0pt_jpsiSel);  //getting 11/20
  //everythin working well
  hpT_eta_mu->Fill(pdau_eta, pdau_pt);
  hpT_eta_mu->Fill(ndau_eta, ndau_pt);
  hpT_rap1_->Fill(V0rapidity_jpsiSel, V0pt_jpsiSel);
  
  bool is_dcut = kTRUE;

  //if (V0pt_jpsiSel < pTmin_ || V0pt_jpsiSel > pTmax_) continue;
  //if (std::abs(V0rapidity_jpsiSel) < Rapmin_1 || std::abs(V0rapidity_jpsiSel) > Rapmax_1) continue;
  //if (!((V0rapidity_jpsiSel > -2.86 && V0rapidity_jpsiSel < -1.86) || (V0rapidity_jpsiSel > 0.94 && V0rapidity_jpsiSel < 1.94))) continue;
  //if (V0mass_jpsiSel < 2.6 || V0mass_jpsiSel > 3.5) continue;
  //if (pdau_pt < 3.0) continue;
  //if (ndau_pt < 3.0) continue;
  //if (abs(ndau_eta) > 2.4) continue;
  //if (abs(pdau_eta) > 2.4) continue;

if (V0pt_jpsiSel < 0.2 || V0pt_jpsiSel > 10.0) continue;
if (std::abs(V0rapidity_jpsiSel) < 1.4 || std::abs(V0rapidity_jpsiSel) > 2.4) continue;
 
  int ipt = hV0pTbin->FindBin(V0pt_jpsiSel) - 1;

  jpsi_pT[ipt]->Fill(V0mass_jpsiSel);

  hV0mass_wocut_jpsiSel_->Fill(V0mass_jpsiSel);
  hV0pT_jpsiSel_->Fill(V0pt_jpsiSel);
  hV0eta_jpsiSel_->Fill(V0eta_jpsiSel);
  hV0phi_jpsiSel_->Fill(V0phi_jpsiSel);
  hV0rapidity_jpsiSel_->Fill(V0rapidity_jpsiSel);

  hpT_eta_->Fill(V0eta_jpsiSel, V0pt_jpsiSel);
  hpT_rap_->Fill(V0rapidity_jpsiSel, V0pt_jpsiSel);

  int index1_jpsiSel = GetpTbin(V0pt_jpsiSel, is_dcut);
  if (index1_jpsiSel == -1) continue;

  AssignpTbins(V0pt_jpsiSel, V0eta_jpsiSel, V0phi_jpsiSel, V0id_jpsiSel, V0mass_jpsiSel,
               pdau_pt, pdau_eta, pdau_phi,
               ndau_pt, ndau_eta, ndau_phi,
               index1_jpsiSel, is_dcut);

  nevent_jpsiSel++;
}

if (nevent_jpsiSel > 0)
  hevent_V0_CH->AddBinContent(1,1);
  // Jpsi added 

/*
  //~~~~~~~~~~~~~~~~~~~~~~~~~~~ charged hadron ~~~~~~~~~~~~~~~~~~~~~~~
    int nevent_ch = 0;
    double ch_ntrk= 0;

    auto fillChargedHadron = [&](const reco::Track* trk_ch) {
      if (!trackPassesBaseCuts(trk_ch)) return;

      const double pt = trk_ch->pt();
      const double eta = trk_ch->eta();
      const double phi = trk_ch->phi();
      const int charge = trk_ch->charge();
      bool is_dcut = kTRUE;

      if (pt <= 0.4) return;

      if (pt <= pTmin_ch_ || pt > pTmax_ch_) return;
      if (eta <= Etamin_ || eta >= Etamax_) return;

      const int id = (charge > 0) ? 1 : -1;
      const int index_ch = GetpTbin(pt, is_dcut);
      if (index_ch == -1) return;

      const double massall = 0.139570;
      hch_pt_->Fill(pt);
      hch_eta_->Fill(eta);
      hch_phi_->Fill(phi);
      ch_ntrk++;
      AssignpTbins_ch(pt, eta, phi, id, massall, ch_ntrk, pt, eta, phi, pt, eta, phi, index_ch, is_dcut);
      nevent_ch++;
    };
*/
/*
    if (usePackedTracks) {
      for (size_t itrk = 0; itrk < packed->size(); ++itrk) {
        const pat::PackedCandidate& cand_ch = (*packed)[itrk];
        if (!cand_ch.hasTrackDetails()) continue;
        if (cand_ch.charge() == 0) continue;
        edm::Ref<pat::PackedCandidateCollection> candRef(packed, itrk);
        const reco::Track* trk_ch = (*pc2track)[candRef].get();
        fillChargedHadron(trk_ch);
      }
    } else {
      for (const auto& trk : *recoTracks) {
        fillChargedHadron(&trk);
      }
    }
*/
/*
    if (usePackedTracks) {
  for (size_t itrk = 0; itrk < packed->size(); ++itrk) {

    const pat::PackedCandidate& cand_ch = (*packed)[itrk];

    if (cand_ch.charge() == 0) continue;

    edm::Ref<pat::PackedCandidateCollection> candRef(packed, itrk);

    if ((*pc2track)[candRef].isNull()) continue;

    const reco::Track* trk_ch = (*pc2track)[candRef].get();

    fillChargedHadron(trk_ch);
  }
} else {
  for (const auto& trk : *recoTracks) {

    fillChargedHadron(&trk);

  }
}
    if(nevent_ch > 0) hevent_V0_CH->AddBinContent(3, 1);
  */


  int  nevent_ch = 0;
double ch_ntrk = 0;
 math::XYZPoint bestvtx(pv->x(), pv->y(), pv->z());
const double xVtxError = pv->xError();
const double yVtxError = pv->yError();
const double zVtxError = pv->zError();
 auto fillChargedHadron = [&](const reco::Track& trk_ch) {

    // ── Basic quality & charge ───────────────────────────────────────────
    if (!trk_ch.quality(reco::TrackBase::highPurity)) return;
    if (trk_ch.charge() == 0)                         return;

    // ── Impact-parameter quantities ──────────────────────────────────────
    const double dzvtx_ch   = trk_ch.dz(bestvtx);
    const double dxyvtx_ch  = trk_ch.dxy(bestvtx);
    const double dzerror_ch = std::sqrt(std::pow(trk_ch.dzError(),  2)
                                      + std::pow(zVtxError,         2));
    const double dxyerror_ch= std::sqrt(std::pow(trk_ch.d0Error(),  2)
                                      + std::pow(xVtxError,         2)
                                      + std::pow(yVtxError,         2));
    const double pterror_ch = trk_ch.ptError();
        const double pt     = trk_ch.pt();
    const double eta    = trk_ch.eta();
    const double phi    = trk_ch.phi();
    const int    charge = trk_ch.charge();
    bool         is_dcut = kTRUE;

    // ── Track selection cuts (identical to MINIAOD block) ────────────────
    if (std::abs(pterror_ch) / pt              >= 0.1 ) return;
    if (std::abs(dzvtx_ch   / dzerror_ch)      >= 3.0 ) return;
    if (std::abs(dxyvtx_ch  / dxyerror_ch)     >= 3.0 ) return;

    if (pt  <= pTmin_ch_ || pt  >  pTmax_ch_)  return;
    if (eta <= Etamin_   || eta >= Etamax_)     return;

    // ── Fill histograms & counters ───────────────────────────────────────
    const int    id        = (charge > 0) ? 1 : -1;
    const int    index_ch  = GetpTbin(pt, is_dcut);
    if (index_ch == -1) return;

    const double massall = 0.139570;   // charged pion mass
    hch_pt_ ->Fill(pt);
    hch_eta_->Fill(eta);
    hch_phi_->Fill(phi);

    ch_ntrk++;
    AssignpTbins_ch(pt, eta, phi, id, massall, ch_ntrk,
                    pt, eta, phi,
                    pt, eta, phi,
                    index_ch, is_dcut);
    nevent_ch++;
};
 for (const reco::Track& trk : *recoTracks) {
    fillChargedHadron(trk);
}

// ── Event counter (same as before) ───────────────────────────────────────
if (nevent_ch > 0) hevent_V0_CH->AddBinContent(3, 1);
 
  V0pt_vect.clear();
  V0eta_vect.clear();
  V0phi_vect.clear();
  V0id_vect.clear();
  V0mass_vect.clear();

  pdau_pt_vect.clear();
  pdau_eta_vect.clear();
  pdau_phi_vect.clear();
  pdau_chi2_vect.clear();

  ndau_pt_vect.clear();
  ndau_eta_vect.clear();
  ndau_phi_vect.clear();
  ndau_chi2_vect.clear();

}

//======================================================================
/*
bool RaghuV0Ana::passSingleMuonAcc(double pt, double eta) {
  const double Eta[10] = {-2.4,-1.7,-1.3,-1.3,-1.0, 1.0, 1.3, 1.3, 1.7, 2.4};
  const double pT [10] = { 1.0, 1.0, 1.53, 2.1, 3.3, 3.3, 2.1, 1.53, 1.0, 1.0};

  for (int i = 0; i < 9; i++) {
    if (eta >= Eta[i] && eta < Eta[i+1] && pt >= pT[i]) return true;
  }
  return false;
}
*/
//===========================================================================================================================================
bool RaghuV0Ana::passSingleMuonAcc(double pt, double eta)
{
    const double aeta = std::abs(eta);

    if (aeta > 2.4) return false;
    if (aeta <= 1.0) return pt >= 3.3;
    if (aeta <= 1.3) return pt >= ((2.1 - 3.3) / (1.3 - 1.0)) * (aeta - 1.0) + 3.3;
    if (aeta <= 1.7) return pt >= ((1.0 - 2.1) / (1.7 - 1.3)) * (aeta - 1.3) + 2.1;

    return pt >= 1.0;
}

//=========================================================================================================================================== 
/*
Double_t RaghuV0Ana::trkAcc(Double_t *x, Double_t *)
{
    const double aeta = std::abs(x[0]);

    // Outside acceptance
    if (aeta > 2.4) return 1e6;
 
    // |η| ≤ 1.0  → pT ≥ 3.3
    if (aeta <= 1.0) {
        return 3.3;
    }

    // 1.0 < |η| ≤ 1.3 : (1.0,3.3) → (1.3,2.1)
    if (aeta <= 1.3) {
        const double m = (2.1 - 3.3) / (1.3 - 1.0);
        return m * (aeta - 1.0) + 3.3;
    }

    // 1.3 < |η| ≤ 1.7 : (1.3,2.1) → (1.7,1.0)
    if (aeta <= 1.7) {
        const double m = (1.0 - 2.1) / (1.7 - 1.3);
        return m * (aeta - 1.3) + 2.1;
    }

    // 1.7 < |η| ≤ 2.4 → pT ≥ 1.0
    return 1.0;
}
bool RaghuV0Ana::passSingleMuonAcc(double pt, double eta)
{
    Double_t x[1];
    x[0] = eta;

    double ptMin = trkAcc(x, nullptr);

    return (pt >= ptMin);
}
*/
//===========================================================================================================================================
/*
bool RaghuV0Ana::passSingleMuonAcc(double pt, double eta) {
    double aeta = std::abs(eta);

    if (aeta <= 1.0) {
        return pt >= 3.3;
    }
    else if (aeta <= 1.3) {
        // (1.0, 3.3) → (1.3, 2.1)
        double m = (2.1 - 3.3) / (1.3 - 1.0);
        double ptMin = m * (aeta - 1.0) + 3.3;
        return pt >= ptMin;
    }
    else if (aeta <= 1.7) {
        // (1.3, 2.1) → (1.7, 1.0)
        double m = (1.0 - 2.1) / (1.7 - 1.3);
        double ptMin = m * (aeta - 1.3) + 2.1;
        return pt >= ptMin;
    }
    else if (aeta <= 2.4) {
        return pt >= 1.0;
    }

    return false;
}
*/
//======================================================================
int RaghuV0Ana::GetpTbin(double V0pt, bool is_dcut)
{
  int idx = -1;
  //if(is_dcut)
  //{
  is_dcut=kTRUE;
      for(unsigned int trgidx = 0; trgidx < pTmin_trg_.size(); ++trgidx)
	
	{
	  if(V0pt >= pTmin_trg_[trgidx] && V0pt <= pTmax_trg_[trgidx]){
	    idx = trgidx;
	  }
	}
      // }
//else
      //{
      for(unsigned int assidx = 0; assidx < pTmin_ass_.size(); ++assidx)
	
	{
	  if(V0pt >= pTmin_ass_[assidx] && V0pt <= pTmax_ass_[assidx]){
	    idx = assidx;
	  }
	}
      //}
  return idx;
}
//===========================================================================================================================================
void
RaghuV0Ana::AssignpTbins(double V0pt, double V0eta, double V0phi,int V0id, double v0mass, double pdau_pt, double pdau_eta, double pdau_phi, double ndau_pt, double ndau_eta, double ndau_phi, int idx, bool is_dcut)
  
  
{

  TVector3 pvector;                    
  // pvector.SetPtEtaPhiM(V0pt, V0eta, V0phi, V0mass);
  pvector.SetPtEtaPhi(V0pt, V0eta, V0phi);
  TVector3 pvector_pdau;
  // pvector_pdau.SetPtEtaPhiM(pdau_pt, pdau_eta, pdau_phi, 0.139570 );
  pvector_pdau.SetPtEtaPhi(pdau_pt, pdau_eta, pdau_phi);
  TVector3 pvector_ndau;
  // pvector_ndau.SetPtEtaPhiM(ndau_pt, ndau_eta, ndau_phi, 0.139570 );
  pvector_ndau.SetPtEtaPhi(ndau_pt, ndau_eta, ndau_phi);

  
  if(is_dcut)
    {
      (evt_->pVect_trg[idx]).push_back(pvector);
      (evt_->chgVect_trg[idx]).push_back(V0id);
      (evt_->massVect_trg[idx]).push_back(v0mass);
      (evt_->pVect_daup_trg[idx]).push_back(pvector_pdau);
      (evt_->pVect_daun_trg[idx]).push_back(pvector_ndau);
      //hV0mass1_trg_[idx]->Fill(V0mass);
    }
}
// ch-Hadrons
//==========================================================================================================================================
void
RaghuV0Ana::AssignpTbins_ch(double V0pt, double V0eta, double V0phi,int V0id, double v0mass,  double ch_ntrk, double pdau_pt, double pdau_eta, double pdau_phi, double ndau_pt, double ndau_eta, double ndau_phi, int idx, bool is_dcut)

{

  TVector3 pvector;
  // pvector.SetPtEtaPhiM(V0pt, V0eta, V0phi, V0mass);                                                                                                                                             
  pvector.SetPtEtaPhi(V0pt, V0eta, V0phi);
  TVector3 pvector_pdau;
  // pvector_pdau.SetPtEtaPhiM(pdau_pt, pdau_eta, pdau_phi, 0.139570 );                                                                                                                            
  pvector_pdau.SetPtEtaPhi(pdau_pt, pdau_eta, pdau_phi);
  TVector3 pvector_ndau;
  // pvector_ndau.SetPtEtaPhiM(ndau_pt, ndau_eta, ndau_phi, 0.139570 );                                                                                                                            
  pvector_ndau.SetPtEtaPhi(ndau_pt, ndau_eta, ndau_phi);

  if(is_dcut)
    {
      (evt_->pVect_trg[idx]).push_back(pvector);
      (evt_->chgVect_trg[idx]).push_back(V0id);
      (evt_->massVect_trg[idx]).push_back(v0mass);
      //(evt_->weightVect_all[idx]).push_back(v0eff);
      (evt_->chgVect_ass[idx]).push_back(ch_ntrk);
      (evt_->pVect_daup_trg[idx]).push_back(pvector_pdau);
      (evt_->pVect_daun_trg[idx]).push_back(pvector_ndau);

    }

}

//==========================================================================================================================================                                                                                                                                
int RaghuV0Ana::GetCentbin(float cent)
{
  int cbin = hcent_bin->FindBin(cent/2.)-1;
  return cbin;
}
//==========================================================================================================================================  

Int_t 
RaghuV0Ana::getHiBinFromhiHF(const Double_t hiHF)
{
  Int_t binPos = -1;
  for(int i = 0; i < ncBins; ++i){
    
    if(hiHF >= binTable[i] && hiHF < binTable[i+1]){
      binPos = i;
      break;
    }
  }
  
  binPos = ncBins - 1 - binPos;
  
  return (Int_t)(200*((Double_t)binPos)/((Double_t)ncBins));
  
}
//TYPELOOKUP_DATA_REG(TransientTrackRecord);
//==========================================================================================================================================  
DEFINE_FWK_MODULE(RaghuV0Ana);
