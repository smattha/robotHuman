from PyQt5.QtCore import pyqtSlot
from partb import Ui_MainWindow
from PyQt5 import QtCore
from PyQt5.QtWidgets import ( QMainWindow)

from PyQt5 import QtCore, QtWidgets
from time import sleep
import time
from   exersiceDigitSpan.controller2 import controller2
from stroop.stroopController import stroopController
from sart.controller5 import controller5
from corsi.corsiController import corsi
from goNoGo.goNoGoController import goNoGoController

class ExersiceC(QMainWindow):
    
    def keyPressEvent(self, event):
        
        self.c.keyPressEvent(event)
    
    def resizeEvent(self, event):
        height = event.size().height()
        width = event.size().width()
        self.c.height=height
        self.c.width=width
        self._ui.corbiLabel.setGeometry(QtCore.QRect( 0, 10, width, 600))


    def __init__(self,exercise):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)




        if(exercise=='1'):  
          self.c=corsi(self._ui,self)
        elif (exercise=='2'):
          self.c=controller2(self._ui,self)
        elif (exercise=='3'):
          self.c=goNoGoController(self._ui,self)
        elif (exercise=='4'):
          self.c=stroopController(self._ui,self)
        elif (exercise=='5'):
          self.c=controller5(self._ui,self)
        
        self.c.height=1900
        self.c.width=1200
    
        

        