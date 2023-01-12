#!/usr/bin/env python3

import cv2
from displayImage.srv import *
import rospy 
from threading import Thread
import time


imagePath='/home/stergios/Downloads/1.jpeg'
sleepTime=1

def add_two_ints(req):
    global imagePath
    print ('Services called. Image path is ' + req.name)
    imagePath=req.name
    time.sleep(sleepTime)
    return imageNameResponse(1)

def displayImageFunction():
        while 1==1:
            time.sleep(sleepTime)
            img = cv2.imread(imagePath, cv2.IMREAD_COLOR)
            cv2.imshow("image", img)
            print('name '+imagePath)
            cv2.waitKey(100)


def add_two_ints_server():
    rospy.init_node('..')
    s = rospy.Service('add_two_ints', imageName, add_two_ints)
    rospy.spin()

if __name__ == "__main__":
    thread = Thread(target=displayImageFunction, args=(), daemon=True)
    thread.start()
    print("Display image thread was started")
    add_two_ints_server()
        