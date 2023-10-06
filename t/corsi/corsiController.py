from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtCore, QtWidgets

from time import sleep
import random

import random
from corsi.stats import stats
from corsi.row import row
from corsi.msgList import msg
from TableView import TableView

class corsi():

    def keyPressEvent(self, event):
        if(event.text()==chr(27)):
            self.finishEx()
        if (event.text()=='s' or event.text()==' ') and self.step=='A':
              self.initialize()
              self.step='B'


    def __init__(self, ui,timerUI):
        print(timerUI)
        self._ui=ui
        self.timerUI=timerUI
        self.counter=0
        self.maxCounter=3
        self.stats=stats()
        self.height=1200
        self.width=1600

        self.timer=300
        self.corbi=3
        self.countdown=3
        self.first=True
        self.msg=msg()
        self._ui.corbiLabel.setText(  self.msg.INSTRUNCTIONS)    
        self.currentRows=[]
        self.stepA=True

        self.step='A'
        self.counterPause=3


    
    def clearUI(self):
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
        self.first=True

    def drawUI(self):

        counter1=0
        self.buttonArray = [] 

        self.clearUI()
        self.first=False
        
        ratio=1600/self.width
        
        for i in self.positions:
                x=(400+i%6*100)/ratio
                y=(int(i/5)*100+100)/ratio
                self.buttonArray.append( QtWidgets.QPushButton(self._ui.widget) )
                self.buttonArray[counter1].setObjectName("pushButton"+str(counter1))
                self.buttonArray[counter1].clicked.connect( lambda: self.exAClick)
                self.buttonArray[counter1].setGeometry(QtCore.QRect(x,y, 80/ratio, 80/ratio))
                self.buttonArray[counter1].setStyleSheet("background-color : pink;" )
                
                self.buttonArray[counter1].show()
                counter1=counter1+1



        self._ui.button1=self.buttonArray[0]
        self._ui.button2=self.buttonArray[1]
        self._ui.button3=self.buttonArray[2]
        self._ui.button4=self.buttonArray[3]
        self._ui.button5=self.buttonArray[4]
        self._ui.button6=self.buttonArray[5]
        self._ui.button7=self.buttonArray[6]
        self._ui.button8=self.buttonArray[7]
        self._ui.button9=self.buttonArray[8]

        
    def button_released(self):
        sending_button = self.sender()
        self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))


    def exALoop(self):
        self.buttonArray = [] 
        self.drawUI()
        if (self.state=='yellow' and self.counterPause>0):
             self.counterPause=self.counterPause-1
             return
        if(self.counter==self.currentRow.currentCorsi):
            self.exA.stop()
            self.state='Answer'

            self.buttonArray[0].clicked.connect( lambda: self.exAClick(0))
            self.buttonArray[1].clicked.connect( lambda: self.exAClick(1))
            self.buttonArray[2].clicked.connect( lambda: self.exAClick(2))
            self.buttonArray[3].clicked.connect( lambda: self.exAClick(3))
            self.buttonArray[4].clicked.connect( lambda: self.exAClick(4))
            self.buttonArray[5].clicked.connect( lambda: self.exAClick(5))
            self.buttonArray[6].clicked.connect( lambda: self.exAClick(6))
            self.buttonArray[7].clicked.connect( lambda: self.exAClick(7))
            self.buttonArray[8].clicked.connect( lambda: self.exAClick(8))
            self._ui.corbiLabel.setText(self.msg.INSTRUNCTIONS2)
            self.stats.startTimer()
            self.counterTimeout=6
            self.exC.start(1000)
            
        else:
            self.state='yellow'
            self.counterPause=3
            if (self.stepA):
                self.stepA=False
                i=round(random.randint(0,8))
                while  i  in self.currentRow.ids:
                    i=round(random.randint(0,8))
                self.currentRow.ids.append(i)
                for ii in self.buttonArray:
                        ii.setStyleSheet("background-color : pink;" )
                self.buttonArray[i].setStyleSheet("background-color : yellow;")
                self.counter=self.counter+1
            else:
                self.stepA=True
                for ii in self.buttonArray:
                        ii.setStyleSheet("background-color : pink;" )


    def initialize(self):
        a=row()
        self.start(a)
        self.errorCurrent=0;
        self.totalError=0

    def start(self,r_o_w: row):
        self.countdown=2
        self.counter=0
        self.state='Read'

        self.currentRow=r_o_w
        self.exA = QtCore.QTimer(self.timerUI)
        self.exA.stop()

        self.exB = QtCore.QTimer(self.timerUI)
        self.exB.stop()

        self.exB.start(self.currentRow.timer1sec)
        self.positions=[]


        self.exC = QtCore.QTimer(self.timerUI)
        self.exC.stop()

        while len(self.positions) <9:   
            i=round(random.randint(0,29))
            while  i  in self.positions:
                i=round(random.randint(0,29))
            self.positions.append(i)


        self.exA.timeout.connect(self.exALoop)
        self.exB.timeout.connect(self.countdownA)

    def timeout(self):
        if (self.counterTimeout>0):
            self.counterTimeout=self.counterTimeout-1
            return
        print('Return')
        self.exAClick(-1)
        self.exC.stop()

    def countdownA(self):
        if (self.countdown>3):
            self.countdown=self.countdown-1
            return

        if (self.countdown==-1):
            self.exB.stop()
            self.exA.start(self.currentRow.timer)
            return
                  
        self._ui.corbiLabel.setText(self.msg.countDown(str(self.currentRow.currentCorsi),str(self.countdown)))
        self.countdown=self.countdown-1

    def exAClick(self,i):
        self.buttonArray[i].setStyleSheet("background-color : blue;")
        if self.state=='Answer':
            self.currentRow.idsAnswer.append(i)
            x=len(self.currentRow.idsAnswer)
            if (self.currentRow.ids[x-1]!=i):
                self.exC.stop()
               
                self.counterPause=5
                self._ui.corbiLabel.setText(self.msg.WRONG)
                if (i==-1):
                     self._ui.corbiLabel.setText(self.msg.TIMEOUT)
                timer=self.stats.stopTimer()
                self.currentRow.time2Answer=timer
                self.clearUI()
                self.currentRow.success=False
                self.currentRows.append(self.currentRow)
                
                a=row()
                a.timer=self.timer*2
                self.timer=a.timer
                a.currentCorsi=self.corbi
                self.errorCurrent=self.errorCurrent+1;
                self.totalError=self.totalError+1;
                if self.errorCurrent==2 or self.totalError==3:
                    self.finishEx()
                    return
                self.start(a)   
                return



            if(x==len(self.currentRow.ids)):
                    self.exC.stop()
                    self.errorCurrent=0;
                   
                    timer=self.stats.stopTimer()
                    self.currentRow.time2Answer=timer

                    self.clearUI()
                    a=row()
                    a.currentCorsi=self.corbi+1
                    self.corbi=self.corbi+1
                    self.currentRow.success=False
                    self.currentRows.append(self.currentRow)
                    self._ui.corbiLabel.setText(  self.msg.CORRECT)     

                    self.start(a)   

    def finishEx(self):
        self.showTable()
        self.exA.stop()

        self.exB.stop()

        self.exC.stop()
        s=0
        counter=0
        maxCorsi=0

        for i in self.currentRows:
            counter=counter+1
            i.print(counter)
            s=s+i.time2Answer
            len1=i.getLenght()
            if (len1>maxCorsi):
                    maxCorsi=len1
    
        if (self.currentRows==0):
            s=round(s/len(self.currentRows),2)
        else:
            s=0
            
        print('Mean time = '+str(s))
        self.step='A'

        self.timer=300
        self.corbi=3
        self.countdown=3
        self.first=True
        self.msg=msg()
        self.currentRows=[]
        self.stepA=True



        self._ui.corbiLabel.setText(self.msg.finishedMsg(s,maxCorsi))

        self.clearUI()

    def showTable(self):
        if (len(self.currentRows)>0):
            data=[]
            headers=[]
            for row in self.currentRows:
                data.append(row.getData())
                headers=row.getHeader()
        table = TableView(self._ui.widget,data,headers)