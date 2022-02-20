#!/usr/bin/env python3
"""
    Hello Python!
"""
import rospy
import hello_python

if __name__== "__main__":
    rospy.init_node('hello_python') # Resgistering node in ros master
        
    hp = hello_python.HelloPython()
    hp.spin()
