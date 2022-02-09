#!/usr/bin/env python3

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from model.mainWindowModel import MainWindowModel
from controllers.menuCntl import MenuCntl
from controllers.ex1Cntrl import Ex1Cntrl
from views.menuView import MenuView
from exersiceController.ControllerExersice1 import ControllerExersice1
from rosInterface.audioServiceInterface import Ros_Audio_Service
from signal import signal, SIGINT
from sys import exit

class App(QApplication):
    def __init__(self, sys_argv,model):
        super(App, self).__init__(sys_argv)
        self.model=model
        
        self._rosInterface=Ros_Audio_Service()
        self._controllerEx1= ControllerExersice1(self._rosInterface)
        self.main_controller = MenuCntl(self.model,self._controllerEx1)
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
    model = MainWindowModel()
    app = App(sys.argv,model)
    print('Starting main menu!!')
    app.exec_()
