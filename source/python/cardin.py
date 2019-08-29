
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cardin.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
#import stackwidget
from threading import Thread
import time 
	

class Ui_Cardin(object):


    def setupUi(self, CardWindow):
        CardWindow.setObjectName("CardWindow")
        CardWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(CardWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(460, 70, 317, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pb_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_1.setMinimumSize(QtCore.QSize(45, 45))
        self.pb_1.setMaximumSize(QtCore.QSize(80, 60))
        self.pb_1.setStyleSheet("font: italic 28pt \"PibotoLt\";")
        self.pb_1.setObjectName("pb_1")
        self.gridLayout.addWidget(self.pb_1, 0, 0, 1, 1)
        self.pb_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_5.setEnabled(True)
        self.pb_5.setMinimumSize(QtCore.QSize(45, 45))
        self.pb_5.setMaximumSize(QtCore.QSize(80, 60))
        self.pb_5.setStyleSheet("font: italic 28pt \"PibotoLt\";")
        self.pb_5.setObjectName("pb_5")
        self.gridLayout.addWidget(self.pb_5, 1, 1, 1, 1)
        self.pb_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_7.setEnabled(True)
        self.pb_7.setMinimumSize(QtCore.QSize(45, 45))
        self.pb_7.setMaximumSize(QtCore.QSize(80, 60))
        self.pb_7.setStyleSheet("font: italic 28pt \"PibotoLt\";")
        self.pb_7.setObjectName("pb_7")
        self.gridLayout.addWidget(self.pb_7, 2, 0, 1, 1)
        self.pb_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_4.setEnabled(True)
        self.pb_4.setMinimumSize(QtCore.QSize(45, 45))
        self.pb_4.setMaximumSize(QtCore.QSize(80, 60))
        self.pb_4.setStyleSheet("font: italic 28pt \"PibotoLt\";")
        self.pb_4.setObjectName("pb_4")
        self.gridLayout.addWidget(self.pb_4, 1, 0, 1, 1)
        self.pb_delete = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_delete.setEnabled(True)
        self.pb_delete.setMinimumSize(QtCore.QSize(45, 45))
        self.pb_delete.setMaximumSize(QtCore.QSize(80, 60))
        self.pb_delete.setStyleSheet("font: italic 14pt \"PibotoLt\";")
        self.pb_delete.setObjectName("pb_delete")
        self.gridLayout.addWidget(self.pb_delete, 3, 0, 1, 1)
        self.pb_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_8.setEnabled(True)
        self.pb_8.setMinimumSize(QtCore.QSize(45, 45))
        self.pb_8.setMaximumSize(QtCore.QSize(80, 60))
        self.pb_8.setStyleSheet("font: italic 28pt \"PibotoLt\";")
        self.pb_8.setObjectName("pb_8")
        self.gridLayout.addWidget(self.pb_8, 2, 1, 1, 1)
        self.pb_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_0.setEnabled(True)
        self.pb_0.setMinimumSize(QtCore.QSize(45, 45))
        self.pb_0.setMaximumSize(QtCore.QSize(80, 60))
        self.pb_0.setStyleSheet("font: italic 28pt \"PibotoLt\";")
        self.pb_0.setObjectName("pb_0")
        self.gridLayout.addWidget(self.pb_0, 3, 1, 1, 1)
        self.pb_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_6.setEnabled(True)
        self.pb_6.setMinimumSize(QtCore.QSize(45, 45))
        self.pb_6.setMaximumSize(QtCore.QSize(80, 60))
        self.pb_6.setStyleSheet("font: italic 28pt \"PibotoLt\";")
        self.pb_6.setObjectName("pb_6")
        self.gridLayout.addWidget(self.pb_6, 1, 2, 1, 1)
        self.pb_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_3.setEnabled(True)
        self.pb_3.setMinimumSize(QtCore.QSize(45, 45))
        self.pb_3.setMaximumSize(QtCore.QSize(80, 60))
        self.pb_3.setStyleSheet("font: italic 28pt \"PibotoLt\";")
        self.pb_3.setObjectName("pb_3")
        self.gridLayout.addWidget(self.pb_3, 0, 2, 1, 1)
        self.pb_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_2.setEnabled(True)
        self.pb_2.setMinimumSize(QtCore.QSize(45, 45))
        self.pb_2.setMaximumSize(QtCore.QSize(80, 60))
        self.pb_2.setStyleSheet("font: italic 28pt \"PibotoLt\";")
        self.pb_2.setObjectName("pb_2")
        self.gridLayout.addWidget(self.pb_2, 0, 1, 1, 1)
        self.pb_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_9.setEnabled(True)
        self.pb_9.setMinimumSize(QtCore.QSize(45, 45))
        self.pb_9.setMaximumSize(QtCore.QSize(80, 60))
        self.pb_9.setStyleSheet("font: italic 28pt \"PibotoLt\";")
        self.pb_9.setObjectName("pb_9")
        self.gridLayout.addWidget(self.pb_9, 2, 2, 1, 1)
        self.pb_check = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_check.setEnabled(True)
        self.pb_check.setMinimumSize(QtCore.QSize(45, 45))
        self.pb_check.setMaximumSize(QtCore.QSize(80, 60))
        self.pb_check.setStyleSheet("font: italic 14pt \"PibotoLt\";")
        self.pb_check.setObjectName("pb_check")
        self.gridLayout.addWidget(self.pb_check, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 471, 51))
        self.label.setStyleSheet("font: italic 22pt \"PibotoLt\";")
        self.label.setObjectName("label")
        self.le_dong = QtWidgets.QLineEdit(self.centralwidget)
        self.le_dong.setGeometry(QtCore.QRect(100, 100, 231, 71))
	self.le_dong.setStyleSheet("font: italic 26pt \"PibotoLt\";")
        self.le_dong.setObjectName("te_dong")
	self.le_dong.setMaxLength(3)
	self.le_dong.setFocus()
	self.le_dong.setAlignment(QtCore.Qt.AlignCenter)
        self.le_ho = QtWidgets.QLineEdit(self.centralwidget)
        self.le_ho.setGeometry(QtCore.QRect(100, 190, 231, 71))
	self.le_ho.setStyleSheet("font: italic 26pt \"PibotoLt\";")
	self.le_ho.setMaxLength(3)    
	self.le_ho.setAlignment(QtCore.Qt.AlignCenter)
        self.le_ho.setObjectName("te_ho")
        self.lb_dong = QtWidgets.QLabel(self.centralwidget)
        self.lb_dong.setGeometry(QtCore.QRect(350, 110, 41, 41))
        self.lb_dong.setStyleSheet("font: italic 28pt \"PibotoLt\";")
        self.lb_dong.setObjectName("lb_dong")
        self.lb_ho = QtWidgets.QLabel(self.centralwidget)
        self.lb_ho.setGeometry(QtCore.QRect(350, 200, 41, 41))
        self.lb_ho.setStyleSheet("font: italic 28pt \"PibotoLt\";")
        self.lb_ho.setObjectName("lb_ho")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 280, 91, 51))
        self.label_4.setStyleSheet("font: italic 28pt \"PibotoLt\";")
        self.label_4.setObjectName("label_4")
        self.lb_cardin = QtWidgets.QLabel(self.centralwidget)
        self.lb_cardin.setGeometry(QtCore.QRect(210, 280, 131, 51))
        self.lb_cardin.setStyleSheet("font: italic 28pt \"PibotoLt\";")
        self.lb_cardin.setObjectName("lb_cardin")
        self.pb_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pb_cancel.setGeometry(QtCore.QRect(100, 340, 101, 71))
        self.pb_cancel.setStyleSheet("font: italic 18pt \"PibotoLt\";")
        self.pb_cancel.setObjectName("pb_cancel")
        CardWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CardWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        CardWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CardWindow)
        self.statusbar.setObjectName("statusbar")
        CardWindow.setStatusBar(self.statusbar)
	
 	self.pb_cancel.clicked.connect(lambda:self.close(CardWindow))
        self.pb_check.clicked.connect(lambda:self.mesagebox(CardWindow))
 	self.pb_delete.clicked.connect(self.dele)
	self.pb_1.clicked.connect(lambda state, button=self.pb_1: self.NumClicked(state, button))
	self.pb_2.clicked.connect(lambda state, button=self.pb_2: self.NumClicked(state, button))
	self.pb_3.clicked.connect(lambda state, button=self.pb_3: self.NumClicked(state, button))
	self.pb_4.clicked.connect(lambda state, button=self.pb_4: self.NumClicked(state, button))
	self.pb_5.clicked.connect(lambda state, button=self.pb_5: self.NumClicked(state, button))
	self.pb_6.clicked.connect(lambda state, button=self.pb_6: self.NumClicked(state, button))
	self.pb_7.clicked.connect(lambda state, button=self.pb_7: self.NumClicked(state, button))
	self.pb_8.clicked.connect(lambda state, button=self.pb_8: self.NumClicked(state, button))
	self.pb_9.clicked.connect(lambda state, button=self.pb_9: self.NumClicked(state, button))
	self.pb_0.clicked.connect(lambda state, button=self.pb_0: self.NumClicked(state, button))
     	CardWindow.showFullScreen()

       # self.threadd()
        self.retranslateUi(CardWindow)
        QtCore.QMetaObject.connectSlotsByName(CardWindow)	
        
#        t1 = Thread(target = my_thread, args = (1,))
#        t1.daemon = False

#        t1.start()

   


 
#    def mesagebox(self,CardWindow):
#	qt = QMessageBox.question(self.gridLayoutWidget,"선택","카드가 등록되었습니다",QMessageBox.Yes)
#	if qt == QMessageBox.Yes:	  
#	    stackwidget.start_stack(self)
#            CardWindow.hide()



    

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    CardWindow = QtWidgets.QMainWindow()  
    ui = Ui_Cardin()
    ui.setupUi(CardWindow)
    CardWindow.show()
    sys.exit(app.exec_())

