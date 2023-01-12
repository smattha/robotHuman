#!/usr/bin/env python3

# Python code to read image
import cv2
from displayImage.srv import *
import rospy 
from threading import Thread
import time
cv2.destroyAllWindows()

name='/home/stergios/Downloads/1.jpeg'

def add_two_ints(req):
    print (req.name)
    
    
    # To read image from disk, we use
    # cv2.imread function, in below method,
    # img = cv2.imread(req.name, cv2.IMREAD_COLOR)

    # Creating GUI window to display an image on screen
    # first Parameter is windows title (should be in string format)
    # Second Parameter is image array

    global name
    
    name=req.name
    # cv2.imshow(req.name, img)
    # print('111111111')

    # To hold the window on screen, we use cv2.waitKey method
    # Once it detected the close input, it will release the control
    # To the next line
    # First Parameter is for holding screen for specified milliseconds
    # It should be positive integer. If 0 pass an parameter, the it will
    # hold the screen until user close it.
    # cv2.waitKey(1000)
    # cv2.destroyAllWindows()
    # img = cv2.imread(name, cv2.IMREAD_COLOR)
    # cv2.imshow("image", img)
    # cv2.imshow("image", img)
    # cv2.waitKey(1000)
    # cv2.destroyAllWindows()
    # k = cv2.waitKey(0)
    # It is for removing/deleting created GUI window from screen
    # and memory

    return imageNameResponse(1)

def updatePosThread():
        while 1==1:
            time.sleep(1)
            img = cv2.imread(name, cv2.IMREAD_COLOR)
            cv2.imshow("image", img)
            print('name '+name)
            cv2.waitKey(1000)
            # cv2.destroyAllWindows()

def startUpdateThread():
        thread = Thread(target=updatePosThread, args=(), daemon=True)
        thread.start()
        print("Thread started")

def add_two_ints_server():
    rospy.init_node('..')
    s = rospy.Service('add_two_ints', imageName, add_two_ints)

      

    # spin() keeps Python from exiting until node is shutdown
    rospy.spin()

if __name__ == "__main__":
    startUpdateThread()
    add_two_ints_server()
        