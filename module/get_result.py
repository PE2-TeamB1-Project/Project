from extract import *
import error
import rsq_ref as ref
import rsq_fit as fit
import i_one
import i_none
import plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from filter import *
import os
import warnings
warnings.filterwarnings('ignore')
from png_signal import *

def clear_png ():
    [os.remove(f) for f in glob.glob("../results/png_files/*")]

def clear_csv():
    [os.remove(f) for f in glob.glob("../results/csv_file/*")]

def make_csv ():
    search('./results/png_files/')
    b=[]
    for i in range(0,len(all_LMZ)):
        a = [TestSiteInfo(all_LMZ[i],"Batch"),
             TestSiteInfo(all_LMZ[i],"Wafer"),
             TestSiteInfo(all_LMZ[i],"Maskset"),
             TestSiteInfo(all_LMZ[i],"TestSite"),
             Name(all_LMZ[i]),
              Date(all_LMZ[i]),
             "process LMZ",
             "0.1",
             "B1",
             "B1 team member",
             TestSiteInfo(all_LMZ[i],"DieRow"),
             TestSiteInfo(all_LMZ[i],"DieColumn"),
             error.ErrorFlag(all_LMZ[i]),
             error.Errorcheck(all_LMZ[i]),
             Wavelength(all_LMZ[i]),
             ref.Rsq_Ref(all_LMZ[i]),
             transmission(all_LMZ[i]),
             fit.Rsq_fit(all_LMZ[i]),
             i_none.negative1(all_LMZ[i]),
             i_one.positive1(all_LMZ[i])]
        if len(file_list) > 0:
            a.append("""=HYPERLINK("C:/Users/junsu/Desktop/Project/results/png_files/Analysis_{0}_({1},{2})_{3}_{4}.png")""".format(
                TestSiteInfo(all_LMZ[i], "Wafer"),
                TestSiteInfo(all_LMZ[i], "DieRow"),
                TestSiteInfo(all_LMZ[i], "DieColumn"),
                TestSiteInfo(all_LMZ[i], 'TestSite'),
                Date(all_LMZ[i])))
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
    for i in range(0,len(all_LMZ)):
        plot.plot(all_LMZ[i])
        plt.savefig("./results/png_files/Analysis_{}_({},{})_{}_{}.png"
                .format(TestSiteInfo(all_LMZ[i],"Wafer"),
                        TestSiteInfo(all_LMZ[i],"DieRow"),
                        TestSiteInfo(all_LMZ[i],"DieColumn"),
                        TestSiteInfo(all_LMZ[i],'TestSite'),
                        Date(all_LMZ[i])))
        plt.close()


# C:/Users/junsu/PE2_Project-1/사진
# C:/Users/ps311/Programming/PycharmProjects/PE2_WorkingSP/Results/PNG_files
#
