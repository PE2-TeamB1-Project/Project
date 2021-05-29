import xml.etree.ElementTree as ET

def negative1(x):
    tree = ET.parse(x)
    c = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/IVMeasurement/Current")
    y_2 = c.text.split(",")
    y_list = list(map(float, y_2))
    y_list_1=[]
    for i in range(len(y_list)):
        g = abs(y_list[i])
        y_list_1.append(g)
    return y_list_1[4]