from PyQt5 import QtWidgets,QtCore, QtGui

#from callin
#from cardin import Ui_Cardin
#from cardin_alert import Ui_Cardin_Alert
from door import Ui_Door
from find import Ui_Find
from password import Ui_Password
from start import Ui_MainWindow
#from callin import Ui_callIn
from locker import Ui_Locker
from cardin_div import EventWindow
from callin_div import EventWindow2
from find_div import EventWindow3

x = 1

def num():
    global x
    return x

def find_div_stack(self):
    self.window  = QtWidgets.QMainWindow()
    self.ui = EventWindow3()
    self.ui.show()
    global x
    x = 2



def cardin_div_stack(self):
    self.window  = QtWidgets.QMainWindow()
    self.ui = EventWindow()
    self.ui.show()

def callin_div_stack(self):
    self.window  = QtWidgets.QMainWindow()
    self.ui = EventWindow2()
    self.ui.show()
    global x
    x =1


   
def locker_stack(self):
    self.window  = QtWidgets.QMainWindow()
    self.ui = Ui_Locker()
    self.ui.setupUi(self.window)
    self.window.show()
    
		

def start_stack(self):	
    self.window  = QtWidgets.QMainWindow()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self.window)
    self.window.show()
        



def password_stack(self):
    self.window  = QtWidgets.QMainWindow()
    self.ui = Ui_Password()
    self.ui.setupUi(self.window)
    self.window.show()
    
    
def door_stack(self):
    self.window = QtWidgets.QMainWindow()
    self.ui = Ui_Door()
    self.ui.setupUi(self.window)
    self.window.show()

