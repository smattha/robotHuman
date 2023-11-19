from PyQt5.QtCore import pyqtSlot
from UiMainWindow import Ui_MainWindow1
from PyQt5 import QtCore
from PyQt5.QtWidgets import ( QMainWindow)

from PyQt5 import QtCore, QtWidgets
from time import sleep
from exercises.exersiceDigitSpan.DigitSpanController import DigitSpanController
from exercises.stroop.stroopController import stroopController
from exercises.sart.controller5 import controller5
from exercises.corsi.CorsiController import CorsiController
from exercises.goNoGo.goNoGoController import goNoGoController
from PyQt5.QtWidgets import QApplication
from pyexpat import model
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
# from exersiceC import ExersiceC
from sys import exit


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
        self._ui = Ui_MainWindow1()
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
    
        

        #!/usr/bin/env python3



class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)

        self.menu_view =ExersiceC(sys.argv[1])
        self.menu_view.show()


if __name__ == '__main__':
    try:
        app = App(sys.argv)
        print ('----------------------|'+sys.argv[1]+'|')
        app.exec_()
        print('Application is up and running')
    except KeyboardInterrupt:
        exit(0)

        # pip install PyQt5