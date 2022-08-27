from data.dataCompiler import DadaCompiler
from UI.ui import *


class Compiler(Ui_MainWindow):

    def setupUi(self, mainWindow):
        super().setupUi(mainWindow)
        mainWindow.setObjectName("MainWindow2")
        self.lineEditConversionLeft.editingFinished.connect(self.onChanged)

    def psi_in_Pa(self):
        return str(float(self.lineEditConversionLeft.text()) * DadaCompiler.PSI_IN_PA)

    def onChanged(self):
        self.lineEditConversionRiqht.setText(self.psi_in_Pa())

