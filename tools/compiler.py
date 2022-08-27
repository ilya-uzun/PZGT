from data.dataCompiler import DadaCompiler
from UI.ui import *


def psi_in_Pa(num: str):
    return str(float(num) * DadaCompiler.PSI_IN_PA)


class Compiler(Ui_MainWindow):

    def setupUi(self, mainWindow):
        super().setupUi(mainWindow)
        mainWindow.setObjectName("MainWindow2")
        self.lineEditConversionLeft.textChanged[str].connect(self.onChanged)

    def onChanged(self, text):
        self.lineEditConversionRiqht.setText(psi_in_Pa(text))

