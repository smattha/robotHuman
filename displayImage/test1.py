#!/usr/bin/env python3

# Python code to read image
import cv2
from imageName.srv import *
import rospy 
cv2.destroyAllWindows()



def add_two_ints(req):
    print (req.a)
    
    
    # To read image from disk, we use
    # cv2.imread function, in below method,
    img = cv2.imread("happiness.png", cv2.IMREAD_COLOR)

    # Creating GUI window to display an image on screen
    # first Parameter is windows title (should be in string format)
    # Second Parameter is image array
    cv2.imshow("image", img)

    # To hold the window on screen, we use cv2.waitKey method
    # Once it detected the close input, it will release the control
    # To the next line
    # First Parameter is for holding screen for specified milliseconds
    # It should be positive integer. If 0 pass an parameter, the it will
    # hold the screen until user close it.
    cv2.waitKey(0)

    # It is for removing/deleting created GUI window from screen
    # and memory

    return imageNameResponse('1')

def add_two_ints_server():
    rospy.init_node(NAME)
    s = rospy.Service('add_two_ints', imageName, add_two_ints)

      

    # spin() keeps Python from exiting until node is shutdown
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()