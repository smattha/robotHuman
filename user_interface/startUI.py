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
from views.start import Ui_MainWindow
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
import signal
import psutil

from sys import exit

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.motorOnline=True

        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.MainWindow.show()
        self.ui.visionStart.clicked.connect(self.startVision)
        self.ui.visionStop.clicked.connect(self.stopVision)

        self.ui.robotFaceStart.clicked.connect(self.startFace)
        self.ui.robotFaceStop.clicked.connect(self.stopFace)


        self.ui.s2tStart.clicked.connect(self.s2tStart)
        self.ui.s2tStop.clicked.connect(self.s2tStop)


        self.ui.t2sStart.clicked.connect(self.t2SStart)
        self.ui.t2sStop.clicked.connect(self.t2SStop)


        self.ui.motorStart.clicked.connect(self.motorStart)
        self.ui.motorStop.clicked.connect(self.motorStop)
        
        self.ui.uiStart.clicked.connect(self.uiStart)
        self.ui.uiStop.clicked.connect(self.uiStop)

        self.ui.trainingStart.clicked.connect(self.trainingStart)
        self.ui.trainingStop.clicked.connect(self.trainingStop)


        self.ui.startAll.clicked.connect(self.startAll)
        self.ui.stopAll.clicked.connect(self.stopAll)

        self.ui.actionOffine.triggered.connect(self.motorChangeFlaq)


        self.ui.roscore.clicked.connect(self.roscore)

    
    def motorChangeFlaq(self):
        self.motorOnline=not self.motorOnline

    def startAll(self):
        self.roscore()
        self.startFace()
        self.s2tStart()
        self.startVision()
        self.t2SStart()
        self.uiStart()
        self.motorStart()

    def stopAll(self):
        self.stopFace()
        self.s2tStop()
        self.stopVision()
        self.s2tStop()
        self.uiStop()
        self.motorStop()


    def kill(self,proc_pid):
        process = psutil.Process(proc_pid)
        for proc in process.children(recursive=True):
            proc.kill()
        process.kill()
            

    def roscore(self):
        self.faceP=subprocess.Popen(["killall -9 rosmaster",
               "arguments"], shell=True, preexec_fn=os.setsid) 
        self.faceP=subprocess.Popen(["roscore",
               "arguments"], shell=True, preexec_fn=os.setsid) 

    def startFace(self):
        self.faceP=subprocess.Popen(["rosrun robot_face robot_face1.py  1 1 p",
               "arguments"], shell=True, preexec_fn=os.setsid) 

    def stopVision(self):
        result = subprocess.run(["rosservice call /shutdown \"input: ''\" "], shell=True, capture_output=True, text=True)
        # self.kill(self.faceP.pid) 


        self.kill(self.visionP.pid) 

    def startVision(self):
        print ("startVision")
        self.visionP=subprocess.Popen(["rosrun unifiedGestureFingertipDetection real-time2.py --detector /robotApp/face_detection_model  --embedding /robotApp/face_rec/openface_nn4.small2.v1.t7   --recognizer /robotApp/outpout9/recognizer.pickle   --le /robotApp/outpout9/le.pickle --faceNew /robotApp/faceNew/",
               "arguments"], shell=True, preexec_fn=os.setsid) 

    def stopFace(self):
        result = subprocess.run(["rosnode kill /robot_face"], shell=True, capture_output=True, text=True)
        self.kill(self.faceP.pid) 

    def s2tStart(self):
        print ("rosrun audio_service test_microphone.py -m=/robotApp/model ")

        self.startS2Tn=subprocess.Popen(["rosrun audio_service audioServiceBlocking.py",
               "arguments"], shell=True, preexec_fn=os.setsid) 

    def s2tStop(self):
        self.kill(self.startS2Tn.pid) 



    def t2SStart(self):
        print ("rosrun audio_service audioServiceBlocking.py")
        self.t2SStartP=subprocess.Popen(["rosrun audio_service audioServiceBlocking.py",
               "arguments"], shell=True, preexec_fn=os.setsid) 

    def t2SStop(self):
        result = subprocess.run(["rosnode kill /speechToTextBlocking"], shell=True, capture_output=True, text=True)
        self.kill(self.t2SStartP.pid)  


    def motorStart(self):
        print ("rosrun motors_controller motors_controller_ros1.py False"+str(self.motorOnline))
        if (self.motorOnline):
            self.motorStartP=subprocess.Popen(["rosrun motors_controller motors_controller_ros1.py False",
               "arguments"], shell=True, preexec_fn=os.setsid) 
        else:
            self.motorStartP=subprocess.Popen(["rosrun motors_controller motors_controller_ros1.py True",
               "arguments"], shell=True, preexec_fn=os.setsid) 

    def motorStop(self):
        result = subprocess.run(["rosnode kill /motors_controller_ros_intf"], shell=True, capture_output=True, text=True)
        self.kill(self.motorStartP.pid)


    def uiStart(self):
        print ("rosrun user_interface mainMenu.py /robotApp 1 1 p")
        self.uiP=subprocess.Popen(["rosrun user_interface mainMenu.py /robotApp 1 1 p",
               "arguments"], shell=True, preexec_fn=os.setsid) 

    def uiStop(self):
        self.kill(self.uiP.pid)
        
    def trainingStart(self):
        print ("roslaunch unifiedGestureFingertipDetection train.launch")
        self.trainingStartP=subprocess.Popen(["roslaunch unifiedGestureFingertipDetection train.launch",
               "arguments"], shell=True, preexec_fn=os.setsid) 

    def trainingStop(self):
        self.kill(self.trainingStartP.pid)
        
if __name__ == '__main__':
    try:
        app = App(sys.argv)
        app.exec_()
        print('Application is up and running')
    except KeyboardInterrupt:
        exit(0)