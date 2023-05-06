#!/usr/bin/env python3
from motorController.Ax12 import Ax12
import threading 
import time 
class MoveController():
        def __init__(self,offline):


            servo_list = [1, 2, 3, 4, 5, 6]  # servo Ids from left to right


            print ( 'Initialize move controller in offline '+str(True))
            super().__init__()
            self.offline=offline
            self.counterForRandomPos=0;

            self.leftHand=1
            self.rightHand=2
            self.rightShoulder=3
            self.leftShoulder=5
            self.torso=4
            self.head=6

            self.speed=85

            self.lock = threading.Lock()

            self.right_hand = Ax12(self.leftHand)
            self.right_shoulder = Ax12(self.rightShoulder)
            self.neck = Ax12(self.torso)
            self.neck_tilt = Ax12(self.head)
            self.left_shoulder = Ax12( self.leftShoulder)
            self.left_hand = Ax12(self.leftHand)

            if self.offline== False:
            
                # e.g 'COM3' windows or '/dev/ttyUSB0' for Linux
                #Ax12.DEVICENAME = '/dev/ttyACM1'
                Ax12.DEVICENAME = '/dev/ttyACM0'
                Ax12.BAUDRATE = 1_000_000
                Ax12.connect()

        def moveMotorsAbs(self,a,b,c,d,e,f):
            self.moveAbs(a,self.leftHand)
            self.moveAbs(b,self.rightHand)
            self.moveAbs(c,self.rightShoulder)
            self.moveAbs(d,self.leftShoulder)
            self.moveAbs(e,self.torso)
            self.moveAbs(f,self.head)

        def moveMotors(self,a,b,c,d,e,f):
            self.move(self.leftHand,a)
            self.move(self.rightHand,b)
            self.move(self.rightShoulder,c)
            self.move(self.leftShoulder,d)
            self.move(self.torso,e)
            self.move(self.head,f)


        def getPosition(self,motor_id):
            self.lock.acquire()
            if self.offline==True:
                self.counterForRandomPos=self.counterForRandomPos+1
                self.lock.release()
                return 10000*motor_id+self.counterForRandomPos
            my_dxl2 = Ax12(motor_id)
            my_dxl2.set_moving_speed(self.speed)
            my_dxl2.set_led(0)
            print("\nPosition of dxl ID: %d is %d " %
                    (my_dxl2.id, my_dxl2.get_present_position()))
            # my_dxl2.set_torque_enable(0)
            pos=my_dxl2.get_present_position()
            self.lock.release()
            time.sleep(0.01)
            return pos


        def disconnect(self):
            Ax12.disconnect()
        
        def move(self,motor_id,input_pos):
                self.lock.acquire()
                print("Move motor" , str(motor_id) , " by  " ,str(input_pos))
                if self.offline==False:
                    my_dxl2 = Ax12(motor_id)
                    my_dxl2.set_goal_position(my_dxl2.get_present_position()+input_pos)
                    my_dxl2.set_moving_speed(85)
                    time.sleep(0.08)
                self.lock.release()
                
                    
        def moveAbs(self,input_pos,motor_id):
                self.lock.acquire()
                print("Move motor" , str(motor_id) , " to pos  " ,str(input_pos))
                if self.offline==False:
                    my_dxl2 = Ax12(motor_id)
                    my_dxl2.set_goal_position(input_pos)
                    my_dxl2.set_moving_speed(85)
                self.lock.release()
                time.sleep(0.05)

        def rotate(self):
            print('inside rotate1')

            self.neck.set_moving_speed(100)
            
            self.neck.set_goal_position(650)
            time.sleep(1)
            self.neck.set_goal_position(850)
            time.sleep(1)
                
        def tilt(self):
            print('inside tilt1')
            self.neck_tilt.set_moving_speed(100)
            self.neck_tilt.set_goal_position(900)            # 853-1023 , goes up
            time.sleep(1)
            self.neck_tilt.set_goal_position(1000)
            time.sleep(1)
            
        def rotate_tilt(self):
            print('inside rotate_tilt')
            
            self.neck_tilt.set_moving_speed(100)
            self.neck.set_moving_speed(100)

            self.neck_tilt.set_goal_position(900)            # 853-1023 , goes up
            self.neck.set_goal_position(650)
            time.sleep(1.5)
            self.neck_tilt.set_goal_position(1000)
            self.neck.set_goal_position(850)
            time.sleep(1.5)
            #time.sleep(.5)
            #self.neck.set_goal_position(720)
                
        def rshoulderupdown(self):
            print('inside rshoulderupdown')
            self.right_hand.set_goal_position(501)
            self.right_shoulder.set_moving_speed(100)
            self.right_shoulder.set_goal_position(100)
            time.sleep(1.5)
            self.right_shoulder.set_goal_position(1000)
            time.sleep(1.5)
            
            
        def rlshoulderupdown(self):
            print('inside rlshoulderupdown')
            self.right_shoulder.set_moving_speed(100)
            self.left_shoulder.set_moving_speed(100)
            self.right_hand.set_goal_position(501)
            self.left_hand.set_goal_position(550)    
            #down
            self.right_shoulder.set_goal_position(770)
            self.left_shoulder.set_goal_position(290)
            time.sleep(1.5)
            #up
            self.right_shoulder.set_goal_position(1020)
            self.left_shoulder.set_goal_position(55)
            time.sleep(1.5)
            
        def rlshoulderupdownoppose(self):
            print('inside rlshoulderupdownoppose')
            self.right_shoulder.set_moving_speed(100)
            self.left_shoulder.set_moving_speed(100)
            self.right_hand.set_goal_position(501)
            self.left_hand.set_goal_position(550)
            self.right_shoulder.set_goal_position(100)    # down
            self.left_shoulder.set_goal_position(50)      # up
            time.sleep(1)
            self.right_shoulder.set_goal_position(1000)   # up
            self.left_shoulder.set_goal_position(250)     # down
            time.sleep(1)
            
        def rhandleftright(self):
            print('inside rhandleftright')
            self.right_hand.set_moving_speed(100)
            
            self.right_hand.set_goal_position(500)
            time.sleep(1.5)
            self.right_hand.set_goal_position(800)
            time.sleep(1.5)
            time.sleep(.5)
            self.right_hand.set_goal_position(500)


        def complex2(self):
            print('inside complex2')
            
            self.right_hand.set_moving_speed(100)
            self.right_shoulder.set_moving_speed(100)
            self.neck.set_moving_speed(100)
            self.neck_tilt.set_moving_speed(100)
            self.left_shoulder.set_moving_speed(100)
            self.left_hand.set_moving_speed(100)
            

            self.right_hand.set_goal_position(450)            # 401-1023      inwards -> outwards
            self.right_shoulder.set_goal_position(700)        # 0-1023        down    -> up
            self.neck.set_goal_position(740)                  # 0-1023        right   -> left (from the robot's view)
            self.neck_tilt.set_goal_position(860)             # 853-1023      up      ->  down
            self.left_shoulder.set_goal_position(280)         # 0-300         down    -> up
            self.left_hand.set_goal_position(550)             # 0-614         outwards -> inwards
            
            time.sleep(1)
            
            self.right_hand.set_goal_position(900)
            self.right_shoulder.set_goal_position(1000)
            self.neck_tilt.set_goal_position(1020)
            self.neck.set_goal_position(850)
            self.left_shoulder.set_goal_position(100)
            self.left_hand.set_goal_position(350)
            time.sleep(1)
                
        def complex21(self):
            print('inside complex21')
            self.right_hand.set_moving_speed(100)
            self.right_shoulder.set_moving_speed(100)
            self.neck.set_moving_speed(100)
            self.neck_tilt.set_moving_speed(100)
            self.left_shoulder.set_moving_speed(100)
            self.left_hand.set_moving_speed(100)

            self.right_hand.set_goal_position(501)            # 401-1023      inwards -> outwards
            self.right_shoulder.set_goal_position(800)        # 0-1023        down    -> up
            self.neck.set_goal_position(650)                  # 0-1023        right   -> left (from the robot's view)
            self.neck_tilt.set_goal_position(853)             # 853-1023      up      ->  down
            self.left_shoulder.set_goal_position(280)         # 0-300         down    -> up
            self.left_hand.set_goal_position(550)             # 0-614         outwards -> inwards
            
            time.sleep(1.5)
            
            self.right_hand.set_goal_position(700)
            self.right_shoulder.set_goal_position(1000)
            self.neck_tilt.set_goal_position(1023)
            self.neck.set_goal_position(850)
            self.left_shoulder.set_goal_position(100)
            self.left_hand.set_goal_position(350)
            time.sleep(1.5)
            
        def complex3(self):
            print('inside complex3')
            self.right_hand.set_moving_speed(80)
            self.right_shoulder.set_moving_speed(80)
            #self.neck.set_moving_speed(80)
            #neck_tilt.set_moving_speed(80)
            self.left_shoulder.set_moving_speed(80)
            self.left_hand.set_moving_speed(80)

            self.right_hand.set_goal_position(501)            # 401-1023      inwards -> outwards
            self.right_shoulder.set_goal_position(800)        # 0-1023        down    -> up
            self.neck.set_goal_position(740)                  # 0-1023        right   -> left (from the robot's view)
            #neck_tilt.set_goal_position(853)             # 853-1023      up      ->  down
            self.left_shoulder.set_goal_position(280)         # 0-300         down    -> up
            self.left_hand.set_goal_position(550)             # 0-614         outwards -> inwards
            
            time.sleep(1.5)
            
            self.right_hand.set_goal_position(700)
            self.right_shoulder.set_goal_position(1000)
            #neck_tilt.set_goal_position(1023)
            #neck.set_goal_position(850)
            self.left_shoulder.set_goal_position(100)
            self.left_hand.set_goal_position(350)
            time.sleep(1.5)
            
        def shouldersmiddlehandsmove(self):
            print('inside shouldersmiddlehandsmove')
            self.right_hand.set_moving_speed(150)
            self.right_shoulder.set_moving_speed(100)
            self.left_hand.set_moving_speed(150)
            self.left_shoulder.set_moving_speed(100)
            
            self.right_shoulder.set_goal_position(800)        # 0-1023
            self.left_shoulder.set_goal_position(300)         # 0-300
            #hands inwards
            self.right_hand.set_goal_position(501)            # 401-1023
            self.left_hand.set_goal_position(550)             # 0-614
            time.sleep(1.5)
            #hands outwards
            self.right_hand.set_goal_position(950)
            self.left_hand.set_goal_position(100)
            time.sleep(1.5)
            
        def shouldersuphandsmove(self):
            print('inside shouldersuphandsmove')
            self.right_hand.set_moving_speed(150)
            self.right_shoulder.set_moving_speed(100)
            self.left_hand.set_moving_speed(150)
            self.left_shoulder.set_moving_speed(100)
            
            self.right_shoulder.set_goal_position(1000)        # 0-1023
            self.left_shoulder.set_goal_position(50)         # 0-300
            #hands inwards
            self.right_hand.set_goal_position(501)            # 401-1023
            self.left_hand.set_goal_position(550)             # 0-614
            time.sleep(1.5)
            #hands outwards
            self.right_hand.set_goal_position(950)
            self.left_hand.set_goal_position(100)
            time.sleep(1.5)
            



