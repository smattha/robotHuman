#!/usr/bin/env python3
import sys
from motors_controller.srv import *
import rospy 
from motorController.MotorController import MoveController

NAME = 'motors_controller_ros_intf'
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

        return motors_controllerResponse(1)

    def add_two_ints_server(self,motorsSimulation):
        print('Initialize node of motor controller')
        self.motor=MoveController(motorsSimulation)
        rospy.init_node(NAME)
        
        s = rospy.Service(SRVNAME, motors_controller,self.move_abs_service)
        print('Ready to receive!')
        
        rospy.spin()

if __name__ == "__main__":
    motorsRosInterface=motor_ros()

    if (len(sys.argv)>1):
            rospy.logerr('2222222222222......................................................')
            if (sys.argv[1]=='False'):
                motorsSimulation=False
            else:
                motorsSimulation=True
    else:
            motorsSimulation=True
    

    rospy.logerr(motorsSimulation)  
    motorsRosInterface.add_two_ints_server(motorsSimulation) 
