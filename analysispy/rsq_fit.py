import xml.etree.ElementTree as ET
import numpy as np
from numpy import exp
from lmfit import Model

def Rsq_fit(x):
    tree = ET.parse(x)
    b = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/IVMeasurement/Voltage")
    c = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/IVMeasurement/Current")
    x_2 = b.text.split(",")
    y_2 = c.text.split(",")
    x_list = list(map(float, x_2))
    y_list = list(map(float, y_2))
    y_list_1 = []
    for i in range(len(y_list)):
        g = abs(y_list[i])
        y_list_1.append(g)

    polyfiti = np.polyfit(x_list, y_list_1, 12)
    fiti = np.poly1d(polyfiti)

    def gaussian(x, q, w, alp):
        return abs(q * (exp(x / w) - 1)) + alp * fiti(x)

    gmodel = Model(gaussian)
    result = gmodel.fit(y_list_1, x=x_list, q=1, w=1, alp=1)

    yhat = result.best_fit
    ybar = np.sum(y_list_1) / len(y_list_1)
    ssreg = np.sum((yhat - ybar) ** 2)
    sstot = np.sum((y_list_1 - ybar) ** 2)
    results = ssreg / sstot
    return results