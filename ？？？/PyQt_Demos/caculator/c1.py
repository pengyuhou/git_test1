# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(300, 120, 321, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 1, 3, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 3, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 2, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 3, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 0, 3, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 3, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 2, 3, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 3, 3, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(460, 40, 160, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_18 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout.addWidget(self.pushButton_18)
        self.pushButton_17 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout.addWidget(self.pushButton_17)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_17.clicked.connect(MainWindow.close)
        res = []

        a = self.pushButton.text()
        tmp1 = a
        def fun():
            res.append(tmp1)
            show_label.setText(''.join(res))

        self.pushButton.clicked.connect(fun)

        a = self.pushButton_2.text()
        tmp2 = a

        def fun():
            res.append(tmp2)
            show_label.setText(''.join(res))

        self.pushButton_2.clicked.connect(fun)

        a = self.pushButton_3.text()
        tmp3 = a

        def fun():
            res.append(tmp3)
            show_label.setText(''.join(res))

        self.pushButton_3.clicked.connect(fun)

        a = self.pushButton_4.text()
        tmp4 = a

        def fun():
            res.append(tmp4)
            show_label.setText(''.join(res))

        self.pushButton_4.clicked.connect(fun)

        a = self.pushButton_5.text()
        tmp5 =a

        def fun():
            res.append(tmp5)
            show_label.setText(''.join(res))

        self.pushButton_5.clicked.connect(fun)

        a = self.pushButton_6.text()
        tmp6 = a

        def fun():
            res.append(tmp6)
            show_label.setText(''.join(res))

        self.pushButton_6.clicked.connect(fun)

        a = self.pushButton_7.text()
        tmp7 = a

        def fun():
            res.append(tmp7)
            show_label.setText(''.join(res))

        self.pushButton_7.clicked.connect(fun)

        a = self.pushButton_8.text()
        tmp8 = a

        def fun():
            res.append(tmp8)
            show_label.setText(''.join(res))

        self.pushButton_8.clicked.connect(fun)

        a = self.pushButton_9.text()
        tmp9 = a

        def fun():
            res.append(tmp9)
            show_label.setText(''.join(res))

        self.pushButton_9.clicked.connect(fun)

        a = self.pushButton_10.text()
        tmp10 = a

        def fun():
            res.append(tmp10)
            show_label.setText(''.join(res))

        self.pushButton_10.clicked.connect(fun)

        a = self.pushButton_11.text()
        tmp11 = a
        def fun():
            res.append(tmp11)
            show_label.setText(''.join(res))

        self.pushButton_11.clicked.connect(fun)

        a = self.pushButton_12.text()
        tmp12 = a

        def fun():
            res.append(tmp12)
            show_label.setText(''.join(res))

        self.pushButton_12.clicked.connect(fun)

        a = self.pushButton_13.text()
        tmp13=a

        def fun():
            res.append(tmp13)
            show_label.setText(''.join(res))

        self.pushButton_13.clicked.connect(fun)

        a = self.pushButton_14.text()
        tmp14 = a

        def fun():
            res.append(tmp14)
            show_label.setText(''.join(res))

        self.pushButton_14.clicked.connect(fun)

        a = self.pushButton_16.text()
        tmp16 = a

        def fun():
            res.append(tmp16)
            show_label.setText(''.join(res))

        self.pushButton_16.clicked.connect(fun)

        def fun_equal():
            s = eval(''.join(res))
            print(s)
            show_label.setText(str(s))
            res[:] = []

        self.pushButton_15.clicked.connect(fun_equal)

        def fun_clear():
            show_label.setText('0')
            res[:] = []
        self.pushButton_18.clicked.connect(fun_clear)

        show_label = QtWidgets.QLabel(MainWindow)
        show_label.setText('0')
        show_label.move(100, 200)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_5.setText(_translate("MainWindow", "8"))
        self.pushButton_7.setText(_translate("MainWindow", "4"))
        self.pushButton_10.setText(_translate("MainWindow", "-"))
        self.pushButton_14.setText(_translate("MainWindow", "."))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_4.setText(_translate("MainWindow", "7"))
        self.pushButton_6.setText(_translate("MainWindow", "5"))
        self.pushButton_8.setText(_translate("MainWindow", "6"))
        self.pushButton_13.setText(_translate("MainWindow", "0"))
        self.pushButton_11.setText(_translate("MainWindow", "*"))
        self.pushButton_15.setText(_translate("MainWindow", "="))
        self.pushButton_12.setText(_translate("MainWindow", "+"))
        self.pushButton_16.setText(_translate("MainWindow", "/"))
        self.pushButton_18.setText(_translate("MainWindow", "clear"))
        self.pushButton_17.setText(_translate("MainWindow", "关闭"))

