from PyQt5 import QtWidgets,QtCore, QtGui

import callin_div 
import find_div

def idnum():
    su = callin_div.idval()
    return su 

def id2num():
    su = find_div.idval2()
    return su

def snnum():
    su = find_div.serctnum()
    return su

def divnum():
    su = find_div.divcard()
    return su