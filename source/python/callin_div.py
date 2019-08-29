
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cardin_div.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!



import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from callin import Ui_callIn
from PyQt5.QtWidgets import *
import stackwidget
import MySQLdb

global_value = 0	

id = 1

def idval():
    global id
    return id

class EventWindow2(QtWidgets.QMainWindow, Ui_callIn):

    def __init__(self, parent = None):
        super(EventWindow2, self).__init__(parent)
	self.setupUi(self)
	self.le_dong.installEventFilter(self)
	self.le_ho.installEventFilter(self)
	self.le_call.installEventFilter(self)

    def eventFilter(self, source, event):
	global global_value
        if event.type() == QtCore.QEvent.FocusIn and source is self.le_dong :
	    global_value = 1
            
        elif event.type() == QtCore.QEvent.FocusIn and source is self.le_ho :
	    global_value =2	
        elif event.type() == QtCore.QEvent.FocusIn and source is self.le_call :
	    global_value =3
	return super(EventWindow2, self). eventFilter(source,event)
 	

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
	elif  global_value  == 3:
	    exist_line_text = self.le_call.text()
	    now_num_text = button.text()

	    self.le_call.setText(exist_line_text + now_num_text)
	   
    def dele(self):
	global global_value

	if global_value  == 1 :
	    de = self.le_dong.text()
	    self.le_dong.setText(de[0:-1])	    
	elif  global_value  == 2:
	    de = self.le_ho.text()
	    self.le_ho.setText(de[0:-1])	
	elif  global_value  == 3:
	    de = self.le_call.text()
	    self.le_call.setText(de[0:-1])	
	

    def close(self,CallWindow):	
	stackwidget.start_stack(self)	
	CallWindow.hide()

    def check(self,CallWindow):
	global id
        dong_text = self.le_dong.text() 
        ho_text = self.le_ho.text()
	call_text = self.le_call.text()
        if len(dong_text) != 0 and len(ho_text) != 0 and len(call_text) != 0 :
            db = MySQLdb.connect("localhost","admin","1234","lee")
            cur = db.cursor()
            sql = "insert into box(dong,ho,callnum,locker1,locker2) values(%s,%s,%s,1,1)"
            cur.execute(sql,(dong_text,ho_text,call_text))
            db.commit()  
            sql = "select user_id from box where dong = %s and ho = %s and callnum = %s"
            cur.execute(sql,(dong_text,ho_text,call_text))    
            sur = cur.fetchone()
	    id = sur[0]
	    cur.close()
            db.commit()
            db.close()
            stackwidget.password_stack(self)
	    CallWindow.hide()
        else :
            QMessageBox.information(self.gridLayoutWidget,"경고","빈칸을 넣어주세요")


          
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = EventWindow2()
    w.show()
    sys.exit(app.exec_())


