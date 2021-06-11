import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from filter import *
def measured(x):
    tree = ET.parse(x)
    for i in range(1, 7):
        L = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep[{}]/L".format(i))
        IL = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep[{}]/IL".format(i))
        L_i = L.text.split(",")
        IL_i = IL.text.split(",")
        L_list_i = list(map(float, L_i))
        IL_list_i = list(map(float, IL_i))
        DBias = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep[{}]".format(i))
        plt.plot(L_list_i, IL_list_i, ".", label=DBias.get("DCBias"))

    L = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/L")
    IL = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/IL")
    L_7 = L.text.split(",")
    IL_7 = IL.text.split(",")
    L_list_7 = list(map(float, L_7))
    IL_list_7 = list(map(float, IL_7))
    DBias = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep")
    plt.plot(L_list_7, IL_list_7, ".", label="reference")
    plt.legend(loc=(0, 0))
    plt.title("Transmission spectra - as measured")
    plt.xlabel('Wavelength [nm]')
    plt.ylabel('Measured transmission [dB]')