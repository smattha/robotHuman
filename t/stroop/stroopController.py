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
from stroop.stats import stats
from stroop.row import row
# from stroop.msgList import msg
from stroop.state import state
import random
import time


class stroopController():


    def keyPressEvent(self, event):
         if (event.text()=='s' or event.text()==' ') and (self.step=='instruction'):
            self.step='color'

         if (event.text()=='s' or event.text()==' ') and (self.step=='sleep'):
            self.step='hide'
            self.sleep=2
            self.row.stopTimer(True)
            if(self.row.correctAnswer()):
                    self.correctCounter=self.correctCounter+1
            else:
                    self.falseCounter=self.falseCounter+1
            # self.row.pressed=
            self.rows.append(self.row)

            
            
    def __init__(self, ui,timerUI):


        self._ui=ui
        self.timerUI=timerUI

        self.stats=stats()
        self.height=1200
        self.width=1900
        self.counterTotal=0

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

        self.tick=time.time()
        self.rows=[]
        self.row=row('--','--')
        self.correctCounter=0
        self.falseCounter=0
        
        self._ui.widget.setGeometry(QtCore.QRect(0, 0,self.timerUI.width() , self.timerUI.height()))
        self._ui.corbiLabel.setText('<b>Stroop</b> <br> <br> Πάτα το space όταν το χρώμα της λέξης και το νόημα είναι το ίδιο.') 
        self._ui.corbiLabel.setGeometry(QtCore.QRect(0, 0,self.timerUI.width() , 200))
        
        self._ui.corbiLabel.setStyleSheet("font-size: 28pt; " )

    def calculatePerc(self):
        str(self.correctCounter)+'/'+str(self.falseCounter)
        if (self.falseCounter>0):
            perc=((self.correctCounter+0.001)/(self.falseCounter+self.correctCounter))*100
            # print(perc)
            if (perc<30):
                return 100
            elif (perc<50):
                return 80
            elif (perc<75):
                return 65  
        return 50
    
    def draw1(self):
        self._ui.corbiLabel.setText('') 
        i=round(random.randint(0,11))
        self._ui.widget.setGeometry(QtCore.QRect(0, 0,self.timerUI.width() , self.timerUI.height()))
        self._ui.corbiLabel.setGeometry(QtCore.QRect(0, 0,self.timerUI.width() , 200))

        self.color='yellow'
        self.text='yellow'

        if i<3: 
            self.color='red'
        elif i<6:
            self.color='green'
        elif i<9:
            self.color='blue'
        
        p=random.randint(0,100)
        if(p>self.calculatePerc()):       
            self.text=self.color
            while (self.text==self.color):
                j=round(random.randint(0,11))
                if j<3: 
                    self.text='red'
                elif j<6:
                    self.text='green'
                elif j<9:
                    self.text='blue'
                elif j<12:
                    self.text='yellow'
        else:
            self.text= self.color
        
        if(self.color==self.text):
            self.counterA=self.counterA+1
        else:
            self.counterB=self.counterB+1
        self.row=row(self.text,self.color)
         
        print('Print correct color:'+str(self.counterA)+"/"+str(self.counterB+self.counterB)+ 'answer '+str(self.correctCounter)+'/'+str(self.falseCounter))

        self.counter1=0
        self.buttonArray = [] 
        self.buttonsExist=True

        

        x=self.timerUI.width()*0.6
        y=(self.timerUI.height()-100)*0.6
        x1=(self.timerUI.width()-x)/2
        y1=(self.timerUI.height()-y)/2

        self.button1= QtWidgets.QPushButton(self._ui.widget)
        self.button1.setObjectName("pushButton"+str(self.counter1))
        self.button1.setGeometry(QtCore.QRect(x1,y1, x,y))       
        
        self.textGR=''
        if (self.text=='green'):
            self.textGR='Πράσινο'
        elif (self.text=='blue'):
            self.textGR='Μπλε'
        elif (self.text=='red'):
            self.textGR='Κόκκινο'
        elif (self.text=='yellow'):
            self.textGR='Κίτρινο'   

        self.button1.setText(self.textGR)     
        self.button1.setStyleSheet('QPushButton {background-color : grey ; color: '+self.color+'; font-size: 52pt; }' )
        self.button1.show()

        self.counter1=self.counter1+1
        
    
        
    def button_released(self):
        sending_button = self.sender()
        self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))



    def exALoop(self):
        # print(str(self.timerUI.width())+' '+str(self.timerUI.height()))
        if (self.step!='instruction'):
            self.counterTotal=self.counterTotal+1 
            self.tock=time.time()
            # print( str(self.counterTotal) +' ' +str(round(self.tock-self.tick,2)))

        if (self.counterTotal>300):
            for i in self.rows:
                i.print()
                self.exA.stop()
                self.button1.hide()
                self._ui.corbiLabel.setText('Τέλος')
            return
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
                self.row.stopTimer(False)
                if(self.row.correctAnswer()):
                    self.correctCounter=self.correctCounter+1
                else:
                    self.falseCounter=self.falseCounter+1
                # self.row.pressed=False
                self.rows.append(self.row)
        elif(self.step=='hide'):
            if(self.sleep>0):
                self.sleep=self.sleep-1
                return
            else :
                self.button1.hide()
                self.step='color'

      

