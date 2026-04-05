import FWCore.ParameterSet.Config as cms

process = cms.Process("RaghuV0Ana")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/user/bibehera/IonPhysics0/2pc_OO_V0_IP0/250724_211030/0000/OO_KS_LM_Test_data_10.root'),
    secondaryFileNames = cms.untracked.vstring(
        '/store/hidata/OORun2025/IonPhysics0/MINIAOD/PromptReco-v1/000/394/183/00000/834141d5-45f7-4032-bb25-5d32a5a14a53.root',
        '/store/hidata/OORun2025/IonPhysics0/MINIAOD/PromptReco-v1/000/394/183/00000/a084027c-71a4-44dd-a0b2-a2d02d803c9e.root'
    )
)
process.CondDB = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionTimeout = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('')
)

process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(
        0.004123, 0.00602, 0.008201, 0.010489, 0.013379,
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807,
        0.058939, 0.125497
    ),
    HFdepthOneParameterB = cms.vdouble(
        -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05,
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107,
        0.000425, 0.000209
    ),
    HFdepthTwoParameterA = cms.vdouble(
        0.002861, 0.004168, 0.0064, 0.008388, 0.011601,
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447,
        0.051579, 0.086593
    ),
    HFdepthTwoParameterB = cms.vdouble(
        -2e-06, -0.0, -7e-06, -6e-06, -2e-06,
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05,
        0.000157, -3e-06
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5000),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.maxLuminosityBlocks = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.nanoDQMIO_perLSoutput = cms.PSet(
    MEsToSave = cms.untracked.vstring( (
        'Hcal/DigiTask/Occupancy/depth/depth1',
        'Hcal/DigiTask/Occupancy/depth/depth2',
        'Hcal/DigiTask/Occupancy/depth/depth3',
        'Hcal/DigiTask/Occupancy/depth/depth4',
        'Hcal/DigiTask/Occupancy/depth/depth5',
        'Hcal/DigiTask/Occupancy/depth/depth6',
        'Hcal/DigiTask/Occupancy/depth/depth7',
        'Hcal/DigiTask/Occupancy/depth/depthHO',
        'Hcal/DigiTask/OccupancyCut/depth/depth1',
        'Hcal/DigiTask/OccupancyCut/depth/depth2',
        'Hcal/DigiTask/OccupancyCut/depth/depth3',
        'Hcal/DigiTask/OccupancyCut/depth/depth4',
        'Hcal/DigiTask/OccupancyCut/depth/depth5',
        'Hcal/DigiTask/OccupancyCut/depth/depth6',
        'Hcal/DigiTask/OccupancyCut/depth/depth7',
        'Hcal/DigiTask/OccupancyCut/depth/depthHO',
        'EcalBarrel/EBOccupancyTask/EBOT digi occupancy',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -',
        'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +',
        'EcalBarrel/EBOccupancyTask/EBOT DCC entries',
        'EcalEndcap/EEOccupancyTask/EEOT DCC entries',
        'Ecal/EventInfo/processedEvents',
        'PixelPhase1/Tracks/charge_PXBarrel',
        'PixelPhase1/Tracks/charge_PXForward',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/charge_PXDisk_-3',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/size_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/size_PXDisk_-3',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm1',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm2',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm3',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalm4',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp1',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp2',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp3',
        'CSC/CSCOfflineMonitor/recHits/hRHGlobalp4',
        'GEM/RecHits/occ_xy_GE11-M-L1',
        'GEM/RecHits/occ_xy_GE11-M-L2',
        'GEM/RecHits/occ_xy_GE11-P-L1',
        'GEM/RecHits/occ_xy_GE11-P-L2',
        'GEM/Digis/occ_GE11-M-L1',
        'GEM/Digis/occ_GE11-M-L2',
        'GEM/Digis/occ_GE11-P-L1',
        'GEM/Digis/occ_GE11-P-L2',
        'HLT/Vertexing/hltPixelVertices/hltPixelVertices/goodvtxNbr',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/mon_unMatched_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_eta',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_hits',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_matched_pt',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_phi',
        'HLT/Tracking/ValidationWRTOffline/hltMergedWrtHighPurityPV/ref_pt',
        'HLT/Tracking/pixelTracks/GeneralProperties/Chi2Prob_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/Chi2oNDFVsEta_ImpactPoint_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DeltaZToPVZoom_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DistanceOfClosestApproachToPVVsPhi_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/DistanceOfClosestApproachToPVZoom_GenTk',
        'HLT/Tracking/pixelTracks/GeneralProperties/NumberOfTracks_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/Chi2Prob_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/Chi2oNDFVsEta_ImpactPoint_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DeltaZToPVZoom_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DistanceOfClosestApproachToPVVsPhi_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/DistanceOfClosestApproachToPVZoom_GenTk',
        'HLT/Tracking/tracks/GeneralProperties/NumberOfTracks_GenTk',
        'HLT/Tracking/tracks/LUMIanalysis/NumberEventsVsLUMI',
        'HLT/Tracking/tracks/PUmonitoring/NumberEventsVsGoodPVtx',
        'PixelPhase1/Tracks/num_clusters_ontrack_PXBarrel',
        'PixelPhase1/Tracks/num_clusters_ontrack_PXForward',
        'PixelPhase1/Tracks/clusterposition_zphi_ontrack',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_1',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_2',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_3',
        'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_4',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+1',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+2',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+3',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-1',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-2',
        'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-3',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4',
        'PixelPhase1/Phase1_MechanicalView/PXForward/digi_occupancy_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_1',
        'PixelPhase1/Phase1_MechanicalView/PXForward/digi_occupancy_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_2',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3',
        'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4',
        'PixelPhase1/Phase1_MechanicalView/PXForward/clusters_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_1',
        'PixelPhase1/Phase1_MechanicalView/PXForward/clusters_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__2',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__3',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__4',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__5',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__6',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__7',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__8',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__9',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__1',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__2',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__3',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__4',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__5',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__6',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__7',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__8',
        'SiStrip/MechanicalView/TEC/MINUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__9',
        'SiStrip/MechanicalView/TIB/layer_1/NormalizedHitResiduals_TIB__Layer__1',
        'SiStrip/MechanicalView/TIB/layer_2/NormalizedHitResiduals_TIB__Layer__2',
        'SiStrip/MechanicalView/TIB/layer_3/NormalizedHitResiduals_TIB__Layer__3',
        'SiStrip/MechanicalView/TIB/layer_4/NormalizedHitResiduals_TIB__Layer__4',
        'SiStrip/MechanicalView/TIB/layer_1/Summary_ClusterStoNCorr__OnTrack__TIB__layer__1',
        'SiStrip/MechanicalView/TIB/layer_2/Summary_ClusterStoNCorr__OnTrack__TIB__layer__2',
        'SiStrip/MechanicalView/TIB/layer_3/Summary_ClusterStoNCorr__OnTrack__TIB__layer__3',
        'SiStrip/MechanicalView/TIB/layer_4/Summary_ClusterStoNCorr__OnTrack__TIB__layer__4',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
        'SiStrip/MechanicalView/TID/PLUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
        'SiStrip/MechanicalView/TID/MINUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
        'SiStrip/MechanicalView/TID/MINUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
        'SiStrip/MechanicalView/TID/MINUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__2',
        'SiStrip/MechanicalView/TID/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__3',
        'SiStrip/MechanicalView/TID/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__1',
        'SiStrip/MechanicalView/TID/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__2',
        'SiStrip/MechanicalView/TID/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__3',
        'SiStrip/MechanicalView/TOB/layer_1/NormalizedHitResiduals_TOB__Layer__1',
        'SiStrip/MechanicalView/TOB/layer_2/NormalizedHitResiduals_TOB__Layer__2',
        'SiStrip/MechanicalView/TOB/layer_3/NormalizedHitResiduals_TOB__Layer__3',
        'SiStrip/MechanicalView/TOB/layer_4/NormalizedHitResiduals_TOB__Layer__4',
        'SiStrip/MechanicalView/TOB/layer_5/NormalizedHitResiduals_TOB__Layer__5',
        'SiStrip/MechanicalView/TOB/layer_6/NormalizedHitResiduals_TOB__Layer__6',
        'SiStrip/MechanicalView/TOB/layer_1/Summary_ClusterStoNCorr__OnTrack__TOB__layer__1',
        'SiStrip/MechanicalView/TOB/layer_2/Summary_ClusterStoNCorr__OnTrack__TOB__layer__2',
        'SiStrip/MechanicalView/TOB/layer_3/Summary_ClusterStoNCorr__OnTrack__TOB__layer__3',
        'SiStrip/MechanicalView/TOB/layer_4/Summary_ClusterStoNCorr__OnTrack__TOB__layer__4',
        'SiStrip/MechanicalView/TOB/layer_5/Summary_ClusterStoNCorr__OnTrack__TOB__layer__5',
        'SiStrip/MechanicalView/TOB/layer_6/Summary_ClusterStoNCorr__OnTrack__TOB__layer__6',
        'SiStrip/MechanicalView/MainDiagonal Position',
        'SiStrip/MechanicalView/NumberOfClustersInPixel',
        'SiStrip/MechanicalView/NumberOfClustersInStrip',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/TkHMap_NumberOfDigi_TIDP_D1',
        'SiStrip/MechanicalView/TID/PLUS/wheel_1/TkHMap_NumberOfCluster_TIDP_D1',
        'SiStrip/MechanicalView/TIB/layer_1/TkHMap_NumberOfDigi_TIB_L1',
        'SiStrip/MechanicalView/TIB/layer_1/TkHMap_NumberOfCluster_TIB_L1',
        'SiStrip/MechanicalView/TOB/layer_1/TkHMap_NumberOfDigi_TOB_L1',
        'SiStrip/MechanicalView/TOB/layer_1/TkHMap_NumberOfCluster_TOB_L1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/TkHMap_NumberOfDigi_TECP_W1',
        'SiStrip/MechanicalView/TEC/PLUS/wheel_1/TkHMap_NumberOfCluster_TECP_W1',
        'Tracking/TrackParameters/generalTracks/LSanalysis/Chi2oNDF_lumiFlag_GenTk',
        'Tracking/TrackParameters/generalTracks/LSanalysis/NumberOfRecHitsPerTrack_lumiFlag_GenTk',
        'Tracking/TrackParameters/generalTracks/LSanalysis/NumberOfTracks_lumiFlag_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDxyToPV_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDzToPV_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIP3DToPV_GenTk',
        'Tracking/TrackParameters/generalTracks/HitProperties/NumberOfMissingOuterRecHitsPerTrack_GenTk',
        'Tracking/TrackParameters/generalTracks/HitProperties/NumberMORecHitsPerTrackVsPt_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackEtaPhi_ImpactPoint_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/NumberOfTracks_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/NumberOfRecHitsPerTrack_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackPt_ImpactPoint_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/Chi2oNDF_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackPhi_ImpactPoint_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackEta_ImpactPoint_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/NumberOfRecHitsPerTrack_Strip_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/NumberOfRecHitsPerTrack_Pixel_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/DistanceOfClosestApproachToBS_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/DistanceOfClosestApproachToBSdz_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/DistanceOfClosestApproachToBSVsPhi_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/DistanceOfClosestApproachToBSVsEta_GenTk',
        'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackQoverP_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/Quality_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/NumberofTracks_Hardvtx_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/NumberofTracks_PUvtx_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackPtHighpurity_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackPtTight_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackPtLoose_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackEtaHighpurity_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackEtaTight_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackEtaLoose_ImpactPoint_GenTk',
        'Tracking/PrimaryVertices/highPurityTracks/pt_0to1/offline/NumberOfGoodPVtx_offline',
        'Tracking/PrimaryVertices/highPurityTracks/pt_0to1/offline/GoodPVtxNumberOfTracks_offline',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/NumberofTracks_Hardvtx_PUvtx_GenTk',
        'Tracking/PrimaryVertices/highPurityTracks/pt_0to1/offline/FractionOfGoodPVtx_offline',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TkEtaPhi_Ratio_byFoldingmap_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TkEtaPhi_Ratio_byFoldingmap_op_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TkEtaPhi_RelativeDifference_byFoldingmap_ImpactPoint_GenTk',
        'Tracking/TrackParameters/generalTracks/GeneralProperties/TkEtaPhi_RelativeDifference_byFoldingmap_op_ImpactPoint_GenTk',
        'OfflinePV/offlinePrimaryVertices/tagVtxProb',
        'OfflinePV/offlinePrimaryVertices/tagType',
        'OfflinePV/Resolution/PV/pull_x',
        'OfflinePV/Resolution/PV/pull_y',
        'OfflinePV/Resolution/PV/pull_z',
        'OfflinePV/offlinePrimaryVertices/tagDiffX',
        'OfflinePV/offlinePrimaryVertices/tagDiffY',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_highPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_highPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_mediumPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_mediumPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_lowPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/CHFrac_lowPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_highPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_highPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_mediumPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_mediumPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_lowPt_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/ChMultiplicity_lowPt_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Constituents',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Eta',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Eta_uncor',
        'JetMET/Jet/Cleanedak4PFJetsCHS/JetEnergyCorr',
        'JetMET/Jet/Cleanedak4PFJetsCHS/NJets',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Phi_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsCHS/Pt',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/PtJetMET/Jet/Cleanedak4PFJetsPuppi/Phi',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/Phi_Barrel',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/Phi_EndCap',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/JetEnergyCorr',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/NJets',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/Eta',
        'JetMET/Jet/Cleanedak4PFJetsPuppi/Eta_uncor',
        'JetMET/MET/pfMETT1/Cleaned/METSig',
        'JetMET/vertices',
        'JetMET/HIJetValidation/akCs4PFJets/SumPFPt',
        'JetMET/HIJetValidation/akCs4PFJets/NJets',
        'JetMET/HIJetValidation/akCs4PFJets/NPFpart',
        'JetMET/HIJetValidation/akPu4CaloJets/SumCaloPt',
        'JetMET/HIJetValidation/akPu4CaloJets/NCalopart',
        'JetMET/HIJetValidation/akPu4CaloJets/NJets',
        'Muons/MuonRecoAnalyzer/GlbMuon_Glb_pt',
        'Muons/MuonRecoAnalyzer/GlbMuon_Glb_eta',
        'Muons/MuonRecoAnalyzer/GlbMuon_Glb_phi',
        'Muons/MuonRecoAnalyzer/Res_TkGlb_qOverlap',
        'Muons/diMuonHistograms/GlbGlbMuon_LM',
        'Muons/diMuonHistograms/GlbGlbMuon_HM',
        'Muons/Isolation/global/relPFIso_R03',
        'Muons/globalMuons/GeneralProperties/NumberOfMeanRecHitsPerTrack_glb',
        'Muons/standAloneMuonsUpdatedAtVtx/HitProperties/NumberOfValidRecHitsPerTrack_sta',
        'Muons/MuonRecoOneHLT/GlbMuon_Glb_pt',
        'Muons/MuonRecoOneHLT/GlbMuon_Glb_eta',
        'Egamma/Electrons/Ele5_TagAndProbe/ele0_vertexPt_barrel',
        'Egamma/Electrons/Ele5_TagAndProbe/ele1_vertexPt_endcaps',
        'Egamma/Electrons/Ele5_TagAndProbe/ele2_vertexEta',
        'Egamma/Electrons/Ele5_TagAndProbe/ele5_vertexZ',
        'Egamma/Electrons/Ele5_TagAndProbe/ele10_Eop_barrel',
        'Egamma/Electrons/Ele5_TagAndProbe/ele10_Eop_endcaps',
        'Egamma/Electrons/Ele5_TagAndProbe/ele101_etaEff',
        'Egamma/Electrons/Ele5_TagAndProbe/ele102_phiEff',
        'Egamma/Electrons/Ele5_TagAndProbe/ele201_mee_os'
     ) )
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring('ProductNotFound'),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

process.MEtoEDMConverter = cms.EDProducer("MEtoEDMConverter",
    Frequency = cms.untracked.int32(50),
    MEPathToSave = cms.untracked.string(''),
    Name = cms.untracked.string('MEtoEDMConverter'),
    Verbosity = cms.untracked.int32(0)
)


process.centralityBin = cms.EDProducer("CentralityBinProducer",
    Centrality = cms.InputTag("hiCentrality"),
    centralityVariable = cms.string('HFtowers'),
    nonDefaultGlauberModel = cms.string(''),
    pPbRunFlip = cms.uint32(99999999)
)


process.cleanedParticleFlow = cms.EDProducer("HiBadParticleCleaner",
    PFCandidates = cms.InputTag("particleFlow"),
    maxSigLoose = cms.double(100.0),
    maxSigTight = cms.double(10.0),
    minCaloCompatibility = cms.double(0.35),
    minChargedHadronPt = cms.double(20.0),
    minMuonPt = cms.double(20.0),
    minMuonTrackRelErr = cms.double(2.0),
    minMuonTrackRelPtErr = cms.double(2.0),
    minPixelNHits = cms.uint32(3),
    minTrackNHits = cms.uint32(10),
    minTrackerLayersForMuonLoose = cms.int32(7),
    minTrackerLayersForMuonTight = cms.int32(10),
    offlinePV = cms.InputTag("offlinePrimaryVertices")
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
    chi2MapLostTag = cms.InputTag("lostTrackChi2"),
    chi2MapTag = cms.InputTag("packedPFCandidateTrackChi2"),
    chi2perlayer = cms.double(0.18),
    cutEra = cms.int32(2),
    d0d0error = cms.double(3.0),
    dzdzerror = cms.double(3.0),
    dzdzerror_pix = cms.double(10.0),
    flatdelvtx = cms.double(3.0),
    flatminvtx = cms.double(-15.0),
    flatnvtxbins = cms.int32(10),
    loadDB = cms.bool(False),
    lostTag = cms.InputTag("lostTracks"),
    maxet = cms.double(-1),
    maxpt = cms.double(3.0),
    minet = cms.double(-1.0),
    minpt = cms.double(0.3),
    nhitsValid = cms.int32(11),
    nonDefaultGlauberModel = cms.string(''),
    pterror = cms.double(0.1),
    trackTag = cms.InputTag("hiGeneralTracks"),
    vertexTag = cms.InputTag("hiSelectedVertex")
)


process.hiEvtPlaneFlat = cms.EDProducer("HiEvtPlaneFlatProducer",
    CentBinCompression = cms.int32(5),
    FlatOrder = cms.int32(9),
    NumFlatBins = cms.int32(40),
    caloCentRef = cms.double(-1.0),
    caloCentRefWidth = cms.double(-1.0),
    centralityBinTag = cms.InputTag("centralityBin","HFtowers"),
    centralityTag = cms.InputTag("hiCentrality"),
    centralityVariable = cms.string('HFtowers'),
    flatdelvtx = cms.double(3.0),
    flatminvtx = cms.double(-15.0),
    flatnvtxbins = cms.int32(10),
    inputPlanesTag = cms.InputTag("hiEvtPlane"),
    nonDefaultGlauberModel = cms.string(''),
    trackTag = cms.InputTag("generalTracks"),
    useOffsetPsi = cms.bool(True),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


process.packedPFCandidates = cms.EDProducer("PATPackedCandidateProducer",
    PuppiNoLepSrc = cms.InputTag("puppiNoLep"),
    PuppiSrc = cms.InputTag("puppi"),
    chargedHadronIsolation = cms.InputTag("chargedHadronPFTrackIsolation"),
    covariancePackingSchemas = cms.vint32(8, 264, 520, 776, 0),
    covarianceVersion = cms.int32(0),
    inputCollection = cms.InputTag("particleFlow"),
    inputVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    minPtForChargedHadronProperties = cms.double(3.0),
    minPtForLowQualityTrackProperties = cms.double(0.0),
    minPtForTrackProperties = cms.double(0.95),
    originalTracks = cms.InputTag("generalTracks"),
    originalVertices = cms.InputTag("offlinePrimaryVertices"),
    pfCandidateTypesForHcalDepth = cms.vint32(),
    secondaryVerticesForWhiteList = cms.VInputTag(cms.InputTag("inclusiveCandidateSecondaryVertices"), cms.InputTag("inclusiveCandidateSecondaryVerticesCvsL"), cms.InputTag("generalV0Candidates","Kshort"), cms.InputTag("generalV0Candidates","Lambda")),
    storeHcalDepthEndcapOnly = cms.bool(False),
    storeTiming = cms.bool(False),
    timeMap = cms.InputTag(""),
    timeMapErr = cms.InputTag(""),
    vertexAssociator = cms.InputTag("primaryVertexAssociation","original")
)


process.packedPFCandidatesRemoved = cms.EDProducer("PATPackedCandidateProducer",
    PuppiNoLepSrc = cms.InputTag("puppiNoLep"),
    PuppiSrc = cms.InputTag("puppi"),
    chargedHadronIsolation = cms.InputTag("chargedHadronPFTrackIsolation"),
    covariancePackingSchemas = cms.vint32(8, 264, 520, 776, 0),
    covarianceVersion = cms.int32(0),
    inputCollection = cms.InputTag("cleanedParticleFlow","removed"),
    inputVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    minPtForChargedHadronProperties = cms.double(3.0),
    minPtForLowQualityTrackProperties = cms.double(0.0),
    minPtForTrackProperties = cms.double(0.95),
    originalTracks = cms.InputTag("generalTracks"),
    originalVertices = cms.InputTag("offlinePrimaryVertices"),
    pfCandidateTypesForHcalDepth = cms.vint32(),
    secondaryVerticesForWhiteList = cms.VInputTag(cms.InputTag("inclusiveCandidateSecondaryVertices"), cms.InputTag("inclusiveCandidateSecondaryVerticesCvsL"), cms.InputTag("generalV0Candidates","Kshort"), cms.InputTag("generalV0Candidates","Lambda")),
    storeHcalDepthEndcapOnly = cms.bool(False),
    storeTiming = cms.bool(False),
    timeMap = cms.InputTag(""),
    timeMapErr = cms.InputTag(""),
    vertexAssociator = cms.InputTag("primaryVertexAssociationCleaned","original")
)


process.pfNoPileUpJME = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    matchByPtrDirect = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpJME")
)


process.pfNoPileUpPFBRECO = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    matchByPtrDirect = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpPFBRECO")
)


