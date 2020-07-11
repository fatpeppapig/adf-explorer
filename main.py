import sys

from PyQt5.QtWidgets import QApplication
from app import App

if __name__ == '__main__':
    qtapp = QApplication(sys.argv)
    app = App()
    code = qtapp.exec_()
    app.cleanUp()
    sys.exit(code)
