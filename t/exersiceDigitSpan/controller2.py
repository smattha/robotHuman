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
from exersiceDigitSpan.stats import stats
from row import row
from exersiceDigitSpan.msgList import msg
from exersiceDigitSpan.state import state

class controller2():


    def keyPressEvent(self, event):
         if (event.text()=='s' or event.text()==' '):
              self.sleep=0

    def __init__(self, ui,timerUI):
        self._ui=ui
        self.timerUI=timerUI

        self.stats=stats()
        self.height=1200
        self.width=1600


        self.buttonsExist=False
 
        self.currentRows=[]
        self.stepA=True
        # self.drawUI()
        self.exA = QtCore.QTimer()
        self.exA.timeout.connect(self.exALoop)
        self.exA.start(100)
        self.sleep=00;
        self.state=state()
    
    def clearUI(self):
        if (self.buttonsExist==True):
            for i in range(0,self.counter1):
                self.buttonArray[i].deleteLater()
        self.buttonsExist=True

    def drawUI(self):

        self.clearUI()
        self.counter1=0
        self.buttonArray = [] 
        self.buttonsExist=True
        
        ratio=1600/self.width
        
        for i in [1,2,3]:
                for j in [0,1,2,3]:
                    x=(560+i*100)/ratio
                    y=(int(j)*100+150)/ratio
                    button1= QtWidgets.QPushButton(self._ui.widget)
                    button1.setText(str(3*j+i))
                    self.buttonArray.append( button1)
                    self.buttonArray[self.counter1].setObjectName("pushButton"+str(self.counter1))
                    self.buttonArray[self.counter1].clicked.connect( lambda: self.exAClick)
                    self.buttonArray[self.counter1].setGeometry(QtCore.QRect(x,y, 80/ratio, 80/ratio))
                    self.buttonArray[self.counter1].setStyleSheet("background-color : pink;" )
                    
                    self.buttonArray[self.counter1].show()
                    self.counter1=self.counter1+1


        x=(560+1*100)/ratio
        y=(int(5)*100+150)/ratio
        
        self.buttonArray[3].setText(msg.CLEAR)
        self.buttonArray[3].setGeometry(QtCore.QRect(x,y, 80/ratio, 80/ratio))
        
        
        self.buttonArray[7].setText('0')

        x=(560+3*100)/ratio
        y=(int(5)*100+150)/ratio
        self.buttonArray[11].setGeometry(QtCore.QRect(x,y, 80/ratio, 80/ratio))
        self.buttonArray[11].setText(msg.CONTINUE)


        self.buttonArray[0].clicked.connect( lambda: self.exAClick(1))
        self.buttonArray[1].clicked.connect( lambda: self.exAClick(4))
        self.buttonArray[2].clicked.connect( lambda: self.exAClick(7))
        self.buttonArray[3].clicked.connect( lambda: self.clear('clear'))
        self.buttonArray[4].clicked.connect( lambda: self.exAClick(2))
        self.buttonArray[5].clicked.connect( lambda: self.exAClick(5))
        self.buttonArray[6].clicked.connect( lambda: self.exAClick(8))
        self.buttonArray[7].clicked.connect( lambda: self.exAClick(0))
        self.buttonArray[8].clicked.connect( lambda: self.exAClick(3))
        self.buttonArray[9].clicked.connect( lambda: self.exAClick(6))
        self.buttonArray[10].clicked.connect( lambda: self.exAClick(9))
        self.buttonArray[11].clicked.connect( lambda: self.exAClickContinuou('Continue'))

        

    def draw1(self, number):
        self.stats.number=self.stats.number+str(number)
        self.clearUI()
        self.counter1=0
        self.buttonArray = [] 
        self.buttonsExist=True
        
        ratio=1600/self.width
        

        x=(560+2*100)/ratio
        y=(int(1.5*100+150))/ratio
        button1= QtWidgets.QPushButton(self._ui.widget)
        button1.setText(number)
        self.buttonArray.append( button1)
        self.buttonArray[self.counter1].setObjectName("pushButton"+str(self.counter1))
        self.buttonArray[self.counter1].clicked.connect( lambda: self.exAClick)
        self.buttonArray[self.counter1].setGeometry(QtCore.QRect(x,y, 80/ratio, 80/ratio))
        self.buttonArray[self.counter1].setStyleSheet("background-color : pink;" )
        
        self.buttonArray[self.counter1].show()


        self.counter1=self.counter1+1
        self.state

        
    
        
    def button_released(self):
        sending_button = self.sender()
        self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))



    def exALoop(self):

        if (self.sleep==-10):
            print('waitForButton')

        if (self.sleep>0):
            self.sleep=self.sleep-1
            return
        

        curState=self.state.getCurrentRecord()
        
        
        if (curState.UI=='drawUI'):
            self.drawUI()
            print('--')
        if (curState.UI=='draw1'):
            self.draw1(curState.number)

        self.msg=msg()
        self._ui.corbiLabel.setText(curState.label)   

        self.sleep=curState.pause
        self.state.changeState()




    def exAClick(self,i):
        self.currentNumber=self._ui.corbiLabel.text()+str(i)
        self._ui.corbiLabel.setText(self._ui.corbiLabel.text()+str(i)) 
        curState=self.state.getCurrentRecord()
        curState.label=self.currentNumber

        return
       


    def exAClickContinuou(self,i):
        wrong=False
        if(self.stats.number==self.currentNumber):
            print ('Correct')
            self.stats.wrong=0
        else :
            wrong=True
            self.stats.wrong=self.stats.wrong+1
            if self.stats.wrong == 3:
                self.clearUI()    
                self.currentNumber=''
                return
            print (self.stats.number+' !== '+self.currentNumber)
        print(i)
        
        self.state.addChangeState(wrong,self.stats.wrong)
        self.sleep=0
        print(i)
        self.currentNumber=''
        return
       
    def storedata(self):
        print('Store data!!')
    def clear(self,i):
        Str=self._ui.corbiLabel.text()
        Str = Str[:len(Str)-1]
        self._ui.corbiLabel.setText(Str)
        return
    
