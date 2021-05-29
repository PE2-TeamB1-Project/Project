import xml.etree.ElementTree as ET
from dateutil.parser import parse

def Date(x):
    tree = ET.parse(x)
    c= tree.find("./ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo")
    w =str(parse(c.get("DateStamp")))
    return (w[0:4]+w[5:7]+w[8:10]+"_"+w[11:13]+w[14:16]+w[17:19])