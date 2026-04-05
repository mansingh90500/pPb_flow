import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
from   Configuration.StandardSequences.Eras import eras

#----------------------------------------------------------------------------

# Setup Settings for ONIA SKIM (DATA):
ispPb         = True      # pPb dataset
isMC           = False     # DATA
isPromptDATA   = True      # Prompt RECO DATA (matches dataset you gave)
keepExtraColl  = True     # keep extra collections in output
applyEventSel  = True     # apply pPb event selection (vertex + scraping)
muonSelection  = "Trk"    # Single muon selection: Glb, GlbTrk, Trk

#----------------------------------------------------------------------------

# Print Onia Skim settings:
print(" ")
print("[INFO] Settings used for ONIA SKIM: ")
print("[INFO] ispPb        = " + ("True" if ispPb else "False") )
print("[INFO] isMC          = " + ("True" if isMC else "False") )
print("[INFO] isPromptDATA  = " + ("True" if isPromptDATA else "False") )
print("[INFO] keepExtraColl = " + ("True" if keepExtraColl else "False") )
print("[INFO] applyEventSel = " + ("True" if applyEventSel else "False") )
print("[INFO] muonSelection = " + muonSelection )
print(" ")

# set up process
process = cms.Process("Onia2MuMuPAT", eras.Run2_2016_pA)

# setup 'analysis'  options
options = VarParsing.VarParsing ('analysis')

# Defaults: input file from your dataset (PromptReco AOD file)
# (this matches the file referenced in your log)
options.inputFiles = '/store/hidata/PARun2016C/PAHighMultiplicity1/AOD/PromptReco-v1/000/285/505/00000/006F1E14-85AF-E611-9F9E-02163E014508.root'
options.outputFile = 'onia2MuMuPAT_DATA_pPb80X_compare.root'
options.maxEvents = -1 # -1 means all events
#options.maxEvents = 4000
# get and parse the command line arguments
options.parseArguments()

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

# load the Geometry and Magnetic Field for the TransientTrackBuilder
process.load('Configuration.StandardSequences.Services_cff')
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
# Use heavy-ions reconstruction for pA era as in your original DATA cfg
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')

# Global Tag (Prompt data)
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_Prompt_v15', '')
# avoid trigger prescale errors like in your previous cfg
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")

# Centrality for pPb
process.load('RecoHI.HiCentralityAlgos.pACentrality_cfi')

# HLT Dimuon / pPb triggers
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltOniaHI = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()

# Use wildcarded HLT names to avoid exact-version mismatches and also include
# the pA multiplicity triggers that may exist in the dataset.
process.hltOniaHI.HLTPaths = [
    "HLT_PADoubleMuOpen_HFOneTowerVeto_v*",
    "HLT_PADoubleMuOpen_HFOneTowerVeto_SingleTrack_v*",
    "HLT_PADoubleMuOpen_HFTwoTowerVeto_SingleTrack_v*",
    "HLT_PASingleMuOpen_HFOneTowerVeto_v*",
    "HLT_PASingleMuOpen_HFTwoTowerVeto_v*",
    "HLT_PASingleMuOpen_PixelTrackGt0Lt10_v*",
    "HLT_PASingleMuOpen_PixelTrackGt0Lt15_v*",
    "HLT_PAFullTracks_Multiplicity120_v*",
    "HLT_PAFullTracks_Multiplicity150_v*",
    "HLT_PAFullTracks_Multiplicity185_*",
    "HLT_PAFullTracks_Multiplicity220_*",
    "HLT_PAFullTracks_Multiplicity250_v*"
]
process.hltOniaHI.throw = False
process.hltOniaHI.andOr = True
process.hltOniaHI.TriggerResultsTag = cms.InputTag("TriggerResults", "", "HLT")

from HiSkim.HiOnia2MuMu.onia2MuMuPAT_cff import *
# For DATA: set MC=False, HLT="HLT", Filter=True so HLT filtering is applied
onia2MuMuPAT(process, GlobalTag=process.GlobalTag.globaltag, MC=isMC, HLT="HLT", Filter=True)

##### Onia2MuMuPAT input collections/options
process.onia2MuMuPatGlbGlb.dimuonSelection          = cms.string("mass > 0")
# For data, avoid requiring gen-level references
process.onia2MuMuPatGlbGlb.resolvePileUpAmbiguity   = False

