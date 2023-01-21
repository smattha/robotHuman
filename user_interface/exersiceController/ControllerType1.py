#!/usr/bin/env python3

from threading import Thread
from exersiceController.RootController import RootController
from exersiceController.ControllerType1Data import  ControllerType1Data
class ControllerType1(RootController,ControllerType1Data):
    def __init__(self,ros,model):
        super().__init__()
        print("Initialize the controller for Excersice 1 ")
        self._rosInterface=ros
        self.mainPage=1
        self.model=model
        self._feedback=''
        self._imageAnswerFlag=0
        self._answerEx1=''
        self._feedback=''
        self.path=self.model.path










