# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ogban\Desktop\The-All-In-One-Project\The-All-In-One-Project\AIO Gui\IUOP.ui'
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
        self.label.setGeometry(QtCore.QRect(10, 20, 471, 141))
        self.label.setMaximumSize(QtCore.QSize(491, 530))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(230, 200, 85);")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.Ok = QtWidgets.QPushButton(Dialog)
        self.Ok.setGeometry(QtCore.QRect(10, 470, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.Ok.setFont(font)
        self.Ok.setStyleSheet("background-color: rgb(213, 0, 0);")
        self.Ok.setObjectName("Ok")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 310, 471, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(230, 200, 85);")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AIO | IUOP"))
        self.label.setText(_translate("Dialog", "Icorrect:                            Username Or Password                         AIO Error: Error 2"))
        self.Ok.setText(_translate("Dialog", "OK"))
        self.label_2.setText(_translate("Dialog", "You have enter a incorect username or password please click ok and try again"))
        self.label_3.setText(_translate("Dialog", "AIO \"GUI Edittion\" | Version: v-2.1.0 REV-2 | GUI Version:Alpha 0.0.1 | Copyright AIO 2022"))
import logo_rc
