# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from  PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.fun)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def fun(self):
        def fun1():
            time = cal.selectedDate()
            label.setText(time.toString('yyyy-MM-dd dddd'))
        dialog = QtWidgets.QDialog()
        label = QtWidgets.QLabel(dialog)
        # button = QtWidgets.QPushButton('确定',dialog)
        # button.clicked.connect(dialog.close)
        # button.move(50,50)
        # dialog.setWindowTitle('对话框')
        # # dialog.setWindowModality(Qt.ApplicationModal)
        # dialog.exec_()
        cal = QtWidgets.QCalendarWidget(dialog)

        # 初始化当前时间
        date = cal.selectedDate()
        label.setText(date.toString('yyyy-MM-dd dddd'))

        cal.clicked.connect(fun1)

        label.move(20,10)
        cal.setWindowTitle('日历')
        dialog.resize(400,500)
        cal.move(50,50)

        dialog.exec_()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

