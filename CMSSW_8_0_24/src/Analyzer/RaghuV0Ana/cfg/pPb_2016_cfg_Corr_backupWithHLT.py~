import FWCore.ParameterSet.Config as cms
process = cms.Process("RaghuV0Ana")
# __________________ General _________________

# Configure the logger
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
#process.load('Configuration.StandardSequences.MagneticField_cff')
#process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
#process.load('Configuration.StandardSequences.MagneticField_38T_cff')
#process.load('RecoVertex.PrimaryVertexProducer.OfflinePrimaryVerticesRecovery_cfi')
#process.load('RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi')
#process.load("PhysicsTools.PatAlgos.slimming.packedPFCandidates_cff")
process.load('RecoHI.HiEvtPlaneAlgos.HiEvtPlane_cfi')
process.load('RecoHI.HiEvtPlaneAlgos.hiEvtPlaneFlat_cfi')

# Configure the number of maximum event the analyser run on in interactive mode
process.maxEvents = cms.untracked.PSet( 
    input = cms.untracked.int32(-1) 
    #input = cms.untracked.int32(2000) 
    )

# __________________ I/O files _________________
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'root://cms-xrd-global.cern.ch///store/user/singhm/PAHighMultiplicity1/JPsi_HiSkim_pPb_2016_v2/260308_202326/0000/onia2MuMuPAT_DATA_pPb80X_11.root'
        #'/store/user/singhm/PAHighMultiplicity3/JPsi_HiSkim_pPb_2016_HM_3_dataset/260309_124749/0000/onia2MuMuPAT_DATA_pPb80X_130.root'
        #'/store/user/singhm/PAHighMultiplicity4/JPsi_HiSkim_pPb_2016_HM_4_dataset/260309_124937/0000/onia2MuMuPAT_DATA_pPb80X_10.root'
    ),
    secondaryFileNames = cms.untracked.vstring(
        #'/store/hidata/PARun2016C/PAHighMultiplicity1/AOD/PromptReco-v1/000/285/505/00000/006F1E14-85AF-E611-9F9E-02163E014508.root' #HM
        'root://cms-xrd-global.cern.ch///store/hidata/PARun2016C/PAHighMultiplicity1/AOD/PromptReco-v1/000/285/505/00000/1C87A9F1-8DAF-E611-82E8-FA163EF22524.root'
        #'/store/hidata/PARun2016C/PAHighMultiplicity3/AOD/PromptReco-v1/000/285/517/00000/1E2BDF9D-50B0-E611-AB47-FA163E18AD50.root'
        #'/store/hidata/PARun2016C/PAHighMultiplicity4/AOD/PromptReco-v1/000/285/505/00000/16AE5589-6FAF-E611-A96C-FA163EC0FD51.root'
    )
)
'''
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        'root://cms-xrd-global.cern.ch//store/user/singhm/PAHighMultiplicity1/JPsi_HiSkim_pPb_2016_v2/260308_202326/0000/onia2MuMuPAT_DATA_pPb80X_603.root'
        # 'root://cms-xrd-global.cern.ch//store/user/singhm/PAHighMultiplicity1/JPsi_HiSkim_pPb_2016_v2/260308_202326/0000/onia2MuMuPAT_DATA_pPb80X_11.root'
        # 'root://cms-xrd-global.cern.ch//store/user/singhm/PAHighMultiplicity3/...130.root'
        # 'root://cms-xrd-global.cern.ch//store/user/singhm/PAHighMultiplicity4/...10.root'
    ),
    secondaryFileNames = cms.untracked.vstring(
        'root://cms-xrd-global.cern.ch//store/hidata/PARun2016C/PAHighMultiplicity1/AOD/PromptReco-v1/000/285/530/00000/D67D774D-8FB0-E611-B262-02163E013422.root'
        # 'root://cms-xrd-global.cern.ch//store/hidata/PARun2016C/...1C87A9F1.root'
        # 'root://cms-xrd-global.cern.ch//store/hidata/PARun2016C/...D67D774D.root'
    )
)
'''
# Define output file name
import os
process.TFileService = cms.Service("TFileService",
        fileName = cms.string('cent_pPb_flow_jpsi.root')
)

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

# __________________ Detector conditions _________________

# Configure the Global Tag
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag

