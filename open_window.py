import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel
from PyQt5.QtCore import QCoreApplication
import get_result as mo
import test

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('xml_analysis')
        self.move(300,300)
        self.resize(400,400)

        btn = QPushButton('Quit',self)
        btn.move(250,300)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        label1 = QLabel('csv', self)
        label1.move(20,20)
        label2 = QLabel('images', self)
        label2.move(20,60)
        label3 = QLabel('csv + images',self)
        label3.move(20,100)

        btn1 = QPushButton('Yes', self)
        btn1.move(120,13)
        btn2 = QPushButton('Yes',self)
        btn2.move(120,53)
        btn3 = QPushButton('Yes',self)
        btn3.move(120,93)
        btn1.clicked.connect(self.dl_csv)
        btn2.clicked.connect(self.dl_images)
        btn3.clicked.connect(self.dl_csv_images)

        self.show()

    def dl_csv(self):

        mo.clear_xlsx()
        mo.make_xlsx()
    def dl_images(self):
        mo.clear_png()
        mo.make_png()
    def dl_csv_images(self):
        mo.clear_xlsx()
        mo.clear_png()
        mo.make_png()
        mo.make_xlsx()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())