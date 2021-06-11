from extract import *
import error
import rsq_ref as ref
import rsq_fit as fit
import i_one
import i_none
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from filter import *
import shutil
import warnings
import openpyxl
warnings.filterwarnings('ignore')
from png_signal import *

def clear_png ():
    shutil.rmtree("./results/png_files")
    os.mkdir("./results/png_files")

def clear_xlsx():
    shutil.rmtree("./results/xlsx_file")
    os.mkdir("./results/xlsx_file")
def make_xlsx ():
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
            a.append('=HYPERLINK("../png_files/Analysis_{0}_({1},{2})_{3}_{4}.png","show '
                     'png")'.format(
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

    writer = pd.ExcelWriter("./results/xlsx_file/Analysis_B1.xlsx")
    df.to_excel(writer)
    writer.save()
