from PyQt5.QtCore import pyqtSlot
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

class stats():
    def __init__(self):
        self.level=3
        self.time=300

    def startTimer(self):
         self.tick=time.time()
    
    def stopTimer(self):
        self.tock=time.time()


class row():

    def __init__(self):
        self.currentCorsi=3;
        self.ids=[]
        self.idsAnswer=[]
        self.timer=300
        
        self.timer1sec=1000
        self.first=True

class controller():

    def __init__(self, ui,timerUI):
        self._ui=ui
        self.timerUI=timerUI
        self.counter=0
        self.maxCounter=3
        self.stats=stats

        self.timer=300
        self.corbi=3
        self.countdown=3
        self.first=True

    
    def drawUI(self):

        counter1=0
        self.buttonArray = [] 

        # for i in range(0, self._ui.gridLayout_12.count()):
        #     a=self._ui.gridLayout_12.itemAt(i)
        #     a.widget().deleteLater()

        if (self.first==False):
            self._ui.button1.deleteLater()
            self._ui.button2.deleteLater()
            self._ui.button3.deleteLater()
            self._ui.button4.deleteLater()
            self._ui.button5.deleteLater()
            self._ui.button6.deleteLater()
            self._ui.button7.deleteLater()
            self._ui.button8.deleteLater()
            self._ui.button9.deleteLater()

        self.first=False
        for i in self.positions:
                print()
                print(i)
                print(40*(1+i%6*30))
                print(60*((i/5)*60+1))
                self.buttonArray.append( QtWidgets.QPushButton(self._ui.widget) )
                self.buttonArray[counter1].setObjectName("pushButton"+str(counter1))
                # self.buttonArray[counter1].setText("\n\n")
                self.buttonArray[counter1].clicked.connect( lambda: self.exAClick)
                # self.buttonArray[counter1].setStyleSheet("background-color : pink; padding-left: 12px;   padding-top: 1px; padding-bottom: 1px; width: 16px; height: 40px;" )
                self.buttonArray[counter1].setGeometry(QtCore.QRect((50+i%6*60), (i/5*60+60), 40, 40))
            
                # self._ui.gridLayout_12.addWidget( self.buttonArray[counter1], i/5, i%6, 1, 1)
                counter1=counter1+1
            

                
        # for j in range(0,16):    
            # self.buttonArray[j].clicked.connect( lambda: self.exAClick(j))
        self.buttonArray[0].clicked.connect( lambda: self.exAClick(0))
        self.buttonArray[1].clicked.connect( lambda: self.exAClick(1))
        self.buttonArray[2].clicked.connect( lambda: self.exAClick(2))
        self.buttonArray[3].clicked.connect( lambda: self.exAClick(3))
        self.buttonArray[4].clicked.connect( lambda: self.exAClick(4))
        self.buttonArray[5].clicked.connect( lambda: self.exAClick(5))
        self.buttonArray[6].clicked.connect( lambda: self.exAClick(6))
        self.buttonArray[7].clicked.connect( lambda: self.exAClick(7))
        self.buttonArray[8].clicked.connect( lambda: self.exAClick(8))


        self._ui.button1=self.buttonArray[0]
        self._ui.button2=self.buttonArray[1]
        self._ui.button3=self.buttonArray[2]
        self._ui.button4=self.buttonArray[3]
        self._ui.button5=self.buttonArray[4]
        self._ui.button6=self.buttonArray[5]
        self._ui.button7=self.buttonArray[6]
        self._ui.button8=self.buttonArray[7]
        self._ui.button9=self.buttonArray[8]


        self._ui.button1.show()
        self._ui.button2.show()
        self._ui.button3.show()
        self._ui.button4.show()
        self._ui.button5.show()
        self._ui.button6.show()
        self._ui.button7.show()
        self._ui.button8.show()
        self._ui.button9.show()



        # self.buttonArray[9].clicked.connect( lambda: self.exAClick(9))
        # self.buttonArray[10].clicked.connect( ttolambda: self.exAClick(10))
        # self.buttonArray[11].clicked.connect( lambda: self.exAClick(11))
        # self.buttonArray[12].clicked.connect( lambda: self.exAClick(12))
        # self.buttonArray[13].clicked.connect( lambda: self.exAClick(13))
        # self.buttonArray[14].clicked.connect( lambda: self.exAClick(14))
        # self.buttonArray[15].clicked.connect( lambda: self.exAClick(15))
        
    def button_released(self):
        sending_button = self.sender()
        self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))



    def exALoop(self):

        self.buttonArray = [] 
        self.drawUI()
        if(self.counter==self.currentRow.currentCorsi):
            self.exA.stop()
            self.stats.startTimer
            self.state='Answer'
        else:
            
            i=round(random.randint(0,8))
            while  i  in self.currentRow.ids:
                i=round(random.randint(0,8))
            self.currentRow.ids.append(i)
            for ii in self.buttonArray:
                    ii.setStyleSheet("background-color : pink;" )

            self.buttonArray[i].setStyleSheet("background-color : white;")
        self.counter=self.counter+1

    def startZero(self):
        a=row()
        self.start(a)

    def start(self,r_o_w):
        self.countdown=5
        self.counter=0
        self.state='Read'

        self.currentRow=r_o_w
        self.exA = QtCore.QTimer(self.timerUI)
        self.exA.stop()

        self.exB = QtCore.QTimer(self.timerUI)
        self.exB.stop()
        self.exB.start(self.currentRow.timer1sec)
        self.positions=[]

        while len(self.positions) <9:   
            i=round(random.randint(0,30))
            while  i  in self.positions:
                i=round(random.randint(0,30))
            self.positions.append(i)

        # self.drawUI()
        
        # self._ui.corbiLabel.setText(".....................")

        # self.startLevel()
        self.exA.timeout.connect(self.exALoop)
        self.exB.timeout.connect(self.countdownA)

    def countdownA(self):
        if (self.countdown>3):
            self.countdown=self.countdown-1
            return

        if (self.countdown==-1):
            self.exB.stop()
            self.exA.start(self.currentRow.timer)
            self._ui.corbiLabel.setText('Επιπεδό '+str(self.currentRow.currentCorsi))
            return
                  
        self._ui.corbiLabel.setText('Επιπεδό '+str(self.currentRow.currentCorsi)+' '+str(self.countdown))
        self.countdown=self.countdown-1

    def exAClick(self,i):
        print('Answer '+str(i))
        if self.state=='Answer':
            self.currentRow.idsAnswer.append(i)
            x=len(self.currentRow.idsAnswer)
            if (self.currentRow.ids[x-1]==i):
                print ('Correct '+ str(self.currentRow.ids[x-1]))
            else:
                print('Wrong')
                self._ui.corbiLabel.setText("Wrong")
                a=row()
                a.timer=self.timer*2
                self.timer=a.timer
                a.currentCorsi=self.corbi
                self.start(a)   
                return

        if(x==len(self.currentRow.ids)):
                self._ui.corbiLabel.setText("Correct")      
                a=row()
                a.currentCorsi=self.corbi+1
                self.corbi=self.corbi+1
                self.start(a)     


        