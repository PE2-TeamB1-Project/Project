import analysispy
from analysispy import *

b=[]
for i in range(0,len(all_LMZ)):
     a = [analysispy.TestSiteInfo(all_LMZ[i],"Batch"),
          analysispy.TestSiteInfo(all_LMZ[i],"Wafer"),
          analysispy.TestSiteInfo(all_LMZ[i],"Maskset"),
          analysispy.TestSiteInfo(all_LMZ[i],"TestSite"),
          analysispy.Name(all_LMZ[i]),
          analysispy.Date(all_LMZ[i]),
          "process LMZ",
          "0.1",
          "B1",
          "B1 team member",
          analysispy.TestSiteInfo(all_LMZ[i],"DieRow"),
          analysispy.TestSiteInfo(all_LMZ[i],"DieColumn"),
          analysispy.ErrorFlag(all_LMZ[i]),
          analysispy.Errorcheck(all_LMZ[i]),
          analysispy.Wavelength(all_LMZ[i]),
          analysispy.Rsq_Ref(all_LMZ[i]),
          analysispy.transmission(all_LMZ[i]),
          analysispy.Rsq_fit(all_LMZ[i]),
          analysispy.negative1(all_LMZ[i]),
          analysispy.positive1(all_LMZ[i])]
     b.append(a)