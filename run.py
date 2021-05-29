from analysispy import *
import analysispy
import os

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



df = pd.DataFrame(np.array(b),columns=['Lot','Wafer','Mask',
                                       'TestSite','Name','Date','Scrip ID','Script Version',
                                       "Script Owner","Operator","Row","Column"
                                        ,"ErrorFlag","Error description","Analysis Wavelengh",
                                       "Rsq of Ref.spectrum(6th)","Max transmission of Ref spec(dB)",
                                       "Rsq of IV","I at -1V[A]","I at 1V[A]"])

# df.to_csv("Analysis_B1.csv",mode="w")
os.mkdir("C:/Users/dream/Desktop/수업자료/3-1학기/공프2/clone/images")
# ------------------------------------------------------------------------------
for i in range(0,len(all_LMZ)):
    plot.plot(all_LMZ[i])
    plt.savefig("C:/Users/dream/Desktop/수업자료/3-1학기/공프2/clone/images/Analysis{}.png"
                .format(i))
# C:/Users/junsu/Desktop/Project/images
#C:/Users/dream/Desktop/수업자료/3-1학기/공프2/PE_project
#
