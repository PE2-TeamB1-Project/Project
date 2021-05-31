from glob import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import warnings
warnings.filterwarnings('ignore')
import module as mo

def clear_png ():
    [os.remove(f) for f in glob.glob("../results/png_files/*")]

def clear_csv():
    [os.remove(f) for f in glob.glob("../results/csv_file/*")]

def make_csv ():
    mo.search('./results/png_files/')
    b=[]
    for i in range(0,len(mo.all_LMZ)):
        a = [mo.TestSiteInfo(mo.all_LMZ[i],"Batch"),
             mo.TestSiteInfo(mo.all_LMZ[i],"Wafer"),
             mo.TestSiteInfo(mo.all_LMZ[i],"Maskset"),
             mo.TestSiteInfo(mo.all_LMZ[i],"TestSite"),
             mo.Name(mo.all_LMZ[i]),
             mo.Date(mo.all_LMZ[i]),
             "process LMZ",
             "0.1",
             "B1",
             "B1 team member",
             mo.TestSiteInfo(mo.all_LMZ[i],"DieRow"),
             mo.TestSiteInfo(mo.all_LMZ[i],"DieColumn"),
             mo.ErrorFlag(mo.all_LMZ[i]),
             mo.Errorcheck(mo.all_LMZ[i]),
             mo.Wavelength(mo.all_LMZ[i]),
             mo.Rsq_Ref(mo.all_LMZ[i]),
             mo.transmission(mo.all_LMZ[i]),
             mo.Rsq_fit(mo.all_LMZ[i]),
             mo.negative1(mo.all_LMZ[i]),
             mo.positive1(mo.all_LMZ[i])]
        if len(mo.file_list) > 0:
            a.append("""=HYPERLINK("./results/png_files/Analysis_{0}_({1},{2})_{3}_{4}.png",
                    "Analysis_{0}_({1},{2})_{3}_{4}")""".format(
                mo.TestSiteInfo(mo.all_LMZ[i], "Wafer"),
                mo.TestSiteInfo(mo.all_LMZ[i], "DieRow"),
                mo.TestSiteInfo(mo.all_LMZ[i], "DieColumn"),
                mo.TestSiteInfo(mo.all_LMZ[i], 'TestSite'),
                mo.Date(mo.all_LMZ[i])))
        else:
            a.append(['NaN'])
        b.append(a)

    df = pd.DataFrame(np.array(b),
          columns=['Lot',
                   'Wafer',
                   'Mask',
                   'TestSite',
                   'Name',
                   'Date',
                   'Scrip ID',
                   'Script Version',
                   "Script Owner",
                   "Operator",
                   "Row",
                   "Column",
                   "ErrorFlag",
                   "Error description",
                   "Analysis Wavelengh",
                   "Rsq of Ref.spectrum(6th)",
                   "Max transmission of Ref spec(dB)",
                   "Rsq of IV",
                   "I at -1V[A]",
                   "I at 1V[A]",
                   "HyperLink"])

    df.to_csv("./results/csv_file/Analysis_B1.csv",mode="w")
# ------------------------------------------------------------------------------
def make_png ():
    for i in range(0,len(mo.all_LMZ)):
        mo.plot(mo.all_LMZ[i])
        plt.savefig("./results/png_files/Analysis_{}_({},{})_{}_{}.png"
                .format(mo.TestSiteInfo(mo.all_LMZ[i],"Wafer"),
                        mo.TestSiteInfo(mo.all_LMZ[i],"DieRow"),
                        mo.TestSiteInfo(mo.all_LMZ[i],"DieColumn"),
                        mo.TestSiteInfo(mo.all_LMZ[i],'TestSite'),
                        mo.Date(mo.all_LMZ[i])))
        plt.close()


# C:/Users/junsu/PE2_Project-1/사진
# C:/Users/ps311/Programming/PycharmProjects/PE2_WorkingSP/Results/PNG_files
# C:/Users/dream/Desktop/수업자료/3-1학기/공프2/hatefinal
