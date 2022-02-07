from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from views.ui.ex1 import Ui_Form
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import  QtWidgets,QtGui

class Exercise1View(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_Form()
        self._ui.setupUi(self)
        
        # self._ui.mainImage.setPixmap(QtGui.QPixmap("./resources/images/test.jpg"))
        # self._ui.answer1.setPixmap(QtGui.QPixmap("./resources/images/1.png"))
        # self._ui.answer2.setPixmap(QtGui.QPixmap("./resources/images/1.png"))
        # self._ui.answer3.setPixmap(QtGui.QPixmap("./resources/images/1.png"))
        # self._ui.answer4.setPixmap(QtGui.QPixmap("./resources/images/1.png"))
        # self._ui.answer5.setPixmap(QtGui.QPixmap("./resources/images/1.png"))

        # self._ui.mainImage.setScene(item)
        

        

        # pic.setPixmap(QPixmap.fromImage(self.image_qt))

    
        ################################################################################################
        # # connect widgets to controller
        self._ui.answer1.clicked.connect(lambda: self._main_controller.clickLabel(self._ui.answer1.objectName()))
        self._ui.answer2.clicked.connect(lambda: self._main_controller.clickLabel(self._ui.answer2.objectName()))
        self._ui.answer3.clicked.connect(lambda: self._main_controller.clickLabel(self._ui.answer3.objectName()))
        self._ui.answer4.clicked.connect(lambda: self._main_controller.clickLabel(self._ui.answer4.objectName()))
        self._ui.answer5.clicked.connect(lambda: self._main_controller.clickLabel(self._ui.answer5.objectName()))
        # self._ui.clearMenu.clicked.connect(lambda: self._main_controller.clearClicked())
        # self._ui.saveMenu.clicked.connect(lambda:  self._main_controller.saveClicked(self._ui.name.toPlainText(),self._ui.surname.toPlainText(),self._ui.ageTextBox.toPlainText()))
        
        # self._ui.selectExersiceButton.clicked.connect(lambda:  self._main_controller.selectButtonClicked(''+self._ui.selectExercise.currentText()) )
        
        

        # self._ui.selectExercise.addItems(self._model.listAvailableExersice)

        #################################################################################################
        # # listen for model event signals
        # self._model.amount_changed.connect(self.on_amount_changed)
        # self._model.even_odd_changed.connect(self.on_even_odd_changed)
        # self._model.enable_reset_changed.connect(self.on_enable_reset_changed)

        # set a default value
        #self._main_controller.change_amount(42)

    # @pyqtSlot(int)
    # def on_name_changed(self, value):
    #     print('Set Text')
    #     self._ui.name.setText('.....')

    # @pyqtSlot(str)
    # def on_even_odd_changed(self, value):
    #     self._ui.label_even_odd.setText(value)

    # @pyqtSlot(bool)
    # def on_enable_reset_changed(self, value):
    #     self._ui.pushButton_reset.setEnabled(value)
