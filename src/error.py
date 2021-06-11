import xml.etree.ElementTree as ET
import numpy as np

def polyfitT(x, y, degree):
    coeffs = np.polyfit(x, y, degree)
    # r-squared
    p = np.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)  # or [p(z) for z in x]
    ybar = np.sum(y) / len(y)  # or sum(y)/len(y)
    ssreg = np.sum((yhat - ybar) ** 2)  # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = np.sum((y - ybar) ** 2)  # or sum([ (yi - ybar)**2 for yi in y])
    results = ssreg / sstot
    return results

def Errorcheck(x):
    tree = ET.parse(x)
    L7 = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/L")
    IL7 = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/IL")
    L7 = L7.text.split(",")
    IL7 = IL7.text.split(",")
    L7 = list(map(float, L7))
    IL7 = list(map(float, IL7))
    Rsq_Ref = polyfitT(L7, IL7, 6)

    c = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/IVMeasurement/Current")
    y_2 = c.text.split(",")
    y_list = list(map(float, y_2))
    y_list_1 = []
    for i in range(len(y_list)):
        g = abs(y_list[i])
        y_list_1.append(g)
    x = y_list_1[12]
    x = float(x)
    if Rsq_Ref >= 0.996 and x >= (10**-7):
        return "No Error"
    elif Rsq_Ref <= 0.996 and x >= (10**-7):
        return "Rsq_Ref Error"
    elif Rsq_Ref >= 0.996 and x <= (10**-7):
        return "IV-fitting"
    else:
        return "Rsq_Ref Error and IV-fitting"

def ErrorFlag(x):
    tree = ET.parse(x)
    L7 = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/L")
    IL7 = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/IL")
    L7 = L7.text.split(",")
    IL7 = IL7.text.split(",")
    L7 = list(map(float, L7))
    IL7 = list(map(float, IL7))
    Rsq_Ref = polyfitT(L7, IL7, 6)

    c = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/IVMeasurement/Current")
    y_2 = c.text.split(",")
    y_list = list(map(float, y_2))
    y_list_1 = []
    for i in range(len(y_list)):
        g = abs(y_list[i])
        y_list_1.append(g)
    x = y_list_1[12]
    x = float(x)

    if Rsq_Ref >= 0.996 and x >= (10 ** -7):
        return 0
    elif Rsq_Ref <= 0.996 and x >= (10 ** -7):
        return 1
    elif Rsq_Ref >= 0.996 and x <= (10 ** -7):
        return 2
    else:
        return 3