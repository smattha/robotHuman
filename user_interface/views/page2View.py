from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from sqlalchemy import false
from views.ui.page2 import Ui_Form
from PyQt5 import  QtWidgets,QtGui
from PyQt5.QtWidgets import (QAction, QApplication, QColorDialog, QFileDialog,
        QInputDialog, QMainWindow, QMenu, QMessageBox, QWidget)
from PyQt5.QtCore import QDir, QPoint, QRect, QSize, Qt
from views.DisplayImage import DisplayImageWidget
class DialogFeedback(QMainWindow):
    def __init__(self):
        super().__init__()
        self._dialog = Ui_Dialog()
        self._dialog.setupUi(self)
        
    

class page2View(QWidget):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_Form()
        self._ui.setupUi(self)

        #self._dialog.hide()
        self.move(model.poseX,model.poseY)
        self.resize(model.sizeY, model.sizeY)


        #####################################################################################
        # #Exercise 1
        #####################################################################################

        # self._ui.mainImage.setPixmap(QtGui.QPixmap(self._model.resourcesImage1))



        self._ui.label_3.setText(self._main_controller.title)
        self._ui.label_7.setText(self._main_controller.title)
        # self._ui.gridLayout_4 = QtWidgets.QGridLayout(self)
        # self._ui.gridLayout_4.setObjectName("gridLayout_41")
        # self._ui.gridLayout_4.addLayout(self._ui.gridLayout_5, 0, 0, 1, 1)
      
        #Exersice 1
        # self._ui.selectExercise.currentIndexChanged.connect(lambda:  self._main_controller.selectButtonClicked(self._ui.selectExercise.currentIndex()) )        
        
        # self._ui.answer5.setObjectName(self._main_controller.title)

        self.answer51 = QtWidgets.QPushButton()
        self.answer51.setObjectName(self._main_controller.title)
        self.answer51.clicked.connect(lambda: self._main_controller.nextPage3(self._main_controller))

        self._ui.gridLayout_5.addWidget(self.answer51, 4, 1, 1, 1)

        # self._ui.answer2.clicked.connect(lambda: self._main_controller._exercisesController[0].storeAnswer(2))
        # self._ui.answer3.clicked.connect(lambda: self._main_controller._exercisesController[0].storeAnswer(3))
        # self._ui.answer4.clicked.connect(lambda: self._main_controller._exercisesController[0].storeAnswer(4))
        # self._ui.answer5.clicked.connect(lambda: self._main_controller._exercisesController[0].storeAnswer(5))


        #################################################################################################
        # # listen for model event signals
        self._model.nextImgSingal.connect(self.nextImg)
        self._ui.stackedWidget.setCurrentIndex(0)
        # self._model.resetFieldSingal.connect(self.resetField)
        # self._model.setPageSignal.connect(self.setPage)
        # self._model.nextPageSignalEx5.connect(self.setImage)
        # self._model.nextPageSignalEx4.connect(self.setImageEx4)
        # self._model.nextPageSignalEx6.connect(self.nextPageSignalEx6)


        # self.answer5 = QtWidgets.QPushButton(self.widget)
        # self.answer5.setObjectName("answer5")
        # self.gridLayout_5.addWidget(self.answer5, 5, 1, 1, 1)
        #Feedback
        # self._model.feedbackShowButton.connect(self.feedbackShowButton)
        
 
        for row in self._main_controller._imagesAnswer:
            

            self.label_4 = QtWidgets.QLabel()
            self.label_4.setText("")
            self.label_4.setPixmap(QtGui.QPixmap(row[1]))
            self.label_4.setScaledContents(False)
            self.label_4.setObjectName(row[1])
            self.label_4.setMaximumSize(QtCore.QSize(480, 480))
            self.label_4.setScaledContents(True)
            self._ui.horizontalLayout.addWidget(self.label_4)


            answer5_2 = QtWidgets.QPushButton()
            answer5_2.setObjectName(row[0])
            answer5_2.clicked.connect(lambda: self._main_controller.storeAnswer(self._main_controller))
            answer5_2.setText(row[0])

            self._ui.horizontalLayout_2.addWidget(answer5_2)





        # self.label_4 = QtWidgets.QLabel()
        # self.label_4.setText("")
        # self.label_4.setPixmap(QtGui.QPixmap("./resources/images/ex4/1.png"))
        # self.label_4.setScaledContents(False)
        # self.label_4.setObjectName("label_5")
        # self.label_4.setMaximumSize(QtCore.QSize(120, 120))
        # self.label_4.setScaledContents(True)
        # self._ui.horizontalLayout.addWidget(self.label_4)


        # self.answer5_2 = QtWidgets.QPushButton()
        # self.answer5_2.setObjectName("answer5_3")
        # self._ui.horizontalLayout_2.addWidget(self.answer5_2)


        # self.label_5 = QtWidgets.QLabel()
        # self.label_5.setText("")
        # self.label_5.setPixmap(QtGui.QPixmap("./resources/images/ex4/1.png"))
        # self.label_5.setScaledContents(False)
        # self.label_5.setObjectName("label_4")
        # self.label_5.setMaximumSize(QtCore.QSize(120, 120))
        # self.label_5.setScaledContents(True)
        # self._ui.horizontalLayout.addWidget(self.label_5)


        # self.answer5_3 = QtWidgets.QPushButton()
        # self.answer5_3.setObjectName("answer5_3")
        # self._ui.horizontalLayout_2.addWidget(self.answer5_3)


    @pyqtSlot(str)
    def changeDscrChanged(self, value):
        print('Set Text ',value)
        self._ui.descriptionTxt.setText(value)


    @pyqtSlot(str)
    def nextImg(self, value):
        if value=='0':
            self._ui.stackedWidget.setCurrentIndex(1)           
        else:
            self._ui.stackedWidget.setCurrentIndex(0)    
            self._ui.label.setPixmap(QtGui.QPixmap(value))
            self._ui.label.setMaximumSize(QtCore.QSize(640, 640))
            self._ui.label.setScaledContents(True)

    @pyqtSlot(int)
    def setPage(self, value):
        print('Empty field ',value)
        # self._ui.stackedWidget.setCurrentIndex(value)

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

