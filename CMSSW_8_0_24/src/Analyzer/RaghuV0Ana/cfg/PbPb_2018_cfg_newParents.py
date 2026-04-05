import FWCore.ParameterSet.Config as cms
process = cms.Process("RaghuV0Ana")


# __________________ General _________________

# Configure the logger
process.load('Configuration.StandardSequences.Services_cff')
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load("RecoVertex.PrimaryVertexProducer.OfflinePrimaryVerticesRecovery_cfi")

# Configure the number of maximum event the analyser run on in interactive mode
# -1 == ALL
process.maxEvents = cms.untracked.PSet( 
    #input = cms.untracked.int32(-1) 
    input = cms.untracked.int32(500) 
    )


# __________________ I/O files _________________

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
#"root://cms-xrd-global.cern.ch://store/user/qwang/V0Production2018/HIMinimumBias4/V0Skim_v3/190827_145751/0001/reco_1087.root" #--HM4
"/store/himc/HINPbPbAutumn18DR/MinBias_Hydjet_Drum5F_2018_5p02TeV/AODSIM/NoPUmva98_103X_upgrade2018_realistic_HI_v11-v1/120000/0816F843-27D9-A64F-8C27-DA319B780FBB.root"
#"/store/himc/HINPbPbAutumn18DR/MinBias_ReggeGribovPartonMC_EposLHC_2018_5p02TeV/AODSIM/NoPUmva98_103X_upgrade2018_realistic_HI_v11-v1/270000/0A5ECE89-39D1-4449-90A4-671625121057.root"
#"/store/himc/HINPbPbAutumn18DR/MinBias_AMPT_NoStringMelting_2018_5p02TeV/AODSIM/NoPU_103X_upgrade2018_realistic_HI_v11-v1/120000/096D4FDB-3CB0-BC47-940C-3F8947F01BBC.root"
#"/store/user/clindsey/MinBias_Hydjet_Drum5F_2018_5p02TeV/RECODEBUG_20190625/190626_194626/0000/step2_RAW2DIGI_L1Reco_RECO_1.root",
#"/store/user/clindsey/MinBias_Hydjet_Drum5F_2018_5p02TeV/RECODEBUG_20190625/190626_194626/0000/step2_RAW2DIGI_L1Reco_RECO_10.root"
        ),
)     



# Define output file name
import os
process.TFileService = cms.Service("TFileService",
         fileName = cms.string('kppip_test1.root')
)
process.options = cms.untracked.PSet(
SkipEvent = cms.untracked.vstring('ProductNotFound')
)
# __________________ Detector conditions _________________

# Configure the Global Tag

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '103X_dataRun2_Prompt_v2', '')

process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
process.GlobalTag.toGet.extend([
        cms.PSet(record = cms.string("HeavyIonRcd"),
                 tag = cms.string("CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1033p1x01_offline"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
                 label = cms.untracked.string("HFtowers")
                 ),
        ])
process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")
process.load('RecoHI.HiCentralityAlgos.CentralityFilter_cfi')
process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
process.load('HeavyIonsAnalysis.Configuration.hfCoincFilter_cff')

#process.eventSelections = cms.Sequence(
#    process.clusterCompatibilityFilter
#    + process.primaryVertexFilter
#    + process.hfCoincFilter2Th4
#    )
# __________________ Analyze Sequence _________________
# Load you analyzer with initial configuration
process.load("Analyzers.RaghuV0Ana.raghuv0ana_cff")
process.RAGHUV0   = process.V0ana_1030.clone()

process.p = cms.Path(#process.offlinePrimaryVerticesRecovery*
                     process.centralityBin *
                     process.RAGHUV0 )
                     
#process.offlinePrimaryVerticesRecovery.oldVertexLabel = "offlinePrimaryVertices"                                                                
#from HLTrigger.Configuration.CustomConfigs import MassReplaceInputTag                                                                           
#process = MassReplaceInputTag(process,"offlinePrimaryVertices","offlinePrimaryVerticesRecovery")    


