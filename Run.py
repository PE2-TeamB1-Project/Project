import project as ifm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from filter import *

b=[]
for i in range(0,len(all_LMZ)):
     a = [ifm.TestSiteInfo(all_LMZ[i],"Batch"),
          ifm.TestSiteInfo(all_LMZ[i],"Wafer"),
          ifm.TestSiteInfo(all_LMZ[i],"Maskset"),
          ifm.TestSiteInfo(all_LMZ[i],"TestSite"),
          ifm.Name(all_LMZ[i]),
          ifm.Date(all_LMZ[i]),
          "process LMZ",
          "0.1",
          "B1",
          "B1 team member",
          ifm.TestSiteInfo(all_LMZ[i],"DieRow"),
          ifm.TestSiteInfo(all_LMZ[i],"DieColumn"),
          ifm.ErrorFlag(all_LMZ[i]),
          ifm.Errorcheck(all_LMZ[i]),
          ifm.Wavelength(all_LMZ[i]),
          ifm.Rsq_Ref(all_LMZ[i]),
          ifm.transmission(all_LMZ[i]),
          ifm.Rsq_fit(all_LMZ[i]),
          ifm.negative1(all_LMZ[i]),
          ifm.positive1(all_LMZ[i])]
     b.append(a)



df = pd.DataFrame(np.array(b),columns=['Lot','Wafer','Mask',
                                       'TestSite','Name','Date','Scrip ID','Script Version',
                                       "Script Owner","Operator","Row","Column"
                                        ,"ErrorFlag","Error description","Analysis Wavelengh",
                                       "Rsq of Ref.spectrum(6th)","Max transmission of Ref spec(dB)",
                                       "Rsq of IV","I at -1V[A]","I at 1V[A]"])

df.to_csv("pandas.csv",mode="w")
# ------------------------------------------------------------------------------
for i in range(0,len(all_LMZ)):
    ifm.plot(all_LMZ[i])
    plt.savefig("C:/Users/junsu/PE2_Project-1/사진/Analysis_{}_({},{}).png".format(ifm.TestSiteInfo(all_LMZ[i],"Wafer"),ifm.TestSiteInfo(all_LMZ[i],"DieRow"),ifm.TestSiteInfo(all_LMZ[i],"DieColumn")))