process.pfPileUpJME = cms.EDProducer("PFPileUp",
    DzCutForChargedFromPUVtxs = cms.double(0.2),
    NumOfPUVtxsForCharged = cms.uint32(2),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("goodOfflinePrimaryVertices"),
    checkClosestZVertex = cms.bool(False),
    enable = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    useVertexAssociation = cms.bool(False),
    verbose = cms.untracked.bool(False),
    vertexAssociation = cms.InputTag(""),
    vertexAssociationQuality = cms.int32(0)
)


process.pfPileUpPFBRECO = cms.EDProducer("PFPileUp",
    DzCutForChargedFromPUVtxs = cms.double(0.2),
    NumOfPUVtxsForCharged = cms.uint32(0),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("offlinePrimaryVertices"),
    checkClosestZVertex = cms.bool(True),
    enable = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    useVertexAssociation = cms.bool(False),
    verbose = cms.untracked.bool(False),
    vertexAssociation = cms.InputTag(""),
    vertexAssociationQuality = cms.int32(0)
)


process.primaryVertexAssociation = cms.EDProducer("PFCandidatePrimaryVertexSorter",
    assignment = cms.PSet(
        DzCutForChargedFromPUVtxs = cms.double(0.2),
        EtaMinUseDz = cms.double(-1),
        NumOfPUVtxsForCharged = cms.uint32(0),
        OnlyUseFirstDz = cms.bool(False),
        PtMaxCharged = cms.double(-1),
        maxDistanceToJetAxis = cms.double(0.07),
        maxDtSigForPrimaryAssignment = cms.double(3),
        maxDxyForJetAxisAssigment = cms.double(0.1),
        maxDxyForNotReconstructedPrimary = cms.double(0.01),
        maxDxySigForNotReconstructedPrimary = cms.double(2),
        maxDzErrorForPrimaryAssignment = cms.double(0.05),
        maxDzForJetAxisAssigment = cms.double(0.1),
        maxDzForPrimaryAssignment = cms.double(0.1),
        maxDzSigForPrimaryAssignment = cms.double(5),
        maxJetDeltaR = cms.double(0.5),
        minJetPt = cms.double(25),
        preferHighRanked = cms.bool(False),
        useTiming = cms.bool(False),
        useVertexFit = cms.bool(True)
    ),
    jets = cms.InputTag("ak4PFJets"),
    mightGet = cms.optional.untracked.vstring,
    particles = cms.InputTag("particleFlow"),
    produceAssociationToOriginalVertices = cms.bool(True),
    produceNoPileUpCollection = cms.bool(False),
    producePileUpCollection = cms.bool(False),
    produceSortedVertices = cms.bool(False),
    qualityForPrimary = cms.int32(2),
    sorting = cms.PSet(

    ),
    usePVMET = cms.bool(True),
    vertices = cms.InputTag("offlinePrimaryVertices")
)


