from PyQt5.QtCore import pyqtSlot
from partb import Ui_MainWindow
from PyQt5 import QtCore
from PyQt5.QtWidgets import ( QMainWindow)

from PyQt5 import QtCore, QtWidgets
from time import sleep
from exercises.exersiceDigitSpan.DigitSpanController import DigitSpanController
from stroop.stroopController import stroopController
from sart.controller5 import controller5
from exercises.corsi.CorsiController import CorsiController
from goNoGo.goNoGoController import goNoGoController
from PyQt5.QtWidgets import QApplication

class ExersiceC(QMainWindow):
    
    def keyPressEvent(self, event):
        # print('---')
        if event.text()=='t' or event.text()=='T' or event.text()=='τ' or event.text()=='Τ':
          QApplication.exit(0)
          
        self.c.keyPressEvent(event)
    
    def resizeEvent(self, event):
        height = event.size().height()
        width = event.size().width()
        self.c.height=height
        self.c.width=width
        self._ui.corbiLabel.setGeometry(QtCore.QRect( int(0), int(10), int(width), int(height)))


    def __init__(self,exercise):
        self.exercise=exercise
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
      
        self.init(self._ui)
        
    def init(self,ui):

        exercise=self.exercise

        if(exercise=='1'):  
          self.c=CorsiController(ui,self)
        elif (exercise=='2'):
          self.c=DigitSpanController(ui,self)
        elif (exercise=='3'):
          self.c=goNoGoController(ui,self)
        elif (exercise=='4'):
          self.c=stroopController(ui,self)
        elif (exercise=='5'):
          self.c=controller5(ui,self)
        self.c.height=1920
        self.c.width=1200
    
        

        