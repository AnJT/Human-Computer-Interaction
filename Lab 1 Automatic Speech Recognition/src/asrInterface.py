# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asrInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from ast import Pass
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
 
class Ui_MainWindow(object): 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 482)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(30, 50, 354, 31))
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_1.setTextFormat(QtCore.Qt.AutoText)
        self.label_1.setWordWrap(True)
        self.label_1.setObjectName("label_1")
        self.label_1.setWordWrap(True)
        self.label_1.setAlignment(QtCore.Qt.AlignTop)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 354, 31))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 354, 81))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_3.setWordWrap(True)
        self.label_3.setAlignment(QtCore.Qt.AlignTop)
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 354, 81))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_4.setWordWrap(True)
        self.label_4.setAlignment(QtCore.Qt.AlignTop)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 280, 354, 81))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_4")
        self.label_5.setWordWrap(True)
        self.label_5.setAlignment(QtCore.Qt.AlignTop)

        self.siriFig = QtWidgets.QLabel(self.centralwidget)
        self.siriFig.setGeometry(QtCore.QRect(20, 340, 374, 141))
        self.siriFig.setText("")
        self.siriGif = QMovie("icon/siri.gif")
        self.siriFig.setMovie(self.siriGif)
        self.siriGif.start()
        self.siriFig.setScaledContents(True)
        self.siriFig.setObjectName("siriFig")
        self.siriFig.lower()

        rec_font = QtGui.QFont()
        rec_font.setFamily("Calibri")
        rec_font.setPointSize(14)
        rec_font.setStyleStrategy(QtGui.QFont.PreferAntialias)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 30, 354, 281))
        self.label_6.setFont(rec_font)
        self.label_6.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_4")
        self.label_6.setWordWrap(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.hide()


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Assistant"))
        self.label_1.setText(_translate("MainWindow", "Hi! How can I help?"))
        self.label_2.setText(_translate("MainWindow", "You can:"))
        self.label_3.setText(_translate("MainWindow", "1. Enjoy music by saying \"Play music\""))
        self.label_4.setText(_translate("MainWindow", "2. Take some notes by saying \"Open Notepad\""))
        self.label_5.setText(_translate("MainWindow", "3. Do some calculations by saying \"Open the Calculator\""))

    def showRecUi(self, label_6_text):
        self.label_1.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.show()
        _translate = QtCore.QCoreApplication.translate
        self.label_6.setText(_translate("MainWindow", label_6_text))
    
    def hideRecUi(self):
        self.label_1.show()
        self.label_2.show()
        self.label_3.show()
        self.label_4.show()
        self.label_5.show()
        self.label_6.hide()
        

