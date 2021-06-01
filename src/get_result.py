import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import warnings
warnings.filterwarnings('ignore')
import src
import shutil

def clear_png ():
    shutil.rmtree("./results/png_files")
    os.mkdir("./results/png_files")
def clear_csv():
    shutil.rmtree("./results/csv_file")
    os.mkdir("./results/csv_file")

def make_csv():
    src.search('./results/png_files/')
    b=[]
    for i in range(0,len(src.all_LMZ)):
        a = [src.TestSiteInfo(src.all_LMZ[i],"Batch"),
             src.TestSiteInfo(src.all_LMZ[i],"Wafer"),
             src.TestSiteInfo(src.all_LMZ[i],"Maskset"),
             src.TestSiteInfo(src.all_LMZ[i],"TestSite"),
             src.Name(src.all_LMZ[i]),
             src.Date(src.all_LMZ[i]),
             "process LMZ",
             "0.1",
             "B1",
             "B1 team member",
             src.TestSiteInfo(src.all_LMZ[i],"DieRow"),
             src.TestSiteInfo(src.all_LMZ[i],"DieColumn"),
             src.ErrorFlag(src.all_LMZ[i]),
             src.Errorcheck(src.all_LMZ[i]),
             src.Wavelength(src.all_LMZ[i]),
             src.Rsq_Ref(src.all_LMZ[i]),
             src.transmission(src.all_LMZ[i]),
             src.Rsq_fit(src.all_LMZ[i]),
             src.negative1(src.all_LMZ[i]),
             src.positive1(src.all_LMZ[i])]
        if len(src.file_list) > 0:
            a.append("""=HYPERLINK("./results/png_files/Analysis_{0}_({1},{2})_{3}_{4}.png",
                    "Analysis_{0}_({1},{2})_{3}_{4}")""".format(
                src.TestSiteInfo(src.all_LMZ[i], "Wafer"),
                src.TestSiteInfo(src.all_LMZ[i], "DieRow"),
                src.TestSiteInfo(src.all_LMZ[i], "DieColumn"),
                src.TestSiteInfo(src.all_LMZ[i], 'TestSite'),
                src.Date(src.all_LMZ[i])))
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
    for i in range(0,len(src.all_LMZ)):
        src.plot(src.all_LMZ[i])
        plt.savefig("./results/png_files/Analysis_{}_({},{})_{}_{}.png"
                .format(src.TestSiteInfo(src.all_LMZ[i],"Wafer"),
                        src.TestSiteInfo(src.all_LMZ[i],"DieRow"),
                        src.TestSiteInfo(src.all_LMZ[i],"DieColumn"),
                        src.TestSiteInfo(src.all_LMZ[i],'TestSite'),
                        src.Date(src.all_LMZ[i])))
        plt.close()


# C:/Users/junsu/PE2_Project-1/사진
# C:/Users/ps311/Programming/PycharmProjects/PE2_WorkingSP/Results/PNG_files
# C:/Users/dream/Desktop/수업자료/3-1학기/공프2/hatefinal