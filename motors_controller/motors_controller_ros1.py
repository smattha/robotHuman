#!/usr/bin/env python3
import sys
from motors_controller.srv import *
import rospy 
import time
from motorController.MotorController import MoveController
from threading import Thread

NAME = 'motors_controller_ros_intf'
SRVNAME=NAME+'_srv_abs'
SRVNAME_2=NAME+'_srv_file'
class motor_ros:
    def move_abs_service(self,req):
        print (req.a)   
    
        self.motor.getPosition(int(1))
        self.motor.moveAbs(req.a,self.motor.leftHand)
        self.motor.moveAbs(req.b,self.motor.rightHand)
        self.motor.moveAbs(req.c,self.motor.rightShoulder)
        self.motor.moveAbs(req.d,self.motor.leftShoulder)
        self.motor.moveAbs(req.e,self.motor.torso)
        self.motor.moveAbs(req.f,self.motor.head)

        return motors_controllerResponse(1)

    def moveRobotFileThread(self,req):
        print ("!!!!!!!!!!!!!!!!!!!!!!!1")
        print (req.name)   
        f = open(req.name, "r")
        for x in f:
            print("     New line")
   
            lineSplited=x.split(',')
            print(''.join(lineSplited)+' '+str(len(lineSplited))) 
            if (lineSplited[0]=='sleep'):
                print("Sleeping for ",lineSplited[1])
                time.sleep(int(lineSplited[1])/1000)
                # motors1=lineSplited/2
            elif (len(lineSplited)==16):
                print("             Moving to position "+str(lineSplited[0])+" "+str(lineSplited[1])+" "+str(lineSplited[2])+" "+str(lineSplited[3])+" "+str(lineSplited[4])+" "+str(lineSplited[5]))
                # self.motor.getPosition(1))
                self.motor.moveAbsStr(lineSplited[0],self.motor.leftHand,lineSplited[8])
                self.motor.moveAbsStr(lineSplited[1],self.motor.rightHand,lineSplited[9])
                self.motor.moveAbsStr(lineSplited[2],self.motor.rightShoulder,lineSplited[10])
                self.motor.moveAbsStr(lineSplited[3],self.motor.leftShoulder,lineSplited[11])
                self.motor.moveAbsStr(lineSplited[4],self.motor.torso,lineSplited[12])
                self.motor.moveAbsStr(lineSplited[5],self.motor.head,lineSplited[13])
                self.motor.moveAbsStr(lineSplited[6],self.motor.torso,lineSplited[14])
                self.motor.moveAbsStr(lineSplited[7],self.motor.head,lineSplited[15])
            else:
                print("Error!!!!!")
        print ("Done!!!")

    def moveRobotFile(self,req):
        thread = Thread(target=self.moveRobotFileThread, args=(req,), daemon=True)
        # if hasattr(self, "threadID"):
        #     self
        self.threadID=thread.start()
        print("Thread started")

        return moveRobotFileResponse(1)

    def add_two_ints_server(self,motorsSimulation):
        print('Initialize node of motor controller')
        self.motor=MoveController(motorsSimulation)
        rospy.init_node(NAME)
        s = rospy.Service(SRVNAME_2, moveRobotFile,self.moveRobotFile)
        s = rospy.Service(SRVNAME, motors_controller,self.move_abs_service)
        print('Ready to receive!')
        
        rospy.spin()

def destroy(req):
	print ("destroy")
	rospy.signal_shutdown("test")
	print ("Done")
	return shutdownSrvResponse("")

if __name__ == "__main__":
    motorsRosInterface=motor_ros()

    if (len(sys.argv)>1):
            rospy.logerr('.....................................................')
            if (sys.argv[1]=='False'):
                motorsSimulation=False
            else:
                motorsSimulation=True
    else:
            motorsSimulation=True
    

    rospy.Service('shutdownMotor', shutdownSrv,destroy)
    rospy.logerr(motorsSimulation)  
    motorsRosInterface.add_two_ints_server(motorsSimulation)