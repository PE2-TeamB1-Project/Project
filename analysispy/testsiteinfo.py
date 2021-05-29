import xml.etree.ElementTree as ET

def TestSiteInfo(x,y): #Lot, Wafer,Maskset,TestSite,DieRow,DieColumn
    tree = ET.parse(x)
    a = tree.find("./TestSiteInfo")
    return (a.get(y))