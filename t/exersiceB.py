from PyQt5.QtCore import pyqtSlot
from partb import Ui_MainWindow
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import ( QMainWindow)

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import tty
import sys
import termios
from threading import Thread
from time import sleep
import random
path_of_image = '/home/stergios/Desktop/a.png'
import time
import random
from   controller import controller
class ExersiceB(QMainWindow):
    
    def keyPressEvent(self, event):
        if(self.lock==True):
            return
        print('...........')
        self.tock=time.time()

        print("You pressed"+ event.text()+ " mode "+ self.mode+ " time " +str(self.tock-self.tick))

        
        if (self.mode=='fish'):
            print ("Mode Fish")
            self.correctFish=self.correctFish+1
            self.totalTime=self.totalTime+ self.tock-self.tick
        elif (self.mode=='sharck') :
            print('Else')
            self.errorFish=self.errorFish+1
            self.totalTime=self.totalTime+ self.tock-self.tick
       

    def __init__(self):
        super().__init__()

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.c=controller(self._ui,self)
        
        self.c.startZero()