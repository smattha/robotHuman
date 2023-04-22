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

class detectFace():
	def __init__(self,ap):
		print ('test')
		self.found=False
		self.xx=10
		self.yy=10
					
		ap.add_argument("-d", "--detector", required=True,
			help="path to OpenCV's deep learning face detector")
		ap.add_argument("-m", "--embedding", required=True,
			help="path to OpenCV's deep learning face embedding model")
		ap.add_argument("-r", "--recognizer", required=True,
			help="path to model trained to recognize faces")
		ap.add_argument("-l", "--le", required=True,
			help="path to label encoder")
		ap.add_argument("-c", "--confidence", type=float, default=0.5,
			help="minimum probability to filter weak detections")
		ap.add_argument("-hm", "--hand_detection_method", required=True,
			help="path to OpenCV's deep learning face detector")
		ap.add_argument("-hp", "--hand_detection_method_weight", required=True,
			help="path to OpenCV's deep learning face detector")
		ap.add_argument("-f", "--fingertips", required=True,
			help="path to OpenCV's deep learning face detector")
		ap.add_argument("-o", "--offline", required=True,
			help="offline")
		ap.add_argument("-faceNew", "--faceNew", required=True,
			help="faceNew")
		ap.add_argument("-t", "--topic", required=True,
			help="offline")

		argsTemp, unknown = ap.parse_known_args()
		args = vars(argsTemp)
		self.topicFlag=('True'==args["topic"])
		self.offline=('True'==args["offline"])

		self.confidence=args["confidence"]
		# load our serialized face detector from disk
		print("[INFO] loading face detector...")
		protoPath = os.path.sep.join([args["detector"], "deploy.prototxt"])
		modelPath = os.path.sep.join([args["detector"],
			"res10_300x300_ssd_iter_140000.caffemodel"])
		self.detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

		# load our serialized face embedding model from disk
		print("[INFO] loading face recognizer...")
		self.embedder = cv2.dnn.readNetFromTorch(args["embedding"])

		# load the actual face recognition model along with the label encoder
		self.recognizer = pickle.loads(open(args["recognizer"], "rb").read())
		self.le = pickle.loads(open(args["le"], "rb").read())


		
		# Load the gesture recognizer model

		path=args["faceNew"] 
		modelPath=path+'mp_hand_gesture'
		print(modelPath)
		self.handModel = load_model(modelPath)

		# Load class names
		namePath=path+'gesture.names'
		f = open( namePath, 'r')
		self.classNames = f.read().split('\n')
		f.close()


	def detectFace(self,frame):



		# loop over frames from the video file stream
		#while True:
			# grab the frame from the threaded video stream

			# resize the frame to have a width of 600 pixels (while
			# maintaining the aspect ratio), and then grab the image
			# dimensions
			frame = imutils.resize(frame, width=600)
			(h, w) = frame.shape[:2]

			# construct a blob from the image
			imageBlob = cv2.dnn.blobFromImage(
				cv2.resize(frame, (300, 300)), 1.0, (300, 300),
				(104.0, 177.0, 123.0), swapRB=False, crop=False)

			# apply OpenCV's deep learning-based face detector to localize
			# faces in the input image
			self.detector.setInput(imageBlob)
			detections = self.detector.forward()

			# loop over the detections
			for i in range(0, detections.shape[2]):
				# extract the confidence (i.e., probability) associated with
				# the prediction
				confidence = detections[0, 0, i, 2]

				# filter out weak detections
				if confidence >self.confidence:
					# compute the (x, y)-coordinates of the bounding box for
					# the face
					box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
					(startX, startY, endX, endY) = box.astype("int")

					# extract the face ROI
					face = frame[startY:endY, startX:endX]
					(fH, fW) = face.shape[:2]

					# ensure the face width and height are sufficiently large
					if fW < 20 or fH < 20:
						continue

					# construct a blob for the face ROI, then pass the blob
					# through our face embedding model to obtain the 128-d
					# quantification of the face
					faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
						(96, 96), (0, 0, 0), swapRB=True, crop=False)
					self.embedder.setInput(faceBlob)
					vec = self.embedder.forward()

					# perform classification to recognize the face
					preds = self.recognizer.predict_proba(vec)[0]
					j = np.argmax(preds)
					proba = preds[j]
					name = self.le.classes_[j]
					print(name+"----------------------------------------------------")
					# draw the bounding box of the face along with the
					# associated probability
					text = "{}: {:.2f}%".format(name, proba * 100)
					y = startY - 10 if startY - 10 > 10 else startY + 10
					cv2.rectangle(frame, (startX, startY), (endX, endY),
						(0, 0, 255), 2)
					
					self.xx=round((startX+endX)/2)
					self.yy=round((startY+endY)/2)
					
					image = cv2.circle(frame, (self.xx,self.yy), radius=12,
						color=(15, 15, 240), thickness=-2)
					
					cv2.putText(frame, text, (startX, startY),
						cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)



			# show the output frame
			cv2.imshow("Frame", frame)
			key = cv2.waitKey(1) & 0xFF
			print('Return false')
			return False





if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	det=detection(ap)
	# det.found=False


	rospy.loginfo("---------------------------------------------det.topicFlag|%s|-----------------", det.topicFlag)
	detface= detectFace(argparse.ArgumentParser());
     
	if det.topicFlag==True:
		while True:
			det.grapImg()
			# det.detectFace()
			detface.detectFace(det.img_frame )
			
			det.detectFingersNew()			
			det.contact()
			# det.detectFingers()

	else :
		s = rospy.Service('face', face,det.faceSrv)
		print('Ready to receive!')
		
		s = rospy.Service('fingers', fingers,det.fingers)
		print('Ready to receive!')

		rospy.spin()



	det.destroy()
