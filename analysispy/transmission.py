import xml.etree.ElementTree as ET

def transmission(x):
    tree = ET.parse(x)
    IL7 = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/IL")
    IL7 = IL7.text.split(",")
    IL7 = list(map(float, IL7))
    return max(IL7)