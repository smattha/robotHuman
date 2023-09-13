#!/usr/bin/env python3

from pyexpat import model
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from exersiceDigitSpan.exersiceB import ExersiceB
from exersiceC import ExersiceC

from sys import exit

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)


        self.menu_view =ExersiceC(sys.argv[1])
        self.menu_view.show()


if __name__ == '__main__':
    try:
        app = App(sys.argv)
        print ('----------------------|'+sys.argv[1]+'|')
        app.exec_()
        print('Application is up and running')
    except KeyboardInterrupt:
        exit(0)