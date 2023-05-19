#!/usr/bin/env python3

import cv2
from robot_face.srv import *
import rospy 
from threading import Thread
import time

positionX=20
positionY=20

sleepTime=1
global flag

def changeImg(req):
    global imagePath
    global flag
    print ('Services called. Image path is ' + req.name)
    imagePath=req.name
    time.sleep(sleepTime)
    flag=not flag
    return imageNameResponse(1)

def displayImageFunction():
        cv2.namedWindow("image",flags=cv2.WINDOW_GUI_NORMAL)
        cv2.moveWindow("image",positionX,positionY)
        # cv2.namedWindow('image',cv2.WND_PROP_FULLSCREEN)
        # cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.setWindowTitle("image","")
        while 1==1:
            time.sleep(sleepTime)
            img = cv2.imread(imagePath, cv2.IMREAD_COLOR)
            cv2.imshow("image", img)
            print('name '+imagePath)
            cv2.waitKey(100)



def playVideo():
        file="/home/stergios/Desktop/a.mp4"
        print ("play Video")
        video=cv2.VideoCapture(file)
        while True:
            ret, frame=video.read()
            if not ret:
                video=cv2.VideoCapture(file)
                break
            if cv2.waitKey(25) == ord("q"):
                break
            cv2.imshow("Video", frame)
            while flag:
                print("sleep")
                cv2.waitKey(50)
            
        video.release()
        cv2.destroyAllWindows()


def robot_face_srv():
    rospy.init_node('robot_face')
    s = rospy.Service('robot_face_srv', imageName, changeImg)
    rospy.spin()


def destroy(req):
	print ("destroy")
	rospy.signal_shutdown("test")
	print ("Done")
	return shutdownSrvResponse("")

if __name__ == "__main__":
    if (len(sys.argv)>=2):
            positionX =int(sys.argv[1])
            positionY=int( sys.argv[2])

    global flag
    
    flag=True

    rospy.Service('shutdownRobotFace', shutdownSrv,destroy)

    global imagePath
    imagePath='/robotApp/faces/smile.jpg'
    thread = Thread(target=playVideo, args=(), daemon=True)
    thread.start()
    
    robot_face_srv()


        
