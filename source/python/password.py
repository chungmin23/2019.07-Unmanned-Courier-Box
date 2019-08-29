# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from door import Ui_Door
from PyQt5.QtWidgets import *
import stackwidget
import idvalue 
import MySQLdb
import serial

class Ui_Password(object):
    def setupUi(self, PasswordWindow):
        PasswordWindow.setObjectName("PasswordWindow")
        PasswordWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(PasswordWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(450, 40, 317, 341))
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
        self.lb_pw = QtWidgets.QLabel(self.centralwidget)
        self.lb_pw.setGeometry(QtCore.QRect(30, 160, 161, 41))
        self.lb_pw.setStyleSheet("\n"
"font: italic 26pt \"PibotoLt\";")
        self.lb_pw.setObjectName("lb_pw")
        self.lb_text = QtWidgets.QLabel(self.centralwidget)
        self.lb_text.setGeometry(QtCore.QRect(30, 60, 401, 51))
        self.lb_text.setStyleSheet("\n"
"font: italic 14pt \"PibotoLt\";\n"
"")
        self.lb_text.setObjectName("lb_text")
        self.pb_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pb_cancel.setGeometry(QtCore.QRect(30, 340, 101, 71))
        self.pb_cancel.setStyleSheet("font: italic 18pt \"PibotoLt\";\n"
"")
        self.pb_cancel.setObjectName("pb_cancel")
        self.le_pw = QtWidgets.QLineEdit(self.centralwidget)
        self.le_pw.setGeometry(QtCore.QRect(30, 220, 331, 51))
        self.le_pw.setStyleSheet("font: italic 24pt \"PibotoLt\";")
        self.le_pw.setText("")
	self.le_pw.setEchoMode(QtWidgets.QLineEdit.Password)
	self.le_pw.setMaxLength(4)
        self.le_pw.setObjectName("le_pw")
        PasswordWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PasswordWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        PasswordWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PasswordWindow)
        self.statusbar.setObjectName("statusbar")
        PasswordWindow.setStatusBar(self.statusbar)
	self.pb_check.clicked.connect(lambda:self.btPwClicked(PasswordWindow))
	self.pb_cancel.clicked.connect(lambda:self.close(PasswordWindow))
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
     	PasswordWindow.showFullScreen()

        self.retranslateUi(PasswordWindow)
        QtCore.QMetaObject.connectSlotsByName(PasswordWindow)
   
    def NumClicked(self,state,button):
	exist_line_text = self.le_pw.text()
	now_num_text = button.text()

	self.le_pw.setText(exist_line_text + now_num_text)
   
    def dele(self):
	de = self.le_pw.text()
	self.le_pw.setText(de[0:-1])


    def close(self,PasswordWindow):
	su = stackwidget.num()
	if su == 1:	
	    stackwidget.callin_div_stack(self)
            db = MySQLdb.connect("localhost","admin","1234","lee")
            cur = db.cursor()
            sql = "delete from box where user_id = %s" % idvalue.idnum()
            cur.execute(sql)
            cur.close()
            db.commit()
            db.close()	        	
	else:
	    stackwidget.find_div_stack(self)	
	PasswordWindow.hide()
	
    def btPwClicked(self,PasswordWindow):
	su = stackwidget.num()
	password_text = self.le_pw.text()
	if len(password_text) != 0:
	    if su == 1:
	        stackwidget.locker_stack(self)
                db = MySQLdb.connect("localhost","admin","1234","lee")
                cur = db.cursor()
                sql = "update  box set password = %s where user_id = %s"
                cur.execute(sql,(password_text,idvalue.idnum()))
                cur.close()
                db.commit()
                db.close()	  
            else:
                stackwidget.door_stack(self)
                db = MySQLdb.connect("localhost","admin","1234","lee")
                cur = db.cursor()
                cur2 = db.cursor()
		sql = "select password from box where user_id = %s" % idvalue.id2num() 
                sql2 = "select locker1,locker2 from box where user_id = %s" % idvalue.id2num()
		cur.execute(sql)
		cur2.execute(sql2)
		sur = cur2.fetchone()
		con = serial.Serial('/dev/ttyUSB0',9600)
		if sur[0] == 2:
		    con.write('5')
		elif sur[1] == 2:
		    con.write('6')
		cur.close()
		cur2.close()
                cur.close()
                db.commit()
                db.close()
	    PasswordWindow.hide()
        else :
            QMessageBox.information(self.gridLayoutWidget,"경고","빈칸을 넣어주세요")	        
	

    def retranslateUi(self, PasswordWindow):
        _translate = QtCore.QCoreApplication.translate
        PasswordWindow.setWindowTitle(_translate("PasswordWindow", "PasswordWindow"))
        self.pb_1.setText(_translate("PasswordWindow", "1"))
        self.pb_5.setText(_translate("PasswordWindow", "5"))
        self.pb_7.setText(_translate("PasswordWindow", "7"))
        self.pb_4.setText(_translate("PasswordWindow", "4"))
        self.pb_delete.setText(_translate("PasswordWindow", "지우기"))
        self.pb_8.setText(_translate("PasswordWindow", "8"))
        self.pb_0.setText(_translate("PasswordWindow", "0"))
        self.pb_6.setText(_translate("PasswordWindow", "6"))
        self.pb_3.setText(_translate("PasswordWindow", "3"))
        self.pb_2.setText(_translate("PasswordWindow", "2"))
        self.pb_9.setText(_translate("PasswordWindow", "9"))
        self.pb_check.setText(_translate("PasswordWindow", "확인"))
        self.lb_pw.setText(_translate("PasswordWindow", "비밀번호"))
        self.lb_text.setText(_translate("PasswordWindow", "비밀번호를 입력하시고 확인버튼을 눌러주세요"))
        self.pb_cancel.setText(_translate("PasswordWindow", "취소"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PasswordWindow = QtWidgets.QMainWindow()
    ui = Ui_Password()
    ui.setupUi(PasswordWindow)
    PasswordWindow.show()
    sys.exit(app.exec_())

