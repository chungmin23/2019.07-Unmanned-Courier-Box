# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'door.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
import locker
from PyQt5.QtWidgets import *
import MySQLdb
import idvalue 
import stackwidget
import serial
import time 
from threading import Thread
import sys
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException


#stop_threads = False
num =1
num2 = 1
flag = 0
datavalue = 0

class Ui_Door(object):
    def setupUi(self, DoorWindow):
        DoorWindow.setObjectName("DoorWindow")
        DoorWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(DoorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_text = QtWidgets.QLabel(self.centralwidget)
        self.lb_text.setGeometry(QtCore.QRect(160, 60, 551, 111))
        self.lb_text.setStyleSheet("font: italic 36pt \"PibotoLt\";")
        self.lb_text.setObjectName("lb_text")
        self.lb_text2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_text2.setGeometry(QtCore.QRect(350, 190, 191, 111))
        self.lb_text2.setStyleSheet("font: italic 36pt \"PibotoLt\";")
        self.lb_text2.setObjectName("lb_text2")
        self.lb_number = QtWidgets.QLabel(self.centralwidget)
        self.lb_number.setGeometry(QtCore.QRect(300, 190, 41, 111))
        self.lb_number.setStyleSheet("font: italic 36pt \"PibotoLt\";")
        self.lb_number.setObjectName("lb_number")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 320, 231, 61))
        self.pushButton.setStyleSheet("font: italic 24pt \"PibotoLt\";")
        self.pushButton.setObjectName("pushButton")
        DoorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DoorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        DoorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DoorWindow)
        self.statusbar.setObjectName("statusbar")
        DoorWindow.setStatusBar(self.statusbar)
	self.selct1()
	self.selct2()
        self.DoorWindow = DoorWindow	
        t1 = Thread(target = self.my_thread, args=())
        t1.daemon = False
        t1.start()
	self.pushButton.clicked.connect(lambda:self.doorend(DoorWindow))
	DoorWindow.showFullScreen()

        self.retranslateUi(DoorWindow)
        QtCore.QMetaObject.connectSlotsByName(DoorWindow)
   
    def my_thread(self):
	global datavalue	
	con = serial.Serial('/dev/ttyUSB0',9600,timeout=100)
        while True:
            data2 = con.readline() 
            datavalue = data2.strip()	
            con.close()
	    time.sleep(2)
	    break


    
	
    def doorend(self,DoorWindow):
	su = stackwidget.num()     
        global datavalue
        data = datavalue		   	
        if data == "10" or data == "11": 
            if su == 2 :
                if idvalue.divnum() == 1:
	            db = MySQLdb.connect("localhost","admin","1234","lee")
                    cur = db.cursor()
                    sql = "delete from box where user_id = %s" % idvalue.id2num()
		    print sql
                    cur.execute(sql)
                    cur.close()
                    db.commit()
                    db.close()
	        elif idvalue.divnum() == 2 :
		    db = MySQLdb.connect("localhost","admin","1234","lee")
                    cur = db.cursor()
                    sql = "delete from box where user_id = %s" % idvalue.snnum()
		    print sql
                    cur.execute(sql)
                    cur.close()
                    db.commit()
                    db.close()
	#    else:
	 #       self.message()
	    stackwidget.start_stack(self)
	    DoorWindow.hide()	           
	else:
             QMessageBox.information(self.centralwidget,"경고","문을 닫아주세요")
            
   
	    
    # 물품 찾기 이름 보관함 이름 변경을 위한 함수 
    def selct1(self):
	 global num
         db = MySQLdb.connect("localhost","admin","1234","lee")
         cur = db.cursor()
	 cur2 = db.cursor()
         sql = "select locker1  from box where user_id = %s" % idvalue.id2num() 
         sql2 ="select locker2 from box where user_id = %s" % idvalue.id2num()  
	 cur.execute(sql)
	 cur2.execute(sql2)
	 sur= cur.fetchone()
	 sur2 = cur2.fetchone()
	 if sur == None or sur2 == None: 
	     pass
	 elif sur[0] == 2:
	     num = 1
         elif sur2[0] == 2:
             num = 2 
         cur.close()
         db.commit()
         db.close() 

    # 카드 등록후 이름 변경을 위한 함수  
    def selct2 (self):
	global num2
        db = MySQLdb.connect("localhost","admin","1234","lee")
        cur = db.cursor()
	cur2 = db.cursor()
        sql = "select locker1  from box where user_id = %s" % idvalue.snnum() 
        sql2 ="select locker2 from box where user_id = %s" % idvalue.snnum()  
	cur.execute(sql)
        cur2.execute(sql2)
	sur= cur.fetchone()
	sur2 = cur2.fetchone()
	if sur == None or sur2 == None: 
	    pass
	elif sur[0] == 2:
	    num2 = 1
        elif sur2[0] == 2:
            num2 = 2 
        cur.close()
        db.commit()
        db.close()
	 	
    def message(self):
#	'''
	number = 0
	db = MySQLdb.connect("localhost","admin","1234","lee")
        cur = db.cursor()
        sql = "select LPAD(callnum,11,'0'),locker1,locker2,password  from box where user_id = %s" % idvalue.idnum() 
	cur.execute(sql)
	row = cur.fetchone()
	phone = row[0]
	if row[1] == 2:
	     number = 1
        elif row[2] == 2:
             number = 2
	password = row[3]   
	print phone          
        cur.close()
        db.commit()
        db.close()
	print row[0]

	
	 # set api key, api secret
        api_key = "#"
        api_secret = "#"

        ## 4 params(to, from, type, text) are mandatory. must be filled
        params = dict()
        params['type'] = 'sms' # Message type ( sms, lms, mms, ata )
        params['to'] = phone #'01099504047 Recipients Number '01000000000,01000000001'
        params['from'] = '#' # Sender number
        params['text'] = (' %s 보관함에 보관되었습니다'+'\n'+'패스워드는 %s 입니다'+'\n'+'찾아가시길 바랍니다 ') % (number,password) # Message

        cool = Message(api_key, api_secret)
        try:
            response = cool.send(params)
            print("Success Count : %s" % response['success_count'])
            print("Error Count : %s" % response['error_count'])
            print("Group ID : %s" % response['group_id'])

            if "error_list" in response:
                print("Error List : %s" % response['error_list'])

        except CoolsmsException as e:
            print("Error Code : %s" % e.code)
            print("Error Message : %s" % e.msg)

#        sys.exit()
 #       '''
    def retranslateUi(self, DoorWindow):
	su = stackwidget.num()
	global num
        global num2
        _translate = QtCore.QCoreApplication.translate
	lbnum= locker.num() # 보관함 번호 
        DoorWindow.setWindowTitle(_translate("DoorWindow", "DoorWindow"))
        self.lb_text.setText(_translate("DoorWindow", "사용 후 문을 닫아주세요"))
        self.lb_text2.setText(_translate("DoorWindow", "보관함"))
	if su == 1:
            self.lb_number.setText(_translate("DoorWindow", str(lbnum)))
        elif su == 2:
	    if idvalue.divnum() == 1:
                self.lb_number.setText(_translate("DoorWindow", str(num)))
	    elif idvalue.divnum() == 2:
		self.lb_number.setText(_translate("DoorWindow", str(num2)))
        self.pushButton.setText(_translate("MainWindow", "확인"))
 

if __name__ == "__main__":
  #  import sys
    app = QtWidgets.QApplication(sys.argv)
    DoorWindow = QtWidgets.QMainWindow()
    ui = Ui_Door()
    ui.setupUi(DoorWindow)
    DoorWindow.show()
    sys.exit(app.exec_())

