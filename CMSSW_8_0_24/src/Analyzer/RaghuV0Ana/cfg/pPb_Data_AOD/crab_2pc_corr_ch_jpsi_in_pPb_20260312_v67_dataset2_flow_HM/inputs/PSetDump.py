import FWCore.ParameterSet.Config as cms

process = cms.Process("RaghuV0Ana")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/user/singhm/PAHighMultiplicity1/JPsi_HiSkim_pPb_2016_v2/260308_202326/0000/onia2MuMuPAT_DATA_pPb80X_11.root'),
    secondaryFileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/hidata/PARun2016C/PAHighMultiplicity1/AOD/PromptReco-v1/000/285/505/00000/1C87A9F1-8DAF-E611-82E8-FA163EF22524.root')
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

process.MEtoEDMConverter = cms.EDProducer("MEtoEDMConverter",
    Frequency = cms.untracked.int32(50),
    MEPathToSave = cms.untracked.string(''),
    Name = cms.untracked.string('MEtoEDMConverter'),
    Verbosity = cms.untracked.int32(0),
    deleteAfterCopy = cms.untracked.bool(True)
)


process.hiEvtPlane = cms.EDProducer("EvtPlaneProducer",
    CentBinCompression = cms.int32(5),
    FlatOrder = cms.int32(9),
    NumFlatBins = cms.int32(40),
    caloCentRef = cms.double(80.0),
    caloCentRefWidth = cms.double(5.0),
    caloTag = cms.InputTag("towerMaker"),
    castorTag = cms.InputTag("CastorTowerReco"),
    centralityBinTag = cms.InputTag("centralityBin","HFtowers"),
    centralityVariable = cms.string('HFtowers'),
    chi2 = cms.double(40.0),
    dzerr = cms.double(10.0),
    loadDB = cms.bool(False),
    maxet = cms.double(-1.0),
    maxpt = cms.double(3.0),
    maxvtx = cms.double(25.0),
    minet = cms.double(-1.0),
    minpt = cms.double(0.3),
    minvtx = cms.double(-25.0),
    nonDefaultGlauberModel = cms.string(''),
    trackTag = cms.InputTag("hiGeneralTracks"),
    vertexTag = cms.InputTag("hiSelectedVertex")
)


process.hiEvtPlaneFlat = cms.EDProducer("HiEvtPlaneFlatProducer",
    CentBinCompression = cms.int32(5),
    FlatOrder = cms.int32(9),
    Noffmax = cms.int32(10000),
    Noffmin = cms.int32(-1),
    NumFlatBins = cms.int32(40),
    caloCentRef = cms.double(80.0),
    caloCentRefWidth = cms.double(5.0),
    centralityBinTag = cms.InputTag("centralityBin","HFtowers"),
    centralityTag = cms.InputTag("hiCentrality"),
    centralityVariable = cms.string('HFtowers'),
    inputPlanesTag = cms.InputTag("hiEvtPlane"),
    nonDefaultGlauberModel = cms.string(''),
    trackTag = cms.InputTag("hiGeneralTracks"),
    useOffsetPsi = cms.bool(True),
    vertexTag = cms.InputTag("hiSelectedVertex")
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.towersAboveThreshold = cms.EDProducer("CaloTowerCandidateCreator",
    minimumE = cms.double(3.0),
    minimumEt = cms.double(0.0),
    src = cms.InputTag("towerMaker"),
    verbose = cms.untracked.int32(0)
)


process.Filter = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 999.0, 999.0, 999.0, 999.0, 
        4.0, 1.5, 1.0, 0.8, 0.6, 
        0.5, 0.4, 0.3, 0.2, 0.2, 
        0.2, 0.2, 0.1, 0.1, 0.1, 
        0.0, 0.0, 0.0, 0.0),
    dzTolerance = cms.double(1.0),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.NoScraping = cms.EDFilter("FilterOutScraping",
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False),
    numtrack = cms.untracked.uint32(10),
    thresh = cms.untracked.double(0.25)
)


process.PAprimaryVertexFilter = cms.EDFilter("VertexSelector",
    cut = cms.string('!isFake && abs(z) <= 25 && position.Rho <= 2 && tracksSize >= 2'),
    filter = cms.bool(True),
    src = cms.InputTag("offlinePrimaryVertices")
)


