import sys
sys.path.append('./src')
from selection import *

while True:
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = MyApp()
        sys.exit(app.exec_())

# 변경 사항 있습니다.
def example():
    return
