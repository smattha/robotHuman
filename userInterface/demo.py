#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication
from model.model import Model
from controllers.main_ctrl import MainCntl
from views.menu import MainView


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.main_controller = MainCntl(self.model)
        self.main_view = MainView(self.model, self.main_controller)
        self.main_view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    print('hello!!')
    sys.exit(app.exec_())