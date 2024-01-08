from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import ( QMainWindow)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 


from threading import Thread
from time import sleep

from utilities.stats import stats
from exercises.exersiceDigitSpan.row import row
from exercises.exersiceDigitSpan.state import state
from utilities.TableView import TableView
from Text.DIGITAL_SPAN_MSG import DIGITAL_SPAN_MSG
import re

class DigitSpanController():


    def keyPressEvent(self, event):
        if (self._ui.ros.isTalking):
            return
        if(event.text()==chr(27)):
            self.finishEx()
        if (self.stateVariable=='end' and  event.text()==' '):
            self.stateVariable='start'
            self.init(self._ui,self.timerUI)
            try:
                self.table.table1.hide()
            except:
                print("An exception occurred")
    
        if (event.text()=='s' or event.text()==' '):
            if (self.sleep==-10):
                self.sleep=0

    def __init__(self, ui,timerUI):
        self.init(ui,timerUI)
        self.stateVariable='start'
        self.msg= DIGITAL_SPAN_MSG()
        self.pattern = re.compile('<.*?>')

    def init(self,ui,timerUI):
        self._ui=ui
        self.timerUI=timerUI

        self.stats=stats()
        self.height=self.timerUI.height()
        self.width=self.timerUI.width()
        self._ui.corbiLabel.setStyleSheet("font-size: 24pt; color : blue; " )
        self.buttonsExist=False
 
        self.rows=[]
        self.rowsTotal=[]
        self.stepA=True
        # self.drawUI()
        self.exA = QtCore.QTimer()
        self.exA.timeout.connect(self.exALoop)
        self.exA.start(int(100/3))
        self.sleep=00;
        self.state=state()
        self.currentNumber=''
        self.draw1Done=False

        self._ui.corbiLabel.setGeometry(QtCore.QRect( 0, int(10), int( self.width), int(900)))

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
                    x=(250+i*220)/ratio
                    y=(int(j)*120+150)/ratio
                    button1= QtWidgets.QPushButton(self._ui.widget)
                    button1.setText(str(3*j+i))
                    self.buttonArray.append( button1)
                    self.buttonArray[self.counter1].setObjectName("pushButton"+str(self.counter1))
                    self.buttonArray[self.counter1].clicked.connect( lambda: self.exAClick)
                    self.buttonArray[self.counter1].setGeometry(QtCore.QRect(int(x),int(y), int(200/ratio), int(100/ratio)))
                    self.buttonArray[self.counter1].setStyleSheet("background-color : pink; font-size: 34pt; " )

                    fontId = QFontDatabase.addApplicationFont("fonts/Mansalva.ttf")
                    if fontId < 0:
                        print('font not loaded')
                    else :
                        families = QtGui.QFontDatabase.applicationFontFamilies(fontId)
                        font = QtGui.QFont(families[0])
                        self.buttonArray[self.counter1].setFont(font)
          
                    
                    self.buttonArray[self.counter1].show()
                    self.counter1=self.counter1+1


        x=(250+1*220)/ratio
        y=(int(5)*100+150)/ratio
        
        self.buttonArray[3].setText(self.msg.CLEAR)
        self.buttonArray[3].setGeometry(QtCore.QRect(int(x),int(y), int(200/ratio+80), int(120/ratio)))
        self.buttonArray[3].setStyleSheet("background-color : pink; font-size: 22pt; " )
        
        self.buttonArray[7].setText('0')

        x=(250+3*220)/ratio
        y=(int(5)*100+150)/ratio
        self.buttonArray[11].setGeometry(QtCore.QRect(int(x-80),int(y), int(200/ratio+80), int(120/ratio)))
        self.buttonArray[11].setText(self.msg.CONTINUE)
        self.buttonArray[11].setStyleSheet("background-color : pink; font-size: 22pt; " )

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
        self.buttonArray[self.counter1].setGeometry(QtCore.QRect(int(x-40),int(y-40), int(160/ratio), int(160/ratio)))
        self.buttonArray[self.counter1].setStyleSheet("background-color : pink;font-size: 34pt; " )        
        self.buttonArray[self.counter1].show()
        self.counter1=self.counter1+1
            
    def button_released(self):
        sending_button = self.sender()
        self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))

    def exALoop(self):
        if (self._ui.ros.isTalking):
            return
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
        if (curState.UI=='back'):
            pixmap = QPixmap(curState.label)
            self._ui.label.setPixmap(pixmap)
            self._ui.label.setScaledContents( True );
            self._ui.label.show()
        if (curState.UI=='backhide'):
            self._ui.label.hide()

        self.msg= DIGITAL_SPAN_MSG()
        self._ui.corbiLabel.setText(curState.label)   
        if(curState.ros!=''):
            self._ui.ros.startUpdateThread(re.sub(self.pattern, '',curState.ros))
        self._ui.corbiLabel.setStyleSheet("font-size: 24pt; color : "+curState.color )

        self.sleep=curState.pause
        self.state.changeState(self.stats.number)


    def exAClick(self,i,button):
        self.buttonArray[11].setEnabled(True)
        self.buttonArray[3].setEnabled(True)
        button.setEnabled(False)
        self.currentNumber=self._ui.corbiLabel.text()+str(i)
        self._ui.corbiLabel.setText(self._ui.corbiLabel.text()+str(i)) 
        self._ui.corbiLabel.setStyleSheet("font-size: 24pt; color : red; " )
        curState=self.state.getCurrentRecord()
        curState.label=self.currentNumber
        curState.color='red'
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
        self.stateVariable='end'
        self.showTable()
        self.stats.wrong=0
        self.hide()

        self.state.restart()    
        self.exA.stop()           

        self.currentNumber=''
        self.stats.number=''

        spans=[]
        counter=0
        meanTimer=0
        for i in self.rows:
            meanTimer=meanTimer+i.timePrint
            if(i.correctFlag):
                span=len(i.number)
                spans.append(span)    
            i.print(counter=counter+1)
            self.rowsTotal.append(i)
        
        if (len(self.rows)>0):
            meanTimer=meanTimer/len(self.rows)

        if(len(spans)<2):
            self._ui.corbiLabel.setText(self.msg.ZERO_CORRECT_DATA)
        else:
            span=len(spans)//2+1
            self._ui.corbiLabel.setText(self.msg.finishedMsg(meanTimer,span) )

        
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
        if (len(self.rows)):
            self.table = TableView(self._ui.widget,data,headers,'digitalSpan')