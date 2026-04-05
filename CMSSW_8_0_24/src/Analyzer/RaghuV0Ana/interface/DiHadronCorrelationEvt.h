
#ifndef DiHadronCorrelationEvt_
#define DiHadronCorrelationEvt_
#include <vector>
#include <TVector3.h>
#include <TLorentzVector.h>

//massVect_trg

class DiHadronCorrelationEvt {                                                                                  

 public:                                                                                           
  //std::vector< std:: vector<TLorentzVector> >  pVect_trg;
  std::vector<std::vector<TVector3>> pVect_trg; 
  std::vector<double>                    nMultCorrVect_trg;
  std::vector< std:: vector<double> >    chgVect_trg;
  std::vector< std:: vector<double> >    massVect_trg;
  std::vector< std:: vector<double> >    effVect_trg;
  std::vector< std:: vector<double> >    weightVect_all;
  std::vector< std:: vector<double> >    phiWVect_trg;
  std::vector< std:: vector<double> >    chgVect_daup_trg;
  // std::vector< std:: vector<TLorentzVector> >  pVect_daup_trg;
  std::vector<std::vector<TVector3>> pVect_daup_trg;
  std::vector< std:: vector<double> >    chgVect_daun_trg;
  //std::vector< std:: vector<TLorentzVector> >  pVect_daun_trg;
  std::vector<std::vector<TVector3>> pVect_daun_trg;
  //std::vector< std:: vector<TLorentzVector> >  pVect_ass;
  std::vector<std::vector<TVector3>> pVect_ass; 
  std::vector<double>                    nMultCorrVect_ass;
  std::vector< std:: vector<double> >    chgVect_ass;
  std::vector< std:: vector<double> >    effVect_ass;
  std::vector< std:: vector<double> >    phiWVect_ass;
  std::vector< std:: vector<double> >    chgVect_daup_ass;
  //std::vector< std:: vector<TLorentzVector> >  pVect_daup_ass;
  std::vector<std::vector<TVector3>> pVect_daup_ass; 
  std::vector< std:: vector<double> >    chgVect_daun_ass;
  //std::vector< std:: vector<TLorentzVector> >  pVect_daun_ass;
  std::vector<std::vector<TVector3>> pVect_daun_ass;
  
  int    run;
  int    event;
  double zvtx;
  float cntbin;
  double noff;
  int ntrkOFF;
  int cent;
  
   bool operator<(const DiHadronCorrelationEvt & b) const{
     if (zvtx != b.zvtx) return zvtx < b.zvtx;
        else return false;
   }

   DiHadronCorrelationEvt()
   {
     pVect_trg.resize(10); 
     nMultCorrVect_trg.resize(10); 
     chgVect_trg.resize(10);
     massVect_trg.resize(10);
     effVect_trg.resize(10);
     weightVect_all.resize(10);
     phiWVect_trg.resize(10);
     pVect_daup_trg.resize(10);
     chgVect_daup_trg.resize(10);
     pVect_daun_trg.resize(10);
     chgVect_daun_trg.resize(10);

     pVect_ass.resize(10); 
     nMultCorrVect_ass.resize(10); 
     chgVect_ass.resize(10);
     effVect_ass.resize(10);
     phiWVect_ass.resize(10);
     pVect_daup_ass.resize(10);
     chgVect_daup_ass.resize(10);
     pVect_daun_ass.resize(10);
     chgVect_daun_ass.resize(10);
   }

   DiHadronCorrelationEvt(unsigned int size_trg, unsigned int size_ass)
   {
     pVect_trg.resize(size_trg); 
     nMultCorrVect_trg.resize(size_trg); 
     chgVect_trg.resize(size_trg);
     massVect_trg.resize(size_trg);
     effVect_trg.resize(size_trg);
     weightVect_all.resize(size_trg);
     phiWVect_trg.resize(size_trg);
     pVect_daup_trg.resize(size_trg);
     chgVect_daup_trg.resize(size_trg);
     pVect_daun_trg.resize(size_trg);
     chgVect_daun_trg.resize(size_trg);

     pVect_ass.resize(size_ass); 
     nMultCorrVect_ass.resize(size_ass); 
     chgVect_ass.resize(size_ass);
     effVect_ass.resize(size_ass);
     phiWVect_ass.resize(size_ass);
     pVect_daup_ass.resize(size_ass);
     chgVect_daup_ass.resize(size_ass);
     pVect_daun_ass.resize(size_ass);
     chgVect_daun_ass.resize(size_ass);


   }

