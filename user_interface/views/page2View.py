from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from views.ui.page2 import Ui_Form
from PyQt5 import  QtWidgets,QtGui
from PyQt5.QtWidgets import QWidget

    

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


        self._ui.label_3.setText(self._main_controller.title)
        self._ui.label_3.setAlignment(QtCore.Qt.AlignCenter)


        self.answer51 = QtWidgets.QPushButton()
        self.answer51.setObjectName(self._main_controller.title)
        self.answer51.clicked.connect(lambda: self._main_controller.nextPage3(self._main_controller))

        self._ui.optionA.clicked.connect(lambda: self._main_controller.step2Store('A'))
        self._ui.optionB.clicked.connect(lambda: self._main_controller.step2Store('B'))
        self._ui.optionC.clicked.connect(lambda: self._main_controller.step2Store('C'))
        
        self.answer51.setText("Επόμενο")
        self.answer51.hide()

        self._ui.gridLayout_5.addWidget(self.answer51, 4, 1, 1, 1)



        #################################################################################################
        # # listen for model event signals
        self._model.nextImgSingal.connect(self.nextImg)
        self._ui.stackedWidget.setCurrentIndex(0)

        # self._ui.label_7.setText(self._main_controller.answerEx3)
        self.i=self._model.i
        i=0
        for row in self._main_controller._imagesAnswer:
            

            self.label_4 = QtWidgets.QLabel()
            self.label_4.setText("")
            self.label_4.setPixmap(QtGui.QPixmap(row[1]))
            self.label_4.setScaledContents(True)
            self.label_4.setObjectName(row[1])
            self.label_4.setMaximumSize(QtCore.QSize(480/self.i, 480/self.i))
            self.label_4.setScaledContents(True)
            self._ui.horizontalLayout.addWidget(self.label_4)

            if (i==0):
                answer5_2 = QtWidgets.QPushButton()
                answer5_2.setObjectName(row[0])
                answer5_2.clicked.connect(lambda: self._main_controller.storeAnswer('1'))
                answer5_2.setText(row[0])
                self._ui.horizontalLayout_2.addWidget(answer5_2)

            if (i==1):
                answer5_3 = QtWidgets.QPushButton()
                answer5_3.setObjectName(row[0])
                answer5_3.clicked.connect(lambda: self._main_controller.storeAnswer('2'))
                answer5_3.setText(row[0])
                self._ui.horizontalLayout_2.addWidget(answer5_3)
            if (i==2):
                answer5_4 = QtWidgets.QPushButton()
                answer5_4.setObjectName(row[0])
                answer5_4.clicked.connect(lambda: self._main_controller.storeAnswer('3'))
                answer5_4.setText(row[0])
                self._ui.horizontalLayout_2.addWidget(answer5_4)
            i=i+1
        self._ui.answer5.hide()
        self._ui.label_7.setText(self._main_controller.answerEx3)



    @pyqtSlot(str)
    def changeDscrChanged(self, value):
        # print('Set Text ',value)
        self._ui.descriptionTxt.setText(value)
        self._ui.descriptionText.setAlignment(QtCore.Qt.AlignCenter)


    @pyqtSlot(str)
    def nextImg(self, value):
        if value=='0':
            self._ui.stackedWidget.setCurrentIndex(1)      
        elif value=='1':
            self._ui.stackedWidget.setCurrentIndex(2)              
        else:
            self._ui.stackedWidget.setCurrentIndex(0)
            self._ui.label.setScaledContents(True)
            self._ui.label.setPixmap(QtGui.QPixmap(value))
            self._ui.label.setMaximumSize(QtCore.QSize(900/self.i, 480/self.i))
            # self._ui.label.setScaledContents(True)
            self._ui.descriptionBox.setText(self._main_controller._imagesStoryCur)

    @pyqtSlot(int)
    def setPage(self, value):
        print('Empty field ',value)


    @pyqtSlot(str)
    def setImage(self, value):
        print('Set Image',value)
        if value=='0' : 
            self.test3.openImage(self._model.resourcesImage3B)
            self.test3.resize()
        

    @pyqtSlot(str)
    def setImageEx4(self, value):
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
        self.test6.openImage(value)
        self.test6.resize()     