process.hfNegFilter = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegFilter2 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(2),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegFilter3 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(3),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegFilter4 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(4),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegFilter5 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(5),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegTowers = cms.EDFilter("EtaPtMinCandSelector",
    etaMax = cms.double(-3.0),
    etaMin = cms.double(-6.0),
    ptMin = cms.double(0),
    src = cms.InputTag("towersAboveThreshold")
)


process.hfPosFilter = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosFilter2 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(2),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosFilter3 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(3),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosFilter4 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(4),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosFilter5 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(5),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosTowers = cms.EDFilter("EtaPtMinCandSelector",
    etaMax = cms.double(6.0),
    etaMin = cms.double(3.0),
    ptMin = cms.double(0),
    src = cms.InputTag("towersAboveThreshold")
)


process.hltfilter = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring('HLT_PAFullTracks_Multiplicity185*'),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    throw = cms.bool(True)
)


process.pileupVertexFilterCutE = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(True),
    doDzNtrkCut = cms.bool(False),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 3.0, 2.4, 2.0, 1.2, 
        1.2, 0.9, 0.6),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutEandG = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(True),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 3.0, 2.4, 2.0, 1.2, 
        1.2, 0.9, 0.6),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutG = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 3.0, 2.4, 2.0, 1.2, 
        1.2, 0.9, 0.6),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutGloose = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 4.5, 3.2, 3.0, 1.8, 
        1.8, 1.35, 0.9),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutGplus = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(0.05),
    dzCutByNtrk = cms.vdouble(999.0, 999.0, 999.0, 3.0, 2.0, 
        1.6, 1.4, 1.2, 1.1, 1.0, 
        0.9, 0.8, 0.7, 0.7, 0.6, 
        0.6, 0.5, 0.5, 0.4, 0.4, 
        0.4, 0.3, 0.3, 0.3, 0.3, 
        0.3, 0.2, 0.2, 0.2, 0.2, 
        0.0),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutGplusNV = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 999.0, 999.0, 3.0, 2.0, 
        1.6, 1.4, 1.2, 1.1, 1.0, 
        0.9, 0.8, 0.7, 0.7, 0.6, 
        0.6, 0.5, 0.5, 0.4, 0.4, 
        0.4, 0.3, 0.3, 0.3, 0.3, 
        0.3, 0.2, 0.2, 0.2, 0.2, 
        0.0),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutGplusUpsPP = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 999.0, 1.5, 1.0, 0.8, 
        0.6, 0.5, 0.4, 0.3, 0.2, 
        0.2, 0.2, 0.2, 0.2, 0.2, 
        0.2, 0.0),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutGplusplus = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(False),
    doSurfaceCut = cms.bool(True),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(0.05),
    dzCutByNtrk = cms.vdouble(999.0, 3.0, 2.4, 2.0, 1.2, 
        1.2, 0.9, 0.6),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(28.593, -1.525, 2.636788, -1.5e-05, 200.0, 
        0.0),
    surfaceFunctionString = cms.string('[0]*exp([1]*(x-([3]*(y-[4])**2+[5])))+[2]'),
    surfaceMinDzEval = cms.double(0.0),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutGtight = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 2.0, 1.6, 1.333, 0.8, 
        0.8, 0.6, 0.4),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutW = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(False),
    doSurfaceCut = cms.bool(True),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 3.0, 2.4, 2.0, 1.2, 
        1.2, 0.9, 0.6),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutWplus = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(False),
    doSurfaceCut = cms.bool(True),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(0.05),
    dzCutByNtrk = cms.vdouble(999.0, 3.0, 2.4, 2.0, 1.2, 
        1.2, 0.9, 0.6),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.MEtoMEComparitor = cms.EDAnalyzer("MEtoMEComparitor",
    Diffgoodness = cms.double(0.1),
    KSgoodness = cms.double(0.9),
    MEtoEDMLabel = cms.string('MEtoEDMConverter'),
    OverAllgoodness = cms.double(0.9),
    autoProcess = cms.bool(True),
    dirDepth = cms.uint32(1),
    lumiInstance = cms.string('MEtoEDMConverterLumi'),
    processNew = cms.string('RERECO'),
    processRef = cms.string('HLT'),
    runInstance = cms.string('MEtoEDMConverterRun')
)


