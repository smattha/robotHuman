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
from utilities.stats import stats
from exercises.sart.row import row
from Text.SART_MSG import SART_MSG
# from exercises.sart.state import state
import random
from PyQt5.QtWidgets import QLabel 
from PyQt5.QtGui import * 
from utilities.TableView import TableView
import os
import re
class sartController():


    def keyPressEvent(self, event):
                
        if (self._ui.ros.isTalking):
            return
        
        if (event.text()=='s' or event.text()==' ') and (self.step=='instruction'):
            self.step='color'
            self._ui.corbiLabel.setText('')
            self.displayBackground('img/back.png')
        if (event.text()=='s' or event.text()==' ') and (self.step=='finished'):
            self.step='color'
            self._ui.corbiLabel.setText('')
            self.displayBackground('img/back.png')
            self.init()
            try:
                self.table.table1.hide()
            except:
                print('...')

        elif(event.text()==chr(27)):
            self.finish()
        elif (event.text()==' '):
              self.sleep=-1

    def finish(self):
        print('Finish')
        self.exA.stop()
        self.step='finished'


        meanTime=0
        correctCounter=0
        falseCounter=0
        
        for i in self.rows:
            i.print()
            meanTime=meanTime+i.time
            if (i.correct):
                correctCounter=correctCounter+1
            else:
                falseCounter=falseCounter+1

        if (len(self.rows)):
            meanTime= round(meanTime/len(self.rows),2)


        self._ui.corbiLabel.setText(self.MSG.result(meanTime,correctCounter,falseCounter))
        self.displayBackground('img/happy.png')

        try:
            self.button1.hide()
        except :
            print('..')

        try:
            self.label.hide()
        except :
            print('..')
        
        self.showTable()

    def showTable(self):
        if (len(self.rows)>0):
            data=[]
            headers=[]
            for row in self.rows:
                data.append(row.getData())
                headers=row.getHeader()
        if (len(self.rows)):
            self.table = TableView(self._ui.widget,data,headers,'sart')

    def __init__(self, ui,timerUI):
        self._ui=ui
        self.timerUI=timerUI

        self.init()

    def init(self):

        self.stats=stats()
        self.height=1200
        self.width=1600


        self.buttonsExist=False
 
        self.rows=[]
        self.rowsTotal=[]
        self.stepA=True
        self.exA = QtCore.QTimer()
        self.exA.timeout.connect(self.exALoop)
        self.exA.start(5)
        self.timeFactor=20
        self.sleep=00;
        self.maxCounter=12000 
        self.counterTotal=0
        # self.state=state()
        self.currentNumber=''
        self.draw1Done=False
        self.currentRow=row()

        self.step='instruction'
        self.counter=10
    
        self.MSG=SART_MSG()
        self.pattern = re.compile('<.*?>')  

        self.path = "img/sart"
        self.dir_list = os.listdir(self.path)
        
        
   
    def draw1(self):

        i=round(random.randint(0,9))

        self._ui.corbiLabel.setText('')
        color='red'
        if i<8: 
            color='green'
            i=round(random.randint(0,len(self.dir_list)-1))
            print(self.path+self.dir_list[i])
            self.displayLabel('img/sart/'+self.dir_list[i])
        else:
            self.displayLabel("img/fresh-red-apple.png")
            

        self.counter1=0
        self.buttonArray = [] 
        self.buttonsExist=True
        
        ratio=1600/self.width
        

        x=(500+2*100)/ratio
        y=(int(1.5*100+100))/ratio
        self.button1= QtWidgets.QPushButton(self._ui.widget)
        self.button1.setText(str(i))
     
        self.button1.setObjectName("pushButton"+str(self.counter1))
        self.button1.setGeometry(QtCore.QRect(int(x),int(y), int(250/ratio), int(160/ratio)))
        self.button1.hide()
        
        if color=='green':
            self.button1.setStyleSheet("background-color : pink ;font-size: 22pt; " )
        else :
            self.button1.setStyleSheet("background-color : pink ;font-size: 22pt; " )
        self.counter1=self.counter1+1
        self.currentRow=row();
        self.currentRow.greenGo=color
    
    def displayBackground(self,img):
        pixmap = QPixmap(img)
        self._ui.label.setPixmap(pixmap)
        self._ui.label.setScaledContents( True );
        self._ui.label.show()

    def displayLabel(self,img):
        self.label = QLabel(self._ui.widget)
        pixmap = QPixmap(img)
        self.label.setPixmap(pixmap)

        ratio=1600/self.width
        x=(500+2*100)/ratio
        y=(int(1.5*100+100))/ratio

        self.label.setGeometry(int(x),int(y),300,300)
        self.label.setScaledContents( True );
        self.label.show()    
        

    def button_released(self):
        sending_button = self.sender()
        self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))


    def exALoop(self):
                
        if (self._ui.ros.isTalking):
            return

        self.counterTotal=self.counterTotal+1
        if (self.counterTotal>=self.maxCounter):
            self.finish()
            return
        if (self.step=='instruction')and self._ui.corbiLabel.text()!=self.MSG.INSTRUNCTIONS:
            self._ui.corbiLabel.setText(self.MSG.INSTRUNCTIONS)     
            self._ui.ros.startUpdateThread(re.sub(self.pattern, '',self.MSG.INSTRUNCTIONS_ROS))
            self._ui.corbiLabel.setStyleSheet("font-size: 24pt; color : blue" )
            return
        elif (self.step=='color'):
            self.step='sleep'
            self.draw1()
            self.sleep=20*self.timeFactor
            return
        elif (self.step=='sleep'):
            if(self.sleep>0):
                self.sleep=self.sleep-1
                return
            elif self.sleep==0 :
                print('...')
                self.currentRow.timeout=True
                self.currentRow.stopTimer()
                self.rows.append(self.currentRow)
                self.step='hide'
                if (self.currentRow.correct):
                    self.sleep=3*self.timeFactor
                else:
                    self.sleep=10*self.timeFactor
            else:
                print('...')
                self.currentRow.timeout=False
                self.currentRow.pressed=True
                self.currentRow.stopTimer()
                self.rows.append(self.currentRow)
                self.step='hide'
                if (self.currentRow.correct):
                    self.sleep=3*self.timeFactor
                else:
                    self.sleep=10*self.timeFactor
        elif(self.step=='hide'):
            # print(self.currentRow.correct)
            self._ui.corbiLabel.setText(self.currentRow.correctGR)
            if(self.sleep>0):
                self.sleep=self.sleep-1
                self.button1.hide()
                self.label.hide()
                return
            else :
                self.button1.hide()
                self.step='color'
      
    def storedata(self):
        print('Store data!!')


    
