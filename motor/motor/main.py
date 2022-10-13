#!/usr/bin/env python3
from Ax12 import Ax12

from range_limits import *
import time


#Ax12.DEVICENAME = serial_port
Ax12.DEVICENAME = '/dev/ttyACM0'
Ax12.BAUDRATE = 1_000_000

# sets baudrate and opens com port
Ax12.connect()


servo_list = [1, 2, 3, 4, 5, 6]  # servo Ids from left to right

right_hand = Ax12(servo_list[0])
right_shoulder = Ax12(servo_list[1])
neck = Ax12(servo_list[2])
neck_tilt = Ax12(servo_list[3])
left_shoulder = Ax12(servo_list[4])
left_hand = Ax12(servo_list[5])


def move_1():

    right_hand.set_moving_speed(200)
    right_shoulder.set_moving_speed(100)
    # neck.set_moving_speed(100)
    # neck_tilt.set_moving_speed(100)
    # left_shoulder.set_moving_speed(100)
    # left_hand.set_moving_speed(100)

    # right_hand.set_goal_position(501)
    # right_shoulder.set_goal_position(866)
    # neck.set_goal_position(0)
    # neck_tilt.set_goal_position(1023)
    # left_shoulder.set_goal_position(221)
    # left_hand.set_goal_position(544)


def move_2():

    right_hand.set_moving_speed(200)
    right_shoulder.set_moving_speed(100)
    neck.set_moving_speed(100)
    neck_tilt.set_moving_speed(100)
    left_shoulder.set_moving_speed(100)
    left_hand.set_moving_speed(100)

    right_hand.set_goal_position(845)
    right_shoulder.set_goal_position(1023)
    neck.set_goal_position(162)
    neck_tilt.set_goal_position(894)
    left_shoulder.set_goal_position(65)
    left_hand.set_goal_position(295)


move_1()

time.sleep(3)
move_2()
Ax12.disconnect()

###################################################################################################################

