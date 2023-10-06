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
from exersiceDigitSpan.row import row
from exersiceDigitSpan.msgList import msg
from exersiceDigitSpan.state import state
from TableView import TableView

class controller2():


    def keyPressEvent(self, event):
        if(event.text()==chr(27)):
            self.finishEx()
        if (event.text()=='s' or event.text()==' '):
            if (self.sleep==-10):
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
        self.exA.start(100/3)
        self.sleep=00;
        self.state=state()
        self.currentNumber=''
        self.draw1Done=False

        self._ui.corbiLabel.setGeometry(QtCore.QRect( 0, 10, self.width, 600))

        self.buttonArray=[]

    
    def clearUI(self):
        self.draw1Done=False
        if (self.buttonsExist==True):
            for i in range(0,self.counter1):
                self.buttonArray[i].deleteLater()
        self.buttonsExist=True

    def drawUI(self):
        if self.draw1Done==True:
            return
       
       

        self.clearUI()
        self.draw1Done=True
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
                    self.buttonArray[self.counter1].setStyleSheet("background-color : pink; font-size: 18pt; " )
                    
                    self.buttonArray[self.counter1].show()
                    self.counter1=self.counter1+1


        x=(560+1*100)/ratio
        y=(int(5)*100+150)/ratio
        
        self.buttonArray[3].setText(msg.CLEAR)
        self.buttonArray[3].setGeometry(QtCore.QRect(x,y, 80/ratio+40, 80/ratio))
        
        
        self.buttonArray[7].setText('0')

        x=(560+3*100)/ratio
        y=(int(5)*100+150)/ratio
        self.buttonArray[11].setGeometry(QtCore.QRect(x-40,y, 80/ratio+40, 80/ratio))
        self.buttonArray[11].setText(msg.CONTINUE)


        self.buttonArray[0].clicked.connect( lambda: self.exAClick(1,self.buttonArray[0]))
        self.buttonArray[1].clicked.connect( lambda: self.exAClick(4,self.buttonArray[1]))
        self.buttonArray[2].clicked.connect( lambda: self.exAClick(7,self.buttonArray[2]))
        self.buttonArray[3].clicked.connect( lambda: self.clear('clear'))
        self.buttonArray[4].clicked.connect( lambda: self.exAClick(2,self.buttonArray[4]))
        self.buttonArray[5].clicked.connect( lambda: self.exAClick(5,self.buttonArray[5]))
        self.buttonArray[6].clicked.connect( lambda: self.exAClick(8,self.buttonArray[6]))
        self.buttonArray[7].clicked.connect( lambda: self.exAClick(0,self.buttonArray[7]))
        self.buttonArray[8].clicked.connect( lambda: self.exAClick(3,self.buttonArray[8]))
        self.buttonArray[9].clicked.connect( lambda: self.exAClick(6,self.buttonArray[9]))
        self.buttonArray[10].clicked.connect( lambda: self.exAClick(9,self.buttonArray[10]))
        self.buttonArray[11].clicked.connect( lambda: self.exAClickContinuou('Continue'))

        self.buttonArray[11].setEnabled(False)
        self.buttonArray[3].setEnabled(False)
        # self.buttonArray[3].setStyleSheet("background-color : pink; font-size: 14pt; " )
        # self.buttonArray[11].setStyleSheet("background-color : pink; font-size: 14pt; " )
        self.stats.startTimer()

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
        self.buttonArray[self.counter1].setStyleSheet("background-color : pink;font-size: 22pt; " )
        
        self.buttonArray[self.counter1].show()


        self.counter1=self.counter1+1
        self.state

        
    
        
    def button_released(self):
        sending_button = self.sender()
        self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))



    def exALoop(self):
        # print(self.state.current)
        if (self.sleep==-10):
            print(".", end="")
            return

        if (self.sleep>0):
            self.sleep=self.sleep-1
            return
        
        if (self.state.records==0):
            return;
        curState=self.state.getCurrentRecord()
        
        
        if (curState.UI=='drawUI'):
            self.drawUI()
        if (curState.UI=='draw1'):
            self.draw1(curState.number)

        self.msg=msg()
        self._ui.corbiLabel.setText(curState.label)   

        self.sleep=curState.pause
        self.state.changeState(self.stats.number)




    def exAClick(self,i,button):
        self.buttonArray[11].setEnabled(True)
        self.buttonArray[3].setEnabled(True)
        button.setEnabled(False)
        self.currentNumber=self._ui.corbiLabel.text()+str(i)
        self._ui.corbiLabel.setText(self._ui.corbiLabel.text()+str(i)) 
        curState=self.state.getCurrentRecord()
        curState.label=self.currentNumber

        return
       
    

    def hide(self):
        if (len(self.buttonArray)==0):
            return
        
        for b in self.buttonArray:
            b.setDisabled(True)
            b.hide()


    def exAClickContinuou(self,i):
        self.stats.stopTimer()
        newRow=row(self.stats.number,self.currentNumber,self.stats.number==self.currentNumber,self.stats.timePrint())
        self.rows.append(newRow)
        self.draw1Done=False
        self.hide()
        wrong=False
        if(self.stats.number==self.currentNumber):
            self.stats.wrong=0
            print (self.stats.number+' === '+self.currentNumber)
        else :
            wrong=True
            self.stats.wrong=self.stats.wrong+1
            if self.stats.wrong == 2:
                self.finishEx()

                


            print (str(self.stats.wrong)+' '+self.stats.number+' !== '+self.currentNumber)


        
        self.stats.number=''
        self.state.addChangeState(wrong,self.stats.wrong,self.stats.number)
        self.sleep=0
        
        self.currentNumber=''
        return
    def finishEx(self):
        self.showTable()
        self.stats.wrong=0
        # self.clearUI()    
        self.hide()

        self.state.restart()    
        self.exA.stop()           

        # self.state.current=self.state.current+1
        self.currentNumber=''
        self.stats.number=''

        spans=[]
        counter=0
        for i in self.rows:
            if(i.correctFlag):
                span=len(i.number)
                spans.append(span)    
            i.print(counter=counter+1)
            self.rowsTotal.append(i)
        
        if(len(spans)<2):
            self._ui.corbiLabel.setText('Tέλος\n\n Digital span 0')
        else:
            span=len(spans)//2
            self._ui.corbiLabel.setText('Tέλος\n\n Digital span '+str(span+1))

        
        self.rows=[]
        return
    def storedata(self):
        print('Store data!!')


    def clear(self,i):
        Str=self.currentNumber
        i=Str[len(Str)-1]
        if (i=='0'):
            button=self.buttonArray[7]
        elif(i=='1'):
            button=self.buttonArray[0]
        elif(i=='2'):
            button=self.buttonArray[4]
        elif(i=='3'):
            button=self.buttonArray[8]
        elif(i=='4'):
            button=self.buttonArray[1]
        elif(i=='5'):
            button=self.buttonArray[5]       
        elif(i=='6'):
            button=self.buttonArray[9]        
        elif(i=='7'):
            button=self.buttonArray[2]      
        elif(i=='8'):
            button=self.buttonArray[6]
        elif(i=='9'):
            button=self.buttonArray[10]
        
        button.setEnabled(True)


        Str = Str[:len(Str)-1]
        self.currentNumber=Str
        self._ui.corbiLabel.setText(Str)
        self.state.getCurrentRecord().label=Str   
        
        if (len(Str)==0):
            self.buttonArray[11].setEnabled(False)
            self.buttonArray[3].setEnabled(False)

        return
    
    def showTable(self):
        if (len(self.rows)>0):
            data=[]
            headers=[]
            for row in self.rows:
                data.append(row.getData())
                headers=row.getHeader()
        table = TableView(self._ui.widget,data,headers)