import sys
sys.path.append('./src')
from selection import *

while True:
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = MyApp()
        sys.exit(app.exec_())