process.primaryVertexAssociationJME = cms.EDProducer("PFCandidatePrimaryVertexSorter",
    assignment = cms.PSet(
        DzCutForChargedFromPUVtxs = cms.double(0.2),
        EtaMinUseDz = cms.double(2.4),
        NumOfPUVtxsForCharged = cms.uint32(2),
        OnlyUseFirstDz = cms.bool(True),
        PtMaxCharged = cms.double(20.0),
        maxDistanceToJetAxis = cms.double(0.07),
        maxDtSigForPrimaryAssignment = cms.double(3),
        maxDxyForJetAxisAssigment = cms.double(0.1),
        maxDxyForNotReconstructedPrimary = cms.double(0.01),
        maxDxySigForNotReconstructedPrimary = cms.double(2),
        maxDzErrorForPrimaryAssignment = cms.double(10000000000.0),
        maxDzForJetAxisAssigment = cms.double(0.1),
        maxDzForPrimaryAssignment = cms.double(0.3),
        maxDzSigForPrimaryAssignment = cms.double(10000000000.0),
        maxJetDeltaR = cms.double(0.5),
        minJetPt = cms.double(25),
        preferHighRanked = cms.bool(False),
        useTiming = cms.bool(False),
        useVertexFit = cms.bool(True)
    ),
    jets = cms.InputTag("ak4PFJets"),
    mightGet = cms.optional.untracked.vstring,
    particles = cms.InputTag("particleFlow"),
    produceAssociationToOriginalVertices = cms.bool(True),
    produceNoPileUpCollection = cms.bool(False),
    producePileUpCollection = cms.bool(False),
    produceSortedVertices = cms.bool(False),
    qualityForPrimary = cms.int32(2),
    sorting = cms.PSet(

    ),
    usePVMET = cms.bool(True),
    vertices = cms.InputTag("goodOfflinePrimaryVertices")
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.siPixelRecHits = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("siPixelClusters")
)


