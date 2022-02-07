#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication
from model.mainWindowModel import MainWindowModel
from controllers.menuCntl import MenuCntl
from controllers.ex1Cntrl import Ex1Cntrl
from views.menuView import MenuView
from views.ex1 import Exercise1View

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = MainWindowModel()
        self.main_controller = MenuCntl(self.model)
        self.menu_view =MenuView(self.model, self.main_controller)
        self.menu_view.show()
        # self.main_view = MenuView(self.model, self.main_controller)

        # self.ex1_controller = Ex1Cntrl(self.model)
        # # self.ex1_view = Exercise1View(self.model, self.ex1_controller)
        # self.ex1_view.show()

class Ex(QApplication):
    def __init__(self, sys_argv):
        super(Ex, self).__init__(sys_argv)
        self.model = MainWindowModel()
        # self.main_view = MenuView(self.model, self.main_controller)

        self.ex1_controller = Ex1Cntrl(self.model)
        self.ex1_view = Exercise1View(self.model, self.ex1_controller)
        self.ex1_view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    print('hello!!')
    app.exec_()
    ex = Ex(sys.argv)
    print('hello!!')
    ex.exec_()