# pPb: use generalTracks + offlinePrimaryVertices as in your earlier DATA cfg
process.onia2MuMuPatGlbGlb.srcTracks                = cms.InputTag("generalTracks")
process.onia2MuMuPatGlbGlb.primaryVertexTag         = cms.InputTag("offlinePrimaryVertices")
process.patMuonsWithoutTrigger.pvSrc                = cms.InputTag("offlinePrimaryVertices")
# For pPb Prompt data do NOT add muonless primary vertex (matches your earlier cfg)
process.onia2MuMuPatGlbGlb.addMuonlessPrimaryVertex = False

##### Dimuon pair selection
commonP1 = ""
commonP2 = ""
if muonSelection == "Glb":
    highP = "isGlobalMuon"  # At least one muon must pass this selection
    process.onia2MuMuPatGlbGlb.higherPuritySelection = cms.string("("+highP+commonP1+")"+commonP2)
    lowP = "isGlobalMuon"   # BOTH muons must pass this selection
    process.onia2MuMuPatGlbGlb.lowerPuritySelection = cms.string("("+lowP+commonP1+")"+commonP2)
elif muonSelection == "GlbTrk":
    highP = "(isGlobalMuon && isTrackerMuon)";
    process.onia2MuMuPatGlbGlb.higherPuritySelection = cms.string("("+highP+commonP1+")"+commonP2)
    lowP = "(isGlobalMuon && isTrackerMuon)";
    process.onia2MuMuPatGlbGlb.lowerPuritySelection = cms.string("("+lowP+commonP1+")"+commonP2)
elif muonSelection == "Trk":
    highP = "isTrackerMuon";
    process.onia2MuMuPatGlbGlb.higherPuritySelection = cms.string("("+highP+commonP1+")"+commonP2)
    lowP = "isTrackerMuon";
    process.onia2MuMuPatGlbGlb.lowerPuritySelection = cms.string("("+lowP+commonP1+")"+commonP2)
else:
    print("ERROR: Incorrect muon selection " + muonSelection + " . Valid options are: Glb, Trk, GlbTrk")

##### Event Selection (pPb)
if applyEventSel:
    # vertex selector (offlinePrimaryVertices) - same cut as in your original DATA cfg
    process.PAprimaryVertexFilter = cms.EDFilter("VertexSelector",
                                                 src = cms.InputTag("offlinePrimaryVertices"),
                                                 cut = cms.string("!isFake && abs(z) <= 25 && position.Rho <= 2 && tracksSize >= 2"),
                                                 filter = cms.bool(True),
                                                 )
    # Scraping filter as in your original DATA config
    process.NoScraping = cms.EDFilter("FilterOutScraping",
                                      applyfilter = cms.untracked.bool(True),
                                      debugOn = cms.untracked.bool(False),
                                      numtrack = cms.untracked.uint32(10),
                                      thresh = cms.untracked.double(0.25),
                                      )
    # Insert the vertex & scraping filters after the HLT filter in the patMuonSequence
    process.patMuonSequence.replace(process.hltOniaHI, process.hltOniaHI * process.PAprimaryVertexFilter * process.NoScraping )

##### If extra collections has to be kept (matching your earlier DATA cfg)
if keepExtraColl:
    process.outOnia2MuMu.outputCommands.append("keep *_generalTracks_*_*")
    process.outOnia2MuMu.outputCommands.append("keep *_standAloneMuons_*_*")
    process.outOnia2MuMu.outputCommands.append("keep *_towerMaker_*_*")
    process.outOnia2MuMu.outputCommands.append("keep *_Castor*Reco_*_*")
    process.outOnia2MuMu.outputCommands.append("keep *_castorreco_*_*")
    process.outOnia2MuMu.outputCommands.append("keep *_offlinePrimaryVertices_*_*")
    process.outOnia2MuMu.outputCommands.append("keep *_pACentrality_*_*")

# Source / IO
process.source.fileNames      = cms.untracked.vstring(options.inputFiles)
process.maxEvents             = cms.untracked.PSet(input = cms.untracked.int32(options.maxEvents))
process.outOnia2MuMu.fileName = cms.untracked.string(options.outputFile)

process.e  = cms.EndPath(process.outOnia2MuMu)
# Schedule Onia2MuMuPAT then output
process.schedule = cms.Schedule(process.Onia2MuMuPAT, process.e)

from Configuration.Applications.ConfigBuilder import MassReplaceInputTag
MassReplaceInputTag(process)