   ~DiHadronCorrelationEvt()
   {
     pVect_trg.clear(); 
     nMultCorrVect_trg.clear(); 
     chgVect_trg.clear();
     massVect_trg.clear();
     effVect_trg.clear();
     weightVect_all.clear();
     phiWVect_trg.clear();
     pVect_daup_trg.clear();
     chgVect_daup_trg.clear();
     pVect_daun_trg.clear();
     chgVect_daun_trg.clear();
     
     //std::vector< std:: vector<TLorentzVector> >().swap(pVect_trg);
     std::vector< std:: vector<TVector3> >().swap(pVect_trg); 
     std::vector<double>().swap(nMultCorrVect_trg); 
     std::vector< std:: vector<double> >().swap(chgVect_trg);
     std::vector< std:: vector<double> >().swap(massVect_trg);
     std::vector< std:: vector<double> >().swap(effVect_trg);
     std::vector< std:: vector<double> >().swap(weightVect_all);
     std::vector< std:: vector<double> >().swap(phiWVect_trg);
     // std::vector< std:: vector<TLorentzVector> >().swap(pVect_daup_trg);
     std::vector< std:: vector<TVector3> >().swap(pVect_daup_trg);
     std::vector< std:: vector<double> >().swap(chgVect_daup_trg); 
     // std::vector< std:: vector<TLorentzVector> >().swap(pVect_daun_trg);
     std::vector< std:: vector<TVector3> >().swap(pVect_daun_trg);
     std::vector< std:: vector<double> >().swap(chgVect_daun_trg); 

     pVect_ass.clear(); 
     nMultCorrVect_ass.clear(); 
     chgVect_ass.clear();
     //massVect_ass.clear();
     effVect_ass.clear();
     phiWVect_ass.clear();
     pVect_daup_ass.clear();
     chgVect_daup_ass.clear();
     pVect_daun_ass.clear();
     chgVect_daun_ass.clear();
     
     //std::vector< std:: vector<TLorentzVector> >().swap(pVect_ass);
     std::vector< std:: vector<TVector3> >().swap(pVect_ass);
     std::vector<double>().swap(nMultCorrVect_ass); 
     std::vector< std:: vector<double> >().swap(chgVect_ass);
     std::vector< std:: vector<double> >().swap(effVect_ass);
     std::vector< std:: vector<double> >().swap(phiWVect_ass);
     //std::vector< std:: vector<TLorentzVector> >().swap(pVect_daup_ass);
     std::vector< std:: vector<TVector3> >().swap(pVect_daup_ass);
     std::vector< std:: vector<double> >().swap(chgVect_daup_ass); 
     //std::vector< std:: vector<TLorentzVector> >().swap(pVect_daun_ass);
     std::vector< std:: vector<TVector3> >().swap(pVect_daun_ass);
     std::vector< std:: vector<double> >().swap(chgVect_daun_ass); 
   }

