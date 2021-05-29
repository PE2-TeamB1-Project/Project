import xml.etree.ElementTree as ET

def Name(x):
    tree = ET.parse(x)
    b= tree.find('./ElectroOpticalMeasurements/ModulatorSite/Modulator/DeviceInfo')
    return (b.get("Name"))