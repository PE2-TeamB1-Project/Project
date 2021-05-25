import testsiteinfo as info
import name
import date
import error
import wavelength as wave
import rsq_ref as ref
import rsq_fit as fit
import transmission as tms
import I_one
import I_none
import plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from filter import *
import os

b=[]
for i in range(0,len(all_LMZ)):
     a = [info.TestSiteInfo(all_LMZ[i],"Batch"),
          info.TestSiteInfo(all_LMZ[i],"Wafer"),
          info.TestSiteInfo(all_LMZ[i],"Maskset"),
          info.TestSiteInfo(all_LMZ[i],"TestSite"),
          name.Name(all_LMZ[i]),
          date.Date(all_LMZ[i]),
          "process LMZ",
          "0.1",
          "B1",
          "B1 team member",
          info.TestSiteInfo(all_LMZ[i],"DieRow"),
          info.TestSiteInfo(all_LMZ[i],"DieColumn"),
          error.ErrorFlag(all_LMZ[i]),
          error.Errorcheck(all_LMZ[i]),
          wave.Wavelength(all_LMZ[i]),
          ref.Rsq_Ref(all_LMZ[i]),
          tms.transmission(all_LMZ[i]),
          fit.Rsq_fit(all_LMZ[i]),
          I_none.negative1(all_LMZ[i]),
          I_one.positive1(all_LMZ[i])]
     b.append(a)



df = pd.DataFrame(np.array(b),columns=['Lot','Wafer','Mask',
                                       'TestSite','Name','Date','Scrip ID','Script Version',
                                       "Script Owner","Operator","Row","Column"
                                        ,"ErrorFlag","Error description","Analysis Wavelengh",
                                       "Rsq of Ref.spectrum(6th)","Max transmission of Ref spec(dB)",
                                       "Rsq of IV","I at -1V[A]","I at 1V[A]"])

df.to_csv("Analysis_B1.csv",mode="w")
os.mkdir("C:/Users/junsu/PE2_Project-1/images")
# ------------------------------------------------------------------------------
for i in range(0,len(all_LMZ)):
    plot.plot(all_LMZ[i])
    plt.savefig("C:/Users/junsu/PE2_Project-1/images/Analysis_{}_({},{})_{}_{}.png"
                .format(info.TestSiteInfo(all_LMZ[i],"Wafer"),info.TestSiteInfo(all_LMZ[i],"DieRow")
                        ,info.TestSiteInfo(all_LMZ[i],"DieColumn"),info.TestSiteInfo(all_LMZ[i],"TestSite")[4:],date.Date(all_LMZ[i])))
     plt.close()
# C:/Users/junsu/Desktop/Project/images
#C:/Users/dream/Desktop/수업자료/3-1학기/공프2/PE_project
#
