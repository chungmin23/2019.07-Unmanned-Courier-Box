# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'find.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will beh
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
#global address

class Ui_Find(object):


    def setupUi(self, FindWindow):
	#global address
	#address  = FindWindow
        FindWindow.setObjectName("FindWindow")
        FindWindow.resize(800, 480)

	self.FindWindow = FindWindow

        self.centralwidget = QtWidgets.QWidget(FindWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_call_2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_call_2.setGeometry(QtCore.QRect(230, 170, 41, 41))
        self.lb_call_2.setStyleSheet("font: italic 26pt \"PibotoLt\";\n"
"")
        self.lb_call_2.setObjectName("lb_call_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(440, 50, 317, 341))
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
        self.label.setGeometry(QtCore.QRect(10, 60, 421, 51))
        self.label.setStyleSheet("\n"
"font: italic 13pt \"PibotoLt\";\n"
"")
        self.label.setObjectName("label")
        self.pb_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pb_cancel.setGeometry(QtCore.QRect(30, 350, 101, 71))
        self.pb_cancel.setStyleSheet("font: italic 18pt \"PibotoLt\";\n"
"")
        self.pb_cancel.setObjectName("pb_cancel")
        self.lb_ho = QtWidgets.QLabel(self.centralwidget)
        self.lb_ho.setGeometry(QtCore.QRect(230, 240, 41, 41))
        self.lb_ho.setStyleSheet("\n"
"font: italic 26pt \"PibotoLt\";")
        self.lb_ho.setObjectName("lb_ho")
        self.le_dong = QtWidgets.QLineEdit(self.centralwidget)
        self.le_dong.setGeometry(QtCore.QRect(30, 170, 181, 51))
        self.le_dong.setStyleSheet("font: italic 24pt \"PibotoLt\";")
        self.le_dong.setText("")
	self.le_dong.setFocus()
	self.le_dong.setAlignment(QtCore.Qt.AlignCenter)
	self.le_dong.setMaxLength(3)
        self.le_dong.setObjectName("le_dong")
        self.le_ho = QtWidgets.QLineEdit(self.centralwidget)
        self.le_ho.setGeometry(QtCore.QRect(30, 240, 181, 51))
        self.le_ho.setStyleSheet("font: italic 24pt \"PibotoLt\";")
	self.le_ho.setMaxLength(3)
	self.le_ho.setAlignment(QtCore.Qt.AlignCenter)
        self.le_ho.setObjectName("le_ho")
        self.lb_card = QtWidgets.QLabel(self.centralwidget)
        self.lb_card.setGeometry(QtCore.QRect(670, 0, 91, 31))
        self.lb_card.setStyleSheet("font: italic 26pt \"PibotoLt\";\n"
"color: rgb(255, 0, 0);")
        FindWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FindWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        FindWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FindWindow)
        self.statusbar.setObjectName("statusbar")
        FindWindow.setStatusBar(self.statusbar)
	self.pb_cancel.clicked.connect(lambda:self.close(FindWindow))
	self.pb_check.clicked.connect(lambda:self.check(FindWindow))
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
     	FindWindow.showFullScreen()

        self.retranslateUi(FindWindow)
        QtCore.QMetaObject.connectSlotsByName(FindWindow)



    def retranslateUi(self, FindWindow):
        _translate = QtCore.QCoreApplication.translate
        FindWindow.setWindowTitle(_translate("FindWindow", "FindWindow"))
        self.lb_call_2.setText(_translate("FindWindow", "동"))
        self.pb_1.setText(_translate("FindWindow", "1"))
        self.pb_5.setText(_translate("FindWindow", "5"))
        self.pb_7.setText(_translate("FindWindow", "7"))
        self.pb_4.setText(_translate("FindWindow", "4"))
        self.pb_delete.setText(_translate("FindWindow", "지우기"))
        self.pb_8.setText(_translate("FindWindow", "8"))
        self.pb_0.setText(_translate("FindWindow", "0"))
        self.pb_6.setText(_translate("FindWindow", "6"))
        self.pb_3.setText(_translate("FindWindow", "3"))
        self.pb_2.setText(_translate("FindWindow", "2"))
        self.pb_9.setText(_translate("FindWindow", "9"))
        self.pb_check.setText(_translate("FindWindow", "확인"))
        self.label.setText(_translate("FindWindow", "\"동\"과\"호\" 혹은 카드를 입력하시고 확인을 눌러주세요"))
        self.pb_cancel.setText(_translate("FindWindow", "취소"))
        self.lb_ho.setText(_translate("FindWindow", "호"))
	self.lb_card.setText(_translate("MainWindow", "CARD"))
 
    def hid(self):
#	global address
#	address.hide() 
	self.FindWindow.hide()

    #app = QtWidgets.QApplication(sys.argv)
    #FindWindow = QtWidgets.QMainWindow()


if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FindWindow = QtWidgets.QMainWindow()

    ui = Ui_Find()
    ui.setupUi(FindWindow)
    FindWindow.show()
    sys.exit(app.exec_())

