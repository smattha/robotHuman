
from pickle import TRUE
from tkinter import FALSE
from motor.Ax12 import Ax12

class MotorTest():
        def __init__(self):
            super().__init__()
            self.offline=TRUE
            self.pos=0;
            if self.offline== FALSE:
            
                # e.g 'COM3' windows or '/dev/ttyUSB0' for Linux
                #Ax12.DEVICENAME = '/dev/ttyACM1'
                Ax12.DEVICENAME = '/dev/ttyACM0'
                Ax12.BAUDRATE = 1_000_000

                # sets baudrate and opens com port
                Ax12.connect()


        def getPosition(self,motor_id):
            if self.offline==TRUE:
                self.pos=self.pos+1
                return 10000*motor_id+self.pos
            my_dxl2 = Ax12(motor_id)
            my_dxl2.set_moving_speed(85)
            my_dxl2.set_led(0)
            print("\nPosition of dxl ID: %d is %d " %
                    (my_dxl2.id, my_dxl2.get_present_position()))
            my_dxl2.set_torque_enable(0)
            return my_dxl2.get_present_position()

        def disconnect():
            Ax12.disconnect()
        
        def move(self,motor_id,input_pos):
                print("Move motor "+ str(motor_id)+ " "+ str(input_pos))
                if self.offline==FALSE:
                    my_dxl2 = Ax12(motor_id)
                    my_dxl2.set_goal_position(my_dxl2.get_present_position()+input_pos)
                    my_dxl2.set_moving_speed(85)
                    

# # create AX12 instance with ID 10
# motor_id = 0
# my_dxl = Ax12(motor_id)
# my_dxl.set_moving_speed(5)
# my_dxl.set_led(0)
# # my_dxl.set_goal_position(400)


# motor_id = 1
# my_dxl2 = Ax12(motor_id)
# my_dxl2.set_moving_speed(5)
# my_dxl2.set_led(0)




# print("\nPosition of dxl ID: %d is %d " %
#               (my_dxl.id, my_dxl.get_present_position()))

# print("\nPosition of dxl ID: %d is %d " %
#               (my_dxl2.id, my_dxl2.get_present_position()))

# my_dxl.set_goal_position(100)

# my_dxl2.set_goal_position(450)





# def user_input():
#     """Check to see if user wants to continue"""
#     ans = input('Continue? : y/n ')
#     if ans == 'n':
#         return False
#     else:
#         return True


# def main(motor_object):
#     """ sets goal position based on user input """
#     bool_test = True
#     while bool_test:

#         print("\nPosition of dxl ID: %d is %d " %
#               (motor_object.id, motor_object.get_present_position()))
#         # desired angle input
#         input_pos = int(input("goal pos: "))
#         motor_object.set_goal_position(input_pos)
#         print("Position of dxl ID: %d is now: %d " %
#               (motor_object.id, motor_object.get_present_position()))
#         bool_test = user_input()


# # pass in AX112 object
# main(my_dxl)

# # disconnect
# my_dxl.set_torque_enable(0)
# Ax12.disconnect()
