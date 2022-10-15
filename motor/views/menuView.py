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


        value='1'
        self.startUpdateThread()


        # self._ui.listOfPoints.addItems(entries)

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
        # self.startUpdateThread()  


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
        value=mult *int(self._ui.movingStep.text())
        print('\t\t\t\tActivate Widget',value)
        self.motor.move(id,value)
        # time.sleep(1.2)
        # self.updatePos()

    def setGoal(self, value,id):
        print('\t\t\t\tActivate Widget',value)
        # self.updatePos()   

    def startUpdateThread(self):
        thread = Thread(target=self.updatePosThread, args=(), daemon=True)
        thread.start()
        print("Thread finished...exiting")

    


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
            time.sleep(10)

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
           
        # self._ui.goalA.textChanged.connect(self.setGoal(1))
        
    #     self._ui.pushButtonResultsNext.clicked.connect( lambda: self.loadResultsByIDCounter(1) )

    #     self._ui.pushButtoResultPrevius.clicked.connect( lambda: self.loadResultsByIDCounter(-1) )


   


    #     #Exersice 1
    #     self._ui.selectExercise.currentIndexChanged.connect(lambda:  self._main_controller.selectButtonClicked(self._ui.selectExercise.currentIndex()) )        
        

    #     self._ui.go2Home.clicked.connect(lambda: self._main_controller.go2Home1())
    #     self._ui.nextExersice.clicked.connect(lambda: self._main_controller.move2NextPage())


    #     self._ui.terminateButton.clicked.connect(lambda: self._main_controller.go2Home(  self._ui.name.text(),self._ui.surname.text(),self._ui.ageTextBox.text() ) )
    #     self._ui.feedbackEasyButton.clicked.connect(lambda: self._main_controller.feedback('1'))
    #     self._ui.feedbackNormalButton.clicked.connect(lambda: self._main_controller.feedback('2'))
    #     self._ui.feedbackHardButton.clicked.connect(lambda: self._main_controller.feedback('3'))



    #     #################################################################################################xml
    #     # # listen for model event signals
    #     self._model.changeDscrSingal.connect(self.changeDscrChanged)
    #     self._model.resetFieldSingal.connect(self.resetField)
    #     self._model.moveMotorSignal.connect(self.moveMotor)

    #     self._model.showButtons.connect(self.showButtons)

    #     #Feedback
    #     self._model.feedbackShowButton.connect(self.feedbackShowButton)

    #     self._ui.pushButtonHome.clicked.connect( lambda: self.moveMotor(0) )


    # @pyqtSlot(str)
    # def changeDscrChanged(self, value):
    #     print('Set Text ',value)
    #     self._ui.descriptionTxt.setText(value)


    # @pyqtSlot(str)
    # def resetField(self, value):
    #     print('Empty field ',value)
    #     self._ui.name.setText('')
    #     self._ui.ageTextBox.setText('')
    #     self._ui.surname.setText('')

    # @pyqtSlot(int)

        # if value==1:
        #     j=self._ui.stackedWidget.count()
        #     self.page1=page1View(self._model,self._main_controller._exercisesController[0])
        #     self._ui.stackedWidget.addWidget(self.page1)
        #     self._ui.stackedWidget.setCurrentIndex(j)
        
    #     elif value==2:
    #         j=self._ui.stackedWidget.count()
    #         self.page2=page1View(self._model,self._main_controller._exercisesController[1])
    #         self._ui.stackedWidget.addWidget(self.page2)
    #         self._ui.stackedWidget.setCurrentIndex(j)
        
    #     elif value==3:
    #         j=self._ui.stackedWidget.count()
    #         self.page3=page2View(self._model,self._main_controller._exercisesController[2])
    #         self._ui.stackedWidget.addWidget(self.page3._ui.stackedWidget)
    #         self._ui.stackedWidget.setCurrentIndex(j)
        
    #     elif value==4:
    #         j=self._ui.stackedWidget.count()
    #         self.page4=page2View(self._model,self._main_controller._exercisesController[3])
    #         self._ui.stackedWidget.addWidget(self.page4._ui.stackedWidget)
    #         self._ui.stackedWidget.setCurrentIndex(j)

    #     elif value==5:
    #         j=self._ui.stackedWidget.count()
    #         self._ui.stackedWidget.setCurrentIndex(15)    
    #         self.test3=page1View(self._model,self._main_controller._exercisesController[4])
    #         self._ui.stackedWidget.addWidget(self.test3._ui.widget)
    #         self._ui.stackedWidget.setCurrentIndex(j)        

    #         j=self._ui.stackedWidget.count()
    #         self._main_controller._exercisesController[4]._image2 = j+100
    #         self.test=(DisplayImageWidget(self._main_controller._exercisesController[4]._imagePath,self._model.displayImageRatio))
    #         self.test.setController(self._main_controller._exercisesController[4])
    #         self._ui.stackedWidget.addWidget(self.test)

    #     elif value==6:
    #         j=self._ui.stackedWidget.count()
    #         self.test4=page2View(self._model,self._main_controller._exercisesController[5])
    #         self.test4.answer51.show()
    #         self._ui.stackedWidget.addWidget(self.test4._ui.widget)
    #         self._ui.stackedWidget.setCurrentIndex(j)
    #         self._ui.stackedWidget.setCurrentIndex(0)
    #         self._ui.stackedWidget.setCurrentIndex(j)
            


    #     elif value==7:
    #         j=self._ui.stackedWidget.count()
    #         self.page7=page1View(self._model,self._main_controller._exercisesController[6])
    #         self._ui.stackedWidget.addWidget(self.page7)
    #         self._ui.stackedWidget.setCurrentIndex(j)

    #     elif value==8:
    #         j=self._ui.stackedWidget.count()
    #         self.page8=page1View(self._model,self._main_controller._exercisesController[7])
    #         self._ui.stackedWidget.addWidget(self.page8)
    #         self._ui.stackedWidget.setCurrentIndex(j)

    #     elif value==9:
    #         j=self._ui.stackedWidget.count()
    #         self.page9=page2View(self._model,self._main_controller._exercisesController[8])
    #         self._ui.stackedWidget.addWidget(self.page9._ui.stackedWidget)
    #         self._ui.stackedWidget.setCurrentIndex(j)

    #     elif value==10:
    #         j=self._ui.stackedWidget.count()
    #         self.page10=page2View(self._model,self._main_controller._exercisesController[9])
    #         self._ui.stackedWidget.addWidget(self.page10._ui.stackedWidget)
    #         self._ui.stackedWidget.setCurrentIndex(j)

    #     elif value==11:
    #         j=self._ui.stackedWidget.count()
    #         self._ui.stackedWidget.setCurrentIndex(15)    
    #         self.test11=page1View(self._model,self._main_controller._exercisesController[10])
    #         self._ui.stackedWidget.addWidget(self.test11._ui.widget)

    #         self._ui.stackedWidget.setCurrentIndex(j)        
    #         j=self._ui.stackedWidget.count()
    #         self._main_controller._exercisesController[10]._image2 = j+100
    #         self.test10B=(DisplayImageWidget(self._main_controller._exercisesController[10]._imagePath,self._model.displayImageRatio))
    #         self.test10B.setController(self._main_controller._exercisesController[10])
    #         self._ui.stackedWidget.addWidget(self.test10B)


    #     elif value==12:
    #         j=self._ui.stackedWidget.count()
    #         self.test12=page2View(self._model,self._main_controller._exercisesController[11])
    #         self._ui.stackedWidget.addWidget(self.test12._ui.widget)
    #         self.test12.answer51.show()
    #         self._ui.stackedWidget.setCurrentIndex(j)
    #         self._ui.stackedWidget.setCurrentIndex(0)
    #         self._ui.stackedWidget.setCurrentIndex(j)

    #     else:
    #         if value>100:
    #             value=value-100
    #         self._ui.stackedWidget.setCurrentIndex(value)
    #         if value==3:
    #             self._ui.pushButtoResultPrevius.hide()
    #             self.loadResultsByID(0)
    #         if value==1:
    #             self.hideButtons()


    # @pyqtSlot(str)
    # def feedbackShowButton(self,value):   
    #     if value=='show':
    #         self._ui.terminateButton.setDisabled(False)
    #         self._ui.nextExersice.setDisabled(False)
    #         self._ui.feedbackEasyButton.setDisabled(True)
    #         self._ui.feedbackNormalButton.setDisabled(True)
    #         self._ui.feedbackHardButton.setDisabled(True)
    #     else:
    #         self._ui.terminateButton.setDisabled(True)
    #         self._ui.nextExersice.setDisabled(True)
            
    #         self._ui.feedbackEasyButton.setDisabled(False)
    #         self._ui.feedbackNormalButton.setDisabled(False)
    #         self._ui.feedbackHardButton.setDisabled(False)

    # @pyqtSlot(str)
    # def nextPageSignalEx6(self, value):
    #     print("Image 6")
    #     self.test6.openImage(value)
    #     self.test6.resize()     



    # def hideButtons(self):
    #     self._ui.feedbackEasyButton.setDisabled(True)
    #     self._ui.feedbackNormalButton.setDisabled(True)
    #     self._ui.feedbackHardButton.setDisabled(True)
    #     self._ui.terminateButton.setDisabled(True)
    #     self._ui.nextExersice.setDisabled(True)
     

    # def showButtons(self,str):
    #     # time.sleep(self._model.sleepForAnswer)
    #     self._ui.feedbackEasyButton.setDisabled(False)
    #     self._ui.feedbackNormalButton.setDisabled(False)
    #     self._ui.feedbackHardButton.setDisabled(False)

    # def loadResults(self,results):
    #     # time.sleep(5)
    #     self._ui.checkBox.setChecked(False)
    #     self._ui.checkBox2.setChecked(False)
    #     self._ui.checkBox3.setChecked(False)
    #     self._ui.checkBox4.setChecked(False)
    #     self._ui.checkBox5.setChecked(False)
    #     self._ui.checkBox6.setChecked(False)
    #     self._ui.checkBox7.setChecked(False)
    #     self._ui.checkBox8.setChecked(False)
    #     self._ui.checkBox9.setChecked(False)
    #     self._ui.checkBox10.setChecked(False)
    #     self._ui.checkBox11.setChecked(False)
    #     self._ui.checkBox12.setChecked(False)
    #     self._ui.checkBox13.setChecked(False)
    #     self._ui.checkBox14.setChecked(False)
    #     self._ui.checkBox15.setChecked(False)
    #     self._ui.checkBox16.setChecked(False)
    #     self._ui.checkBox17.setChecked(False)
    #     self._ui.checkBox18.setChecked(False)
    #     self._ui.checkBox19.setChecked(False)
    #     self._ui.checkBox20.setChecked(False)
    #     self._ui.checkBox21.setChecked(False)
    #     self._ui.checkBox22.setChecked(False)
    #     self._ui.checkBox23.setChecked(False)
    #     self._ui.checkBox24.setChecked(False)
    #     self._ui.checkBox25.setChecked(False)
    #     self._ui.checkBox26.setChecked(False)
    #     self._ui.checkBox27.setChecked(False)
    #     self._ui.checkBox28.setChecked(False)
    #     self._ui.checkBox29.setChecked(False)
    #     self._ui.checkBox30.setChecked(False)
    #     self._ui.checkBox31.setChecked(False)
    #     self._ui.checkBox32.setChecked(False)
    #     self._ui.checkBox33.setChecked(False)
    #     self._ui.checkBox34.setChecked(False)
    #     self._ui.checkBox35.setChecked(False)
    #     self._ui.checkBox36.setChecked(False)

    #     self._ui.lineResultsEx1.setText(results.answerEx1)
    #     self._ui.lineResultsEx2.setText(results.answerEx2)
    #     self._ui.lineResultsEx3.setText(results.answerEx3)
    #     self._ui.lineResultsEx4.setText(results.answerEx4)
    #     self._ui.lineResultsEx5.setText(results.answerEx5A)
    #     self._ui.lineResultsEx6.setText(results.answerEx6A)
    #     self._ui.lineResultsEx7.setText(results.answerEx7)
    #     self._ui.lineResultsEx8.setText(results.answerEx8)
    #     self._ui.lineResultsEx9.setText(results.answerEx9)
    #     self._ui.lineResultsEx10.setText(results.answerEx10)
    #     self._ui.lineResultsEx11.setText(results.answerEx11A)
    #     self._ui.lineResultsEx12.setText(results.answerEx12A)
    #     self._ui.lineResultName.setText(results.name)
    #     self._ui.lineResultsSurname.setText(results.surname)

    #     if(results.feedbackE1=='1'):
    #         self._ui.checkBox.setChecked(True)
    #     elif (results.feedbackE1=='2'):
    #         self._ui.checkBox13.setChecked(True)
    #     elif (results.feedbackE1=='3'):
    #         self._ui.checkBox25.setChecked(True)
    #     if(results.feedbackE2=='1'):
    #         self._ui.checkBox2.setChecked(True)
    #     elif (results.feedbackE2=='2'):
    #         self._ui.checkBox14.setChecked(True)
    #     elif (results.feedbackE2=='3'):
    #         self._ui.checkBox26.setChecked(True)

    #     if(results.feedbackE3=='1'):
    #         self._ui.checkBox3.setChecked(True)
    #     elif (results.feedbackE3=='2'):
    #         self._ui.checkBox15.setChecked(True)
    #     elif (results.feedbackE2=='3'):
    #         self._ui.checkBox27.setChecked(True)

    #     if(results.feedbackE4=='1'):
    #         self._ui.checkBox4.setChecked(True)
    #     elif (results.feedbackE4=='2'):
    #         self._ui.checkBox16.setChecked(True)
    #     elif (results.feedbackE4=='3'):
    #         self._ui.checkBox28.setChecked(True)

    #     if(results.feedbackE5=='1'):
    #         self._ui.checkBox5.setChecked(True)
    #     elif (results.feedbackE5=='2'):
    #         self._ui.checkBox17.setChecked(True)
    #     elif (results.feedbackE5=='3'):
    #         self._ui.checkBox29.setChecked(True)

    #     if(results.feedbackE6=='1'):
    #         self._ui.checkBox6.setChecked(True)
    #     elif (results.feedbackE5=='2'):
    #         self._ui.checkBox18.setChecked(True)
    #     elif (results.feedbackE6=='3'):
    #         self._ui.checkBox30.setChecked(True)


    #     if(results.feedbackE7=='1'):
    #         self._ui.checkBox7.setChecked(True)
    #     elif (results.feedbackE7=='2'):
    #         self._ui.checkBox19.setChecked(True)
    #     elif (results.feedbackE7=='3'):
    #         self._ui.checkBox31.setChecked(True)


    #     if(results.feedbackE8=='1'):
    #         self._ui.checkBox8.setChecked(True)
    #     elif (results.feedbackE8=='2'):
    #         self._ui.checkBox20.setChecked(True)
    #     elif (results.feedbackE8=='3'):
    #         self._ui.checkBox32.setChecked(True)


    #     if(results.feedbackE9=='1'):
    #         self._ui.checkBox9.setChecked(True)
    #     elif (results.feedbackE9=='2'):
    #         self._ui.checkBox21.setChecked(True)
    #     elif (results.feedbackE9=='3'):
    #         self._ui.checkBox33.setChecked(True)

    #     if(results.feedbackE10=='1'):
    #         self._ui.checkBox10.setChecked(True)
    #     elif (results.feedbackE10=='2'):
    #         self._ui.checkBox22.setChecked(True)
    #     elif (results.feedbackE10=='3'):
    #         self._ui.checkBox34.setChecked(True)

    #     if(results.feedbackE11=='1'):
    #         self._ui.checkBox11.setChecked(True)
    #     elif (results.feedbackE11=='2'):
    #         self._ui.checkBox23.setChecked(True)
    #     elif (results.feedbackE11=='3'):
    #         self._ui.checkBox35.setChecked(True)


    #     if(results.feedbackE12=='1'):
    #         self._ui.checkBox11.setChecked(True)
    #     elif (results.feedbackE12=='2'):
    #         self._ui.checkBox23.setChecked(True)
    #     elif (results.feedbackE10=='3'):
    #         self._ui.checkBox35.setChecked(True)



    # def loadResultsByID(self,i):
    #     self.loadResults(self._model.result.listResults[i])

    # def loadResultsByIDCounter(self,value):
    #     print(" change ",value)
    #     self.counter=self.counter+value
    #     print(" counter ",self.counter)
    #     self.loadResults(self._model.result.listResults[self.counter])

    #     if ( ( self.counter +1 )==len(self._model.result.listResults)):
    #         self._ui.pushButtonResultsNext.hide()
    #     else:
    #         self._ui.pushButtonResultsNext.show()


    #     if ( 0== len(self._model.result.listResults)):
    #         self._ui.pushButtoResultPrevius.hide()
    #     else:
    #         self._ui.pushButtoResultPrevius.show()

