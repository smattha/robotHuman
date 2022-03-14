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

