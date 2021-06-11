from lmfit import Model
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from fitting import *
from filter import *
def iv(x):
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
    plt.plot(x_list, y_list_1, "ro", label='initial fit')
    plt.yscale("log")
    plt.title("IV-analysis")
    plt.xlabel('Voltage [V]')
    plt.ylabel('Current [A]')

    gmodel = Model(IVfittting)
    result = gmodel.fit(y_list_1, x=x_list, q=1, w=1, alp=1, xi = x_list, yi = y_list_1)

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