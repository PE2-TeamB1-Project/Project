import xml.etree.ElementTree as ET

def Wavelength(x):
    tree = ET.parse(x)
    d = tree.find('./ElectroOpticalMeasurements/ModulatorSite/Modulator/DeviceInfo/DesignParameters/DesignParameter[2]')
    return d.text