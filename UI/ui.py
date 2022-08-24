# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 591, 401))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.scheme = QtWidgets.QWidget()
        self.scheme.setObjectName("scheme")

        self.label_2 = QtWidgets.QLabel(self.scheme)
        self.label_2.setGeometry(QtCore.QRect(350, 190, 91, 91))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        #
        self.movie = QMovie("img/gif/alarm_exclamation_red_reversing.gif")
        self.label_2.setMovie(self.movie)
        self.startAnimation()

        self.pushButton = QtWidgets.QPushButton(self.scheme)
        self.pushButton.setGeometry(QtCore.QRect(130, 240, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.scheme, "")
        self.unit_converter = QtWidgets.QWidget()
        self.unit_converter.setObjectName("unit_converter")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.unit_converter)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 20, 361, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.unit_converter)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(110, 120, 361, 73))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_2.addWidget(self.textEdit_2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/equals.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.tabWidget.addTab(self.unit_converter, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scheme), _translate("MainWindow", "Схема"))
        self.comboBox.setItemText(0, _translate("MainWindow", "psi"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Паскаль"))
        self.comboBox.setItemText(2, _translate("MainWindow", "bar"))
        self.comboBox.setItemText(3, _translate("MainWindow", "атм"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "psi"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Паскаль"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "bar"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "атм"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.unit_converter), _translate("MainWindow", "Конвертер единиц"))

    # Start Animation
    def startAnimation(self):
        self.movie.start()

    # Stop Animation(According to need)
    def stopAnimation(self):
        self.movie.stop()