#!/usr/bin/env python3

from pyexpat import model
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from model.mainWindowModel import MainWindowModel
from controllers.MainMenuCntl import MainMenuCntl
from views.menuView import MenuView
from exersiceController.ControllerType1 import ControllerType1
from exersiceController.ControllerType2 import ControllerType2
from exersiceController.ControllerExersice5 import ControllerExersice5
from exersiceController.ControllerExersice6 import ControllerExersice6
from rosInterface.audioServiceInterface import Ros_Audio_Service

from sys import exit

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)

        self.path="/home/stergios/git/src/robotHuman"

        if (len(sys.argv)>=2):
            self.path =  sys.argv[1]
            self.i=int( sys.argv[2])
            self.displaymageRation=int(sys.argv[3])
            self.flag=sys.argv[4]
            print("...................")
        else:
            self.path = "/home/stergios/git/src/robotHuman"
            self.i=2
            self.displaymageRation=1
            self.flag="test"

        self.model= MainWindowModel( self.path)
        

        self.model.i= self.i
        self.model.displayImageRatio =self.displaymageRation


        # self._rosInterface=Ros_Audio_Service()
        # self._rosInterface.getText()
        # return
        

        # self._rosInterface.getRecognitionResult()

        #self._rosInterface.displayImg()

        self._rosInterface.flag=self.flag


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

        self.main_controller = MainMenuCntl(self.model,[self._controllerEx1,self._controllerEx2,self._controllerEx3,self._controllerEx4,self._controllerEx5,self._controllerEx6,
                                                   self._controllerEx7,self._controllerEx8,self._controllerEx9,self._controllerEx10,self._controllerEx11,self._controllerEx12])
        self.menu_view =MenuView(self.model, self.main_controller)
        self.menu_view.show()


if __name__ == '__main__':
    try:
        app = App(sys.argv)
        app.exec_()
        print('Application is up and running')
    except KeyboardInterrupt:
        exit(0)