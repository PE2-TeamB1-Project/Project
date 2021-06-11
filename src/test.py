from extract import *
import error
import rsq_ref as ref
import rsq_fit as fit
import i_one
import i_none
import plot
import iv
import reference
import transmission_measured as tm
import transmission_processed as tp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from filter import *
import shutil
import warnings
warnings.filterwarnings('ignore')
from png_signal import *


def test():
    for i in range(0, len(all_LMZ)):
        if TestSiteInfo(all_LMZ[i], "Wafer") == "D08":
            iv.iv(all_LMZ[i])
            plt.savefig("./results/png_files/Analysis_{}_({},{})_{}_{}_IV.png"
                        .format(TestSiteInfo(all_LMZ[i], "Wafer"),
                                TestSiteInfo(all_LMZ[i], "DieRow"),
                                TestSiteInfo(all_LMZ[i], "DieColumn"),
                                TestSiteInfo(all_LMZ[i], 'TestSite'),
                                Date(all_LMZ[i])))
            plt.close()