from CRABClient.UserUtilities import config
config = config()

config.section_('General')
config.General.requestName = 'Upsilon_Coherent2s_HiSkim_UPC_modified'
config.General.workArea = 'Monte_Crab_Projects_HiSkim'

config.General.transferOutputs = True
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'onia2MuMuPAT_pPb_80x_MC_cfg.py'

#config.Data.inputDBS = 'global'
config.Data.inputDBS = 'phys03'
#config.Data.inputDataset ='/pLHEqedStarLightMonteCarloProduction/singhm-RECOSTARLightUpsilonQEDMonteCarlo-7ec867a76e3c5f2a337cacb1196f52aa/USER'
#config.Data.inputDataset = '/pLHECoherent1sStarLightMonteCarloProduction/singhm-RECOSTARLightUpsilonCoherent1sMonteCarlo-7ec867a76e3c5f2a337cacb1196f52aa/USER'
config.Data.inputDataset = '/pLHECoherent2sStarLightMonteCarloProduction/singhm-RECOSTARLightUpsilonCoherent2sMonteCarlo-7ec867a76e3c5f2a337cacb1196f52aa/USER'
#config.Data.inputDataset = '/pLHECoherent3sStarLightMonteCarloProduction/singhm-RECOSTARLightUpsilonCoherent3sMonteCarlo-7ec867a76e3c5f2a337cacb1196f52aa/USER'
#config.Data.inputDataset = '/pLHEIncoherent1sStarLightMonteCarloProduction/singhm-RECOSTARLightUpsilonIncoherent1sMonteCarlo-7ec867a76e3c5f2a337cacb1196f52aa/USER'
#config.Data.inputDataset = '/pLHEIncoherent2sStarLightMonteCarloProduction/singhm-RECOSTARLightUpsilonIncoherent2sMonteCarlo-7ec867a76e3c5f2a337cacb1196f52aa/USER'
#config.Data.inputDataset = '/pLHEIncoherent3sStarLightMonteCarloProduction/singhm-RECOSTARLightUpsilonIncoherent3sMonteCarlo-7ec867a76e3c5f2a337cacb1196f52aa/USER'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.JobType.allowUndistributedCMSSW =True
config.section_('Data')
#config.Data.outLFNDirBase = '/store/group/phys_heavyions/subehera/skimForaccEff/'
config.Data.allowNonValidInputDataset = True
config.Data.publication = True
config.Data.outputDatasetTag = 'MonteCarloUpsilonCoherent2sModifiedHiSkim'
config.Site.storageSite = 'T2_US_Vanderbilt'

