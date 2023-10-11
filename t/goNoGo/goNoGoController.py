
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QLabel 

     
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from time import sleep
import random
import time

from goNoGo.stats import stats
from goNoGo.row import row
from goNoGo.state import state
import datetime
from TableView import TableView

class goNoGoController():

    def keyPressEvent(self, event):
        if(event.text()==chr(27)):
            self.counterTotal=self.maxCounter
        if (self.stateVariable=='end' and  event.text()==' '):
            print('---')
            self.stateVariable='start'
            self.init()
            self.table.table1.hide()
            self.step='instruction'           
            self.labelInstStart.show()
            self.labelInstStop.show()
            self._ui.label.hide()
            return
        if (event.text()=='s' or event.text()==' ') and (self.step=='instruction'):
            self.step='color'
            pixmap = QPixmap('img/back.png')
            self._ui.label.setPixmap(pixmap)
            self._ui.label.setScaledContents( True );
            self._ui.label.show()
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
        self.stateVariable ='start'     
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
        ratio=1600/self.width
        

        x=self.timerUI.width()*0.6
        y=(self.timerUI.height()*0.5)
        x1=(self.timerUI.width()-x+100)/2
        y1=(self.timerUI.height()-y)/2+200

        self.button1= QtWidgets.QPushButton(self._ui.widget)
        self.button1.setObjectName("pushButton"+str(1))
        self.button1.setGeometry(QtCore.QRect(x1,y1, x,y))


        self.button1.hide()
        self.button1.setDisabled(True)
        self.rows=[]

        self.tick=time.time()
        
        self._ui.corbiLabel.setText('<h1>Go/No-go task</h1> <br>\
                                     Σε αυτό το παιχνίδι εμφανίζονται διαδοχικά δυο εικόνες.<br> \
 Πάτα το space όταν εμφανίζετε η εικόνα αριστερά.<br> \
 Μη κάνεις τίποτα όταν το εμφανίζετε η εικόνα δεξιά.\
                                        Πάτα το space  για να ξεκινήσουμε!<br>\
    Αν θέλεις να τερματίσεις το παιχνίδι πάτα το ESC') 
        
        self._ui.widget.setGeometry(QtCore.QRect(0, 0,self.timerUI.width() , self.timerUI.height()))
        self._ui.corbiLabel.setGeometry(QtCore.QRect(0, 0,self.timerUI.width() , 1200))

        self.correctCounter=0
        self.falseCounter=0
        self.displayImg1()
        self.displayImgInstr(x1,y1,x/2,y/2)

        self.maxCounter=200*self.sleepFactor
        
        # table=TableView()
        # self.showTable()

    def displayImgInstr(self,x,y,w,h):
        self.labelInstStart = QLabel(self._ui.widget)
        pixmap = QPixmap("start.png")
        self.labelInstStart.setPixmap(pixmap)
        self.labelInstStart.setGeometry(x,y,w,h)
        self.labelInstStart.setScaledContents( True );


        self.labelInstStop = QLabel(self._ui.widget)
        pixmap = QPixmap("stop.png")
        self.labelInstStop.setPixmap(pixmap)
        self.labelInstStop.setGeometry(x+1.1*w,y,w,h)
        self.labelInstStop.setScaledContents( True );

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
        self._ui.corbiLabel.setGeometry(QtCore.QRect(0, 0,self.timerUI.width() , 1200))

        color='green'
        if i<self.calculatePerc(): 
            color='red'
        
        self.row.greenGo=color

        self.counter1=0
        self.buttonArray = [] 
        self.buttonsExist=True
        
        width=self.timerUI.width()*0.5
        height=(self.timerUI.height()*0.5)

        xPos=(self.timerUI.width()-width)/2
        yPos=(self.timerUI.height()-height)/2

        if color=='green':
            self.button1.hide()
            self.button1.setDisabled(True)
            
            self.button1.setStyleSheet("background-color : green ;font-size: 22pt; " )
            pixmap = QPixmap("start.png")
            self.label.setPixmap(pixmap)
            self.label.setGeometry(xPos,yPos,width,height)
            self.label.show()
          
        else :
            self.button1.hide()           
            self.button1.setDisabled(True)
            pixmap = QPixmap("stop.png")
            self.label.setPixmap(pixmap)            
            self.label.setGeometry(xPos,yPos,width,height)
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


    def showTable(self):
        self.stateVariable='end'
        if (len(self.rows)>0):
            data=[]
            headers=[]
            for row in self.rows:
                data.append(row.getData())
                headers=row.getHeader()
            self.table = TableView(self._ui.widget,data,headers)
        # table.show()
        
    def exALoop(self):

        if (self.counterTotal>=self.maxCounter):
            self.table1=self.showTable()

            for i in self.rows:
                i.print()
            self.exA.stop()
            self.button1.hide()
            self.label.hide()

            str(self.correctCounter)+'/'+str(self.falseCounter)
            self._ui.corbiLabel.setText('<h1> Τέλος </h1>\
                                         Απάντησες σωστά σε '+str(self.correctCounter)+' σε συνολικά '+str(self.correctCounter+self.falseCounter)\
                                                                                                           +".<br>Πάτα το space  για να ξεκινήσουμε από την αρχή!") 
            
            pixmap = QPixmap('img/happy.png')
            self._ui.label.setPixmap(pixmap)
            self._ui.label.setScaledContents( True );
            return

        if (self.step!='instruction'):
            self.counterTotal=self.counterTotal+1 
            self.tock=time.time()
            self.labelInstStart.hide()
            self.labelInstStop.hide()

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
                self._ui.corbiLabel.setText('<h1>Λάθος απάντηση</h1>') 
                self.sleep=10*self.sleepFactor
                self.falseCounter=self.falseCounter+1

            self.step='interval'
            self.rows.append(self.row)

            return

        if (self.step=='interval'):
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
                self._ui.corbiLabel.setText('<h1>Λάθος απάντηση</h1>') 
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
    
    