process.RAGHUV0 = cms.EDAnalyzer("RaghuV0Ana",
    Chi2Max = cms.untracked.double(7.0),
    DCAMax = cms.untracked.double(0.5),
    DecayXYZMin = cms.untracked.double(5.0),
    EtaMax = cms.untracked.double(2.4),
    EtaMaxJ = cms.untracked.double(8.0),
    EtaMin = cms.untracked.double(-2.4),
    EtaMinJ = cms.untracked.double(-8.0),
    MassMax = cms.untracked.double(3.5),
    MassMax_jpsi = cms.untracked.double(3.5),
    MassMin = cms.untracked.double(2.6),
    MassMin_jpsi = cms.untracked.double(2.6),
    RapMax1 = cms.untracked.double(2.4),
    RapMax2 = cms.untracked.double(-1.4),
    RapMin1 = cms.untracked.double(1.4),
    RapMin2 = cms.untracked.double(-2.4),
    ThetaXYZMin = cms.untracked.double(0.999),
    V0Src_jpsi = cms.InputTag("onia2MuMuPatGlbGlb","","Onia2MuMuPAT"),
    binTable = cms.untracked.vdouble(0, 0.717572, 1.43514, 2.15272, 2.87029, 
        3.58786, 4.30543, 5.023, 5.74057, 6.45815, 
        7.17572, 7.89329, 8.61086, 9.32843, 10.046, 
        10.5615, 10.9358, 11.3222, 11.7114, 12.1054, 
        12.5071, 12.9114, 13.3242, 13.7529, 14.1895, 
        14.6323, 15.0788, 15.5384, 16.0017, 16.4718, 
        16.954, 17.4529, 17.965, 18.4818, 19.0081, 
        19.5384, 20.0798, 20.6295, 21.1904, 21.7624, 
        22.3333, 22.9144, 23.5082, 24.108, 24.7103, 
        25.3327, 25.9643, 26.6021, 27.2404, 27.8889, 
        28.551, 29.2201, 29.8838, 30.5609, 31.2582, 
        31.959, 32.6755, 33.3996, 34.127, 34.8736, 
        35.624, 36.3835, 37.1513, 37.9462, 38.7306, 
        39.5312, 40.3522, 41.1784, 41.9996, 42.8382, 
        43.7007, 44.5735, 45.4614, 46.3438, 47.2291, 
        48.1364, 49.0614, 49.9993, 50.9485, 51.9135, 
        52.8921, 53.8808, 54.8964, 55.893, 56.9136, 
        57.9568, 59.0177, 60.0888, 61.1833, 62.2824, 
        63.399, 64.5337, 65.6807, 66.8337, 68.0214, 
        69.219, 70.4243, 71.651, 72.9014, 74.165, 
        75.4546, 76.7537, 78.0703, 79.4045, 80.7569, 
        82.1322, 83.5298, 84.9421, 86.3744, 87.8423, 
        89.3304, 90.8548, 92.361, 93.9159, 95.4992, 
        97.0799, 98.6655, 100.303, 101.96, 103.647, 
        105.32, 107.036, 108.77, 110.55, 112.332, 
        114.116, 115.936, 117.785, 119.708, 121.683, 
        123.605, 125.589, 127.588, 129.583, 131.654, 
        133.746, 135.887, 138.016, 140.191, 142.401, 
        144.623, 146.867, 149.14, 151.514, 153.909, 
        156.277, 158.74, 161.209, 163.662, 166.177, 
        168.728, 171.298, 173.901, 176.575, 179.302, 
        182.038, 184.793, 187.576, 190.47, 193.355, 
        196.279, 199.296, 202.355, 205.406, 208.567, 
        211.746, 215.007, 218.296, 221.624, 224.981, 
        228.464, 231.972, 235.5, 239.147, 242.785, 
        246.538, 250.308, 254.2, 258.246, 262.353, 
        266.531, 270.819, 275.228, 279.794, 284.51, 
        289.356, 294.368, 299.561, 305.114, 310.888, 
        316.984, 323.451, 330.516, 337.981, 346.265, 
        355.527, 366.193, 379.001, 395.659, 421.298, 
        1000),
    bkgFactor = cms.untracked.uint32(10),
    dauNhitsMin = cms.untracked.int32(4),
    dauPixelhitsMin = cms.untracked.int32(1),
    dau_etaphi = cms.untracked.double(1e-13),
    dbCent = cms.untracked.InputTag("centralityBin","HFtowers"),
    del_R = cms.untracked.double(0.03),
    isMC = cms.untracked.bool(False),
    mSB1High = cms.untracked.double(2.95),
    mSB1Low = cms.untracked.double(2.7),
    mSB2High = cms.untracked.double(3.45),
    mSB2Low = cms.untracked.double(3.23),
    mSigHigh = cms.untracked.double(3.18),
    mSigLow = cms.untracked.double(3.0),
    mis_jpsi_range = cms.untracked.double(0.02),
    mis_ph_range = cms.untracked.double(0.015),
    mvaCut = cms.untracked.double(0.2),
    mvaXML = cms.untracked.InputTag("MC_Full_BDT250_D4.LM.weights.xml"),
    nmass_jpsi_binedge = cms.untracked.vdouble(2.5933, 2.7023, 2.8172, 2.9331, 3.0379, 
        3.1367, 3.2448, 3.3676, 3.496),
    npt_binedge = cms.untracked.vdouble(0.2, 1.8, 3.0, 4.5, 6.0, 
        8.0, 10.0),
    ntrkbin_binedge = cms.untracked.vdouble(0, 100000),
    pTmaxTrk_ass = cms.untracked.vdouble(3.0),
    pTmaxTrk_ass_jpsi = cms.untracked.double(3.0),
    pTmaxTrk_trg = cms.untracked.vdouble(10.0),
    pTmaxTrk_trg_jpsi = cms.untracked.double(10.0),
    pTminTrk_ass = cms.untracked.vdouble(0.3),
    pTminTrk_ass_jpsi = cms.untracked.double(0.3),
    pTminTrk_trg = cms.untracked.vdouble(1.0),
    pTminTrk_trg_jpsi = cms.untracked.double(1.0),
    packedCandidates = cms.InputTag("packedPFCandidates"),
    ptMax = cms.untracked.double(10.0),
    ptMax_ch = cms.untracked.double(3.0),
    ptMin = cms.untracked.double(1.0),
    ptMin_ch = cms.untracked.double(0.3),
    recoTracksSrc = cms.InputTag("generalTracks"),
    trackAssociation = cms.InputTag("unpackedTracksAndVertices"),
    tracks = cms.InputTag("genParticles"),
    tracksSrc = cms.InputTag("packedPFCandidates"),
    vertexSrc = cms.InputTag("offlinePrimaryVertices"),
    zmaxVtx = cms.untracked.double(15.0),
    zminVtx = cms.untracked.double(-15.0)
)


