if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException
    
    from CRABClient.UserUtilities import config
    config = config()
    
    config.General.workArea = 'hydjet_2018PbPb'
    config.General.transferOutputs = True
    config.General.transferLogs = False
    config.JobType.pluginName = 'Analysis'
    #config.JobType.maxMemoryMB = 4000
    #config.JobType.maxJobRuntimeMin = 2100
    #config.JobType.psetName = '../cfg/raghuv0ana_base_cfg.py'
    config.Data.unitsPerJob = 10
    config.Data.totalUnits = -1
    config.Data.inputDBS = 'phys03'
    #config.Data.splitting = 'LumiBased'
    config.Data.splitting = 'FileBased'
    config.Data.useParent = True
    #config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())                                                                                                         
    config.Data.outLFNDirBase = '/store/user/rpradhan/'
    config.Data.publication = False
    config.Site.storageSite = 'T2_IN_TIFR'
    
    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)
 #############################################################################################                                                                                      
 ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##                                                                                      
 #############################################################################################                                                                                      
            
 ###############################                                                                                                                                              
 #    Standard analysis        #                                                                                                                                                    
 ###############################                                                                                                                                                    
            
    config.General.requestName = 'hydjet_2018PbPb_LAL_daucut_check_reco_match_Jan25_2022_newnew'
    config.JobType.psetName = '../cfg/PbPb_2018_cfg.py'
    config.Data.inputDataset = '/MinBias_Hydjet_Drum5F_2018_5p02TeV/qwang-crab_HydjetDrum5F_RECODEBUG_V0Skim_v2-4fb2a1ba2f6b043399c08fb9db565e25/USER'
    #config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
    config.Data.outputDatasetTag = 'hydjet_2018PbPb_LAL_daucut_check_reco_match_Jan25_2022_newnew'
    submit(config)
    
            
    
