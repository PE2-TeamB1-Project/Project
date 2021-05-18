import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
from numpy import exp
from lmfit import Model
import datetime
from dateutil.parser import parse
from filter import *


def TestSiteInfo(x,y): #Lot, Wafer,Maskset,TestSite,DieRow,DieColumn
    tree = ET.parse(x)
    a = tree.find("./TestSiteInfo")
    return (a.get(y))
# print(TestSiteInfo(xml_list[0],"DieRow"))
def Name(x):
    tree = ET.parse(x)
    b= tree.find('./ElectroOpticalMeasurements/ModulatorSite/Modulator/DeviceInfo')
    return (b.get("Name"))

def Date(x):
    tree = ET.parse(x)
    c= tree.find("./ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo")
    w =str(parse(c.get("DateStamp")))
    return (w[0:4]+w[5:7]+w[8:10]+"_"+w[11:13]+w[14:16]+w[17:19])

def Wavelength(x):
    tree = ET.parse(x)
    d = tree.find('./ElectroOpticalMeasurements/ModulatorSite/Modulator/DeviceInfo/DesignParameters/DesignParameter[2]')
    return d.text

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

def Rsq_Ref(x):
    tree = ET.parse(x)
    L7 = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/L")
    IL7 = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/IL")
    L7 = L7.text.split(",")
    IL7 = IL7.text.split(",")
    L7 = list(map(float, L7))
    IL7 = list(map(float, IL7))
    Rsq_Ref = polyfitT(L7, IL7, 6)
    return Rsq_Ref

def transmission(x):
    tree = ET.parse(x)
    IL7 = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/IL")
    IL7 = IL7.text.split(",")
    IL7 = list(map(float, IL7))
    return max(IL7)

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
def positive1(x):
    tree = ET.parse(x)
    c = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/IVMeasurement/Current")
    y_2 = c.text.split(",")
    y_list = list(map(float, y_2))
    y_list_1=[]
    for i in range(len(y_list)):
        g = abs(y_list[i])
        y_list_1.append(g)
    return y_list_1[12]
def Errorcheck(x):
    tree = ET.parse(x)
    L7 = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/L")
    IL7 = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/IL")
    L7 = L7.text.split(",")
    IL7 = IL7.text.split(",")
    L7 = list(map(float, L7))
    IL7 = list(map(float, IL7))
    Rsq_Ref = polyfitT(L7, IL7, 6)
    if Rsq_Ref >= 0.996:
        return "No Error"
    else:
        return "Rsq_Ref Error"
def ErrorFlag(x):
    tree = ET.parse(x)
    L7 = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/L")
    IL7 = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/IL")
    L7 = L7.text.split(",")
    IL7 = IL7.text.split(",")
    L7 = list(map(float, L7))
    IL7 = list(map(float, IL7))
    Rsq_Ref = polyfitT(L7, IL7, 6)
    if Rsq_Ref >= 0.996:
        return 0
    else:
        return 1
def plot(x):
    tree = ET.parse(x)
    grid = (10, 15)
    plt.figure(figsize=(16, 10))
    plt.subplot2grid(grid, (0, 0), rowspan=4, colspan=4)

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

    plt.subplot2grid(grid, (0, 5), rowspan=4, colspan=4)

    L = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/L")
    IL = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/IL")
    L_7 = L.text.split(",")
    IL_7 = IL.text.split(",")
    L_list_7 = list(map(float, L_7))
    IL_list_7 = list(map(float, IL_7))
    DBias = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep")
    plt.scatter(L_list_7, IL_list_7, s=15, label="reference", alpha=0.01, facecolor='none', edgecolor='r')

    def polyfitT(x, y, degree):
        coeffs = np.polyfit(x, y, degree)
        p = np.poly1d(coeffs)
        yhat = p(x)
        ybar = np.sum(y) / len(y)
        ssreg = np.sum((yhat - ybar) ** 2)
        sstot = np.sum((y - ybar) ** 2)
        results = ssreg / sstot
        return results

    for i in range(2, 9):
        polyfiti = np.polyfit(L_list_7, IL_list_7, i)
        fiti = np.poly1d(polyfiti)
        plt.plot(L_list_7, fiti(L_list_7), label="{}th R^2 = {}".format(i, polyfitT(L_list_7, IL_list_7, i)))
    plt.legend(loc="best")
    plt.title("Reference fitting")
    plt.xlabel('Wavelength [nm]')
    plt.ylabel('Measured transmission [dB]')

    plt.subplot2grid(grid, (0, 10), rowspan=4, colspan=4)

    polyfit6 = np.polyfit(L_list_7, IL_list_7, 6)
    fit6 = np.poly1d(polyfit6)

    for i in range(1, 7):
        L = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep[{}]/L".format(i))
        IL = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep[{}]/IL".format(i))
        L_i = L.text.split(",")
        IL_i = IL.text.split(",")
        L_list_i = list(map(float, L_i))
        IL_list_i = list(map(float, IL_i))
        DBias = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/WavelengthSweep[{}]".format(i))
        plt.plot(L_list_i, IL_list_i - fit6(L_list_i), ".", label=DBias.get("DCBias"))

    L = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/L")
    IL = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep/IL")
    L_7 = L.text.split(",")
    IL_7 = IL.text.split(",")
    L_list_7 = list(map(float, L_7))
    IL_list_7 = list(map(float, IL_7))
    DBias = tree.find(".ElectroOpticalMeasurements/ModulatorSite/Modulator[2]/PortCombo/WavelengthSweep")
    plt.plot(L_list_7, IL_list_7 - fit6(L_list_7), ".",label = DBias.get("DCBias"))
    plt.legend(loc=(0, 0))
    plt.title("Transmission spectra - as processed")
    plt.xlabel('Wavelength [nm]')
    plt.ylabel('flat Measured transmission [dB]')

    plt.subplot2grid(grid, (5, 0), rowspan=4, colspan=4)
    from numpy import exp
    from lmfit import Model

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
    plt.plot(x_list, y_list_1, "ro", label='initial fit')
    plt.yscale("log")
    plt.title("IV-analysis")
    plt.xlabel('Voltage [V]')
    plt.ylabel('Current [A]')

    polyfiti = np.polyfit(x_list, y_list_1, 12)
    fiti = np.poly1d(polyfiti)

    def IVfittting(x, q, w, alp):
        return abs(q * (exp(x / w) - 1)) + alp * fiti(x)

    gmodel = Model(IVfittting)
    result = gmodel.fit(y_list_1, x=x_list, q=1, w=1, alp=1)

    yhat = result.best_fit
    ybar = np.sum(y_list_1) / len(y_list_1)
    ssreg = np.sum((yhat - ybar) ** 2)
    sstot = np.sum((y_list_1 - ybar) ** 2)
    results = ssreg / sstot

    plt.plot(x_list, result.best_fit, 'b-', label='best fit R^2={}'.format(results))
    plt.xlabel('Voltage [V]')
    plt.ylabel('Current [A]')
    plt.title('IV-fitting')
    plt.text(-1, result.best_fit[4], str(result.best_fit[4]), color='g', horizontalalignment='center',
             verticalalignment='bottom')
    plt.text(1, result.best_fit[12], str(result.best_fit[12]), color='g', horizontalalignment='center',
             verticalalignment='bottom')
    plt.legend()