process.siPixelRecHitsPreSplitting = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("siPixelClustersPreSplitting")
)


process.siPixelRecHitsPreSplittingAlpaka = cms.EDProducer("SiPixelRecHitAlpakaPhase1@alpaka",
    CPE = cms.string('PixelCPEFastParams'),
    alpaka = cms.untracked.PSet(
        backend = cms.untracked.string(''),
        synchronize = cms.optional.untracked.bool
    ),
    beamSpot = cms.InputTag("offlineBeamSpotDevice"),
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("siPixelClustersPreSplittingAlpaka")
)


process.siPixelRecHitsPreSplittingAlpakaSerial = cms.EDProducer("alpaka_serial_sync::SiPixelRecHitAlpakaPhase1",
    CPE = cms.string('PixelCPEFastParams'),
    beamSpot = cms.InputTag("offlineBeamSpotDevice"),
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("siPixelClustersPreSplittingAlpakaSerial")
)


process.unpackedTracksAndVertices = cms.EDProducer("TrackAndVertexUnpacker",
    mightGet = cms.optional.untracked.vstring,
    packedCandidateNormChi2Map = cms.VInputTag("packedPFCandidateTrackChi2", "lostTrackChi2", ""),
    packedCandidates = cms.VInputTag("packedPFCandidates", "lostTracks", "lostTracks:eleTracks"),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    recoverTracks = cms.bool(True),
    secondaryVertices = cms.InputTag("slimmedSecondaryVertices")
)


process.centralityFilter = cms.EDFilter("CentralityFilter",
    BinLabel = cms.InputTag("centralityBin","HFtowers"),
    selectedBins = cms.vint32(0)
)


process.clusterCompatibilityFilter = cms.EDFilter("HIClusterCompatibilityFilter",
    cluscomSrc = cms.InputTag("hiClusterCompatibility"),
    clusterPars = cms.vdouble(0.0, 0.0045),
    clusterTrunc = cms.double(2.0),
    maxZ = cms.double(20.05),
    minZ = cms.double(-20.0),
    nhitsTrunc = cms.int32(150)
)


process.goodOfflinePrimaryVertices = cms.EDFilter("VertexSelector",
    cut = cms.string('!isFake && ndof >= 4.0 && abs(z) <= 24.0 && abs(position.Rho) <= 2.0'),
    filter = cms.bool(False),
    src = cms.InputTag("offlinePrimaryVertices")
)


process.hltPixelClusterShapeFilter = cms.EDFilter("HLTPixelClusterShapeFilter",
    clusterPars = cms.vdouble(0, 0.0045),
    clusterTrunc = cms.double(2),
    inputTag = cms.InputTag("siPixelRecHits"),
    maxZ = cms.double(20.05),
    mightGet = cms.optional.untracked.vstring,
    minZ = cms.double(-20),
    nhitsTrunc = cms.int32(150),
    saveTags = cms.bool(True),
    zStep = cms.double(0.2)
)


process.hltfilter = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring('HLT_MinimumBiasHF_OR_BptxAND_v1'),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    eventSetupPathsLabel = cms.string(''),
    mightGet = cms.optional.untracked.vstring,
    throw = cms.bool(True)
)


process.phfCoincFilterPF1Th10 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(1),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(10)
)


process.phfCoincFilterPF1Th3 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(1),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(3)
)


process.phfCoincFilterPF1Th4 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(1),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(4.0)
)


process.phfCoincFilterPF1Th5 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(1),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(5)
)


process.phfCoincFilterPF1Th6 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(1),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(6)
)


process.phfCoincFilterPF1Th7 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(1),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(7)
)


process.phfCoincFilterPF1Th8 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(1),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(8)
)


process.phfCoincFilterPF1Th9 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(1),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(9)
)


process.phfCoincFilterPF2Th10 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(2),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(10)
)


process.phfCoincFilterPF2Th3 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(2),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(3)
)


process.phfCoincFilterPF2Th4 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(2),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(4.0)
)


process.phfCoincFilterPF2Th5 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(2),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(5)
)


process.phfCoincFilterPF2Th6 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(2),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(6)
)


process.phfCoincFilterPF2Th7 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(2),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(7)
)


process.phfCoincFilterPF2Th8 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(2),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(8)
)


process.phfCoincFilterPF2Th9 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(2),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(9)
)


process.phfCoincFilterPF3Th10 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(3),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(10)
)


process.phfCoincFilterPF3Th3 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(3),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(3)
)


process.phfCoincFilterPF3Th4 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(3),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(4.0)
)


process.phfCoincFilterPF3Th5 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(3),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(5)
)


process.phfCoincFilterPF3Th6 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(3),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(6)
)


process.phfCoincFilterPF3Th7 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(3),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(7)
)


process.phfCoincFilterPF3Th8 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(3),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(8)
)


process.phfCoincFilterPF3Th9 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(3),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(9)
)


process.phfCoincFilterPF4Th10 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(4),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(10)
)


process.phfCoincFilterPF4Th2 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(4),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(2)
)


process.phfCoincFilterPF4Th3 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(4),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(3)
)


process.phfCoincFilterPF4Th4 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(4),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(4.0)
)


process.phfCoincFilterPF4Th5 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(4),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(5)
)


process.phfCoincFilterPF4Th6 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(4),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(6)
)


process.phfCoincFilterPF4Th7 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(4),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(7)
)


process.phfCoincFilterPF4Th8 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(4),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(8)
)


process.phfCoincFilterPF4Th9 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(4),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(9)
)


process.phfCoincFilterPF5Th10 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(5),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(10)
)


process.phfCoincFilterPF5Th3 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(5),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(3)
)


process.phfCoincFilterPF5Th4 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(5),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(4.0)
)


process.phfCoincFilterPF5Th5 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(5),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(5)
)


process.phfCoincFilterPF5Th6 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(5),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(6)
)


process.phfCoincFilterPF5Th7 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(5),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(7)
)


process.phfCoincFilterPF5Th8 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(5),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(8)
)


process.phfCoincFilterPF5Th9 = cms.EDFilter("HiHFFilterPF",
    minnumtowers = cms.int32(5),
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    threshold = cms.double(9)
)


process.pileupvertexfilter = cms.EDFilter("PileUpVertexFilter",
    doNeNe = cms.bool(False),
    doOO = cms.bool(True),
    surfaceCutParameters1NeNe = cms.vdouble(
        0.864887, 0.759109, 0.69555, 0.646559, 0.615701,
        0.576282, 0.508488, 0.49317, 0.375646, 0.05
    ),
    surfaceCutParameters1OO = cms.vdouble(
        0.850271, 0.754963, 0.695127, 0.645343, 0.613325,
        0.590003, 0.505241, 0.37611, 0.42144, 0.0500003
    ),
    surfaceCutParameters2NeNe = cms.vdouble(
        8.52423, 3.6516, 2.76073, 2.60194, 2.25997,
        2.07765, 2.32389, 1.5974, 1.66482, 2.27543
    ),
    surfaceCutParameters2OO = cms.vdouble(
        9.26551, 3.9179, 2.94908, 2.67405, 2.60579,
        1.74096, 1.99159, 2.4446, 2.04628, 2.09011
    ),
    vertexSrc = cms.InputTag("unpackedTracksAndVertices")
)


