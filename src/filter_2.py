import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication, Qt
import iv
import reference
import transmission_measured as tm
import transmission_processed as tp
from get_result import *
import plot
import matplotlib.pyplot as plt
from filter import *
from search import MyApp_search
import warnings
warnings.filterwarnings('ignore')

# geek list
geek_list_1_1 = ["-4", "-3", "-2", "-1", "0", "1", "2", "3"]
geek_list_1_2 = ["-4", "-3", "-2", "-1", "0", "1", "2", "3"]
geek_list_2 = ['D07', 'D08', 'D23', 'D24']
checkedItems1_1 = []
checkedItems1_2 = []
checkedItems2 = []
class CheckableComboBox2(QComboBox):
    # constructor
    def __init__(self, parent=None):
        super(CheckableComboBox2, self).__init__(parent)
        self.view().pressed.connect(self.handleItemPressed)
        self.setModel(QStandardItemModel(self))
    # when any item get pressed
    def handleItemPressed(self, index):
        # getting the item
        item = self.model().itemFromIndex(index)
        # checking if item is checked
        if item.checkState() == Qt.Checked:
            # making it unchecked
            item.setCheckState(Qt.Unchecked)
        # if not checked
        else:
            # making the item checked
            item.setCheckState(Qt.Checked)
        # calling method
        self.check_items()
    # method called by check_items
    def item_checked(self, index):
        # getting item at index
        item = self.model().item(index, 0)
        return item.checkState() == Qt.Checked
    # calling method
    def check_items(self):
        checkedItems2.clear()
        # traversing the items
        for i in range(self.count()):
            # if item is checked add it to the list
            if self.item_checked(i):
                checkedItems2.append(geek_list_2[i])

    # flush
    sys.stdout.flush()
class CheckableComboBox1_1(QComboBox):
    # constructor
    def __init__(self, parent=None):
        super(CheckableComboBox1_1, self).__init__(parent)
        self.view().pressed.connect(self.handleItemPressed)
        self.setModel(QStandardItemModel(self))
    # when any item get pressed
    def handleItemPressed(self, index):
        # getting the item
        item = self.model().itemFromIndex(index)
        # checking if item is checked
        if item.checkState() == Qt.Checked:
            # making it unchecked
            item.setCheckState(Qt.Unchecked)
        # if not checked
        else:
            # making the item checked
            item.setCheckState(Qt.Checked)
        # calling method
        self.check_items()
    # method called by check_items
    def item_checked(self, index):
        # getting item at index
        item = self.model().item(index, 0)
        # return true if checked else false
        return item.checkState() == Qt.Checked
    # calling method
    def check_items(self):
        # blank list
        checkedItems1_1.clear()
        # traversing the items
        for i in range(self.count()):
            # if item is checked add it to the list
            if self.item_checked(i):
                checkedItems1_1.append(geek_list_1_1[i])
    # flush
    sys.stdout.flush()
