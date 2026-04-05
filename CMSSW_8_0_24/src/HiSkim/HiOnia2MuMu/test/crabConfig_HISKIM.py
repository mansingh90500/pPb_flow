from CRABClient.UserUtilities import config
config = config()

config.section_('General')
config.General.requestName = 'Upsilon_Coh1s_HiSkim_UPC'
config.General.workArea = 'Crab_Projects_Skim'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'onia2MuMuPAT_pPb_80x_MC_cfg.py'
#config.JobType.maxMemoryMB = 2400

config.section_('Data')
config.Data.inputDataset = '/pLHEIncoherent3sStarLightMC/singhm-RECOstep2StarLightUpsilonIncoherent3s-7ec867a76e3c5f2a337cacb1196f52aa/USER'
config.Data.inputDBS = 'phys03'
config.Data.unitsPerJob = 1
config.Data.splitting =  'FileBased'
config.JobType.allowUndistributedCMSSW = True
#config.Data.outLFNDirBase = '/store/group/phys_heavyions/subehera/hiOniaSkim/hiskim_IncoProcess/' 
config.Data.publication = False
#config.Data.outputDatasetTag = config.General.requestName

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
