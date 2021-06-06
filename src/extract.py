import xml.etree.ElementTree as ET
from dateutil.parser import parse


#This function is belonging to testsiteinfo.py at junsu
def TestSiteInfo(x,y): #Lot, Wafer,Maskset,TestSite,DieRow,DieColumn
    tree = ET.parse(x)
    a = tree.find("./TestSiteInfo")
    return (a.get(y))

#This function is belonging to date.py at junsu
def Date(x):
    tree = ET.parse(x)
    c= tree.find("./ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo")
    w =str(parse(c.get("DateStamp")))
    return (w[0:4]+w[5:7]+w[8:10]+"_"+w[11:13]+w[14:16]+w[17:19])

#This function is belonging to transmission.py at junsu
def transmission(x):
    tree = ET.parse(x)
    IL7 = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/IL")
    IL7 = IL7.text.split(",")
    IL7 = list(map(float, IL7))
    return max(IL7)

#This function is belonging to name.py at junsu
def Name(x):
    tree = ET.parse(x)
    b= tree.find('./ElectroOpticalMeasurements/ModulatorSite/Modulator/DeviceInfo')
    return (b.get("Name"))

#This function is belonging to wavelength.py at junsu
def Wavelength(x):
    tree = ET.parse(x)
    d = tree.find('./ElectroOpticalMeasurements/ModulatorSite/Modulator/DeviceInfo/DesignParameters/DesignParameter[2]')
    return d.text