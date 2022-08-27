import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from tools.compiler import Compiler


class MainWindow(QMainWindow, Compiler):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.add_function()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    mw = MainWindow()
    mw.show()

    #mw.lineEditConversionRiqht.setText('ds') # gпример вызова напрямую

    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()

    sys.exit(app.exec_())