#process.GlobalTag = GlobalTag(process.GlobalTag, '150X_dataRun3_Prompt_v3', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_Prompt_v15', '') 
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
process.GlobalTag.toGet.extend([
        cms.PSet(record = cms.string("HeavyIonRcd"),
                 tag = cms.string("CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1033p1x01_offline"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
                 label = cms.untracked.string("HFtowers")
                 ),
        ])
#process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
#process.centralityBin.Centrality = cms.InputTag("pACentrality")
#process.centralityBin.centralityVariable = cms.string("HFtowers")
#process.load('RecoHI.HiCentralityAlgos.CentralityFilter_cfi')

# __________________ Event selection _________________                                               
#process.load('HeavyIonsAnalysis.EventAnalysis.skimanalysis_cfi')

#1process.load('HeavyIonsAnalysis.EventAnalysis.collisionEventSelection_cff')

#process.load('HeavyIonsAnalysis.EventAnalysis.hffilterPF_cfi')

#process.primaryVertexFilter = cms.EDFilter("VertexSelector",
    #src = cms.InputTag("offlineSlimmedPrimaryVertices"),
    #cut = cms.string("!isFake && abs(z) <= 25 && position.Rho <= 2"), # && tracksSize >= 2"),                             
    #filter = cms.bool(True),   # otherwise it won't filter the events                                   

#)
##--for Noscarping----                                                                                                                     
process.NoScraping = cms.EDFilter("FilterOutScraping",
                                  applyfilter = cms.untracked.bool(True),
                                  debugOn = cms.untracked.bool(False),
                                  numtrack = cms.untracked.uint32(10),
                                  thresh = cms.untracked.double(0.25)
                                 )

process.load("HeavyIonsAnalysis.VertexAnalysis.PAPileUpVertexFilter_cff")
process.PAprimaryVertexFilter = cms.EDFilter("VertexSelector",
                                             src = cms.InputTag("offlinePrimaryVertices"),
                                             cut = cms.string("!isFake && abs(z) <= 25 && position.Rho <= 2 && tracksSize >= 2"),
                                             filter = cms.bool(True), # otherwise it won't filter the events                               
                                             )
process.load("HeavyIonsAnalysis.Configuration.hfCoincFilter_cff")
from Analyzer.RaghuV0Ana.pileUpFilter_cff import *
process.Filter =olvFilter_pPb8TeV_dz1p0
#process.pileUpFilterpPb =olvFilter_pPb8TeV_dz1p0

    #process.clusterCompatibilityFilter
     #process.phfCoincFilter 
#adding hlt from RB
from Analyzer.RaghuV0Ana.hltFilter_cff import *
process.defaultTrigSel = hlt185.clone()
#process.hltHM185 =hlt185

#added
from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel
process.hltfilter = hltHighLevel.clone(
    HLTPaths = [
        #"HLT_MinimumBiasHF_OR_BptxAND_v1"
        "HLT_PAFullTracks_Multiplicity185*"
        #"HLT_PAFullTracks_Multiplicity185_part*"
        #"HLT_PAFullTracks_Multiplicity185_*_v*"
    ]
)
    
#from HeavyIonsAnalysis.TrackAnalysis.unpackedTracksAndVertices_cfi import *
#process.unpackedTracksAndVertices = unpackedTracksAndVertices

# __________________ Analyze Sequence _________________
# Load you analyzer with initial configuration
process.load("Analyzer.RaghuV0Ana.raghuv0ana_cff")
#process.load("RaghuAna.Analyzer.raghuv0ana_cff") 
process.RAGHUV0   = process.V0ana.clone()
process.RAGHUV0.vertexSrc = cms.InputTag("offlinePrimaryVertices")
process.RAGHUV0.packedCandidates = cms.InputTag("packedPFCandidates")
process.RAGHUV0.trackAssociation = cms.InputTag("unpackedTracksAndVertices")
process.RAGHUV0.tracksSrc = cms.InputTag("packedPFCandidates")
process.RAGHUV0.recoTracksSrc = cms.InputTag("generalTracks")
process.RAGHUV0.V0Src_jpsi = cms.InputTag("onia2MuMuPatGlbGlb", "", "Onia2MuMuPAT")
# Inclusive multiplicity mode (all ntrack in one bin by default).
process.RAGHUV0.ntrkbin_binedge = cms.untracked.vdouble(0, 100000)
#process.RAGHUV0.isMC = cms.untracked.bool(False)

process.p = cms.Path(
    process.defaultTrigSel *   #select events 185 to 250
    #process.hltfilter *
    process.NoScraping *
    process.PAprimaryVertexFilter *
    process.hfCoincFilter *
    #process.pileUpFilterpPb *
    process.Filter*
    process.RAGHUV0
)
