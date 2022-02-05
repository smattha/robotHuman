#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication
from model.mainWindowModel import MainWindowModel
from controllers.menuCntl import MenuCntl
from views.menuView import MenuView


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = MainWindowModel()
        self.main_controller = MenuCntl(self.model)
        self.main_view = MenuView(self.model, self.main_controller)
        self.main_view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    print('hello!!')
    sys.exit(app.exec_())