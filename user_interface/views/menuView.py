from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from sqlalchemy import false, true
from views.ui.menu import Ui_menuWindow
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import ( QMainWindow)
from views.DisplayImage import DisplayImageWidget
from views.page1View import page1View
from views.page2View import page2View
from threading import Thread
import time
    

class MenuView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_menuWindow()
        self._ui.setupUi(self)

        #self._dialog.hide()
        self.move(model.poseX,model.poseY)
        self.resize(model.sizeY, model.sizeY)
        self._ui.selectExercise.addItems(self._model.listAvailableExersice)


        self._ui.easy.setPixmap(QtGui.QPixmap(self._model.easyFeedbackImg ))
        self._ui.normal.setPixmap(QtGui.QPixmap(self._model.normalFeedback))
        self._ui.hard.setPixmap(QtGui.QPixmap(self._model.difficultFeedback))

        self._ui.easy.setMaximumSize(QtCore.QSize(480/model.i, 480/model.i))
        self._ui.easy.setScaledContents(True)

        self._ui.normal.setMaximumSize(QtCore.QSize(480/model.i, 480/model.i))
        self._ui.normal.setScaledContents(True)

        self._ui.hard.setMaximumSize(QtCore.QSize(480/model.i, 480/model.i))
        self._ui.hard.setScaledContents(True)

        self._ui.mainImageHome.setPixmap(QtGui.QPixmap("./resources/images/mainScreen.jpg"))

        self._ui.stackedWidget.setCurrentIndex(0)


        self._ui.terminateButton.setDisabled(True)
        self._ui.nextExersice.setDisabled(True)




        ################################################################################################
        # # connect widgets to controller
        self._ui.clearMenu.clicked.connect(lambda: self._main_controller.clearClicked())
        self._ui.saveMenu.clicked.connect(lambda:  self._main_controller.saveClicked(self._ui.name.text,self._ui.surname.text,self._ui.ageTextBox.text))       
        self._ui.selectExersiceButton.clicked.connect( lambda: self._main_controller.setPage(self._ui.selectExercise.currentIndex()) )        



        #Exersice 1
        self._ui.selectExercise.currentIndexChanged.connect(lambda:  self._main_controller.selectButtonClicked(self._ui.selectExercise.currentIndex()) )        
        

        self._ui.go2Home.clicked.connect(lambda: self._main_controller.go2Home())
        self._ui.nextExersice.clicked.connect(lambda: self._main_controller.move2NextPage())
        
        self._ui.terminateButton.clicked.connect(lambda: self._main_controller.go2Home())
        self._ui.feedbackEasyButton.clicked.connect(lambda: self._main_controller.feedback('1'))
        self._ui.feedbackNormalButton.clicked.connect(lambda: self._main_controller.feedback('2'))
        self._ui.feedbackHardButton.clicked.connect(lambda: self._main_controller.feedback('3'))



        #################################################################################################
        # # listen for model event signals
        self._model.changeDscrSingal.connect(self.changeDscrChanged)
        self._model.resetFieldSingal.connect(self.resetField)
        self._model.setPageSignal.connect(self.setPage)


        #Feedback
        self._model.feedbackShowButton.connect(self.feedbackShowButton)
        



    @pyqtSlot(str)
    def changeDscrChanged(self, value):
        print('Set Text ',value)
        self._ui.descriptionTxt.setText(value)


    @pyqtSlot(str)
    def resetField(self, value):
        print('Empty field ',value)
        self._ui.name.setText('')
        self._ui.ageTextBox.setText('')
        self._ui.surname.setText('')

    @pyqtSlot(int)
    def setPage(self, value):
        print('\t\t\t\tActivate Widget',value)
        if value==1:
            j=self._ui.stackedWidget.count()
            self.page1=page1View(self._model,self._main_controller._exercisesController[0])
            self._ui.stackedWidget.addWidget(self.page1)
            self._ui.stackedWidget.setCurrentIndex(j)
        
        elif value==2:
            j=self._ui.stackedWidget.count()
            self.page2=page1View(self._model,self._main_controller._exercisesController[1])
            self._ui.stackedWidget.addWidget(self.page2)
            self._ui.stackedWidget.setCurrentIndex(j)
        
        elif value==3:
            j=self._ui.stackedWidget.count()
            self.page3=page2View(self._model,self._main_controller._exercisesController[2])
            self._ui.stackedWidget.addWidget(self.page3._ui.stackedWidget)
            self._ui.stackedWidget.setCurrentIndex(j)
        
        elif value==4:
            j=self._ui.stackedWidget.count()
            self.page4=page2View(self._model,self._main_controller._exercisesController[3])
            self._ui.stackedWidget.addWidget(self.page4._ui.stackedWidget)
            self._ui.stackedWidget.setCurrentIndex(j)

        elif value==5:
            j=self._ui.stackedWidget.count()
            self._ui.stackedWidget.setCurrentIndex(15)    
            self.test3=page1View(self._model,self._main_controller._exercisesController[4])
            self._ui.stackedWidget.addWidget(self.test3._ui.widget)
            self._ui.stackedWidget.setCurrentIndex(j)        

            j=self._ui.stackedWidget.count()
            self._main_controller._exercisesController[4]._image2 = j+100
            self.test=(DisplayImageWidget(self._main_controller._exercisesController[4]._imagePath))
            self.test.setController(self._main_controller._exercisesController[4])
            self._ui.stackedWidget.addWidget(self.test)

        elif value==6:
            j=self._ui.stackedWidget.count()
            self.test4=page2View(self._model,self._main_controller._exercisesController[5])
            self._ui.stackedWidget.addWidget(self.test4._ui.widget)
            self._ui.stackedWidget.setCurrentIndex(j)
            self._ui.stackedWidget.setCurrentIndex(0)
            self._ui.stackedWidget.setCurrentIndex(j)


        elif value==7:
            j=self._ui.stackedWidget.count()
            self.page7=page1View(self._model,self._main_controller._exercisesController[6])
            self._ui.stackedWidget.addWidget(self.page7)
            self._ui.stackedWidget.setCurrentIndex(j)

        elif value==8:
            j=self._ui.stackedWidget.count()
            self.page8=page1View(self._model,self._main_controller._exercisesController[7])
            self._ui.stackedWidget.addWidget(self.page8)
            self._ui.stackedWidget.setCurrentIndex(j)

        elif value==9:
            j=self._ui.stackedWidget.count()
            self.page9=page2View(self._model,self._main_controller._exercisesController[8])
            self._ui.stackedWidget.addWidget(self.page9._ui.stackedWidget)
            self._ui.stackedWidget.setCurrentIndex(j)

        elif value==10:
            j=self._ui.stackedWidget.count()
            self.page10=page2View(self._model,self._main_controller._exercisesController[9])
            self._ui.stackedWidget.addWidget(self.page10._ui.stackedWidget)
            self._ui.stackedWidget.setCurrentIndex(j)

        elif value==11:
            j=self._ui.stackedWidget.count()
            self._ui.stackedWidget.setCurrentIndex(15)    
            self.test11=page1View(self._model,self._main_controller._exercisesController[10])
            self._ui.stackedWidget.addWidget(self.test11._ui.widget)

            self._ui.stackedWidget.setCurrentIndex(j)        
            j=self._ui.stackedWidget.count()
            self._main_controller._exercisesController[10]._image2 = j+100
            self.test10B=(DisplayImageWidget(self._main_controller._exercisesController[10]._imagePath))
            self.test10B.setController(self._main_controller._exercisesController[10])
            self._ui.stackedWidget.addWidget(self.test10B)


        elif value==12:
            j=self._ui.stackedWidget.count()
            self.test12=page2View(self._model,self._main_controller._exercisesController[11])
            self._ui.stackedWidget.addWidget(self.test12._ui.widget)
            self._ui.stackedWidget.setCurrentIndex(j)
            self._ui.stackedWidget.setCurrentIndex(0)
            self._ui.stackedWidget.setCurrentIndex(j)

        else:
            if value>100:
                value=value-100
            self._ui.stackedWidget.setCurrentIndex(value)
            if value==1:
                self.hideButtons()


    @pyqtSlot(str)
    def feedbackShowButton(self,value):   
        if value=='show':
            self._ui.terminateButton.setDisabled(False)
            self._ui.nextExersice.setDisabled(False)
        else:
            self._ui.terminateButton.setDisabled(True)
            self._ui.nextExersice.setDisabled(True)
     

    @pyqtSlot(str)
    def nextPageSignalEx6(self, value):
        print("Image 6")
        self.test6.openImage(value)
        self.test6.resize()     



    def hideButtons(self):

        self._ui.feedbackEasyButton.setDisabled(true)
        self._ui.feedbackNormalButton.setDisabled(true)
        self._ui.feedbackHardButton.setDisabled(true)
        self._ui.terminateButton.setDisabled(True)
        self._ui.nextExersice.setDisabled(True)
     
        thread = Thread(target = self.stopBeforeShowImageMain,args=(),daemon=True)
        thread.start()
        print("Thread finished...exiting")  


    # #Exercise 6
    # showAnswerButtons = pyqtSignal(str, name='showAnswerButtons')
    # showAnswerButtons.emit(self._description)

    def showButtons(self):
        # while (len(self._imagesStory)>=self._counter):
        #     time.sleep(5)
        #     thread = Thread(target = self.nextPage4,args=(),daemon=True)
        #     thread.start()
        # while (len(self._imagesStory)>self._counter):
        # self.nextPage4()
        time.sleep(5)
        
        self._ui.feedbackEasyButton.setDisabled(false)
        self._ui.feedbackNormalButton.setDisabled(false)
        self._ui.feedbackHArdButton.setDiable(false)