from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from sqlalchemy import false
from views.ui.page1 import Ui_Form
from PyQt5 import  QtWidgets,QtGui
from PyQt5.QtWidgets import (QAction, QApplication, QColorDialog, QFileDialog,
        QInputDialog, QMainWindow, QMenu, QMessageBox, QWidget)
from PyQt5.QtCore import QDir, QPoint, QRect, QSize, Qt
from views.DisplayImage import DisplayImageWidget
class DialogFeedback(QMainWindow):
    def __init__(self):
        super().__init__()
        
    

class page1View(QWidget):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_Form()
        self._ui.setupUi(self)
        DialogFeedback()

        #self._dialog.hide()
        self.move(model.poseX,model.poseY)
        self.resize(model.sizeY, model.sizeY)

        translate = QtCore.QCoreApplication.translate
        self._ui.name.setText(translate("Form", self._main_controller.getTitle()))

        #####################################################################################
        # #Exercise 1
        #####################################################################################

        self._ui.mainImage.setPixmap(QtGui.QPixmap(  self._main_controller.getImagePath()  ))
       
        
        self._ui.answer1.clicked.connect(lambda: self._main_controller.storeAnswer(1))
        self._ui.answer2.clicked.connect(lambda: self._main_controller.storeAnswer(2))
        self._ui.answer3.clicked.connect(lambda: self._main_controller.storeAnswer(3))
        self._ui.answer4.clicked.connect(lambda: self._main_controller.storeAnswer(4))
        self._ui.answer5.clicked.connect(lambda: self._main_controller.storeAnswer(5))

        if self._main_controller._imageAnswerFlag ==0 :
            self._ui.answer1Img.setPixmap(QtGui.QPixmap(  self._main_controller._imageAnswer1 ))
            self._ui.answer2Img.setPixmap(QtGui.QPixmap(  self._main_controller._imageAnswer2 ))
            self._ui.answer3Img.setPixmap(QtGui.QPixmap(  self._main_controller._imageAnswer3 ))
            self._ui.answer4Img.setPixmap(QtGui.QPixmap(  self._main_controller._imageAnswer4 ))
            self._ui.answer5Img.setPixmap(QtGui.QPixmap(  self._main_controller._imageAnswer5 ))
        else:
            self._ui.answer1Img.hide()
            self._ui.answer2Img.hide()
            self._ui.answer3Img.hide()
            self._ui.answer4Img.hide()
            self._ui.answer5Img.hide()


        self._ui.descriptionBox.setText(self._main_controller._exersiceTitleDsr)
        self._ui.Results.setText(self._main_controller._answerDsr)

        self._ui.answer1.setText(self._main_controller._answerEx1Descr)
        self._ui.answer2.setText(self._main_controller._answerEx2Descr)
        self._ui.answer3.setText(self._main_controller._answerEx3Descr)
        self._ui.answer4.setText(self._main_controller._answerEx4Descr)
        self._ui.answer5.setText(self._main_controller._answerEx5Descr)

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

