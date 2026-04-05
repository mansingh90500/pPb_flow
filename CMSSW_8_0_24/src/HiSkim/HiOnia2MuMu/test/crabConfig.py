from CRABClient.UserUtilities import config
config = config()

# === General ===
config.section_('General')
config.General.requestName = 'JPsi_HiSkim_pPb_2016_HM_6_dataset'
config.General.workArea = 'Crab_Projects_JPsi_HiSkim_pPb'

config.General.transferOutputs = True
config.General.transferLogs = True

# === JobType ===
config.section_('JobType')
config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = 'onia2MuMuPATHI_pPbPrompt_DATA_cfg.py'  # Change this to your skim config if different
config.JobType.psetName = 'onia2MuMuPATHI_pPb_HM_DATA_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 3000

# === Data ===
config.section_('Data')
config.Data.inputDataset = '/PAHighMultiplicity6/PARun2016C-PromptReco-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.lumiMask = 'pPb_Collisions16_JSON.txt'  # Your JSON file for pPb 2016
config.Data.allowNonValidInputDataset = True
config.Data.publication = True
#config.Data.outputDatasetTag = 'JPsi_HiSkim_pPb_2016_v2'
config.Data.outputDatasetTag = 'JPsi_HiSkim_pPb_2016_HM_6_dataset' 
# === Site ===
config.section_('Site')
config.Site.storageSite = 'T2_US_Vanderbilt'
