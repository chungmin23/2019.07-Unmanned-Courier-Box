
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cardin_div.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!



import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from find import Ui_Find
from PyQt5.QtWidgets import *
import stackwidget
import MySQLdb
import time 
import serial
from threading import Thread
from PyQt5 import QtTest


global_value = 0	
id2 = 1
threa = 0
survalue = 0
snd = 1

def idval2():
    global id2
    return id2

# 카드 입력시 사용자 id
def serctnum():
    global snd
    return snd

#카드와 비밀번호 구분하기 위해 
def divcard():
    global dicard
    return dicard


class EventWindow3(QtWidgets.QMainWindow, Ui_Find):

    def __init__(self, parent = None):
        super(EventWindow3, self).__init__(parent)
	self.setupUi(self)
	self.le_dong.installEventFilter(self)
	self.le_ho.installEventFilter(self)
        t1 = Thread(target = self.my_thread, args=())
        t1.daemon = False
        t1.start()
	

    def my_thread(self):
	global stop_threads
	global threa
	global survalue
	global snd
	con = serial.Serial('/dev/ttyUSB0',9600,timeout = 10)
        while True:    
            data = con.readline()
            data2 =  data.split(',')
	    data3 =  data2[0].strip()
	    con.close()
	    if not data3:
	        pass
	    else:
                db = MySQLdb.connect("localhost","admin","1234","lee")
                cur = db.cursor()
		cur2 = db.cursor()
                sql = "select dong,ho from card where rfid ='%s' " % data3 
                cur.execute(sql)
	        sur = cur.fetchone()
		ex1 = sur[0]
		ex2 = sur[1]
		sql2 = "select user_id from box where dong = %s and ho = %s" % (ex1,ex2)
		cur2.execute(sql2)
		sur2 = cur2.fetchone()
		print sur2
		cur2.close()
	        cur.close()
                db.commit()
                db.close()	
    
		snd = sur2[0]
	        survalue = sur
	        time.sleep(2) 
	        threa = 1
	        self.lb_card.setStyleSheet("font: italic 26pt \"PibotoLt\";\n""color: rgb(0, 255, 0);")
	    break		    
            

    def eventFilter(self, source, event):
	global global_value
        if event.type() == QtCore.QEvent.FocusIn and source is self.le_dong :
	    global_value = 1
            
        elif event.type() == QtCore.QEvent.FocusIn and source is self.le_ho :
	    global_value =2	
        
	return super(EventWindow3, self). eventFilter(source,event)
 	

    def NumClicked(self,state,button):
	global global_value

	if global_value  == 1 :
	    exist_line_text = self.le_dong.text()
	    now_num_text = button.text()

	    self.le_dong.setText(exist_line_text + now_num_text)
	elif  global_value  == 2:
	    exist_line_text = self.le_ho.text()
	    now_num_text = button.text()

	    self.le_ho.setText(exist_line_text + now_num_text)

    def dele(self):
	global global_value

	if global_value  == 1 :
	    de = self.le_dong.text()
	    self.le_dong.setText(de[0:-1])	    
	elif  global_value  == 2:
	    de = self.le_ho.text()
	    self.le_ho.setText(de[0:-1])	
		

    def close(self,FindWindow):
	stackwidget.start_stack(self)	
	FindWindow.hide()

    def check(self,FindWindow):
	global id2
	global threa
	global survalue 
	global dicard

        dong_text = self.le_dong.text() 
	ho_text = self.le_ho.text()
        if len(dong_text) != 0 and len(ho_text) != 0  :
	    db = MySQLdb.connect("localhost","admin","1234","lee")
            cur = db.cursor()
            sql = "select user_id from box where dong = %s and ho = %s"
            cur.execute(sql,(dong_text,ho_text))
	    row = cur.fetchone()
            if row == None:
	        QMessageBox.information(self.gridLayoutWidget,"경고","맡기신 물건이 없습니다")	        
	    else :
	        id2 = row[0]
		stackwidget.password_stack(self)
	        FindWindow.hide()
		dicard = 1
            cur.close()
            db.commit()
            db.close()
	    
	elif threa == 1:
	    sur = survalue
	    if sur !=  None:
	        dong = sur[0]
                ho = sur[1]
		db = MySQLdb.connect("localhost","admin","1234","lee")
	        cur2 = db.cursor()           
	        sql2 = "select locker1,locker2 from box where  dong = %s and ho = %s " 
	        cur2.execute(sql2,(dong,ho))
	        sur2 = cur2.fetchone()
	        con = serial.Serial('/dev/ttyUSB0',9600)
                if sur2[0] == 2:
                    con.write('5')
	        elif sur2[1] == 2:
                    con.write('6')
         	stop_threads = True
	        cur2.close()
                db.commit()
                db.close()
		dicard = 2	 
	    else:
	        QMessageBox.information(self.gridLayoutWidget,"경고","등록된 카드가 아닙니다")
                stop_threads = True
	    stackwidget.door_stack(self)
            FindWindow.hide()
	    threa = 2   
	    
        else :
            QMessageBox.information(self.gridLayoutWidget,"경고","빈칸을 넣어주세요")

          
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = EventWindow3()
    w.show()
    sys.exit(app.exec_())



