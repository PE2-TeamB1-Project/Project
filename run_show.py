import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QTextEdit, QComboBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication, Qt
from functools import partial
from get_result import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle('only_image')
        self.move(300,300)
        self.resize(380,400)

        Wafer_label = QLabel('Wafer',self)
        Wafer_label.move(30, 50)
        self.Wafer = QComboBox(self)
        self.Wafer.addItem('D07'), \
        self.Wafer.addItem('D08'), \
        self.Wafer.addItem('D23'), \
        self.Wafer.addItem('D24'), \
        self.Wafer.move(30, 80)
        # Wafer_D07 = QCheckBox('D07',self)
        # Wafer_D07.move(30,80)
        # Wafer_D08 = QCheckBox('D08',self)
        # Wafer_D08.move(100,80)
        # Wafer_D23 = QCheckBox('D23',self)
        # Wafer_D23.move(170,80)
        # Wafer_D24 = QCheckBox('D24',self)
        # Wafer_D24.move(240,80)

        Row_label = QLabel('Row : ',self)
        Row_label.move(30, 130)
        self.Row = QComboBox(self)
        self.Row.addItem('-4'), \
        self.Row.addItem('-3'), \
        self.Row.addItem('-2'), \
        self.Row.addItem('-1'), \
        self.Row.addItem('0'), \
        self.Row.addItem('1'), \
        self.Row.addItem('2'), \
        self.Row.addItem('3'), \
        self.Row.move(80,130)

        Col_label = QLabel('Column : ',self)
        Col_label.move(180, 130)
        self.Col = QComboBox(self)
        self.Col.addItem('-4'), \
        self.Col.addItem('-3'), \
        self.Col.addItem('-2'), \
        self.Col.addItem('-1'), \
        self.Col.addItem('0'), \
        self.Col.addItem('1'), \
        self.Col.addItem('2'), \
        self.Col.addItem('3'), \
        self.Col.move(250,130)

        self.IV_Check = QCheckBox('IV_graph(fitting)',self)
        self.IV_Check.move(30,180)
        self.Ts1_Check = QCheckBox('Transmission spectra(measured)',self)
        self.Ts1_Check.move(30, 210)
        self.Ts2_Check = QCheckBox('Transmission spectra(processed)',self)
        self.Ts2_Check.move(30,240)
        self.Rf_Check = QCheckBox('Reference fitting',self)
        self.Rf_Check.move(30,270)
        self.all_Check = QCheckBox('all',self)
        self.all_Check.move(30,300)

        self.btn1 = QPushButton('Plot',self)
        self.btn1.move(50,350)
        self.btn1.clicked.connect(self.test2)

        self.btn2 = QPushButton('check', self)
        self.btn2.move(150, 350)
        self.btn2.clicked.connect(self.test)

        btn = QPushButton('Quit', self)
        btn.move(250,350)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.all_Check.stateChanged.connect(self.turnoff4)

    def test(self):

        x = str(self.Col.currentText())
        y = str(self.Row.currentText())
        z = str(self.Wafer.currentText())
        a=[z,y,x]
        print(a)

    def turnoff4(self):
        if self.all_Check.isChecked():
            self.IV_Check.setEnabled(False)
            self.Ts2_Check.setEnabled(False)
            self.Ts1_Check.setEnabled(False)
            self.Rf_Check.setEnabled(False)
        else:
            self.IV_Check.setEnabled(True)
            self.Ts2_Check.setEnabled(True)
            self.Ts1_Check.setEnabled(True)
            self.Rf_Check.setEnabled(True)

    def test2(self):
        x = str(self.Col.currentText())
        y = str(self.Row.currentText())
        z = str(self.Wafer.currentText())
        a = [z, y, x]

        if self.all_Check.isChecked() == True:
            for i in range(0, len(all_LMZ)):
                if TestSiteInfo(all_LMZ[i], "Wafer") == a[0] and TestSiteInfo(all_LMZ[i], "DieRow") == a[1] and TestSiteInfo(all_LMZ[i], "DieColumn") == a[2]:
                        plot.plot(all_LMZ[i])
                        plt.show()
            # print(a, "all")
        if self.IV_Check.isChecked() == True:
            for i in range(0, len(all_LMZ)):
                if TestSiteInfo(all_LMZ[i], "Wafer") == a[0] and TestSiteInfo(all_LMZ[i], "DieRow") == a[1] and TestSiteInfo(all_LMZ[i], "DieColumn") == a[2]:
                        iv.iv(all_LMZ[i])
                        plt.show()
            # print(a, "IV_graph(fitting)")
        if self.Ts1_Check.isChecked() == True:
            for i in range(0, len(all_LMZ)):
                if TestSiteInfo(all_LMZ[i], "Wafer") == a[0] and TestSiteInfo(all_LMZ[i], "DieRow") == a[1] and TestSiteInfo(all_LMZ[i], "DieColumn") == a[2]:
                        tm.measured(all_LMZ[i])
                        plt.show()
            # print(a, "Transmission spectra(measured)")
        if self.Ts2_Check.isChecked() == True:
            for i in range(0, len(all_LMZ)):
                if TestSiteInfo(all_LMZ[i], "Wafer") == a[0] and TestSiteInfo(all_LMZ[i], "DieRow") == a[1] and TestSiteInfo(all_LMZ[i], "DieColumn") == a[2]:
                        tp.processed(all_LMZ[i])
                        plt.show()
            # print(a, "Transmission spectra(processed)")
        if self.Rf_Check.isChecked() == True:
            for i in range(0, len(all_LMZ)):
                if TestSiteInfo(all_LMZ[i], "Wafer") == a[0] and TestSiteInfo(all_LMZ[i], "DieRow") == a[1] and TestSiteInfo(all_LMZ[i], "DieColumn") == a[2]:
                        reference.reference(all_LMZ[i])
                        plt.show()
            # print(a, "Reference fitting")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())