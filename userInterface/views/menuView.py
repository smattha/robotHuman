from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from views.ui.menu import Ui_menuWindow


class MenuView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_menuWindow()
        self._ui.setupUi(self)

        ################################################################################################
        # # connect widgets to controller
        # #self._ui.spinBox_amount.valueChanged.connect(self._main_controller.change_amount)
        self._ui.clearMenu.clicked.connect(lambda: self._main_controller.clearClicked())
        self._ui.saveMenu.clicked.connect(lambda:  self._main_controller.saveClicked(self._ui.name.toPlainText(),self._ui.surname.toPlainText(),self._ui.ageTextBox.toPlainText()))
        
        self._ui.selectExersiceButton.clicked.connect( lambda: self.close() )        

        self._ui.selectExercise.addItems(self._model.listAvailableExersice)


        self._ui.selectExercise.currentIndexChanged.connect(lambda:  self._main_controller.selectButtonClicked(''+self._ui.selectExercise.currentText()) )        

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