class CheckableComboBox1_2(QComboBox):
    # constructor
    def __init__(self, parent=None):
        super(CheckableComboBox1_2, self).__init__(parent)
        self.view().pressed.connect(self.handleItemPressed)
        self.setModel(QStandardItemModel(self))
    # when any item get pressed
    def handleItemPressed(self, index):
        # getting the item
        item = self.model().itemFromIndex(index)
        # checking if item is checked
        if item.checkState() == Qt.Checked:
            # making it unchecked
            item.setCheckState(Qt.Unchecked)
        # if not checked
        else:
            # making the item checked
            item.setCheckState(Qt.Checked)
        # calling method
        self.check_items()
    # method called by check_items
    def item_checked(self, index):
        # getting item at index
        item = self.model().item(index, 0)
        # return true if checked else false
        return item.checkState() == Qt.Checked
    # calling method
    def check_items(self):
        # blank list
        checkedItems1_2.clear()
        # traversing the items
        for i in range(self.count()):
            # if item is checked add it to the list
            if self.item_checked(i):
                checkedItems1_2.append(geek_list_1_2[i])
    # flush
    sys.stdout.flush()
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle('project_B1_save')
        self.move(300,300)
        self.resize(400,400)
        grid = QGridLayout()
        self.setLayout(grid)

        self.Wafer_label = QLabel('Wafer',self)
        grid.addWidget(self.Wafer_label, 0, 0)
        self.Wafer_all = QCheckBox('전체', self)
        grid.addWidget(self.Wafer_all, 0, 1)
        self.Wafer_all.stateChanged.connect(self.turnoff1)

        self.Col_label = QLabel('Column : ',self)
        grid.addWidget(self.Col_label, 2, 3)
        self.Col_all = QCheckBox('전체', self)
        grid.addWidget(self.Col_all, 2, 4)
        self.Col_all.stateChanged.connect(self.turnoff2)

        self.Row_label = QLabel('Row : ', self)
        grid.addWidget(self.Row_label, 2, 0)
        self.Row_all = QCheckBox('전체', self)
        grid.addWidget(self.Row_all, 2, 1)
        self.Row_all.stateChanged.connect(self.turnoff3)

        self.IV_Check = QCheckBox('IV_graph(fitting)',self)
        grid.addWidget(self.IV_Check, 3, 0)
        self.Ts1_Check = QCheckBox('Transmission spectra(measured)',self)
        grid.addWidget(self.Ts1_Check, 4, 0)
        self.Ts2_Check = QCheckBox('Transmission spectra(processed)',self)
        grid.addWidget(self.Ts2_Check, 5, 0)
        self.Rf_Check = QCheckBox('Reference fitting',self)
        grid.addWidget(self.Rf_Check, 6, 0)
        self.PNG_all = QCheckBox('All', self)
        grid.addWidget(self.PNG_all, 7, 0)

        self.PNG_all.stateChanged.connect(self.turnoff4)
        self.btn1 = QPushButton('Quit', self)
        grid.addWidget(self.btn1, 8, 6)
        self.btn1.resize(self.btn1.sizeHint())
        self.btn1.clicked.connect(QCoreApplication.instance().quit)

        self.btn2 = QPushButton('Plot', self)
        grid.addWidget(self.btn2, 8, 1)
        self.btn2.resize(self.btn2.sizeHint())
        self.btn2.clicked.connect(self.test2)

        self.btn3 = QPushButton('Delete_png', self)
        grid.addWidget(self.btn3, 8, 2)
        self.btn3.resize(self.btn3.sizeHint())
        self.btn3.clicked.connect(self.test5)

        self.btn4 = QPushButton('xlsx', self)
        grid.addWidget(self.btn4, 8, 3)
        self.btn4.resize(self.btn4.sizeHint())
        self.btn4.clicked.connect(self.test3)

        self.btn5 = QPushButton('Check', self)
        grid.addWidget(self.btn5, 8, 4)
        self.btn5.resize(self.btn5.sizeHint())
        self.btn5.clicked.connect(self.test)

        self.label = QLabel('Wafer : \nRow : \n Column : ', self)
        grid.addWidget(self.label, 8, 0)

        self.btn6 = QPushButton('Search', self)
        grid.addWidget(self.btn6, 8, 5)
        self.btn6.resize(self.btn5.sizeHint())
        self.btn6.clicked.connect(self.open_search)

        # creating a check-able combo box object
        self.combo_box_row = CheckableComboBox1_1(self)
        self.combo_box_column = CheckableComboBox1_2(self)
        self.combobox_wafer = CheckableComboBox2(self)

        # setting geometry of combo box
        grid.addWidget(self.combo_box_row, 2, 2)
        grid.addWidget(self.combo_box_column, 2, 5)
        grid.addWidget(self.combobox_wafer, 0, 2)

        # adding list of items to combo box
        self.combo_box_row.addItems(geek_list_1_1)
        self.combo_box_column.addItems(geek_list_1_2)
        self.combobox_wafer.addItems(geek_list_2)

        self.urlLink = "<a href=\"http://github.com/PE2-TeamB1-Project/Project\">'Help'</a>"
        label = QLabel(self)
        label.setText(self.urlLink)
        grid.addWidget(label, 7, 6)
        label.setOpenExternalLinks(True)

    def open_search (self):
        dlg = MyApp_search()
        dlg.exec_()

    def test(self):
        x = str(checkedItems2)
        y = str(checkedItems1_1)
        z = str(checkedItems1_2)
        self.label.setText('Wafer : ' + x[1:-1] +
                           '\nRow : ' + y[1:-1] +
                           '\nColumn : ' + z[1:-1])

    def test5(self):
        clear_png()

    def turnoff1(self):
        checkedItems2.clear()
        if self.Wafer_all.isChecked():
            self.combobox_wafer.setEnabled(False)
            for i in range(0, len(geek_list_2)):
                checkedItems2.append(geek_list_2[i])
        else:
            self.combobox_wafer.setEnabled(True)


    def turnoff2(self):
        checkedItems1_2.clear()
        if self.Col_all.isChecked():
            self.combo_box_column.setEnabled(False)
            for i in range(0, len(geek_list_1_2)):
                checkedItems1_2.append(geek_list_1_2[i])
        else:
            self.combo_box_column.setEnabled(True)


    def turnoff3(self):
        checkedItems1_1.clear()
        if self.Row_all.isChecked():
            self.combo_box_row.setEnabled(False)
            for i in range(0, len(geek_list_1_1)):
                checkedItems1_1.append(geek_list_1_1[i])
        else:
            self.combo_box_row.setEnabled(True)


    def turnoff4(self):
        if self.PNG_all.isChecked():
            self.IV_Check.setEnabled(False)
            self.Ts2_Check.setEnabled(False)
            self.Ts1_Check.setEnabled(False)
            self.Rf_Check.setEnabled(False)
        else:
            self.IV_Check.setEnabled(True)
            self.Ts2_Check.setEnabled(True)
            self.Ts1_Check.setEnabled(True)
            self.Rf_Check.setEnabled(True)

    def test3(self):
        clear_xlsx()
        make_xlsx()

    def test2(self):
        clear_png()

        if self.PNG_all.isChecked() == True:
            a = []
            for x in checkedItems2:
                for y in checkedItems1_1:
                    for z in checkedItems1_2:
                        a.append([x, y, z])
            for w in a:
                for i in range(0, len(all_LMZ)):
                    if TestSiteInfo(all_LMZ[i], "Wafer") == w[0] and TestSiteInfo(all_LMZ[i], "DieRow") == w[1] and TestSiteInfo(all_LMZ[i], "DieColumn") == w[2]:
                        plot.plot(all_LMZ[i])
                        plt.suptitle('Analysis_{}_({},{})_{}_{}'.format(TestSiteInfo(all_LMZ[i], "Wafer"),
                                            TestSiteInfo(all_LMZ[i], "DieRow"),
                                            TestSiteInfo(all_LMZ[i], "DieColumn"),
                                            TestSiteInfo(all_LMZ[i], 'TestSite'),
                                            Date(all_LMZ[i])))
                        plt.savefig("./results/png_files/Analysis_{}_({},{})_{}_{}.png"
                                    .format(TestSiteInfo(all_LMZ[i], "Wafer"),
                                            TestSiteInfo(all_LMZ[i], "DieRow"),
                                            TestSiteInfo(all_LMZ[i], "DieColumn"),
                                            TestSiteInfo(all_LMZ[i], 'TestSite'),
                                            Date(all_LMZ[i])))
                        plt.close()

        if self.IV_Check.isChecked() == True:
            b = []
            for x in checkedItems2:
                for y in checkedItems1_1:
                    for z in checkedItems1_2:
                        b.append([x, y, z])
            for w in b:
                for i in range(0, len(all_LMZ)):
                    if TestSiteInfo(all_LMZ[i], "Wafer") == w[0] and TestSiteInfo(all_LMZ[i], "DieRow") == w[1] and TestSiteInfo(all_LMZ[i], "DieColumn") == w[2]:
                        iv.iv(all_LMZ[i])
                        plt.savefig("./results/png_files/Analysis_{}_({},{})_{}_{}_iv.png"
                                    .format(TestSiteInfo(all_LMZ[i], "Wafer"),
                                            TestSiteInfo(all_LMZ[i], "DieRow"),
                                            TestSiteInfo(all_LMZ[i], "DieColumn"),
                                            TestSiteInfo(all_LMZ[i], 'TestSite'),
                                            Date(all_LMZ[i])))
                        plt.close()

        if self.Ts1_Check.isChecked() == True:
            c = []
            for x in checkedItems2:
                for y in checkedItems1_1:
                    for z in checkedItems1_2:
                        c.append([x, y, z])
            for w in c:
                for i in range(0, len(all_LMZ)):
                    if TestSiteInfo(all_LMZ[i], "Wafer") == w[0] and TestSiteInfo(all_LMZ[i], "DieRow") == w[1] and TestSiteInfo(all_LMZ[i], "DieColumn") == w[2]:
                        tm.measured(all_LMZ[i])
                        plt.savefig("./results/png_files/Analysis_{}_({},{})_{}_{}_measured.png"
                                    .format(TestSiteInfo(all_LMZ[i], "Wafer"),
                                            TestSiteInfo(all_LMZ[i], "DieRow"),
                                            TestSiteInfo(all_LMZ[i], "DieColumn"),
                                            TestSiteInfo(all_LMZ[i], 'TestSite'),
                                            Date(all_LMZ[i])))
                        plt.close()

        if self.Ts2_Check.isChecked() == True:
            d = []
            for x in checkedItems2:
                for y in checkedItems1_1:
                    for z in checkedItems1_2:
                        d.append([x, y, z])
            for w in d:
                for i in range(0, len(all_LMZ)):
                    if TestSiteInfo(all_LMZ[i], "Wafer") == w[0] and TestSiteInfo(all_LMZ[i], "DieRow") == w[1] and TestSiteInfo(all_LMZ[i], "DieColumn") == w[2]:
                        tp.processed(all_LMZ[i])
                        plt.savefig("./results/png_files/Analysis_{}_({},{})_{}_{}_processed.png"
                                    .format(TestSiteInfo(all_LMZ[i], "Wafer"),
                                            TestSiteInfo(all_LMZ[i], "DieRow"),
                                            TestSiteInfo(all_LMZ[i], "DieColumn"),
                                            TestSiteInfo(all_LMZ[i], 'TestSite'),
                                            Date(all_LMZ[i])))
                        plt.close()

        if self.Rf_Check.isChecked() == True:
            e = []
            for x in checkedItems2:
                for y in checkedItems1_1:
                    for z in checkedItems1_2:
                        e.append([x, y, z])
            for w in e:
                for i in range(0, len(all_LMZ)):
                    if TestSiteInfo(all_LMZ[i], "Wafer") == w[0] and TestSiteInfo(all_LMZ[i], "DieRow") == w[1] and TestSiteInfo(all_LMZ[i], "DieColumn") == w[2]:
                        reference.reference(all_LMZ[i])
                        plt.savefig("./results/png_files/Analysis_{}_({},{})_{}_{}_reference.png"
                                    .format(TestSiteInfo(all_LMZ[i], "Wafer"),
                                            TestSiteInfo(all_LMZ[i], "DieRow"),
                                            TestSiteInfo(all_LMZ[i], "DieColumn"),
                                            TestSiteInfo(all_LMZ[i], 'TestSite'),
                                            Date(all_LMZ[i])))
                        plt.close()