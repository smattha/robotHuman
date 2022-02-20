#!/usr/bin/env python3

from pyexpat import model
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from model.mainWindowModel import MainWindowModel
from controllers.menuCntl import MenuCntl
from controllers.ex1Cntrl import Ex1Cntrl
from views.menuView import MenuView
from exersiceController.ControllerExersice1 import ControllerExersice1
from exersiceController.ControllerExersice2 import ControllerExersice2
from exersiceController.ControllerExersice3 import ControllerExersice3
from exersiceController.ControllerExersice4 import ControllerExersice4
from exersiceController.ControllerExersice5 import ControllerExersice5
from exersiceController.ControllerExersice6 import ControllerExersice6
from rosInterface.audioServiceInterface import Ros_Audio_Service
from signal import signal, SIGINT
from sys import exit

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model= MainWindowModel()
        
        self._rosInterface=Ros_Audio_Service()
        self._controllerEx1= ControllerExersice1(self._rosInterface,self.model)
        self._controllerEx2= ControllerExersice2(self._rosInterface,self.model)
        self._controllerEx3= ControllerExersice3(self._rosInterface,self.model)
        self._controllerEx4= ControllerExersice4(self._rosInterface,self.model)
        self._controllerEx5= ControllerExersice5(self._rosInterface,self.model)
        self._controllerEx6= ControllerExersice6(self._rosInterface,self.model)
        self.main_controller = MenuCntl(self.model,[self._controllerEx1,self._controllerEx2,self._controllerEx3,self._controllerEx4,self._controllerEx5,self._controllerEx6])
        self.menu_view =MenuView(self.model, self.main_controller)
        # self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 40, 811, 531))
        self.menu_view.show()
        # self.main_view = MenuView(self.model, self.main_controller)
        # self.ex1_controller = Ex1Cntrl(self.model)
        # # self.ex1_view = Exercise1View(self.model, self.ex1_controller)
        # self.ex1_view.show()

def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

if __name__ == '__main__':
    
    app = App(sys.argv)
    print('Application is up and running')
    app.exec_()