process.primaryVertexFilter = cms.EDFilter("VertexSelector",
    cut = cms.string('!isFake && abs(z) <= 25 && position.Rho <= 2'),
    filter = cms.bool(True),
    src = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.RAGHUV0 = cms.EDAnalyzer("RaghuV0Ana",
    Chi2Max = cms.untracked.double(7.0),
    DCAMax = cms.untracked.double(1.0),
    DecayXYZMin = cms.untracked.double(5.0),
    EtaMax = cms.untracked.double(2.4),
    EtaMin = cms.untracked.double(-2.4),
    MassMax = cms.untracked.double(0.56),
    MassMax_lm = cms.untracked.double(1.16),
    MassMin = cms.untracked.double(0.44),
    MassMin_lm = cms.untracked.double(1.08),
    RapMax = cms.untracked.double(2.0),
    RapMin = cms.untracked.double(-2.0),
    ThetaXYZMin = cms.untracked.double(0.999),
    V0Src = cms.InputTag("generalV0CandidatesNew","Kshort"),
    V0Src_lm = cms.InputTag("generalV0CandidatesNew","Lambda"),
    binTable = cms.untracked.vdouble(
        0, 0.717572, 1.43514, 2.15272, 2.87029,
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
        1000
    ),
    bkgFactor = cms.untracked.uint32(10),
    dauNhitsMin = cms.untracked.int32(4),
    dauPixelhitsMin = cms.untracked.int32(1),
    dau_etaphi = cms.untracked.double(1e-13),
    dbCent = cms.untracked.InputTag("centralityBin","HFtowers"),
    del_R = cms.untracked.double(0.03),
    fname = cms.untracked.InputTag("Eff_OO_2025_Hijing_MB_Centrality_NoPU_3D_Nominal_Official.root"),
    fnameV0 = cms.untracked.InputTag("Eff_OO_2025_lm_dr0p03_dpt0p05_ks_dr0p03_dpt0p04_DCA1_cos999_dr0p3_ef.root"),
    isMC = cms.untracked.bool(False),
    mis_ks_range = cms.untracked.double(0.02),
    mis_la_range = cms.untracked.double(0.01),
    mis_ph_range = cms.untracked.double(0.015),
    mvaCut = cms.untracked.double(0.2),
    mvaXML = cms.untracked.InputTag("MC_Full_BDT250_D4.LM.weights.xml"),
    ncentbin_binedge = cms.untracked.vdouble(140, 160),
    nmass_ks_binedge = cms.untracked.vdouble(
        0.44, 0.449, 0.458, 0.468, 0.476,
        0.48, 0.484, 0.488, 0.492, 0.495,
        0.4975, 0.5, 0.503, 0.506, 0.51,
        0.514, 0.518, 0.52, 0.53, 0.545,
        0.56
    ),
    nmass_lm_binedge = cms.untracked.vdouble(
        1.08, 1.105, 1.109, 1.112, 1.115,
        1.117, 1.12, 1.124, 1.13, 1.143,
        1.16
    ),
    npt_binedge = cms.untracked.vdouble(
        0.7, 1.0, 1.4, 1.8, 2.2,
        2.6, 3.0, 3.6, 4.5, 6.0,
        8.0
    ),
    npt_binedge_lm = cms.untracked.vdouble(
        0.7, 1.0, 1.4, 1.8, 2.2,
        2.6, 3.0, 3.6, 4.5, 6.0,
        8.0
    ),
    pTmaxTrk_ass = cms.untracked.vdouble(3.0),
    pTmaxTrk_ass_ks = cms.untracked.double(3.0),
    pTmaxTrk_ass_lm = cms.untracked.double(3.0),
    pTmaxTrk_trg = cms.untracked.vdouble(8.0),
    pTmaxTrk_trg_ks = cms.untracked.double(8.0),
    pTmaxTrk_trg_lm = cms.untracked.double(8.0),
    pTminTrk_ass = cms.untracked.vdouble(0.3),
    pTminTrk_ass_ks = cms.untracked.double(0.3),
    pTminTrk_ass_lm = cms.untracked.double(0.3),
    pTminTrk_trg = cms.untracked.vdouble(0.7),
    pTminTrk_trg_ks = cms.untracked.double(0.7),
    pTminTrk_trg_lm = cms.untracked.double(0.7),
    packedCandidates = cms.InputTag("packedPFCandidates"),
    ptMax = cms.untracked.double(8.0),
    ptMax_ch = cms.untracked.double(3.0),
    ptMin = cms.untracked.double(0.7),
    ptMin_ch = cms.untracked.double(0.3),
    sigma2_kshort_maxMass = cms.untracked.vdouble(
        0.51319, 0.512784, 0.512784, 0.512784, 0.512251,
        0.512251, 0.511708, 0.511708, 0.511708, 0.511708,
        0.511302, 0.511302, 0.511302, 0.511302, 0.511364,
        0.511364, 0.511364, 0.511244, 0.511244, 0.511244,
        0.511392, 0.511392, 0.511392, 0.511392, 0.512624,
        0.512624, 0.512624, 0.512817, 0.512817, 0.512817,
        0.513892, 0.513568, 0.513568
    ),
    sigma2_kshort_minMass = cms.untracked.vdouble(
        0.482157, 0.482438, 0.482438, 0.482438, 0.483087,
        0.483087, 0.483587, 0.483587, 0.483587, 0.483587,
        0.48388, 0.48388, 0.48388, 0.48388, 0.48377,
        0.48377, 0.48377, 0.483825, 0.483825, 0.483825,
        0.483532, 0.483532, 0.483532, 0.483532, 0.482405,
        0.482405, 0.482405, 0.482283, 0.482283, 0.482283,
        0.480952, 0.481303, 0.481303
    ),
    sigma2_lambda_maxMass = cms.untracked.vdouble(
        1.13322, 1.1226, 1.1226, 1.1226, 1.12193,
        1.12193, 1.12169, 1.12169, 1.12169, 1.12169,
        1.12213, 1.12213, 1.12213, 1.12213, 1.12199,
        1.12199, 1.12199, 1.12207, 1.12207, 1.12207,
        1.12239, 1.12239, 1.12239, 1.12239, 1.12346,
        1.12346, 1.12346, 1.1251, 1.1251, 1.1251,
        1.12977, 1.12373, 1.12373
    ),
    sigma2_lambda_minMass = cms.untracked.vdouble(
        1.10038, 1.11021, 1.11021, 1.11021, 1.11044,
        1.11044, 1.11029, 1.11029, 1.11029, 1.11029,
        1.10974, 1.10974, 1.10974, 1.10974, 1.10964,
        1.10964, 1.10964, 1.10986, 1.10986, 1.10986,
        1.10971, 1.10971, 1.10971, 1.10971, 1.10926,
        1.10926, 1.10926, 1.10823, 1.10823, 1.10823,
        1.10644, 1.1106, 1.1106
    ),
    sigma3_kshort_maxMass = cms.untracked.vdouble(
        0.520949, 0.520371, 0.520371, 0.520371, 0.519542,
        0.519542, 0.518739, 0.518739, 0.518739, 0.518739,
        0.518157, 0.518157, 0.518157, 0.518157, 0.518263,
        0.518263, 0.518263, 0.518098, 0.518098, 0.518098,
        0.518357, 0.518357, 0.518357, 0.518357, 0.520178,
        0.520178, 0.520178, 0.520451, 0.520451, 0.520451,
        0.522127, 0.521634, 0.521634
    ),
    sigma3_kshort_minMass = cms.untracked.vdouble(
        0.474398, 0.474852, 0.474852, 0.474852, 0.475797,
        0.475797, 0.476557, 0.476557, 0.476557, 0.476557,
        0.477025, 0.477025, 0.477025, 0.477025, 0.476871,
        0.476871, 0.476871, 0.47697, 0.47697, 0.47697,
        0.476567, 0.476567, 0.476567, 0.476567, 0.474851,
        0.474851, 0.474851, 0.474649, 0.474649, 0.474649,
        0.472717, 0.473237, 0.473237
    ),
    sigma3_lambda_maxMass = cms.untracked.vdouble(
        1.14143, 1.1257, 1.1257, 1.1257, 1.12481,
        1.12481, 1.12454, 1.12454, 1.12454, 1.12454,
        1.12523, 1.12523, 1.12523, 1.12523, 1.12537,
        1.12537, 1.12537, 1.12502, 1.12502, 1.12502,
        1.12516, 1.12516, 1.12516, 1.12516, 1.12567,
        1.12567, 1.12567, 1.12726, 1.12726, 1.12726,
        1.12977, 1.12373, 1.12373
    ),
    sigma3_lambda_minMass = cms.untracked.vdouble(
        1.09217, 1.10711, 1.10711, 1.10711, 1.10757,
        1.10757, 1.10744, 1.10744, 1.10744, 1.10744,
        1.10664, 1.10664, 1.10664, 1.10664, 1.10649,
        1.10649, 1.10649, 1.10683, 1.10683, 1.10683,
        1.10662, 1.10662, 1.10662, 1.10662, 1.10598,
        1.10598, 1.10598, 1.10443, 1.10443, 1.10443,
        1.10177, 1.10797, 1.10797
    ),
    trackAssociation = cms.InputTag("unpackedTracksAndVertices"),
    tracks = cms.InputTag("genParticles"),
    tracksSrc = cms.InputTag("packedPFCandidates"),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
    zmaxVtx = cms.untracked.double(15.0),
    zminVtx = cms.untracked.double(-15.0)
)


process.V0ana = cms.EDAnalyzer("RaghuV0Ana",
    Chi2Max = cms.untracked.double(7.0),
    DCAMax = cms.untracked.double(1.0),
    DecayXYZMin = cms.untracked.double(5.0),
    EtaMax = cms.untracked.double(2.4),
    EtaMin = cms.untracked.double(-2.4),
    MassMax = cms.untracked.double(0.56),
    MassMax_lm = cms.untracked.double(1.16),
    MassMin = cms.untracked.double(0.44),
    MassMin_lm = cms.untracked.double(1.08),
    RapMax = cms.untracked.double(2.0),
    RapMin = cms.untracked.double(-2.0),
    ThetaXYZMin = cms.untracked.double(0.999),
    V0Src = cms.InputTag("generalV0CandidatesNew","Kshort"),
    V0Src_lm = cms.InputTag("generalV0CandidatesNew","Lambda"),
    binTable = cms.untracked.vdouble(
        0, 0.717572, 1.43514, 2.15272, 2.87029,
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
        1000
    ),
    bkgFactor = cms.untracked.uint32(10),
    dauNhitsMin = cms.untracked.int32(4),
    dauPixelhitsMin = cms.untracked.int32(1),
    dau_etaphi = cms.untracked.double(1e-13),
    dbCent = cms.untracked.InputTag("centralityBin","HFtowers"),
    del_R = cms.untracked.double(0.03),
    fname = cms.untracked.InputTag("Eff_OO_2025_Hijing_MB_Centrality_NoPU_3D_Nominal_Official.root"),
    fnameV0 = cms.untracked.InputTag("Eff_OO_2025_lm_dr0p03_dpt0p05_ks_dr0p03_dpt0p04_DCA1_cos999_dr0p3_ef.root"),
    isMC = cms.untracked.bool(False),
    mis_ks_range = cms.untracked.double(0.02),
    mis_la_range = cms.untracked.double(0.01),
    mis_ph_range = cms.untracked.double(0.015),
    mvaCut = cms.untracked.double(0.2),
    mvaXML = cms.untracked.InputTag("MC_Full_BDT250_D4.LM.weights.xml"),
    ncentbin_binedge = cms.untracked.vdouble(140, 160),
    nmass_ks_binedge = cms.untracked.vdouble(
        0.44, 0.449, 0.458, 0.468, 0.476,
        0.48, 0.484, 0.488, 0.492, 0.495,
        0.4975, 0.5, 0.503, 0.506, 0.51,
        0.514, 0.518, 0.52, 0.53, 0.545,
        0.56
    ),
    nmass_lm_binedge = cms.untracked.vdouble(
        1.08, 1.105, 1.109, 1.112, 1.115,
        1.117, 1.12, 1.124, 1.13, 1.143,
        1.16
    ),
    npt_binedge = cms.untracked.vdouble(
        0.7, 1.0, 1.4, 1.8, 2.2,
        2.6, 3.0, 3.6, 4.5, 6.0,
        8.0
    ),
    npt_binedge_lm = cms.untracked.vdouble(
        0.7, 1.0, 1.4, 1.8, 2.2,
        2.6, 3.0, 3.6, 4.5, 6.0,
        8.0
    ),
    pTmaxTrk_ass = cms.untracked.vdouble(3.0),
    pTmaxTrk_ass_ks = cms.untracked.double(3.0),
    pTmaxTrk_ass_lm = cms.untracked.double(3.0),
    pTmaxTrk_trg = cms.untracked.vdouble(8.0),
    pTmaxTrk_trg_ks = cms.untracked.double(8.0),
    pTmaxTrk_trg_lm = cms.untracked.double(8.0),
    pTminTrk_ass = cms.untracked.vdouble(0.3),
    pTminTrk_ass_ks = cms.untracked.double(0.3),
    pTminTrk_ass_lm = cms.untracked.double(0.3),
    pTminTrk_trg = cms.untracked.vdouble(0.7),
    pTminTrk_trg_ks = cms.untracked.double(0.7),
    pTminTrk_trg_lm = cms.untracked.double(0.7),
    packedCandidates = cms.InputTag("packedPFCandidates"),
    ptMax = cms.untracked.double(8.0),
    ptMax_ch = cms.untracked.double(3.0),
    ptMin = cms.untracked.double(0.7),
    ptMin_ch = cms.untracked.double(0.3),
    sigma2_kshort_maxMass = cms.untracked.vdouble(
        0.51319, 0.512784, 0.512784, 0.512784, 0.512251,
        0.512251, 0.511708, 0.511708, 0.511708, 0.511708,
        0.511302, 0.511302, 0.511302, 0.511302, 0.511364,
        0.511364, 0.511364, 0.511244, 0.511244, 0.511244,
        0.511392, 0.511392, 0.511392, 0.511392, 0.512624,
        0.512624, 0.512624, 0.512817, 0.512817, 0.512817,
        0.513892, 0.513568, 0.513568
    ),
    sigma2_kshort_minMass = cms.untracked.vdouble(
        0.482157, 0.482438, 0.482438, 0.482438, 0.483087,
        0.483087, 0.483587, 0.483587, 0.483587, 0.483587,
        0.48388, 0.48388, 0.48388, 0.48388, 0.48377,
        0.48377, 0.48377, 0.483825, 0.483825, 0.483825,
        0.483532, 0.483532, 0.483532, 0.483532, 0.482405,
        0.482405, 0.482405, 0.482283, 0.482283, 0.482283,
        0.480952, 0.481303, 0.481303
    ),
    sigma2_lambda_maxMass = cms.untracked.vdouble(
        1.13322, 1.1226, 1.1226, 1.1226, 1.12193,
        1.12193, 1.12169, 1.12169, 1.12169, 1.12169,
        1.12213, 1.12213, 1.12213, 1.12213, 1.12199,
        1.12199, 1.12199, 1.12207, 1.12207, 1.12207,
        1.12239, 1.12239, 1.12239, 1.12239, 1.12346,
        1.12346, 1.12346, 1.1251, 1.1251, 1.1251,
        1.12977, 1.12373, 1.12373
    ),
    sigma2_lambda_minMass = cms.untracked.vdouble(
        1.10038, 1.11021, 1.11021, 1.11021, 1.11044,
        1.11044, 1.11029, 1.11029, 1.11029, 1.11029,
        1.10974, 1.10974, 1.10974, 1.10974, 1.10964,
        1.10964, 1.10964, 1.10986, 1.10986, 1.10986,
        1.10971, 1.10971, 1.10971, 1.10971, 1.10926,
        1.10926, 1.10926, 1.10823, 1.10823, 1.10823,
        1.10644, 1.1106, 1.1106
    ),
    sigma3_kshort_maxMass = cms.untracked.vdouble(
        0.520949, 0.520371, 0.520371, 0.520371, 0.519542,
        0.519542, 0.518739, 0.518739, 0.518739, 0.518739,
        0.518157, 0.518157, 0.518157, 0.518157, 0.518263,
        0.518263, 0.518263, 0.518098, 0.518098, 0.518098,
        0.518357, 0.518357, 0.518357, 0.518357, 0.520178,
        0.520178, 0.520178, 0.520451, 0.520451, 0.520451,
        0.522127, 0.521634, 0.521634
    ),
    sigma3_kshort_minMass = cms.untracked.vdouble(
        0.474398, 0.474852, 0.474852, 0.474852, 0.475797,
        0.475797, 0.476557, 0.476557, 0.476557, 0.476557,
        0.477025, 0.477025, 0.477025, 0.477025, 0.476871,
        0.476871, 0.476871, 0.47697, 0.47697, 0.47697,
        0.476567, 0.476567, 0.476567, 0.476567, 0.474851,
        0.474851, 0.474851, 0.474649, 0.474649, 0.474649,
        0.472717, 0.473237, 0.473237
    ),
    sigma3_lambda_maxMass = cms.untracked.vdouble(
        1.14143, 1.1257, 1.1257, 1.1257, 1.12481,
        1.12481, 1.12454, 1.12454, 1.12454, 1.12454,
        1.12523, 1.12523, 1.12523, 1.12523, 1.12537,
        1.12537, 1.12537, 1.12502, 1.12502, 1.12502,
        1.12516, 1.12516, 1.12516, 1.12516, 1.12567,
        1.12567, 1.12567, 1.12726, 1.12726, 1.12726,
        1.12977, 1.12373, 1.12373
    ),
    sigma3_lambda_minMass = cms.untracked.vdouble(
        1.09217, 1.10711, 1.10711, 1.10711, 1.10757,
        1.10757, 1.10744, 1.10744, 1.10744, 1.10744,
        1.10664, 1.10664, 1.10664, 1.10664, 1.10649,
        1.10649, 1.10649, 1.10683, 1.10683, 1.10683,
        1.10662, 1.10662, 1.10662, 1.10662, 1.10598,
        1.10598, 1.10598, 1.10443, 1.10443, 1.10443,
        1.10177, 1.10797, 1.10797
    ),
    trackAssociation = cms.InputTag("unpackedTracksAndVertices"),
    tracks = cms.InputTag("genParticles"),
    tracksSrc = cms.InputTag("packedPFCandidates"),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
    zmaxVtx = cms.untracked.double(15.0),
    zminVtx = cms.untracked.double(-15.0)
)


process.skimanalysis = cms.EDAnalyzer("FilterAnalyzer",
    hltresults = cms.InputTag("TriggerResults","","HiForest"),
    superFilters = cms.vstring('')
)


process.DQMStore = cms.Service("DQMStore")


process.MessageLogger = cms.Service("MessageLogger",
    cerr = cms.untracked.PSet(
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1000)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        enable = cms.untracked.bool(True),
        enableStatistics = cms.untracked.bool(False),
        lineLength = cms.optional.untracked.int32,
        noLineBreaks = cms.optional.untracked.bool,
        noTimeStamps = cms.untracked.bool(False),
        resetStatistics = cms.untracked.bool(False),
        statisticsThreshold = cms.untracked.string('WARNING'),
        threshold = cms.untracked.string('INFO'),
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    cout = cms.untracked.PSet(
        enable = cms.untracked.bool(False),
        enableStatistics = cms.untracked.bool(False),
        lineLength = cms.optional.untracked.int32,
        noLineBreaks = cms.optional.untracked.bool,
        noTimeStamps = cms.optional.untracked.bool,
        resetStatistics = cms.untracked.bool(False),
        statisticsThreshold = cms.optional.untracked.string,
        threshold = cms.optional.untracked.string,
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    debugModules = cms.untracked.vstring(),
    default = cms.untracked.PSet(
        limit = cms.optional.untracked.int32,
        lineLength = cms.untracked.int32(80),
        noLineBreaks = cms.untracked.bool(False),
        noTimeStamps = cms.untracked.bool(False),
        reportEvery = cms.untracked.int32(1),
        statisticsThreshold = cms.untracked.string('INFO'),
        threshold = cms.untracked.string('INFO'),
        timespan = cms.optional.untracked.int32,
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    files = cms.untracked.PSet(
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            enableStatistics = cms.untracked.bool(False),
            extension = cms.optional.untracked.string,
            filename = cms.optional.untracked.string,
            lineLength = cms.optional.untracked.int32,
            noLineBreaks = cms.optional.untracked.bool,
            noTimeStamps = cms.optional.untracked.bool,
            output = cms.optional.untracked.string,
            resetStatistics = cms.untracked.bool(False),
            statisticsThreshold = cms.optional.untracked.string,
            threshold = cms.optional.untracked.string,
            allowAnyLabel_=cms.optional.untracked.PSetTemplate(
                limit = cms.optional.untracked.int32,
                reportEvery = cms.untracked.int32(1),
                timespan = cms.optional.untracked.int32
            )
        )
    ),
    suppressDebug = cms.untracked.vstring(),
    suppressFwkInfo = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    allowAnyLabel_=cms.optional.untracked.PSetTemplate(
        limit = cms.optional.untracked.int32,
        reportEvery = cms.untracked.int32(1),
        timespan = cms.optional.untracked.int32
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    CTPPSFastRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1357987)
    ),
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(987346)
    ),
    RPSiDetDigitizer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(137137)
    ),
    RPixDetDigitizer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(137137)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(98765432)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6541321)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(654321)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(234567)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    fastSimProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(13579)
    ),
    fastTrackerRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(24680)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(88776655)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6453209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(54525)
    ),
    saveFileName = cms.untracked.string(''),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11223344)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('V0_test_IM_newpT.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL',
        'ZDC',
        'CASTOR',
        'EcalBarrel',
        'EcalEndcap',
        'EcalPreshower',
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string(''),
    dump = cms.untracked.vstring(),
    file = cms.untracked.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService",
    maxExtrapolationTimeInSec = cms.uint32(0)
)


