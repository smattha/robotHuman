#!/usr/bin/env python3

import cv2
from robot_face.srv import *
import rospy 
from threading import Thread
import time



sleepTime=1

def changeImg(req):
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
    rospy.init_node('robot_face')
    s = rospy.Service('robot_face_srv', imageName, changeImg)
    rospy.spin()


def destroy(req):
	print ("destroy")
	rospy.signal_shutdown("test")
	print ("Done")
	return shutdownSrvResponse("")

if __name__ == "__main__":
    global imagePath
    imagePath='/home/stergios/Downloads/1.jpeg'
    if (len(sys.argv)>1):
      imagePath=sys.argv[1]
      imagePath=imagePath+'/resources/faces/main.png'
    thread = Thread(target=displayImageFunction, args=(), daemon=True)
    thread.start()
    
    rospy.Service('shutdownRobotFace', shutdownSrv,destroy)
    print("Display image thread was started")
    add_two_ints_server()
        
