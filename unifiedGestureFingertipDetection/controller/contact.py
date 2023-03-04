#!/usr/bin/env python3

import rospy 
import cv2
import numpy as np
from hand_detector.detector import SOLO, YOLO
from unified_detector.unifiedDetector import Fingertips
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import String
import rospy
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import pickle
import time
import os
from unifiedGestureFingertipDetection.srv import *
from  threading import Thread
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import mediapipe as mp
import sys
import dlib
import cv2


class contact():
	def __init__(self):
		self.found=False
		self.xx=10
		self.yy=10
		self.contactdetector = dlib.get_frontal_face_detector()
		
	def contact(self,img):

		color_green = (0,255,0)
		line_width = 3
		rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		dets = self.contactdetector(rgb_image)
		for det in dets:
			cv2.rectangle(img,(det.left(), det.top()), (det.right(), det.bottom()), color_green, line_width)
		cv2.imshow('my webcam', img)
