import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from tools.compiler import Compiler
from UI.ui import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        MainWindow.setObjectName("MainWindow2")

        self.lineEditLeft()
        self.compoler = Compiler()

    def lineEditLeft(self):
        if self.lineEditConversionLeft.text() == None:
            self.lineEditConversionLeft.editingFinished.connect(self.onChanged)


    def onChanged(self):
        self.lineEditConversionRiqht.setText(self.compoler.psi_in_Pa(self.lineEditConversionLeft.text()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