   void reset()
   {
     unsigned int size = 0;
     
     size = pVect_trg.size();
     pVect_trg.clear();
     // std::vector< std:: vector<TLorentzVector> >().swap(pVect_trg);
     std::vector< std:: vector<TVector3> >().swap(pVect_trg); 
     pVect_trg.resize(size);

     size = nMultCorrVect_trg.size();
     nMultCorrVect_trg.clear(); 
     std::vector<double>().swap(nMultCorrVect_trg);
     nMultCorrVect_trg.resize(size);

     size = chgVect_trg.size();
     chgVect_trg.clear();
     std::vector< std:: vector<double> >().swap(chgVect_trg);
     chgVect_trg.resize(size);

     size = massVect_trg.size();
     massVect_trg.clear();
     std::vector< std:: vector<double> >().swap(massVect_trg);
     massVect_trg.resize(size);

     size = effVect_trg.size();
     effVect_trg.clear();
     std::vector< std:: vector<double> >().swap(effVect_trg);
     effVect_trg.resize(size);

     size = weightVect_all.size();
     weightVect_all.clear();
     std::vector< std:: vector<double> >().swap(weightVect_all);
     weightVect_all.resize(size);


     size = phiWVect_trg.size();
     phiWVect_trg.clear();
     std::vector< std:: vector<double> >().swap(phiWVect_trg);
     phiWVect_trg.resize(size);

     size = pVect_daup_trg.size();
     pVect_daup_trg.clear();
     //std::vector< std:: vector<TLorentzVector> >().swap(pVect_daup_trg);
     std::vector< std:: vector<TVector3> >().swap(pVect_daup_trg);
     pVect_daup_trg.resize(size);

     size = chgVect_daup_trg.size();
     chgVect_daup_trg.clear();
     std::vector< std:: vector<double> >().swap(chgVect_daup_trg);
     chgVect_daup_trg.resize(size);

     size = pVect_daun_trg.size();
     pVect_daun_trg.clear();
     //std::vector< std:: vector<TLorentzVector> >().swap(pVect_daun_trg);
     std::vector< std:: vector<TVector3> >().swap(pVect_daun_trg); 
     pVect_daun_trg.resize(size);

     size = chgVect_daun_trg.size();
     chgVect_daun_trg.clear();
     std::vector< std:: vector<double> >().swap(chgVect_daun_trg);
     chgVect_daun_trg.resize(size);

     size = pVect_ass.size();
     pVect_ass.clear();
     //std::vector< std:: vector<TLorentzVector> >().swap(pVect_ass);
     std::vector< std:: vector<TVector3> >().swap(pVect_ass); 
     pVect_ass.resize(size);
 
     size = nMultCorrVect_ass.size();
     nMultCorrVect_ass.clear(); 
     std::vector<double>().swap(nMultCorrVect_ass);
     nMultCorrVect_ass.resize(size);

     size = chgVect_ass.size();
     chgVect_ass.clear();
     std::vector< std:: vector<double> >().swap(chgVect_ass);
     chgVect_ass.resize(size);

     size = effVect_ass.size();
     effVect_ass.clear();
     std::vector< std:: vector<double> >().swap(effVect_ass);
     effVect_ass.resize(size);

     size = phiWVect_ass.size();
     phiWVect_ass.clear();
     std::vector< std:: vector<double> >().swap(phiWVect_ass);
     phiWVect_ass.resize(size);

     size = pVect_daup_ass.size();
     pVect_daup_ass.clear();
     //std::vector< std:: vector<TLorentzVector> >().swap(pVect_daup_ass);
     std::vector< std:: vector<TVector3> >().swap(pVect_daup_ass); 
     pVect_daup_ass.resize(size);

     size = chgVect_daup_ass.size();
     chgVect_daup_ass.clear();
     std::vector< std:: vector<double> >().swap(chgVect_daup_ass);
     chgVect_daup_ass.resize(size);

     size = pVect_daun_ass.size();
     pVect_daun_ass.clear();
     //std::vector< std:: vector<TLorentzVector> >().swap(pVect_daun_ass);
     std::vector< std:: vector<TVector3> >().swap(pVect_daun_ass); 
     pVect_daun_ass.resize(size);

     size = chgVect_daun_ass.size();
     chgVect_daun_ass.clear();
     std::vector< std:: vector<double> >().swap(chgVect_daun_ass);
     chgVect_daun_ass.resize(size);

     run   = -999;
     event = -999;
     zvtx  = -999.;
     cntbin  = -999.; 
     ntrkOFF = -999;
     cent = -999;
   }
};
   
#endif  // DiHadronCorrelationEvt_
