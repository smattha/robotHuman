from PyQt5.QtCore import pyqtSlot
from partb import Ui_MainWindow
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import ( QMainWindow)

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
# import tty
import sys
# import termios
from threading import Thread
from time import sleep
import random
path_of_image = '/home/stergios/Desktop/a.png'
import time
import random
from   exersiceDigitSpan.controller2 import controller2
from stroop.controller4 import controller4
from sart.controller5 import controller5

from goNoGo.controller3 import controller3
from controller import controller
class ExersiceC(QMainWindow):
    
    def keyPressEvent(self, event):
        self.c.keyPressEvent(event)
    
    def resizeEvent(self, event):
        height = event.size().height()
        width = event.size().width()
        self.c.height=height
        self.c.width=width
        self._ui.corbiLabel.setGeometry(QtCore.QRect( 0, 10, width, 300))


    def __init__(self,exercise):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)




        if(exercise=='1'):  
          self.c=controller(self._ui,self)
        elif (exercise=='2'):
          self.c=controller2(self._ui,self)
        elif (exercise=='3'):
          self.c=controller3(self._ui,self)
        elif (exercise=='4'):
          self.c=controller4(self._ui,self)
        elif (exercise=='5'):
          self.c=controller5(self._ui,self)
        
        self.c.height=1900
        self.c.width=1200
    
        

        