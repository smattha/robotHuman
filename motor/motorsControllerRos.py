#!/usr/bin/env python3
import sys
from motor.srv import *
import rospy 
from motorController.MotorController import MoveController

NAME = 'motors_controller_ros_interface'
SRVNAME=NAME+'_srv_abs'
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

        return motorResponse(1)

    def add_two_ints_server(self,motorsSimulation):
        print('Initialize node of motor controller')
        self.motor=MoveController(motorsSimulation)
        rospy.init_node(NAME)
        s = rospy.Service(SRVNAME, motor, self.move_abs_service)
        print('Ready to receive!')
        

        # spin() keeps Python from exiting until node is shutdown
        rospy.spin()

if __name__ == "__main__":
    motorsRosInterface=motor_ros()

    
    rospy.logerr(len(sys.argv))
    rospy.logerr(sys.argv[1])
    


    if (len(sys.argv)>1):
            rospy.logerr('2222222222222......................................................')
            # motorsSimulation = bool(sys.argv[1])
            if (sys.argv[1]=='False'):
                motorsSimulation=False
            else:
                motorsSimulation=True
    else:
            motorsSimulation=True
    

    rospy.logerr(motorsSimulation)
    
    motorsRosInterface.add_two_ints_server(motorsSimulation) 
