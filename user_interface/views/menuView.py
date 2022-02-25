from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from sqlalchemy import false
from views.ui.menu import Ui_menuWindow
from views.ui.dialog import Ui_Dialog
from PyQt5 import  QtWidgets,QtGui
from PyQt5.QtWidgets import (QAction, QApplication, QColorDialog, QFileDialog,
        QInputDialog, QMainWindow, QMenu, QMessageBox, QWidget)
from PyQt5.QtCore import QDir, QPoint, QRect, QSize, Qt
from PyQt5.QtGui import QImage, QImageWriter, QPainter, QPen, qRgb
from views.ScribbleArea import ScribbleArea
class DialogFeedback(QMainWindow):
    def __init__(self):
        super().__init__()
        self._dialog = Ui_Dialog()
        self._dialog.setupUi(self)
        
    

class MenuView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_menuWindow()
        self._ui.setupUi(self)
        DialogFeedback()

        #self._dialog.hide()
        self.move(500,150)
        self.resize(943, 706)
        # #Exercise 1
        # self._ui.mainImage.setPixmap(QtGui.QPixmap(self._model.resourcesImage1))
        
        # #Exercise 2
        self._ui.mainImageEx2page.setPixmap(QtGui.QPixmap(self._model.resourcesImage2))
       
        #Exercise 3
        self._ui.mainImageEx3.setPixmap(QtGui.QPixmap(self._model.resourcesImage3))
        self._ui.exercise5Answer1.setPixmap(QtGui.QPixmap(self._model.exersice3A))
        self._ui.exercise5Answer2.setPixmap(QtGui.QPixmap(self._model.exersice3B))

        #Exercise 4
        self._ui.mainImageEx4.setPixmap(QtGui.QPixmap(self._model.exersice4A))
        self._ui.exercise4Answer1.setPixmap(QtGui.QPixmap(self._model.exersice4B))
        self._ui.exercise4Answer2.setPixmap(QtGui.QPixmap(self._model.exersice4C))
        self._ui.exercise4Answer3.setPixmap(QtGui.QPixmap(self._model.exersice4D))                        

        #Exercise 5
        self._ui.imageExersice5.setPixmap(QtGui.QPixmap(self._model.exersice5A))
        # self._ui.page_3(QtWidgets.QWidget(ScribbleArea()))
        self.test=(ScribbleArea())
        self.test.setController(main_controller)

        self._ui.stackedWidget.addWidget(self.test)


        self.test1=(ScribbleArea(self._ui.testing))
        self.test1.setController(main_controller)

        self._ui.testing=self.test1
        
        #Exercise 6
        self._ui.mainImageExercise6.setPixmap(QtGui.QPixmap(self._model.exersice6A))  




        self._ui.easyFeedback.setPixmap(QtGui.QPixmap( self._model.easyFeedbackImg ))
        self._ui.normalFeedback.setPixmap(QtGui.QPixmap( self._model.normalFeedback ))
        self._ui.difficultFeedback.setPixmap(QtGui.QPixmap( self._model.difficultFeedback))
        # self._ui.yesImage.setPixmap(QtGui.QPixmap("./resources/images/check.png"))
        # self._ui.noImage.setPixmap(QtGui.QPixmap("./resources/images/reject.jpg"))
        self._ui.stackedWidget.setCurrentIndex(0)


        #Feedback
        self._ui.terminateButton.hide()
        self._ui.nextExersice.hide()

        ################################################################################################
        # # connect widgets to controller
        # #self._ui.spinBox_amount.valueChanged.connect(self._main_controller.change_amount)
        self._ui.clearMenu.clicked.connect(lambda: self._main_controller.clearClicked())
        self._ui.saveMenu.clicked.connect(lambda:  self._main_controller.saveClicked(self._ui.name.toPlainText(),self._ui.surname.toPlainText(),self._ui.ageTextBox.toPlainText()))
        
        self._ui.selectExersiceButton.clicked.connect( lambda: self._main_controller.setPage(self._ui.selectExercise.currentIndex()) )        

        self._ui.selectExercise.addItems(self._model.listAvailableExersice)


        #Exersice 1
        self._ui.selectExercise.currentIndexChanged.connect(lambda:  self._main_controller.selectButtonClicked(self._ui.selectExercise.currentIndex()) )        
        self._ui.answer1.clicked.connect(lambda: self._main_controller.storeAnswer(1))
        self._ui.answer2.clicked.connect(lambda: self._main_controller.storeAnswer(2))
        self._ui.answer3.clicked.connect(lambda: self._main_controller.storeAnswer(3))
        self._ui.answer4.clicked.connect(lambda: self._main_controller.storeAnswer(4))
        self._ui.answer5.clicked.connect(lambda: self._main_controller.storeAnswer(5))

        #Exersice 2
        self._ui.answer1Ex2.clicked.connect(lambda: self._main_controller.storeAnswer(1))
        self._ui.answer2Ex2.clicked.connect(lambda: self._main_controller.storeAnswer(2))
        self._ui.answer3Ex2.clicked.connect(lambda: self._main_controller.storeAnswer(3))
        self._ui.answer4Ex2.clicked.connect(lambda: self._main_controller.storeAnswer(4))
        self._ui.answer5Ex2.clicked.connect(lambda: self._main_controller.storeAnswer(5))

        #Exercise3
        self._ui.nextPageExercise3.clicked.connect(lambda: self._main_controller.nextPage3(self._ui.answer5.objectName()))
        self._ui.answer1Ex3.clicked.connect(lambda: self._main_controller.storeAnswer(self._ui.answer4.objectName()))
        self._ui.answer1Ex3.clicked.connect(lambda: self._main_controller.storeAnswer(self._ui.answer5.objectName()))

        #Exercise4
        self._ui.nextPageEx4.clicked.connect(lambda: self._main_controller.nextPage4(self._ui.answer5.objectName()))
        self._ui.answer1Exersice4.clicked.connect(lambda: self._main_controller.storeAnswer(self._ui.answer4.objectName()))
        self._ui.answer2Exersice4.clicked.connect(lambda: self._main_controller.storeAnswer(self._ui.answer5.objectName()))
        self._ui.answer3Exersice4.clicked.connect(lambda: self._main_controller.storeAnswer(self._ui.answer5.objectName()))

        #Exersice 5
        self._ui.answer1Ex5.clicked.connect(lambda: self._main_controller.storeAnswer5(1))
        self._ui.answer2Ex5.clicked.connect(lambda: self._main_controller.storeAnswer5(2))
        self._ui.answer3Ex5.clicked.connect(lambda: self._main_controller.storeAnswer5(3))
        self._ui.answer4Ex5.clicked.connect(lambda: self._main_controller.storeAnswer5(4))
        self._ui.answer5Ex5.clicked.connect(lambda: self._main_controller.storeAnswer5(5))


        #Exercise6
        self._ui.nextPageEx6.clicked.connect(lambda: self._main_controller.nextPageEx6(self._ui.answer5.objectName()))

        self._ui.go2Home.clicked.connect(lambda: self._main_controller.go2Home())


        #Feedback
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
        

        # self._model.enable_reset_changed.connect(self.on_enable_reset_changed)

        # set a default value
        #self._main_controller.change_amount(42)

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
        print('Empty field ',value)
        self._ui.stackedWidget.setCurrentIndex(value)

    @pyqtSlot(str)
    def setImage(self, value):
        print('Set Image',value)
        if value=='0' : 
            self._ui.mainImageEx3.setPixmap(QtGui.QPixmap("./resources/images/ex3/2.png"))

    @pyqtSlot(str)
    def setImageEx4(self, value):
        self._ui.mainImageEx4.setPixmap(QtGui.QPixmap(value))

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
        self._ui.mainImageExercise6.setPixmap(QtGui.QPixmap(value))

