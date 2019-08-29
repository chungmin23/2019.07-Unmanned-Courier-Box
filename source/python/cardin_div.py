
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cardin_div.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!



import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from cardin import Ui_Cardin
from PyQt5.QtWidgets import *
import stackwidget
import MySQLdb
import serial
import time 
from threading import Thread

global_value = 0	
rfidvalue  = ""


class EventWindow(QtWidgets.QMainWindow, Ui_Cardin):

    def __init__(self, parent = None):
        super(EventWindow, self).__init__(parent)
	self.setupUi(self)
	self.le_dong.installEventFilter(self)
	self.le_ho.installEventFilter(self)
	stop_threads = False
        t1 = Thread(target = self.my_thread, args=())
        t1.daemon = False
        t1.start()


    def eventFilter(self, source, event):
	global global_value
        if event.type() == QtCore.QEvent.FocusIn and source is self.le_dong :
	    global_value = 1
            
        elif event.type() == QtCore.QEvent.FocusIn and source is self.le_ho :
	    global_value =2
	    
	return super(EventWindow, self). eventFilter(source,event)
 	
    	 

    def my_thread(self):
	global rfidvalue
	con = serial.Serial('/dev/ttyUSB0',9600,timeout=10)
        while True:
            data = con.readline()
            data2 =  data.split(',')
            rfidvalue = data2[0].strip()
            con.close()
	    if not rfidvalue:
	        pass
            else:
	        _translate = QtCore.QCoreApplication.translate
                self.lb_cardin.setText(_translate("CardWindow", "등록"))
                time.sleep(2)
	    break
           
    def close(self,CardWindow):	
	stackwidget.start_stack(self)	
	CardWindow.hide()	 
   
 
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

 	



    
    
    
    def mesagebox(self,CardWindow):
	global rfidvalue
	dong_text = self.le_dong.text() 
	ho_text = self.le_ho.text()
	if len(dong_text) != 0 and len(ho_text) != 0 :
            db = MySQLdb.connect("localhost","admin","1234","lee")
            cur = db.cursor()
            sql = "insert into card(dong,ho,rfid) values(%s,%s,%s)"
            cur.execute(sql,(dong_text,ho_text,rfidvalue))
            cur.close()
            db.commit()
            db.close()
            qt = QMessageBox.question(self.gridLayoutWidget,"선택","카드가 등록되었습니다",QMessageBox.Yes)  
            if qt == QMessageBox.Yes:	  
	        stackwidget.start_stack(self)
                CardWindow.hide()
	else :
	    QMessageBox.information(self.gridLayoutWidget,"경고","빈칸을 넣어주세요")

    def retranslateUi(self, CardWindow):
        _translate = QtCore.QCoreApplication.translate
        CardWindow.setWindowTitle(_translate("CardWindow", "CardWindow"))
        self.pb_1.setText(_translate("CardWindow", "1"))
        self.pb_5.setText(_translate("CardWindow", "5"))
        self.pb_7.setText(_translate("CardWindow", "7"))
        self.pb_4.setText(_translate("CardWindow", "4"))
        self.pb_delete.setText(_translate("CardWindow", "지우기"))
        self.pb_8.setText(_translate("CardWindow", "8"))
        self.pb_0.setText(_translate("CardWindow", "0"))
        self.pb_6.setText(_translate("CardWindow", "6"))
        self.pb_3.setText(_translate("CardWindow", "3"))
        self.pb_2.setText(_translate("CardWindow", "2"))
        self.pb_9.setText(_translate("CardWindow", "9"))
        self.pb_check.setText(_translate("CardWindow", "확인"))
        self.label.setText(_translate("CardWindow", "\"동\",\"호\" 와 카드 를  등록해주세요"))
        self.lb_dong.setText(_translate("CardWindow", "동"))
        self.lb_ho.setText(_translate("CardWindow", "호"))
        self.label_4.setText(_translate("CardWindow", "카드 :"))
        self.lb_cardin.setText(_translate("CardWindow", "미등록"))	
        self.pb_cancel.setText(_translate("CardWindow", "취소"))
          
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = EventWindow()
    w.show()
    sys.exit(app.exec_())

