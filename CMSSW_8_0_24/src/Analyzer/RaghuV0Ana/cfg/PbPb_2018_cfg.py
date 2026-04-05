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
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
#process.load('Configuration.StandardSequences.MagneticField_38T_cff')
#process.load('RecoVertex.PrimaryVertexProducer.OfflinePrimaryVerticesRecovery_cfi')
#process.load('RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi')
process.load("PhysicsTools.PatAlgos.slimming.packedPFCandidates_cff")
process.load('RecoHI.HiEvtPlaneAlgos.HiEvtPlane_cfi')
process.load('RecoHI.HiEvtPlaneAlgos.hiEvtPlaneFlat_cfi')

# Configure the number of maximum event the analyser run on in interactive mode
# -1 == ALL
process.maxEvents = cms.untracked.PSet( 
    #input = cms.untracked.int32(-1) 
    input = cms.untracked.int32(5000) 
    )

# __________________ I/O files _________________

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
#"root://cms-xrd-global.cern.ch://store/user/qwang/V0Production2018/HIMinimumBias4/V0Skim_v3/190827_145751/0001/reco_1087.root" #--HM4
#"/store/group/phys_heavyions/qwang/V0Production2018/MinBias_Hydjet_Drum5F_2018_5p02TeV/crab_HydjetDrum5F_RECODEBUG_V0Skim_v2/190903_212414/0000/reco_Hydjet_1.root"
                                #'/store/user/bibehera/IonPhysics29/2pc_OO_V0_IP29/250724_214159/0000/OO_KS_LM_Test_data_4.root',
                                #"/store/user/bibehera/IonPhysics0/V0_OO_IP0_Run2025_MiniAOD/250724_195542/0000/OO_KS_LM_Test_data_1.root",
                                '/store/user/bibehera/IonPhysics0/2pc_OO_V0_IP0/250724_211030/0000/OO_KS_LM_Test_data_10.root',
#                                '/store/user/bibehera/IonPhysics0/V0_OO_IP0_Run2025_MiniAOD/250724_195542/0000/OO_KS_LM_Test_data_100.root'
        ),
                            secondaryFileNames = cms.untracked.vstring(
#'root://cms-xrd-global.cern.ch://store/hidata/HIRun2018A/HIMinimumBias4/AOD/04Apr2019-v1/240006/F6653E6D-7A54-4743-AB66-8CD0E890141C.root' #--HM4
                                 '/store/hidata/OORun2025/IonPhysics0/MINIAOD/PromptReco-v1/000/394/183/00000/834141d5-45f7-4032-bb25-5d32a5a14a53.root',
                                '/store/hidata/OORun2025/IonPhysics0/MINIAOD/PromptReco-v1/000/394/183/00000/a084027c-71a4-44dd-a0b2-a2d02d803c9e.root',
                                #'/store/hidata/OORun2025/IonPhysics29/MINIAOD/PromptReco-v1/000/394/153/00000/8cd2f4ad-50e2-474c-85da-291ae1c088d2.root'
                                #'/store/hidata/OORun2025/IonPhysics29/MINIAOD/PromptReco-v1/000/394/153/00000/365e206c-3668-40e9-ad8b-25705a762007.root',
                                #'/store/hidata/OORun2025/IonPhysics29/MINIAOD/PromptReco-v1/000/394/153/00000/9b4fa640-ed3a-4a27-a769-77057d003b72.root',
                               # '/store/hidata/OORun2025/IonPhysics0/MINIAOD/PromptReco-v1/000/394/183/00000/796c5018-38b9-41c9-bd12-5a60b3183c5c.root',
                               #'/store/hidata/OORun2025/IonPhysics0/MINIAOD/PromptReco-v1/000/394/183/00000/834141d5-45f7-4032-bb25-5d32a5a14a53.root',
                                #'/store/hidata/OORun2025/IonPhysics0/MINIAOD/PromptReco-v1/000/394/183/00000/a084027c-71a4-44dd-a0b2-a2d02d803c9e.root',
#                                '/store/hidata/OORun2025/IonPhysics0/MINIAOD/PromptReco-v1/000/394/184/00000/7469570e-591e-4b9b-952d-fd09ec4cd684.root',
#                                '/store/hidata/OORun2025/IonPhysics0/MINIAOD/PromptReco-v1/000/394/184/00000/c5d44688-20b6-45eb-8aa6-5f1816a02e67.root'

),
                            )     



# Define output file name
import os
process.TFileService = cms.Service("TFileService",
         #fileName = cms.string('KS_daucut_check_reco_match.root')
         fileName = cms.string('V0_test_IM_newpT.root')
)
#process.options = cms.untracked.PSet(
#SkipEvent = cms.untracked.vstring('ProductNotFound')
#)
process.options = cms.untracked.PSet(
    #wantSummary = cms.untracked.bool(True),
    Rethrow = cms.untracked.vstring('ProductNotFound')
    #TryToContinue = cms.untracked.vstring('ProductNotFound')
)

##json
#import FWCore.PythonUtilities.LumiList as LumiList
#process.source.lumisToProcess = LumiList.LumiList(filename = 'dummy.json').getVLuminosityBlockRange()



# __________________ Detector conditions _________________

# Configure the Global Tag

#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
#from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '103X_dataRun2_Prompt_v2', '')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag

process.GlobalTag = GlobalTag(process.GlobalTag, '150X_dataRun3_Prompt_v3', '')

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
#process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
#process.load('HeavyIonsAnalysis.Configuration.hfCoincFilter_cff')

# __________________ Event selection _________________                                                                                                     
process.load('HeavyIonsAnalysis.EventAnalysis.skimanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.collisionEventSelection_cff')
process.load('HeavyIonsAnalysis.EventAnalysis.hffilterPF_cfi')

process.primaryVertexFilter = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlineSlimmedPrimaryVertices"),
    cut = cms.string("!isFake && abs(z) <= 25 && position.Rho <= 2"), # && tracksSize >= 2"),                             
    filter = cms.bool(True),   # otherwise it won't filter the events                                   

)

from HeavyIonsAnalysis.TrackAnalysis.unpackedTracksAndVertices_cfi import *
process.unpackedTracksAndVertices = unpackedTracksAndVertices
process.load('HeavyIonsAnalysis.VertexAnalysis.pileupvertexfilter_cfi')
process.pileupvertexfilter.doOO = True
process.pileupvertexfilter.doNeNe = False

process.eventSelections = cms.Sequence(
    process.phfCoincFilterPF2Th4 *
    process.primaryVertexFilter *
    process.clusterCompatibilityFilter *
    process.unpackedTracksAndVertices *
    process.pileupvertexfilter
)
 
from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel
process.hltfilter = hltHighLevel.clone(
    HLTPaths = [
        "HLT_MinimumBiasHF_OR_BptxAND_v1"

    ]
)
    


# __________________ Analyze Sequence _________________
# Load you analyzer with initial configuration
process.load("Analyzer.RaghuV0Ana.raghuv0ana_cff")
process.RAGHUV0   = process.V0ana.clone()
#process.RAGHUV0.isMC = cms.untracked.bool(False)

process.p = cms.Path(process.eventSelections *
                     #process.centralityBin *
                     process.hltfilter *
                     process.RAGHUV0 )
                     
