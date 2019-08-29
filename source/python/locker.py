# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'locker.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import stackwidget
import MySQLdb
import idvalue 
import serial

Y = 0
def num():
    global Y
    return Y
lock = 0
lock2 = 0

class Ui_Locker(object):
    def sel(self):
	global lock
        global lock2
	db = MySQLdb.connect("localhost","admin","1234","lee")
        cur = db.cursor()
        cur2 = db.cursor()
	sql = "select locker1 from box where locker1 = 2" 
        sql2 = "select locker2 from box where locker2 = 2" 
        cur.execute(sql)
	cur2.execute(sql2)	      
	sur = cur.fetchone()
	sur2 = cur2.fetchone()
	if sur == None:
	    lock = 1
	elif sur[0] == 2:
	    lock = 2
	if sur2 == None:
	    lock2 = 1
	elif sur2[0] == 2 :
	    lock2 = 2
	cur.close()
	cur2.close()
        db.commit()
        db.close()  

    def setupUi(self, LockerWindow):
	global lock
	self.sel()
        LockerWindow.setObjectName("LockerWindow")
        LockerWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(LockerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 301, 81))
        self.label.setStyleSheet("font: italic 24pt \"PibotoLt\";")
        self.label.setObjectName("label")
        self.pb_lok_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_lok_1.setGeometry(QtCore.QRect(170, 140, 201, 151))
        #self.pb_lok_1.setStyleSheet("\n""font: 75 20pt \"PibotoLt\";\n""background-color: rgb(0, 255, 0);\n""color: rgb(0, 0, 0);")
        self.pb_lok_1.setObjectName("pb_lok_1")
        self.pb_lok_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_lok_2.setGeometry(QtCore.QRect(430, 140, 201, 151))
        #self.pb_lok_2.setStyleSheet("font: 75 20pt \"PibotoLt\";\n""color: rgb(0, 0, 0);\n""background-color: rgb(0, 255, 0);")
        self.pb_lok_2.setObjectName("pb_lok_2")
	if lock == 1:
            self.pb_lok_1.setStyleSheet("\n""font: 75 20pt \"PibotoLt\";\n""background-color: rgb(0, 255, 0);\n""color: rgb(0, 0, 0);")
	    self.pb_lok_1.setEnabled(True)
	elif lock ==2:
	    self.pb_lok_1.setStyleSheet("\n""font: 75 20pt \"PibotoLt\";\n""background-color: rgb(255, 0, 0);\n""color: rgb(0, 0, 0);")
            self.pb_lok_1.setEnabled(False)
	if lock2 == 1:
            self.pb_lok_2.setStyleSheet("font: 75 20pt \"PibotoLt\";\n""color: rgb(0, 0, 0);\n""background-color: rgb(0, 255, 0);") 
            self.pb_lok_2.setEnabled(True)
	elif lock2 == 2:
            self.pb_lok_2.setStyleSheet("\n""font: 75 20pt \"PibotoLt\";\n""background-color: rgb(255, 0, 0);\n""color: rgb(0, 0, 0);")
            self.pb_lok_2.setEnabled(False)
        self.pb_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pb_cancel.setGeometry(QtCore.QRect(50, 330, 101, 71))
        self.pb_cancel.setStyleSheet("font: italic 18pt \"PibotoLt\";\n"
"")
        self.pb_cancel.setObjectName("pb_cancel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(700, 20, 67, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(700, 60, 67, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(650, 20, 41, 21))
        self.label_4.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(650, 60, 41, 21))
        self.label_5.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        LockerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LockerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        LockerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LockerWindow)
        self.statusbar.setObjectName("statusbar")
        LockerWindow.setStatusBar(self.statusbar)
	self.pb_lok_1.clicked.connect(lambda:self.p1lock(LockerWindow))
	self.pb_lok_2.clicked.connect(lambda:self.p2lock(LockerWindow))
	self.pb_cancel.clicked.connect(lambda:self.close(LockerWindow))
	LockerWindow.showFullScreen()
	
        self.retranslateUi(LockerWindow)
        QtCore.QMetaObject.connectSlotsByName(LockerWindow)

    def close(self,LockerWindow):	
	db = MySQLdb.connect("localhost","admin","1234","lee")
        cur = db.cursor()
        sql = "update box set password = null where user_id = %s" % idvalue.idnum()
        cur.execute(sql)
        cur.close()
        db.commit()
        db.close()    	
	stackwidget.password_stack(self)	
	LockerWindow.hide()




    def p1lock(self,LockerWindow):
	global Y
	Y = 1
	msgbox = QMessageBox.question(self.centralwidget,'Message',"1 보관함에 보관하시겠습니까?",QMessageBox.Yes | QMessageBox.No)
	if msgbox == QMessageBox.Yes:
            db = MySQLdb.connect("localhost","admin","1234","lee")
            cur = db.cursor()
            sql = "update  box set locker1 = 2 where user_id = %s" % idvalue.idnum()
            cur.execute(sql)
	    cur.close()
            db.commit()
            db.close()    
	    con = serial.Serial('/dev/ttyUSB0',9600)
            con.write('5')
	    stackwidget.door_stack(self)
	    LockerWindow.hide()
	    
	
    def p2lock(self,LockerWindow):
	global Y
        Y = 2
	msgbox = QMessageBox.question(self.centralwidget,'Message',"2 보관함에 보관하시겠습니까?",QMessageBox.Yes | QMessageBox.No)
	if msgbox == QMessageBox.Yes:
            db = MySQLdb.connect("localhost","admin","1234","lee")
            cur = db.cursor()
            sql = "update  box set locker2 = 2 where user_id = %s" % idvalue.idnum()
            cur.execute(sql)  
	    cur.close()
            db.commit()
            db.close()      
	    con = serial.Serial('/dev/ttyUSB0',9600)
            con.write('6')
	    stackwidget.door_stack(self)
	    LockerWindow.hide()

     
    def retranslateUi(self, LockerWindow):
        _translate = QtCore.QCoreApplication.translate
        LockerWindow.setWindowTitle(_translate("LockerWindow", "LockerWindow"))
        self.label.setText(_translate("LockerWindow", "보관함을 선택하세요"))
        self.pb_lok_1.setText(_translate("LockerWindow", "1 보관함"))
        self.pb_lok_2.setText(_translate("LockerWindow", "2 보관함"))
        self.pb_cancel.setText(_translate("LockerWindow", "취소"))
        self.label_2.setText(_translate("LockerWindow", "이용 가능"))
        self.label_3.setText(_translate("LockerWindow", "이용 중"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LockerWindow = QtWidgets.QMainWindow()
    ui = Ui_Locker()
    ui.setupUi(LockerWindow)
    LockerWindow.show()
    sys.exit(app.exec_())

