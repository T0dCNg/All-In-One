# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ogban\Desktop\The-All-In-One-Project\The-All-In-One-Project\AIO Gui\Caculations.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(491, 530)
        Dialog.setMinimumSize(QtCore.QSize(491, 530))
        Dialog.setMaximumSize(QtCore.QSize(491, 530))
        Dialog.setStyleSheet("background-color: rgb(40, 41, 35);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 451, 71))
        font = QtGui.QFont()
        font.setPointSize(46)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(230, 200, 85);")
        self.label.setObjectName("label")
        self.Close = QtWidgets.QPushButton(Dialog)
        self.Close.setGeometry(QtCore.QRect(0, 480, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Close.setFont(font)
        self.Close.setStyleSheet("background-color: rgb(213, 0, 0);")
        self.Close.setAutoDefault(False)
        self.Close.setDefault(False)
        self.Close.setObjectName("Close")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 510, 471, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(230, 200, 85);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.Personal = QtWidgets.QPushButton(Dialog)
        self.Personal.setGeometry(QtCore.QRect(130, 120, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Personal.setFont(font)
        self.Personal.setStyleSheet("color: rgb(230, 200, 85);\n"
"background-color: rgb(42, 74, 89);")
        self.Personal.setObjectName("Personal")
        self.Personal_2 = QtWidgets.QPushButton(Dialog)
        self.Personal_2.setGeometry(QtCore.QRect(130, 220, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Personal_2.setFont(font)
        self.Personal_2.setStyleSheet("color: rgb(230, 200, 85);\n"
"background-color: rgb(42, 74, 89);")
        self.Personal_2.setObjectName("Personal_2")
        self.Personal_3 = QtWidgets.QPushButton(Dialog)
        self.Personal_3.setGeometry(QtCore.QRect(130, 320, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Personal_3.setFont(font)
        self.Personal_3.setStyleSheet("color: rgb(230, 200, 85);\n"
"background-color: rgb(42, 74, 89);")
        self.Personal_3.setObjectName("Personal_3")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 90, 491, 20))
        self.line.setMaximumSize(QtCore.QSize(491, 150))
        self.line.setStyleSheet("background-color: rgb(40, 41, 35);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AIO | Caculations"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Caculations</p></body></html>"))
        self.Close.setText(_translate("Dialog", "Close"))
        self.label_3.setText(_translate("Dialog", "AIO \"GUI Edittion\" | Version: v-2.1.0 REV-2 | GUI Version:Alpha 0.0.1 | Copyright AIO 2022"))
        self.Personal.setText(_translate("Dialog", "Basic Caculator"))
        self.Personal_2.setText(_translate("Dialog", "Conversions"))
        self.Personal_3.setText(_translate("Dialog", "text"))
