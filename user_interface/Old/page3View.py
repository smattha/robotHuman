from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from sqlalchemy import false
from PyQt5.QtWidgets import (QMainWindow,  QWidget)
from views.DisplayImage import DisplayImageWidget
        
    

class page3View(QWidget):
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


        #####################################################################################
        # #Exercise 1
        #####################################################################################

        # self._ui.mainImage.setPixmap(QtGui.QPixmap(self._model.resourcesImage1))
        self.displayMainImageExersice1=(DisplayImageWidget(self._model.resourcesImage1))
        self.displayMainImageExersice1.setController(main_controller)
        self._ui.gridLayout_5.addWidget(self.displayMainImageExersice1, 3, 0, 1, 5)




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