process.V0ana = cms.EDAnalyzer("RaghuV0Ana",
    Chi2Max = cms.untracked.double(7.0),
    DCAMax = cms.untracked.double(0.5),
    DecayXYZMin = cms.untracked.double(5.0),
    EtaMax = cms.untracked.double(2.4),
    EtaMaxJ = cms.untracked.double(8.0),
    EtaMin = cms.untracked.double(-2.4),
    EtaMinJ = cms.untracked.double(-8.0),
    MassMax = cms.untracked.double(3.5),
    MassMax_jpsi = cms.untracked.double(3.5),
    MassMin = cms.untracked.double(2.6),
    MassMin_jpsi = cms.untracked.double(2.6),
    RapMax1 = cms.untracked.double(2.4),
    RapMax2 = cms.untracked.double(-1.4),
    RapMin1 = cms.untracked.double(1.4),
    RapMin2 = cms.untracked.double(-2.4),
    ThetaXYZMin = cms.untracked.double(0.999),
    V0Src_jpsi = cms.InputTag("onia2MuMuPatGlbGlb","","Onia2MuMuPAT"),
    binTable = cms.untracked.vdouble(0, 0.717572, 1.43514, 2.15272, 2.87029, 
        3.58786, 4.30543, 5.023, 5.74057, 6.45815, 
        7.17572, 7.89329, 8.61086, 9.32843, 10.046, 
        10.5615, 10.9358, 11.3222, 11.7114, 12.1054, 
        12.5071, 12.9114, 13.3242, 13.7529, 14.1895, 
        14.6323, 15.0788, 15.5384, 16.0017, 16.4718, 
        16.954, 17.4529, 17.965, 18.4818, 19.0081, 
        19.5384, 20.0798, 20.6295, 21.1904, 21.7624, 
        22.3333, 22.9144, 23.5082, 24.108, 24.7103, 
        25.3327, 25.9643, 26.6021, 27.2404, 27.8889, 
        28.551, 29.2201, 29.8838, 30.5609, 31.2582, 
        31.959, 32.6755, 33.3996, 34.127, 34.8736, 
        35.624, 36.3835, 37.1513, 37.9462, 38.7306, 
        39.5312, 40.3522, 41.1784, 41.9996, 42.8382, 
        43.7007, 44.5735, 45.4614, 46.3438, 47.2291, 
        48.1364, 49.0614, 49.9993, 50.9485, 51.9135, 
        52.8921, 53.8808, 54.8964, 55.893, 56.9136, 
        57.9568, 59.0177, 60.0888, 61.1833, 62.2824, 
        63.399, 64.5337, 65.6807, 66.8337, 68.0214, 
        69.219, 70.4243, 71.651, 72.9014, 74.165, 
        75.4546, 76.7537, 78.0703, 79.4045, 80.7569, 
        82.1322, 83.5298, 84.9421, 86.3744, 87.8423, 
        89.3304, 90.8548, 92.361, 93.9159, 95.4992, 
        97.0799, 98.6655, 100.303, 101.96, 103.647, 
        105.32, 107.036, 108.77, 110.55, 112.332, 
        114.116, 115.936, 117.785, 119.708, 121.683, 
        123.605, 125.589, 127.588, 129.583, 131.654, 
        133.746, 135.887, 138.016, 140.191, 142.401, 
        144.623, 146.867, 149.14, 151.514, 153.909, 
        156.277, 158.74, 161.209, 163.662, 166.177, 
        168.728, 171.298, 173.901, 176.575, 179.302, 
        182.038, 184.793, 187.576, 190.47, 193.355, 
        196.279, 199.296, 202.355, 205.406, 208.567, 
        211.746, 215.007, 218.296, 221.624, 224.981, 
        228.464, 231.972, 235.5, 239.147, 242.785, 
        246.538, 250.308, 254.2, 258.246, 262.353, 
        266.531, 270.819, 275.228, 279.794, 284.51, 
        289.356, 294.368, 299.561, 305.114, 310.888, 
        316.984, 323.451, 330.516, 337.981, 346.265, 
        355.527, 366.193, 379.001, 395.659, 421.298, 
        1000),
    bkgFactor = cms.untracked.uint32(10),
    dauNhitsMin = cms.untracked.int32(4),
    dauPixelhitsMin = cms.untracked.int32(1),
    dau_etaphi = cms.untracked.double(1e-13),
    dbCent = cms.untracked.InputTag("centralityBin","HFtowers"),
    del_R = cms.untracked.double(0.03),
    isMC = cms.untracked.bool(False),
    mSB1High = cms.untracked.double(2.95),
    mSB1Low = cms.untracked.double(2.7),
    mSB2High = cms.untracked.double(3.45),
    mSB2Low = cms.untracked.double(3.23),
    mSigHigh = cms.untracked.double(3.18),
    mSigLow = cms.untracked.double(3.0),
    mis_jpsi_range = cms.untracked.double(0.02),
    mis_ph_range = cms.untracked.double(0.015),
    mvaCut = cms.untracked.double(0.2),
    mvaXML = cms.untracked.InputTag("MC_Full_BDT250_D4.LM.weights.xml"),
    nmass_jpsi_binedge = cms.untracked.vdouble(2.5933, 2.7023, 2.8172, 2.9331, 3.0379, 
        3.1367, 3.2448, 3.3676, 3.496),
    npt_binedge = cms.untracked.vdouble(0.2, 1.8, 3.0, 4.5, 6.0, 
        8.0, 10.0),
    ntrkbin_binedge = cms.untracked.vdouble(0, 100000),
    pTmaxTrk_ass = cms.untracked.vdouble(3.0),
    pTmaxTrk_ass_jpsi = cms.untracked.double(3.0),
    pTmaxTrk_trg = cms.untracked.vdouble(10.0),
    pTmaxTrk_trg_jpsi = cms.untracked.double(10.0),
    pTminTrk_ass = cms.untracked.vdouble(0.3),
    pTminTrk_ass_jpsi = cms.untracked.double(0.3),
    pTminTrk_trg = cms.untracked.vdouble(1.0),
    pTminTrk_trg_jpsi = cms.untracked.double(1.0),
    packedCandidates = cms.InputTag("packedPFCandidates"),
    ptMax = cms.untracked.double(10.0),
    ptMax_ch = cms.untracked.double(3.0),
    ptMin = cms.untracked.double(1.0),
    ptMin_ch = cms.untracked.double(0.3),
    recoTracksSrc = cms.InputTag("generalTracks"),
    trackAssociation = cms.InputTag("unpackedTracksAndVertices"),
    tracks = cms.InputTag("genParticles"),
    tracksSrc = cms.InputTag("packedPFCandidates"),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
    zmaxVtx = cms.untracked.double(15.0),
    zminVtx = cms.untracked.double(-15.0)
)


