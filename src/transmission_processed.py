import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from fitting import *

def processed(x):
    tree = ET.parse(x)
    L = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/L")
    IL = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/IL")
    L_7 = L.text.split(",")
    IL_7 = IL.text.split(",")
    L_list_7 = list(map(float, L_7))
    IL_list_7 = list(map(float, IL_7))
    polyfit6 = np.polyfit(L_list_7, IL_list_7, 6)
    fit6 = np.poly1d(polyfit6)

    for i in range(1, 7):
        L = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep[{}]/L".format(i))
        IL = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep[{}]/IL".format(i))
        L_i = L.text.split(",")
        IL_i = IL.text.split(",")
        L_list_i = list(map(float, L_i))
        IL_list_i = list(map(float, IL_i))
        DBias = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep[{}]".format(i))
        plt.plot(L_list_i, IL_list_i - fit6(L_list_i), ".", label=DBias.get("DCBias"))

    plt.plot(L_list_7, IL_list_7 - fit6(L_list_7), ".", label=DBias.get("DCBias"))
    plt.legend(loc=(0, 0))
    plt.title("Transmission spectra - as processed")
    plt.xlabel('Wavelength [nm]')
    plt.ylabel('flat Measured transmission [dB]')
