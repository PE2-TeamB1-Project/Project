import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QTextEdit, QComboBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication, Qt
from functools import partial

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

        Wafer_D07 = QCheckBox('D07',self)
        Wafer_D07.move(30,80)
        Wafer_D08 = QCheckBox('D08',self)
        Wafer_D08.move(100,80)
        Wafer_D23 = QCheckBox('D23',self)
        Wafer_D23.move(170,80)
        Wafer_D24 = QCheckBox('D24',self)
        Wafer_D24.move(240,80)

        Row_label = QLabel('Row : ',self)
        Row_label.move(30, 130)
        Row = QComboBox(self)
        Row.addItem('--'),Row.addItem('-4'), Row.addItem('-3'), Row.addItem('-2'), Row.addItem('-1'), Row.addItem('0'), Row.addItem('1'), Row.addItem('2'), Row.addItem('3'), Row.addItem('4'), Row.addItem('all')
        Row.move(80,130)

        Col_label = QLabel('Column : ',self)
        Col_label.move(180, 130)
        Col = QComboBox(self)
        Col.addItem('--'),Col.addItem('-4'), Col.addItem('-3'), Col.addItem('-2'), Col.addItem('-1'), Col.addItem('0'), Col.addItem('1'), Col.addItem('2'), Col.addItem('3'), Col.addItem('4'), Col.addItem('all')
        Col.move(250,130)

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

        btn1 = QPushButton('Plot',self)
        btn1.move(50,350)

        btn = QPushButton('Quit', self)
        btn.move(250,350)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.all_Check.stateChanged.connect(self.turnoff4)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())