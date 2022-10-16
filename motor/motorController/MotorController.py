from motorController.Ax12 import Ax12
import threading 

class MoveController():
        def __init__(self,offline):

            print ( 'Initialize move controller in offline '+str(True))
            super().__init__()
            self.offline=offline
            self.counterForRandomPos=0;

            self.leftHand=0
            self.rightHand=1
            self.rightShoulder=3
            self.leftShoulder=5
            self.torso=4
            self.head=6

            self.speed=85

            self.lock = threading.Lock()

            if self.offline== False:
            
                # e.g 'COM3' windows or '/dev/ttyUSB0' for Linux
                #Ax12.DEVICENAME = '/dev/ttyACM1'
                Ax12.DEVICENAME = '/dev/ttyACM0'
                Ax12.BAUDRATE = 1_000_000

                # sets baudrate and opens com port
                Ax12.connect()


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
            my_dxl2.set_torque_enable(0)
            pos=my_dxl2.get_present_position()
            self.lock.release()
            return pos


        def disconnect():
            Ax12.disconnect()
        
        def move(self,motor_id,input_pos):
                self.lock.acquire()
                print("Move motor" , str(motor_id) , " by  " ,str(input_pos))
                if self.offline==False:
                    my_dxl2 = Ax12(motor_id)
                    my_dxl2.set_goal_position(my_dxl2.get_present_position()+input_pos)
                    my_dxl2.set_moving_speed(85)
                self.lock.release()
                    
        def moveAbs(self,input_pos,motor_id):
                self.lock.acquire()
                print("Move motor" , str(motor_id) , " to pos  " ,str(input_pos))
                if self.offline==False:
                    my_dxl2 = Ax12(motor_id)
                    my_dxl2.set_goal_position(input_pos)
                    my_dxl2.set_moving_speed(85)
                self.lock.release()





