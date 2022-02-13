from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from views.ui.menu import Ui_menuWindow
from views.ui.dialog import Ui_Dialog
from PyQt5 import  QtWidgets,QtGui

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
        self._ui.mainImage.setPixmap(QtGui.QPixmap("./resources/images/ex1/mainImage.png"))
        self._ui.mainImageEx2page.setPixmap(QtGui.QPixmap("./resources/images/ex2/mainImage.png"))
        self._ui.imageExersice5.setPixmap(QtGui.QPixmap("./resources/images/ex5/image.png"))

        #Exercise 3
        self._ui.mainImageEx3.setPixmap(QtGui.QPixmap("./resources/images/ex3/1.png"))
        self._ui.exercise5Answer1.setPixmap(QtGui.QPixmap("./resources/images/ex3/3.png"))
        self._ui.exercise5Answer2.setPixmap(QtGui.QPixmap("./resources/images/ex3/4.png"))

        #Exercise 4
        self._ui.mainImageEx4.setPixmap(QtGui.QPixmap("./resources/images/ex4/1.png"))
        self._ui.exercise4Answer1.setPixmap(QtGui.QPixmap("./resources/images/ex4/6.png"))
        self._ui.exercise4Answer2.setPixmap(QtGui.QPixmap("./resources/images/ex4/7.png"))
        self._ui.exercise4Answer3.setPixmap(QtGui.QPixmap("./resources/images/ex4/8.png"))                        


        #Exercise 6
        self._ui.mainImageExercise6.setPixmap(QtGui.QPixmap("./resources/images/ex6/1.png"))  

        self._ui.easyFeedback.setPixmap(QtGui.QPixmap("./resources/images/happy.jpg"))
        self._ui.normalFeedback.setPixmap(QtGui.QPixmap("./resources/images/normal.jpg"))
        self._ui.difficultFeedback.setPixmap(QtGui.QPixmap("./resources/images/sad.jpg"))
        self._ui.yesImage.setPixmap(QtGui.QPixmap("./resources/images/check.png"))
        self._ui.noImage.setPixmap(QtGui.QPixmap("./resources/images/reject.jpg"))
        self._ui.stackedWidget.setCurrentIndex(0)
        ################################################################################################
        # # connect widgets to controller
        # #self._ui.spinBox_amount.valueChanged.connect(self._main_controller.change_amount)
        self._ui.clearMenu.clicked.connect(lambda: self._main_controller.clearClicked())
        self._ui.saveMenu.clicked.connect(lambda:  self._main_controller.saveClicked(self._ui.name.toPlainText(),self._ui.surname.toPlainText(),self._ui.ageTextBox.toPlainText()))
        
        self._ui.selectExersiceButton.clicked.connect( lambda: self._main_controller.setPage(self._ui.selectExercise.currentIndex()) )        

        self._ui.selectExercise.addItems(self._model.listAvailableExersice)


        self._ui.selectExercise.currentIndexChanged.connect(lambda:  self._main_controller.selectButtonClicked(self._ui.selectExercise.currentIndex()) )        
        self._ui.answer1.clicked.connect(lambda: self._main_controller.clickLabel(self._ui.answer1.objectName()))
        self._ui.answer2.clicked.connect(lambda: self._main_controller.clickLabel(self._ui.answer2.objectName()))
        self._ui.answer3.clicked.connect(lambda: self._main_controller.clickLabel(self._ui.answer3.objectName()))
        self._ui.answer4.clicked.connect(lambda: self._main_controller.clickLabel(self._ui.answer4.objectName()))
        self._ui.answer5.clicked.connect(lambda: self._main_controller.clickLabel(self._ui.answer5.objectName()))

        #Exercise3
        self._ui.nextPageExercise3.clicked.connect(lambda: self._main_controller.nextPage3(self._ui.answer5.objectName()))

        #Exercise4
        self._ui.nextPageEx4.clicked.connect(lambda: self._main_controller.nextPage4(self._ui.answer5.objectName()))

        #Exercise6
        self._ui.nextPageEx6.clicked.connect(lambda: self._main_controller.nextPageEx6(self._ui.answer5.objectName()))

        #################################################################################################
        # # listen for model event signals
        self._model.changeDscrSingal.connect(self.changeDscrChanged)
        self._model.resetFieldSingal.connect(self.resetField)
        self._model.setPageSignal.connect(self.setPage)
        self._model.nextPageSignalEx5.connect(self.setImage)
        self._model.nextPageSignalEx4.connect(self.setImageEx4)
        self._model.nextPageSignalEx6.connect(self.nextPageSignalEx6)
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
    def nextPageSignalEx6(self, value):
        print("Image 6")
        self._ui.mainImageExercise6.setPixmap(QtGui.QPixmap(value))
    # @pyqtSlot(str)
    # def on_even_odd_changed(self, value):
    #     self._ui.label_even_odd.setText(value)

    # @pyqtSlot(bool)
    # def on_enable_reset_changed(self, value):
    #     self._ui.pushButton_reset.setEnabled(value)
