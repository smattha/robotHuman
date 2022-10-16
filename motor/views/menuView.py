from xxlimited import Str
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QTableWidgetItem
# from views.ui.menu import Ui_menuWindow
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import ( QMainWindow)
# from views.DisplayImage import DisplayImageWidget
# from views.page1View import page1View
# from views.page2View import page2View
from views.motor import Ui_MainWindow;
from threading import Thread
import time




import json
from turtle import position
from PyQt5.QtCore import QObject, pyqtSignal
from sqlalchemy import true
import json
from collections import namedtuple
from os.path import exists
from sqlalchemy import Column, String, Integer
from sqlalchemy import Column, String, Integer

from views.base import Base
# from base import Session, engine, Base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
from threading import Thread

from views.database.pointsClass import pointsClass
# from views.base import base

class MenuView(QMainWindow):
    def __init__(self,motor):
        super().__init__()

        self.path='/home/stergios/git/src/robotHuman/user_interface'
        engine = create_engine('sqlite:///' + self.path + '/database/scheme/mysqlList.db')
        Session = sessionmaker(bind=engine)
        # con = engine.connect()
        # rs = con.execute("SELECT * FROM points t where t.id=1")

        session = Session()

        rs=session.query(pointsClass).filter(pointsClass.id>1).all()
        
        print (rs.pop().motorA)

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.counter=0
        self.motor=motor
        self._ui.movingStep.setText(str(20))


        self.startUpdateThread()
   

        self._ui.minusA.clicked.connect( lambda: self.moveMotor(-1,self.motor.leftHand) )
        self._ui.plusA.clicked.connect( lambda: self.moveMotor(1,self.motor.leftHand) )

        self._ui.minusB.clicked.connect( lambda: self.moveMotor(-1,self.motor.rightHand) )
        self._ui.plusB.clicked.connect( lambda: self.moveMotor(1,self.motor.rightHand) )

        self._ui.minusD.clicked.connect( lambda: self.moveMotor(-1,self.motor.leftShoulder) )
        self._ui.plusD.clicked.connect( lambda: self.moveMotor(1,self.motor.leftShoulder) )

        self._ui.minusE.clicked.connect( lambda: self.moveMotor(-1,self.motor.torso) )
        self._ui.plusE.clicked.connect( lambda: self.moveMotor(1,self.motor.torso) )

        self._ui.minusF.clicked.connect( lambda: self.moveMotor(-1,self.motor.head) )
        self._ui.plusF.clicked.connect( lambda: self.moveMotor(1,self.motor.head) )


        self._ui.minusC.clicked.connect( lambda: self.moveMotor(-1,self.motor.rightShoulder) )
        self._ui.plusC.clicked.connect( lambda: self.moveMotor(1,self.motor.rightShoulder) )


        self._ui.moveButton.clicked.connect( lambda: self.moveMotorToPos() )

        self._ui.sync.clicked.connect( lambda: self.syncPosWithTarget() )
        
        self._ui.recordButton.clicked.connect(self.record)
        self.syncPosWithTarget()

        self._ui.tableWidget.cellClicked.connect(self.updateUiCellClick)



    def storePoints(self, newResult):

        self.path='/home/stergios/git/src/robotHuman/user_interface'
        engine = create_engine('sqlite:///' + self.path + '/database/scheme/mysqlList.db')
        Session = sessionmaker(bind=engine)

        self.session = Session()

        # 9 - persists data
        self.session.add(newResult)


        # 10 - commit and close session
        self.session.commit()

        # self.result.listResults=self.session.query(resultOfPerson).all()


        self.session.close()

        # self.result.listResults.append(listTemp)

        showAnswerButtons = pyqtSignal(str, name='showAnswerButtons')

    def updateUiCellClick(self, row, cell):
        print()

        self._ui.targetPosA.setText(str(self._ui.tableWidget.item(row,0).text()))
        self._ui.targetPosB.setText(str(self._ui.tableWidget.item(row,1).text()))
        self._ui.targetPosC.setText(str(self._ui.tableWidget.item(row,2).text()))
        self._ui.targetPosD.setText(str(self._ui.tableWidget.item(row,3).text()))
        self._ui.targetPosE.setText(str(self._ui.tableWidget.item(row,4).text()))
        self._ui.targetPosF.setText(str(self._ui.tableWidget.item(row,5).text()))

    def moveMotor(self, mult,id):
        value=int(mult )*int(self._ui.movingStep.text())
        print('Move motor'+ str(id)+ 'value' +str(value))
        self.motor.move(id,value)


    def setGoal(self, value,id):
        print('\t\t\t\tActivate Widget',value)
        # self.updatePos()   

    def startUpdateThread(self):
        thread = Thread(target=self.updatePosThread, args=(), daemon=True)
        thread.start()
        print("Thread started")

    


    def record(self):
        
        self._ui.tableWidget.setRowCount(self.counter+1)
        
        # print(r)

        self._ui.tableWidget.setItem(self.counter, 0, QTableWidgetItem(str(self.motor.getPosition(self.motor.leftHand))))
        self._ui.tableWidget.setItem(self.counter, 1, QTableWidgetItem(str(self.motor.getPosition(self.motor.rightHand))))
        self._ui.tableWidget.setItem(self.counter, 2, QTableWidgetItem(str(self.motor.getPosition(self.motor.rightShoulder))))
        self._ui.tableWidget.setItem(self.counter, 3, QTableWidgetItem(str(self.motor.getPosition(self.motor.leftShoulder))))
        self._ui.tableWidget.setItem(self.counter, 4, QTableWidgetItem(str(self.motor.getPosition(self.motor.torso))))
        self._ui.tableWidget.setItem(self.counter, 5, QTableWidgetItem(str(self.motor.getPosition(self.motor.head))))

        res=pointsClass()
        res.motorA=str(self.motor.getPosition(self.motor.leftHand))
        res.motorB=str(self.motor.getPosition(self.motor.rightHand))
        res.motorC=str(self.motor.getPosition(self.motor.rightShoulder))
        res.motorD=str(self.motor.getPosition(self.motor.leftShoulder))
        res.motorE=str(self.motor.getPosition(self.motor.torso))
        res.motorF=str(self.motor.getPosition(self.motor.head))
        self.storePoints(res)

        self.resultTemp=self.session.query(pointsClass).all()



        self.counter=self.counter+1;
        

    def updatePosThread(self):
        while 1==1:
            self.updatePos()
            time.sleep(0.1)

    def updatePos(self):
            self._ui.motorAPosition.setText(str(self.motor.getPosition(self.motor.leftHand)))
            self._ui.motorBPosition.setText(str(self.motor.getPosition(self.motor.rightHand)))
            self._ui.motorCPosition.setText(str(self.motor.getPosition(self.motor.rightShoulder)))
            self._ui.motorDPosition.setText(str(self.motor.getPosition(self.motor.leftShoulder)))
            self._ui.motorEPosition.setText(str(self.motor.getPosition(self.motor.torso)))
            self._ui.motorFPosition.setText(str(self.motor.getPosition(self.motor.head)))

    def syncPosWithTarget(self):
            self._ui.targetPosA.setText(str(self.motor.getPosition(self.motor.leftHand)))
            self._ui.targetPosB.setText(str(self.motor.getPosition(self.motor.rightHand)))
            self._ui.targetPosC.setText(str(self.motor.getPosition(self.motor.rightShoulder)))
            self._ui.targetPosD.setText(str(self.motor.getPosition(self.motor.leftShoulder)))
            self._ui.targetPosE.setText(str(self.motor.getPosition(self.motor.torso)))
            self._ui.targetPosF.setText(str(self.motor.getPosition(self.motor.head)))

    def moveMotorToPos(self):
            self.motor.moveAbs(int(self._ui.targetPosA.text()),self.motor.leftHand)
            self.motor.moveAbs(int(self._ui.targetPosB.text()),self.motor.rightHand)
            self.motor.moveAbs(int(self._ui.targetPosC.text()),self.motor.rightShoulder)
            self.motor.moveAbs(int(self._ui.targetPosD.text()),self.motor.leftShoulder)
            self.motor.moveAbs(int(self._ui.targetPosE.text()),self.motor.torso)
            self.motor.moveAbs(int(self._ui.targetPosF.text()),self.motor.head)
           
  