process.EcalLaserCorrectionServiceMC = cms.ESProducer("EcalLaserCorrectionServiceMC",
    appendToDataLabel = cms.string('')
)


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    fromDD4hep = cms.untracked.bool(False),
    fromDDD = cms.untracked.bool(False)
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


process.TrackerAdditionalParametersPerDet = cms.ESProducer("TrackerAdditionalParametersPerDetESModule",
    appendToDataLabel = cms.string('')
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer",
    usePhase2Stacks = cms.bool(False)
)


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder'),
    appendToDataLabel = cms.string('')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.XMLFromDBSource = cms.ESProducer("XMLIdealGeometryESProducer",
    label = cms.string('Extended'),
    rootDDName = cms.string('cms:OCMS')
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.caloSimulationParameters = cms.ESProducer("CaloSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False)
)


process.ctppsBeamParametersFromLHCInfoESSource = cms.ESProducer("CTPPSBeamParametersFromLHCInfoESSource",
    appendToDataLabel = cms.string(''),
    beamDivX45 = cms.double(0.1),
    beamDivX56 = cms.double(0.1),
    beamDivY45 = cms.double(0.1),
    beamDivY56 = cms.double(0.1),
    lhcInfoLabel = cms.string(''),
    lhcInfoPerFillLabel = cms.string(''),
    lhcInfoPerLSLabel = cms.string(''),
    useNewLHCInfo = cms.bool(False),
    vtxOffsetX45 = cms.double(0.01),
    vtxOffsetX56 = cms.double(0.01),
    vtxOffsetY45 = cms.double(0.01),
    vtxOffsetY56 = cms.double(0.01),
    vtxOffsetZ45 = cms.double(0.01),
    vtxOffsetZ56 = cms.double(0.01),
    vtxStddevX = cms.double(0.02),
    vtxStddevY = cms.double(0.02),
    vtxStddevZ = cms.double(0.02)
)


process.ctppsInterpolatedOpticalFunctionsESSource = cms.ESProducer("CTPPSInterpolatedOpticalFunctionsESSource",
    appendToDataLabel = cms.string(''),
    lhcInfoLabel = cms.string(''),
    lhcInfoPerFillLabel = cms.string(''),
    lhcInfoPerLSLabel = cms.string(''),
    opticsLabel = cms.string(''),
    useNewLHCInfo = cms.bool(False)
)


process.ecalSimulationParametersEB = cms.ESProducer("EcalSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    name = cms.string('EcalHitsEB')
)


process.ecalSimulationParametersEE = cms.ESProducer("EcalSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    name = cms.string('EcalHitsEE')
)


process.ecalSimulationParametersES = cms.ESProducer("EcalSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    name = cms.string('EcalHitsES')
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


process.hcalSimulationConstants = cms.ESProducer("HcalSimulationConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalSimulationParameters = cms.ESProducer("HcalSimParametersESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False)
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
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
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.multipleScatteringParametrisationMakerESProducer = cms.ESProducer("MultipleScatteringParametrisationMakerESProducer",
    appendToDataLabel = cms.string('')
)


process.muonGeometryConstants = cms.ESProducer("MuonGeometryConstantsESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False)
)


process.muonOffsetESProducer = cms.ESProducer("MuonOffsetESProducer",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    names = cms.vstring(
        'MuonCommonNumbering',
        'MuonBarrel',
        'MuonEndcap',
        'MuonBarrelWheels',
        'MuonBarrelStation1',
        'MuonBarrelStation2',
        'MuonBarrelStation3',
        'MuonBarrelStation4',
        'MuonBarrelSuperLayer',
        'MuonBarrelLayer',
        'MuonBarrelWire',
        'MuonRpcPlane1I',
        'MuonRpcPlane1O',
        'MuonRpcPlane2I',
        'MuonRpcPlane2O',
        'MuonRpcPlane3S',
        'MuonRpcPlane4',
        'MuonRpcChamberLeft',
        'MuonRpcChamberMiddle',
        'MuonRpcChamberRight',
        'MuonRpcEndcap1',
        'MuonRpcEndcap2',
        'MuonRpcEndcap3',
        'MuonRpcEndcap4',
        'MuonRpcEndcapSector',
        'MuonRpcEndcapChamberB1',
        'MuonRpcEndcapChamberB2',
        'MuonRpcEndcapChamberB3',
        'MuonRpcEndcapChamberC1',
        'MuonRpcEndcapChamberC2',
        'MuonRpcEndcapChamberC3',
        'MuonRpcEndcapChamberE1',
        'MuonRpcEndcapChamberE2',
        'MuonRpcEndcapChamberE3',
        'MuonRpcEndcapChamberF1',
        'MuonRpcEndcapChamberF2',
        'MuonRpcEndcapChamberF3',
        'MuonEndcapStation1',
        'MuonEndcapStation2',
        'MuonEndcapStation3',
        'MuonEndcapStation4',
        'MuonEndcapSubrings',
        'MuonEndcapSectors',
        'MuonEndcapLayers',
        'MuonEndcapRing1',
        'MuonEndcapRing2',
        'MuonEndcapRing3',
        'MuonEndcapRingA',
        'MuonGEMEndcap',
        'MuonGEMSector',
        'MuonGEMChamber'
    )
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    ),
    appendToDataLabel = cms.string(''),
    siPixelQualityFromDbLabel = cms.string('')
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
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ),
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
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
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
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
        )
    ),
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
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.zdcTopologyEP = cms.ESProducer("ZdcTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionTimeout = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    JsonDumpFileName = cms.untracked.string(''),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    appendToDataLabel = cms.string(''),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    frontierKey = cms.untracked.string(''),
    globaltag = cms.string('150X_dataRun3_Prompt_v3'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    recordsToDebug = cms.untracked.vstring(),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    toGet = cms.VPSet(cms.PSet(
        connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
        label = cms.untracked.string('HFtowers'),
        record = cms.string('HeavyIonRcd'),
        tag = cms.string('CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1033p1x01_offline')
    ))
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ),
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ),
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
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
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379,
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807,
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05,
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107,
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601,
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447,
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06,
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05,
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ),
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ),
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ),
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ),
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ),
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ),
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        noiseCorrelation = cms.vdouble(0.26, 0.254),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(208),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        noiseCorrelation = cms.vdouble(0.26, 0.254),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(208),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(False),
    useHFUpgrade = cms.bool(False),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(True),
    useLayer0Weight = cms.bool(False)
)


