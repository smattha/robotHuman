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
class controller3():


    def keyPressEvent(self, event):
        print (str(self.step)+' '+str(self.row.greenGo))
        if (event.text()=='s' or event.text()==' ') and (self.step=='instruction'):
            self.step='color'
        elif self.step=='wait' and self.row.greenGo=='green':
            self.row.correct=True
            self.row.timeout=False
            self.row.stopTimer()
            self.step='replied'
            self.button1.hide()
        elif self.step=='wait' and not self.row.greenGo=='red':
            self.row.correct=False
            self.row.timeout=False
            self.row.stopTimer()
            self.step='replied'
            self.button1.hide()



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

        # self.completeTask = QtCore.QTimer()
        # self.completeTask.timeout.connect(self.completeTaskF)
        self.counterTotal=0

        self.exA.start(100)
        self.sleep=00;
        self.state=state()
        self.currentNumber=''
        self.draw1Done=False

        self.step='instruction'
        self.counter=10
        self.row=row()
        self.sleep=0
        print('--')
        ratio=1600/self.width
        

        x=(600+2*100)/ratio
        y=(int(1.5*100+100))/ratio

        self.button1= QtWidgets.QPushButton(self._ui.widget)
        self.button1.setObjectName("pushButton"+str(1))
        self.button1.setGeometry(QtCore.QRect(x,y, 250/ratio, 160/ratio))
        self.button1.hide()
        self.button1.setDisabled(True)
        print('--')
        self.rows=[]

        self.tick=time.time()

    def draw1(self):
        self._ui.corbiLabel.setText('') 
        self.row=row()
        i=round(random.randint(0,9))

        color='green'
        if i<5: 
            color='red'
        
        self.row.greenGo=color

        self.counter1=0
        self.buttonArray = [] 
        self.buttonsExist=True
        


     

        
        if color=='green':
            self.button1.setStyleSheet("background-color : green ;font-size: 22pt; " )
        else :
            self.button1.setStyleSheet("background-color : red ;font-size: 22pt; " )

        self.button1.show()
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
            print( str(self.counterTotal) +' ' +str(round(self.tock-self.tick,2)))
        

        if (self.counterTotal==200):
            for i in self.rows:
                i.print()
            self.exA.stop()

        if(self.sleep>0):
            self.sleep=self.sleep-1
            return

        if(self.step=='wait'):
            self.button1.hide()
            self.row.timeout=True
            self.row.stopTimer()
            self.rows.append(self.row)
            self._ui.corbiLabel.setText('Λάθος') 
            self.step='color'
            self.sleep=2

            return

        if (self.step=='interval'):
            print('!!interval')
            self.sleep=2
            self.step='color'
            self.button1.hide()
            return
        
        if (self.step=='instruction'):
            return
        elif (self.step=='color'):
            print('!COLOR!')
            self.draw1()
            self.sleep=20
            self.step='wait'
            return
        elif (self.step=='replied'):

            self.rows.append(self.row)
            if self.row.correct:
                self._ui.corbiLabel.setText('Correct') 
                self.step='interval'
            else :
                self._ui.corbiLabel.setText('Wrong') 
            self.sleep=10
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


    
