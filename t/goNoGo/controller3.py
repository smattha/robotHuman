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
import time
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel

class controller3():


    def keyPressEvent(self, event):
        # print (str(self.step)+' '+str(self.row.greenGo))
        if (event.text()=='s' or event.text()==' ') and (self.step=='instruction'):
            self.step='color'
        elif self.step=='wait' and self.row.greenGo=='green':
            print('Correct')
            self.row.correct=True
            self.row.timeout=False
            self.row.stopTimer()
            self.step='replied'
            self.button1.hide()
            
            self.label.hide()
            self.sleep=0
        elif self.step=='wait' and self.row.greenGo=='red':
            self.row.correct=False
            self.row.timeout=False
            self.row.stopTimer()
            self.step='replied'
            self.button1.hide()
            
            self.label.hide()
            self.sleep=0



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

        self.counterTotal=0
        self.sleepFactor=100/2
        self.exA.start(100/self.sleepFactor)
        self.sleep=00;
        self.state=state()
        self.currentNumber=''
        self.draw1Done=False

        self.step='instruction'
        self.counter=10
        self.row=row()
        self.sleep=0
        # print('--')
        ratio=1600/self.width
        

        x=self.timerUI.width()*0.5
        y=(self.timerUI.height()*0.5)
        x1=(self.timerUI.width()-x)/2
        y1=(self.timerUI.height()-y)/2

        self.button1= QtWidgets.QPushButton(self._ui.widget)
        self.button1.setObjectName("pushButton"+str(1))
        self.button1.setGeometry(QtCore.QRect(x1,y1, x,y))


        self.button1.hide()
        self.button1.setDisabled(True)
        print('--')
        self.rows=[]

        self.tick=time.time()
        
        self._ui.corbiLabel.setText('Go/No-go task\n\n Πάτα το space όταν εμφανίζετε το πράσινο τετραγωνάκι.\n Μη κάνεις τίποτα όταν το τετραγωνάκι είναι κόκκινο.') 
        self._ui.widget.setGeometry(QtCore.QRect(0, 0,self.timerUI.width() , self.timerUI.height()))
        self._ui.corbiLabel.setGeometry(QtCore.QRect(0, 0,self.timerUI.width() , 200))

        self.correctCounter=0
        self.falseCounter=0
        self.displayImg1()


    def displayImg1(self):
        self.label = QLabel(self._ui.widget)
        pixmap = QPixmap("start.png")
        self.label.setPixmap(pixmap)
        self.label.setGeometry(300,300,300,300)
        self.label.setScaledContents( True );
        self.label.hide()
        
    
    def draw1(self):
        self._ui.corbiLabel.setText('') 
        self.row=row()
        i=round(random.randint(0,99))

        self._ui.widget.setGeometry(QtCore.QRect(0, 0,self.timerUI.width() , self.timerUI.height()))
        self._ui.corbiLabel.setGeometry(QtCore.QRect(0, 0,self.timerUI.width() , 200))

        color='green'
        if i<self.calculatePerc(): 
            color='red'
        
        self.row.greenGo=color

        self.counter1=0
        self.buttonArray = [] 
        self.buttonsExist=True
        
        x=self.timerUI.width()*0.5
        y=(self.timerUI.height()*0.5)
        x1=(self.timerUI.width()-x)/2
        y1=(self.timerUI.height()-y)/2
        print(str(x)+' '+str(y))
        if color=='green':
            self.button1.hide()
            self.button1.setDisabled(True)
            
            self.button1.setStyleSheet("background-color : green ;font-size: 22pt; " )
            # self.displayImg("C:\\Users\\smatthai\\gitProjects\\robotHuman\\t\\start.png",x,y,x1,y1)
            pixmap = QPixmap("start.png")
            self.label.setPixmap(pixmap)
            self.label.setGeometry(x1,y1,x,y)
            self.label.show()
          
        else :
            self.button1.hide()           
            self.button1.setDisabled(True)
            pixmap = QPixmap("stop.png")
            self.label.setPixmap(pixmap)            
            self.label.setGeometry(x1,y1,x,y)
            self.label.show()
        # self.button1.show()
        self.counter1=self.counter1+1

    def storeAnswered(self):
        print('storeAnswered')
        
    
        
    def button_released(self):
        sending_button = self.sender()
        self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))

    def completeTaskF(self):
        self.exA.stop()

        
    def exALoop(self):

        if (self.step!='instruction'):
            self.counterTotal=self.counterTotal+1 
            self.tock=time.time()
            # print( str(self.counterTotal) +' ' +str(round(self.tock-self.tick,2)))

        # print('correct/total'+str(self.correctCounter)+'/'+str(self.correctCounter+self.falseCounter))
        

        if (self.counterTotal==200*self.sleepFactor):
            for i in self.rows:
                i.print()
            self.exA.stop()
            self.button1.hide()
            self.label.hide()

        if(self.sleep>0):
            self.sleep=self.sleep-1
            return

        if(self.step=='wait'):
            self.button1.hide()
            self.label.hide()

            self.row.timeout=True
            self.row.stopTimer()
            if(self.row.greenGo=='red'):
                self.row.correct=True
                self.correctCounter=self.correctCounter+1

            else:
                self.row.correct=False
                self._ui.corbiLabel.setText('Λάθος') 
                self.sleep=10*self.sleepFactor
                self.falseCounter=self.falseCounter+1

            self.step='interval'
            self.rows.append(self.row)

            return

        if (self.step=='interval'):
            print('!!interval')
            self.sleep=2*self.sleepFactor
            self.step='color'
            self.button1.hide()
            self.label.hide()
            return
        
        if (self.step=='instruction'):
            return
        elif (self.step=='color'):
            self.draw1()
            if (self.row.greenGo=='green'):
                self.sleep=20*self.sleepFactor
            else:
                self.sleep=10*self.sleepFactor    
            self.step='wait'
            return
        elif (self.step=='replied'):
            self.rows.append(self.row)
            if self.row.correct:
                # self._ui.corbiLabel.setText('Correct') 
                self.step='color'
                self.sleep=3*self.sleepFactor
                self.correctCounter=self.correctCounter+1
            else :
                self._ui.corbiLabel.setText('Λάθος') 
                self.step='color'
                self.sleep=10*self.sleepFactor
                self.falseCounter=self.falseCounter+1

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



    # def exAClick(self,i,button):
    #     self.buttonArray[11].setEnabled(True)
    #     self.buttonArray[3].setEnabled(True)
    #     button.setEnabled(False)
    #     self.currentNumber=self._ui.corbiLabel.text()+str(i)
    #     self._ui.corbiLabel.setText(self._ui.corbiLabel.text()+str(i)) 
    #     curState=self.state.getCurrentRecord()
    #     curState.label=self.currentNumber

    #     return
       

      
    # def storedata(self):
    #     print('Store data!!')


    
