 
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import stackwidget
from PyQt5.QtGui import *

class Ui_MainWindow(object):



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
	MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_in = QtWidgets.QPushButton(self.centralwidget)
        self.bt_in.setGeometry(QtCore.QRect(130, 100, 221, 181))
        self.bt_in.setStyleSheet("font: italic 36pt \"PibotoLt\";\n"
"font: italic 24pt \"PibotoLt\";\n")
        self.bt_in.setObjectName("bt_in")
	self.bt_in.setIcon(QtGui.QIcon("./image/itembox.jpg"))
	self.bt_in.setIconSize(QtCore.QSize(221,181))
        self.bt_card = QtWidgets.QPushButton(self.centralwidget)
        self.bt_card.setGeometry(QtCore.QRect(50, 320, 141, 81))
        self.bt_card.setStyleSheet("font: italic 20pt \"PibotoLt\";")
        self.bt_card.setObjectName("bt_card")
	self.bt_card.setIcon(QtGui.QIcon("./image/cardinsert.jpg"))
	self.bt_card.setIconSize(QtCore.QSize(141,81))
        self.box = QtWidgets.QLabel(self.centralwidget)
        self.box.setGeometry(QtCore.QRect(280, 10, 211, 71))
        self.box.setStyleSheet("font: italic 28pt \"PibotoLt\";")
        self.box.setObjectName("box")
        self.bt_out = QtWidgets.QPushButton(self.centralwidget)
        self.bt_out.setGeometry(QtCore.QRect(440, 100, 221, 181))
        self.bt_out.setStyleSheet("font: italic 36pt \"PibotoLt\";\n""font: italic 24pt \"PibotoLt\";")
        self.bt_out.setObjectName("bt_out")
	self.bt_out.setIcon(QtGui.QIcon("./image/itemfind.jpg"))
	self.bt_out.setIconSize(QtCore.QSize(221,181))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
	self.bt_card.clicked.connect(lambda:self.btClicked(MainWindow))
 	self.bt_in.clicked.connect(lambda:self.boxin(MainWindow))
	self.bt_out.clicked.connect(lambda:self.boxout(MainWindow))
	MainWindow.showFullScreen()		

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
	
    def btClicked(self,MainWindow):
	stackwidget.cardin_div_stack(self)
	MainWindow.hide()
	  
    def boxin(self,MainWindow):
	stackwidget.callin_div_stack(self)
	MainWindow.hide()

    def boxout(self,MainWindow):
	stackwidget.find_div_stack(self)
	MainWindow.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#        self.bt_in.setText(_translate("MainWindow", "물품 보관"))
#        self.bt_card.setText(_translate("MainWindow", "카드 등록"))
      #  self.box.setText(_translate("MainWindow", "물품 보관함"))
 #       self.bt_out.setText(_translate("MainWindow", "물품 찾기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

