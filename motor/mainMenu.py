#!/usr/bin/env python3

import sys
from xmlrpc.client import boolean
from PyQt5.QtWidgets import QApplication
from views.menuView import MenuView
from rosInterface.audioServiceInterface import Ros_Audio_Service
# from motor.MotorController import MoveController
from motorController.MotorController import MoveController

from sys import exit

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)

        motor=MoveController(True);
        
        self.menu_view =MenuView(motor)
        self.menu_view.show()


if __name__ == '__main__':
    try:
        app = App(sys.argv)
        app.exec_()

        print('Application is up and running')
    except KeyboardInterrupt:
        exit(0)