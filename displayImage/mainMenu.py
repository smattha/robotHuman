#!/usr/bin/env python3

import sys
from xmlrpc.client import boolean
from PyQt5.QtWidgets import QApplication
from views.menuView import MenuView
from rosInterface.audioServiceInterface import Ros_Audio_Service
# from motor.MotorController import MoveController
from motorController.MotorController import MoveController

from sys import exit
import time
class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)

        motor=MoveController(False);
        
        # motor.rotate()
        #motor.complex2()
        # motor.complex21()
        # motor.complex3()
        #motor.rlshoulderupdown()
        # motor.rlshoulderupdownoppose()
        # motor.rshoulderupdown()
        # motor.rotate()
        # motor.rotate_tilt()
        # motor.shouldersuphandsmove()
        

        motor.moveMotorsAbs(180,	433,818,196,818,572)
        time.sleep(2)

        motor.moveMotorsAbs(51	,229,	760,	239,	573,	714)
        time.sleep(2)
        motor.moveMotorsAbs(55,	449,	809,	131,	712,	882)
        
        motor.moveMotors(20,	10,0,0,0,0)
        time.sleep(0.2)
        motor.moveMotors(-20,	-10,0,0,0,0)
        time.sleep(0.1)
        motor.moveMotors(20,	10,0,0,0,0)
        time.sleep(0.2)
        motor.moveMotors(-20,	-10,0,0,0,0)

        time.sleep(0.2)
        motor.moveMotors(0,	0,0,0,0,30)
        time.sleep(0.2)
        motor.moveMotors(0,	0,0,0,0,-30)

        time.sleep(0.2)
        motor.moveMotors(0,	0,0,0,0,50)
        time.sleep(0.2)
        motor.moveMotors(0,	0,0,0,0,-50)
        
        time.sleep(0.2)
        motor.moveMotors(0,	0,0,0,50,0)
        time.sleep(0.2)
        motor.moveMotors(0,	0,0,0,-50,0)
    

        time.sleep(0.2)
        motor.moveMotors(25,	25,25,25,100,20)

        time.sleep(0.3)
        motor.moveMotors(-20,	-20,-20,-20,-20,-20)

        time.sleep(1)
        
        motor.moveMotorsAbs(180,	433,818,196,818,572)

        self.menu_view =MenuView(motor)
        self.menu_view.show()


if __name__ == '__main__':
    try:
        app = App(sys.argv)
        app.exec_()

        print('Application is up and running')
    except KeyboardInterrupt:
        exit(0)