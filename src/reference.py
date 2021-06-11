import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from fitting import *

def reference(x):
    tree = ET.parse(x)
    L = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/L")
    IL = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/IL")
    L_7 = L.text.split(",")
    IL_7 = IL.text.split(",")
    L_list_7 = list(map(float, L_7))
    IL_list_7 = list(map(float, IL_7))
    plt.scatter(L_list_7, IL_list_7, s=15, label="reference", alpha=0.01, facecolor='none', edgecolor='r')
    polyfiti = np.polyfit(L_list_7, IL_list_7, 6)
    fiti = np.poly1d(polyfiti)
    x = polyfitT(L_list_7, IL_list_7, 6)
    plt.plot(L_list_7, fiti(L_list_7), label="{}th R^2 = {}".format(6, '%0.5f'% x))
    plt.legend(loc="best")
    plt.title("Reference fitting")
    plt.xlabel('Wavelength [nm]')
    plt.ylabel('Measured transmission [dB]')