process.prefer("es_hardcode")

process.pfNoPileUpJMETask = cms.Task(process.goodOfflinePrimaryVertices, process.pfNoPileUpJME, process.pfPileUpJME)


process.siPixelRecHitsPreSplittingTask = cms.Task(process.siPixelRecHitsPreSplitting)


process.packedPFCandidatesTask = cms.Task(process.packedPFCandidates, process.pfNoPileUpJMETask, process.pfNoPileUpPFBRECO, process.pfPileUpPFBRECO)


process.endOfProcess = cms.Sequence(process.MEtoEDMConverter)


process.pfNoPileUpJMESequence = cms.Sequence(process.pfNoPileUpJMETask)


process.eventSelections = cms.Sequence(process.phfCoincFilterPF2Th4+process.primaryVertexFilter+process.clusterCompatibilityFilter+process.unpackedTracksAndVertices+process.pileupvertexfilter)


process.pphfCoincFilterPF1Th10 = cms.Path(process.phfCoincFilterPF1Th10)


process.pphfCoincFilterPF1Th3 = cms.Path(process.phfCoincFilterPF1Th3)


process.pphfCoincFilterPF1Th4 = cms.Path(process.phfCoincFilterPF1Th4)


process.pphfCoincFilterPF1Th5 = cms.Path(process.phfCoincFilterPF1Th5)


