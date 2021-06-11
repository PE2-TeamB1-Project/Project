from extract import *
import iv
import matplotlib.pyplot as plt
from filter import *
import warnings
warnings.filterwarnings('ignore')



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