process.hfCoincFilter = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter+process.hfNegFilter)


process.endOfProcess_withComparison = cms.Sequence(process.MEtoEDMConverter+process.MEtoMEComparitor)


process.endOfProcess = cms.Sequence(process.MEtoEDMConverter)


process.hfposTowers = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers)


process.hfnegTowers = cms.Sequence(process.towersAboveThreshold+process.hfNegTowers)


process.hfCoincFilter4 = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter4+process.hfNegFilter4)


process.hfCoincFilter5 = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter5+process.hfNegFilter5)


process.hfposFilter4 = cms.Sequence(process.hfposTowers+process.hfPosFilter4)


process.hfposFilter5 = cms.Sequence(process.hfposTowers+process.hfPosFilter5)


process.hfposFilter2 = cms.Sequence(process.hfposTowers+process.hfPosFilter2)


process.hfposFilter3 = cms.Sequence(process.hfposTowers+process.hfPosFilter3)


process.hfCoincFilter2 = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter2+process.hfNegFilter2)


process.hfCoincFilter3 = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter3+process.hfNegFilter3)


process.hfnegFilter = cms.Sequence(process.hfnegTowers+process.hfNegFilter)


process.hfnegFilter2 = cms.Sequence(process.hfnegTowers+process.hfNegFilter2)