process.pphfCoincFilterPF1Th6 = cms.Path(process.phfCoincFilterPF1Th6)


process.pphfCoincFilterPF1Th7 = cms.Path(process.phfCoincFilterPF1Th7)


process.pphfCoincFilterPF1Th8 = cms.Path(process.phfCoincFilterPF1Th8)


process.pphfCoincFilterPF1Th9 = cms.Path(process.phfCoincFilterPF1Th9)


process.pphfCoincFilterPF2Th10 = cms.Path(process.phfCoincFilterPF2Th10)


process.pphfCoincFilterPF2Th3 = cms.Path(process.phfCoincFilterPF2Th3)


process.pphfCoincFilterPF2Th4 = cms.Path(process.phfCoincFilterPF2Th4)


process.pphfCoincFilterPF2Th5 = cms.Path(process.phfCoincFilterPF2Th5)


process.pphfCoincFilterPF2Th6 = cms.Path(process.phfCoincFilterPF2Th6)


process.pphfCoincFilterPF2Th7 = cms.Path(process.phfCoincFilterPF2Th7)


process.pphfCoincFilterPF2Th8 = cms.Path(process.phfCoincFilterPF2Th8)


process.pphfCoincFilterPF2Th9 = cms.Path(process.phfCoincFilterPF2Th9)


process.pphfCoincFilterPF3Th10 = cms.Path(process.phfCoincFilterPF3Th10)


process.pphfCoincFilterPF3Th3 = cms.Path(process.phfCoincFilterPF3Th3)


process.pphfCoincFilterPF3Th4 = cms.Path(process.phfCoincFilterPF3Th4)


process.pphfCoincFilterPF3Th5 = cms.Path(process.phfCoincFilterPF3Th5)


process.pphfCoincFilterPF3Th6 = cms.Path(process.phfCoincFilterPF3Th6)


process.pphfCoincFilterPF3Th7 = cms.Path(process.phfCoincFilterPF3Th7)


process.pphfCoincFilterPF3Th8 = cms.Path(process.phfCoincFilterPF3Th8)


process.pphfCoincFilterPF3Th9 = cms.Path(process.phfCoincFilterPF3Th9)


process.pphfCoincFilterPF4Th10 = cms.Path(process.phfCoincFilterPF4Th10)


process.pphfCoincFilterPF4Th2 = cms.Path(process.phfCoincFilterPF4Th2)


process.pphfCoincFilterPF4Th3 = cms.Path(process.phfCoincFilterPF4Th3)


process.pphfCoincFilterPF4Th4 = cms.Path(process.phfCoincFilterPF4Th4)


process.pphfCoincFilterPF4Th5 = cms.Path(process.phfCoincFilterPF4Th5)


process.pphfCoincFilterPF4Th6 = cms.Path(process.phfCoincFilterPF4Th6)


process.pphfCoincFilterPF4Th7 = cms.Path(process.phfCoincFilterPF4Th7)


process.pphfCoincFilterPF4Th8 = cms.Path(process.phfCoincFilterPF4Th8)


process.pphfCoincFilterPF4Th9 = cms.Path(process.phfCoincFilterPF4Th9)


process.pphfCoincFilterPF5Th10 = cms.Path(process.phfCoincFilterPF5Th10)


process.pphfCoincFilterPF5Th3 = cms.Path(process.phfCoincFilterPF5Th3)


process.pphfCoincFilterPF5Th4 = cms.Path(process.phfCoincFilterPF5Th4)


process.pphfCoincFilterPF5Th5 = cms.Path(process.phfCoincFilterPF5Th5)


process.pphfCoincFilterPF5Th6 = cms.Path(process.phfCoincFilterPF5Th6)


process.pphfCoincFilterPF5Th7 = cms.Path(process.phfCoincFilterPF5Th7)


process.pphfCoincFilterPF5Th8 = cms.Path(process.phfCoincFilterPF5Th8)


process.pphfCoincFilterPF5Th9 = cms.Path(process.phfCoincFilterPF5Th9)


process.p = cms.Path(process.eventSelections+process.hltfilter+process.RAGHUV0)


