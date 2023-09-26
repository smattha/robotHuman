from PyQt5.QtCore import pyqtSlot
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
from goNoGo.stats import stats
from goNoGo.row import row
from goNoGo.msgList import msg
from goNoGo.state import state
import random

class controller4():


    def keyPressEvent(self, event):
         if (event.text()=='s' or event.text()==' ') and (self.step=='instruction'):
            self.step='color'

    def __init__(self, ui,timerUI):
        self._ui=ui
        self.timerUI=timerUI

        self.stats=stats()
        self.height=1200
        self.width=1600


        self.buttonsExist=False
 
        self.rows=[]
        self.rowsTotal=[]
        self.stepA=True
        # self.drawUI()
        self.exA = QtCore.QTimer()
        self.exA.timeout.connect(self.exALoop)
        self.exA.start(100)
        self.sleep=00;
        self.state=state()
        self.currentNumber=''
        self.draw1Done=False

        self.step='instruction'
        self.counter=10

        self.counterA=0
        self.counterB=0

   
    def draw1(self):

        i=round(random.randint(0,11))
        j=round(random.randint(0,11))

        color='yellow'
        text='yellow'

        if i<3: 
            color='red'
        elif i<6:
            color='green'
        elif i<9:
            color='blue'

        if j<3: 
            text='red'
        elif j<6:
            text='green'
        elif j<9:
            text='blue'
    
        if(color==text):
            self.counterA=self.counterA+1
        else:
            self.counterB=self.counterB+1
        
        print('self.counterA +'+str(self.counterA)+" self.counterB "+str(self.counterB))

        self.counter1=0
        self.buttonArray = [] 
        self.buttonsExist=True
        
        ratio=1600/self.width
        

        x=(500+2*100)/ratio
        y=(int(1.5*100+100))/ratio
        self.button1= QtWidgets.QPushButton(self._ui.widget)

        self.button1.setText(text)
        self.button1.setObjectName("pushButton"+str(self.counter1))
        self.button1.setGeometry(QtCore.QRect(x,y, 250/ratio, 160/ratio))
        
        self.button1.setStyleSheet('QPushButton {background-color : black ; color: '+color+'; font-size: 22pt; }' )
        
        self.button1.show()


        self.counter1=self.counter1+1
        self.state

        
    
        
    def button_released(self):
        sending_button = self.sender()
        self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))



    def exALoop(self):
        if (self.step=='instruction'):
            return
        elif (self.step=='color'):
            self.step='sleep'
            self.draw1()
            self.sleep=20
            return
        elif (self.step=='sleep'):
            if(self.sleep>0):
                self.sleep=self.sleep-1
                return
            else :
                self.step='hide'
                self.sleep=3
        elif(self.step=='hide'):
            if(self.sleep>0):
                self.sleep=self.sleep-1
                return
            else :
                self.button1.hide()
                self.step='color'




    def exAClick(self,i,button):
        self.buttonArray[11].setEnabled(True)
        self.buttonArray[3].setEnabled(True)
        button.setEnabled(False)
        self.currentNumber=self._ui.corbiLabel.text()+str(i)
        self._ui.corbiLabel.setText(self._ui.corbiLabel.text()+str(i)) 
        curState=self.state.getCurrentRecord()
        curState.label=self.currentNumber

        return
       

      
    def storedata(self):
        print('Store data!!')


    
