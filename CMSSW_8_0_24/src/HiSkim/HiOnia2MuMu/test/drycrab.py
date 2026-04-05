from CRABClient.UserUtilities import config
config = config()


config.General.transferOutputs = True
config.General.transferLogs = False
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.Data.inputDBS = 'phys03'
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.splitting = 'FileBased'
config.Data.ignoreLocality = False
config.Site.storageSite = 'T2_IN_TIFR'
#config.JobType.maxMemoryMB = 4000
config.General.requestName = 'Reco_accpreffcal_Incoherent'
config.JobType.psetName = 'onia2MuMuPAT_pPb_80x_MC_cfg.py'
config.Data.inputDataset = '/StarLight_pLHEToGS_Incoherent_accEff/subehera-StarLight_Incoherent_aodSIM-3f515a7da8f50f7c0e7244974b1ec87a/USER'
config.Data.outputDatasetTag = 'Reco_accpreffcal_Incoherent'
config.Data.outLFNDirBase = '/store/user/subehera/'
