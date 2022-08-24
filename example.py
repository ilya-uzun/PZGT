# Тестовый класс



from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.lbl = QLabel("Ubuntu", self)

        combo = QComboBox(self)
        combo.addItems(["Ubuntu", "Arch"])

        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()

