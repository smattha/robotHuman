#!/usr/bin/env python3

from pyexpat import model
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from model.mainWindowModel import MainWindowModel
from controllers.menuCntl import MenuCntl
from views.menuView import MenuView
from exersiceController.ControllerType1 import ControllerType1
from exersiceController.ControllerType2 import ControllerType2
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
        
        
        self._controllerEx1= ControllerType1(self._rosInterface,self.model)
        self._controllerEx1.setVariable1()

        self._controllerEx2= ControllerType1(self._rosInterface,self.model)
        self._controllerEx2.setVariable2()

        self._controllerEx3= ControllerType2(self._rosInterface,self.model)
        self._controllerEx3.setVariables3()

        self._controllerEx4= ControllerType2(self._rosInterface,self.model)
        self._controllerEx4.setVariables4()

        self._controllerEx5= ControllerExersice5(self._rosInterface,self.model)
        self._controllerEx5.setVariable1()

        self._controllerEx6= ControllerExersice6(self._rosInterface,self.model)
        self._controllerEx6.setVariable6()




        self._controllerEx7= ControllerType1(self._rosInterface,self.model)
        self._controllerEx7.setVariableB1()

        self._controllerEx8= ControllerType1(self._rosInterface,self.model)
        self._controllerEx8.setVariableB2()

        self._controllerEx9= ControllerType2(self._rosInterface,self.model)
        self._controllerEx9.setVariablesB3()

        self._controllerEx10= ControllerType2(self._rosInterface,self.model)
        self._controllerEx10.setVariablesB4()

        self._controllerEx11= ControllerExersice5(self._rosInterface,self.model)
        self._controllerEx11.setVariable2()

        self._controllerEx12= ControllerExersice6(self._rosInterface,self.model)
        self._controllerEx12.setVariable6B()

        self.main_controller = MenuCntl(self.model,[self._controllerEx1,self._controllerEx2,self._controllerEx3,self._controllerEx4,self._controllerEx5,self._controllerEx6,
                                                   self._controllerEx7,self._controllerEx8,self._controllerEx9,self._controllerEx10,self._controllerEx11,self._controllerEx12])
        self.menu_view =MenuView(self.model, self.main_controller)
        self.menu_view.show()


def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

if __name__ == '__main__':
    try:
        app = App(sys.argv)
        app.exec_()
        print('Application is up and running')
    except KeyboardInterrupt:
        exit(0)