from CRABClient.UserUtilities import config
config = config()

config.section_('General')
config.General.requestName = 'HiSkim_qed_8to20Jan30'
config.General.workArea = 'Monte_Crab_check_HiSkim'

config.General.transferOutputs = True
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'onia2MuMuPAT_pPb_80x_MC_cfg.py'

#config.Data.inputDBS = 'global'
config.Data.inputDBS = 'phys03'
#config.Data.inputDataset ='/pLHECoherent1sStarLightMonteCarloProduction/singhm-RECOUpsilonCoherent1scheck4th-7ec867a76e3c5f2a337cacb1196f52aa/USER'
#config.Data.inputDataset ='/pLHECoherent2sMCProduction/singhm-RECOCoh2s-7ec867a76e3c5f2a337cacb1196f52aa/USER'
#config.Data.inputDataset ='/pLHECoherent3sMCProduction/singhm-RECOCoh3s-7ec867a76e3c5f2a337cacb1196f52aa/USER'
#config.Data.inputDataset ='/pLHEIncoherent1sMCProduction/singhm-RECOIncoh1s-7ec867a76e3c5f2a337cacb1196f52aa/USER'
#config.Data.inputDataset ='/pLHEIncoherent2sMCProduction/singhm-RECOIncoh2s-7ec867a76e3c5f2a337cacb1196f52aa/USER'
#config.Data.inputDataset ='/pLHEIncoherent3sMCProduction/singhm-RECOIncoh3s-7ec867a76e3c5f2a337cacb1196f52aa/USER'
config.Data.inputDataset ='/pLHEqedMCProduction8to20Jan30/singhm-RECOqed8to20Jan30-7ec867a76e3c5f2a337cacb1196f52aa/USER'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.JobType.allowUndistributedCMSSW =True
config.section_('Data')
#config.Data.outLFNDirBase = '/store/group/phys_heavyions/subehera/skimForaccEff/'
config.Data.allowNonValidInputDataset = True
config.Data.publication = True
config.Data.outputDatasetTag = 'HiSkimQED8to20Jan30'
config.Site.storageSite = 'T2_US_Vanderbilt'

