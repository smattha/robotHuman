from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from sqlalchemy import false
from views.ui.menu import Ui_menuWindow
from PyQt5 import  QtWidgets,QtGui
from PyQt5.QtWidgets import (QAction, QApplication, QColorDialog, QFileDialog,
        QInputDialog, QMainWindow, QMenu, QMessageBox, QWidget)
from PyQt5.QtCore import QDir, QPoint, QRect, QSize, Qt
from PyQt5.QtGui import QImage, QImageWriter, QPainter, QPen, qRgb
from views.DisplayImage import DisplayImageWidget
from views.page1View import page1View
from views.page2View import page2View
from views.page5View import page5View
class DialogFeedback(QMainWindow):
    def __init__(self):
        super().__init__()
        
    

class MenuView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_menuWindow()
        self._ui.setupUi(self)
        DialogFeedback()

        #self._dialog.hide()
        self.move(model.poseX,model.poseY)
        self.resize(model.sizeY, model.sizeY)


        #####################################################################################
        # #Exercise 1
        #####################################################################################

        # self._ui.mainImage.setPixmap(QtGui.QPixmap(self._model.resourcesImage1))
        # self.displayMainImageExersice1=(DisplayImageWidget(self._model.resourcesImage1))
        # self.displayMainImageExersice1.setController(main_controller)
        # self._ui.gridLayout_5.addWidget(self.displayMainImageExersice1, 3, 0, 1, 5)



       

        

        #####################################################################################
        #Exercise 4
        #####################################################################################
        # self._ui.mainImageEx4.setPixmap(QtGui.QPixmap(self._model.exersice4A))
        # self.test4=(DisplayImageWidget(self._model.exersice4A))
        # self.test4.setController(main_controller)
        # self._ui.verticalLayout_11.addWidget(self.test4, 1)
        
        # self.exersice3B=(DisplayImageWidget(self._model.exersice3B))
        # self.exersice3B.setController(main_controller)
        # self._ui.gridLayout_14.addWidget(self.exersice3B, 0, 1, 1, 1)

        # self.exersice3A=(DisplayImageWidget(self._model.exersice3A))
        # self.exersice3A.setController(main_controller)
        # self._ui.gridLayout_14.addWidget(self.exersice3A, 0, 0, 1, 1)



        # self._ui.exercise4Answer1.setPixmap(QtGui.QPixmap(self._model.exersice4B))
        # self._ui.exercise4Answer2.setPixmap(QtGui.QPixmap(self._model.exersice4C))
        # self._ui.exercise4Answer3.setPixmap(QtGui.QPixmap(self._model.exersice4D))                        


        #####################################################################################
        #Exercise 5
        #####################################################################################
        # self._ui.imageExersice5.setPixmap(QtGui.QPixmap(self._model.exersice5A))

        # self.test5=(DisplayImageWidget(self._model.exersice5A))
        # self.test5.setController(main_controller)
        # self._ui.verticalLayout_4.addWidget(self.test5, 1)

        # # self._ui.page_3(QtWidgets.QWidget(DisplayImageWidget()))
        # self.test=(DisplayImageWidget('/home/smatt/Documents/git/src/resources/images/ex5/image.png'))
        # self.test.setController(self._main_controller._exercisesController[4])
        # self._ui.stackedWidget.addWidget(self.test)




    
        ###################################################################################################################
        ###############################
        # # self._ui.page_3(QtWidgets.QWidget(DisplayImageWidget()))
    
        # self.page1=page1View(self._model,self._main_controller._exercisesController[0])
        # self._ui.stackedWidget.addWidget(self.page1._ui.widget)

        # self.page2=page1View(self._model,self._main_controller._exercisesController[1])
        # self._ui.stackedWidget.addWidget(self.page2._ui.widget)

        # self.page3=page2View(self._model,self._main_controller._exercisesController[2])
        # self._ui.stackedWidget.addWidget(self.page3._ui.stackedWidget)


        # self.page4=page2View(self._model,self._main_controller._exercisesController[3])
        # self._ui.stackedWidget.addWidget(self.page4._ui.stackedWidget)

        # # # self._ui.page_3(QtWidgets.QWidget(DisplayImageWidget()))
        # self.test3=page1View(self._model,self._main_controller._exercisesController[4])
        # self._ui.stackedWidget.addWidget(self.test3._ui.widget)

    
        # self.test4=page2View(self._model,self._main_controller._exercisesController[5])
        # self._ui.stackedWidget.addWidget(self.test4._ui.widget)

        # # self._ui.page_3(QtWidgets.QWidget(DisplayImageWidget()))

        # self.test=(DisplayImageWidget(self._main_controller._exercisesController[4]._imagePath))
        # self.test.setController(self._main_controller._exercisesController[4])
        # self._ui.stackedWidget.addWidget(self.test)

        # self._ui.exercise5Answer1.setPixmap(QtGui.QPixmap(self._model.exersice3A))
        # self._ui.exercise5Answer2.setPixmap(QtGui.QPixmap(self._model.exersice3B))




        #####################################################################################        
        #Exercise 6
        # self._ui.mainImageExercise6.setPixmap(QtGui.QPixmap(self._model.exersice6A))  
        ####################################################################################

        # self.test6=(DisplayImageWidget(self._model.exersice6A))
        # self.test6.setController(main_controller)
        # # self._ui.gridLayout_13.addWidget(self.test6, 1, 1, 1, 4)
        # self._ui.verticalLayout_12.addWidget(self.test6)


        self.easy=(DisplayImageWidget(self._model.easyFeedbackImg ))
        self.easy.setController(main_controller)
        self._ui.gridLayout_10.addWidget(self.easy, 1, 0, 1, 1)


        self.normal=(DisplayImageWidget(self._model.normalFeedback  ))
        self.normal.setController(main_controller)
        self._ui.gridLayout_10.addWidget(self.normal, 1, 1, 1, 1)

        self.difficultFeedback=(DisplayImageWidget(self._model.difficultFeedback ))
        self.difficultFeedback.setController(main_controller)
        self._ui.gridLayout_10.addWidget(self.difficultFeedback, 1, 2, 1, 1)


        self._ui.stackedWidget.setCurrentIndex(0)


        #Feedback
        self._ui.terminateButton.hide()
        self._ui.nextExersice.hide()

        ################################################################################################
        # # connect widgets to controller
        # #self._ui.spinBox_amount.valueChanged.connect(self._main_controller.change_amount)
        self._ui.clearMenu.clicked.connect(lambda: self._main_controller.clearClicked())
        self._ui.saveMenu.clicked.connect(lambda:  self._main_controller.saveClicked(self._ui.name.text,self._ui.surname.text,self._ui.ageTextBox.text))
        
        self._ui.selectExersiceButton.clicked.connect( lambda: self._main_controller.setPage(self._ui.selectExercise.currentIndex()) )        

        self._ui.selectExercise.addItems(self._model.listAvailableExersice)


        #Exersice 1
        self._ui.selectExercise.currentIndexChanged.connect(lambda:  self._main_controller.selectButtonClicked(self._ui.selectExercise.currentIndex()) )        
        
        self._ui.mainImageHome.setPixmap(QtGui.QPixmap("./resources/images/mainScreen.jpg"))

        




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
        self._model.nextPageSignalEx5.connect(self.setImage)
        self._model.nextPageSignalEx4.connect(self.setImageEx4)
        self._model.nextPageSignalEx6.connect(self.nextPageSignalEx6)

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
        print('Set page !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1',value)
        if value==1:
            # self._ui.stackedWidget.setCurrentIndex(11)
            j=self._ui.stackedWidget.count()
            self.page1=page1View(self._model,self._main_controller._exercisesController[0])
            self._ui.stackedWidget.addWidget(self.page1)
            self._ui.stackedWidget.setCurrentIndex(j)
        elif value==2:
            # self._ui.stackedWidget.setCurrentIndex(12)
            j=self._ui.stackedWidget.count()
            self.page2=page1View(self._model,self._main_controller._exercisesController[1])
            self._ui.stackedWidget.addWidget(self.page2)
            self._ui.stackedWidget.setCurrentIndex(j)
        elif value==3:
            j=self._ui.stackedWidget.count()
            # self._ui.stackedWidget.setCurrentIndex(13)    
            
            self.page3=page2View(self._model,self._main_controller._exercisesController[2])
            self._ui.stackedWidget.addWidget(self.page3._ui.stackedWidget)
            self._ui.stackedWidget.setCurrentIndex(j)
        elif value==4:
            j=self._ui.stackedWidget.count()
            # self._ui.stackedWidget.setCurrentIndex(14)    

            self.page4=page2View(self._model,self._main_controller._exercisesController[3])
            self._ui.stackedWidget.addWidget(self.page4._ui.stackedWidget)
            self._ui.stackedWidget.setCurrentIndex(j)
        elif value==5:
            j=self._ui.stackedWidget.count()
            self._ui.stackedWidget.setCurrentIndex(15)    
            # # # self._ui.page_3(QtWidgets.QWidget(DisplayImageWidget()))
            self.test3=page1View(self._model,self._main_controller._exercisesController[4])
            self._ui.stackedWidget.addWidget(self.test3._ui.widget)

            self._ui.stackedWidget.setCurrentIndex(j)        

            j=self._ui.stackedWidget.count()
            # self._ui.page_3(QtWidgets.QWidget(DisplayImageWidget()))
            self._main_controller._exercisesController[4]._image2 = j
            self.test=(DisplayImageWidget(self._main_controller._exercisesController[4]._imagePath))
            self.test.setController(self._main_controller._exercisesController[4])
            self._ui.stackedWidget.addWidget(self.test)

            # self._ui.exercise5Answer1.setPixmap(QtGui.QPixmap(self._model.exersice3A))
            # self._ui.exercise5Answer2.setPixmap(QtGui.QPixmap(self._model.exersice3B))

        elif value==6:
            j=self._ui.stackedWidget.count()
            # self._ui.stackedWidget.setCurrentIndex(16)    
            self.test4=page2View(self._model,self._main_controller._exercisesController[5])
            self._ui.stackedWidget.addWidget(self.test4._ui.widget)
            self._ui.stackedWidget.setCurrentIndex(j)
            self._ui.stackedWidget.setCurrentIndex(0)
            self._ui.stackedWidget.setCurrentIndex(j)
        # elif value==7:
        #     # self._ui.stackedWidget.setCurrentIndex(11)
        #     j=self._ui.stackedWidget.count()
        #     self.page7=page1View(self._model,self._main_controller._exercisesController[6])
        #     self._ui.stackedWidget.addWidget(self.page7)
        #     self._ui.stackedWidget.setCurrentIndex(j)
        elif value==8:
            # self._ui.stackedWidget.setCurrentIndex(12)
            j=self._ui.stackedWidget.count()
            self.page8=page1View(self._model,self._main_controller._exercisesController[7])
            self._ui.stackedWidget.addWidget(self.page8)
            self._ui.stackedWidget.setCurrentIndex(j)
        elif value==9:
            j=self._ui.stackedWidget.count()
            # self._ui.stackedWidget.setCurrentIndex(13)    
            self.page9=page2View(self._model,self._main_controller._exercisesController[8])
            self._ui.stackedWidget.addWidget(self.page9._ui.stackedWidget)
            self._ui.stackedWidget.setCurrentIndex(j)

        else:
            self._ui.stackedWidget.setCurrentIndex(value)
    @pyqtSlot(str)
    def setImage(self, value):
        print('Set Image',value)
        if value=='0' : 
            self.test3.openImage(self._model.resourcesImage3B)
            self.test3.resize()
        

    @pyqtSlot(str)
    def setImageEx4(self, value):
        # self._ui.mainImageEx4.setPixmap(QtGui.QPixmap(value))
            self.test4.openImage(value)
            self.test4.resize()       


    @pyqtSlot(str)
    def feedbackShowButton(self,value):   
        if value=='show':
            self._ui.terminateButton.show()
            self._ui.nextExersice.show()
        else:
            self._ui.terminateButton.hide()
            self._ui.nextExersice.hide()           

    @pyqtSlot(str)
    def nextPageSignalEx6(self, value):
        print("Image 6")
        self.test6.openImage(value)
        self.test6.resize()     