process.hfnegFilter3 = cms.Sequence(process.hfnegTowers+process.hfNegFilter3)


process.hfposFilter = cms.Sequence(process.hfposTowers+process.hfPosFilter)


process.hfnegFilter4 = cms.Sequence(process.hfnegTowers+process.hfNegFilter4)


process.hfnegFilter5 = cms.Sequence(process.hfnegTowers+process.hfNegFilter5)


process.p = cms.Path(process.hltfilter+process.NoScraping+process.PAprimaryVertexFilter+process.hfCoincFilter+process.Filter+process.RAGHUV0)


process.DQMStore = cms.Service("DQMStore")


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1000)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(987346)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(98765432)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(6541321)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(654321)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(234567)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    famosSimHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(13579)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(88776655)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(6453209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(54525)
    ),
    saveFileName = cms.untracked.string(''),
    siTrackerGaussianSmearingRecHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(24680)
    ),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11223344)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('cent_pPb_flow_jpsi.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer")


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.XMLFromDBSource = cms.ESProducer("XMLIdealGeometryESProducer",
    label = cms.string('Extended'),
    rootDDName = cms.string('cms:OCMS')
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(cms.PSet(
        Label = cms.untracked.string(''),
        NormalizationFactor = cms.untracked.double(1.0),
        Record = cms.string('SiStripApvGainRcd')
    ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('80X_dataRun2_Prompt_v15'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    toGet = cms.VPSet(cms.PSet(
        connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
        label = cms.untracked.string('HFtowers'),
        record = cms.string('HeavyIonRcd'),
        tag = cms.string('CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1033p1x01_offline')
    ))
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HERecalibration = cms.bool(False),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalibration = cms.bool(False),
    iLumi = cms.double(-1.0),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths')
)


process.prefer("es_hardcode")

