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
from unifiedGestureFingertipDetection.msg import *
from  threading import Thread
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import mediapipe as mp
import sys
import dlib
import cv2
import threading
import time

class Results():          # leave this empty
    def __init__(self):   # constructor function using self
        self.positionFaceX = None  # variable using self.
        self.positionFaceY = None
        self.hand=None
        self.focus=None
        self.name=None


class detection():
	def __init__(self,ap):
		self.found=False
		self.xx=10
		self.yy=10
		self.loop=True
					
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
		ap.add_argument("-faceNew", "--faceNew", required=True,
			help="faceNew")


		argsTemp, unknown = ap.parse_known_args()
		args = vars(argsTemp)


		self.resultsArray = [] #empty array
		self.resultsArrayPrevious=[]


        # #./real-time2.py --detector face_detection_model --embedding-model /home/stergios/git/src/face_rec/openface_nn4.small2.v1.t7 --recognizer output2/recognizer.pickle --le output2/le.pickle --hand_detection_method yolo --hand_detection_method_weight /home/stergios/git/src/weights/yolo.h5 --fingertips /home/stergios/git/src/weights/fingertip.h5
		# self.fingertips = Fingertips(weights=args["fingertips"])
		# self.hand_detection_method = args["hand_detection_method"]
		# self.hand_detection_method_weight = args["hand_detection_method_weight"]

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


		# initialize mediapipe
		self.mpHands = mp.solutions.hands
		#hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
		self.hands = self.mpHands.Hands(max_num_hands=1, min_detection_confidence=0.3)

		self.mpDraw = mp.solutions.drawing_utils

		# Load the gesture recognizer model

		path=args["faceNew"] 
		modelPath=path+'mp_hand_gesture'
		print(modelPath)
		self.handModel = load_model(modelPath)

		self.contactdetector = dlib.get_frontal_face_detector()

		# Load class names
		namePath=path+'gesture.names'
		f = open( namePath, 'r')
		self.classNames = f.read().split('\n')
		f.close()

		rate=0.1
		print('Initialize ROS service,Rate',rate)
		# self._pub = rospy.Publisher('fingers', Float32MultiArray, queue_size=10)
		# self._pub_name = rospy.Publisher('face',String, queue_size=10)
		rospy.init_node('talker', anonymous=True)
		self._rate = rospy.Rate(rate) # 10hz
		
		self.cam = cv2.VideoCapture(0)

		self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1980)
		self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)
		




	def detectFingersNew(self):
		# print('Unified Gesture & Fingertips Detection')
		# ret, image = self.cam.read()
		frameNew=self.img_frame


		imageRGB = cv2.cvtColor(frameNew, cv2.COLOR_BGR2RGB)
		results = self.hands.process(imageRGB)


		if results.multi_hand_landmarks:
			for handLms in results.multi_hand_landmarks: # working with each hand
				for id, lm in enumerate(handLms.landmark):
					h, w, c = self.img_frame.shape
					cx, cy = int(lm.x * w), int(lm.y * h)
					if id == 8 :
						cv2.circle(frameNew, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
						image = cv2.line(frameNew, (cx,cy), (self.xx,self.yy), color=(240, 240, 240), thickness=2)	

					distance=1000000;
					posMin=-1;
					# print('111111111111111111111111111111111111111')
					# print(" en(det.resultsArray)    "+str(len(det.resultsArray)))
					for x in range(len(det.resultsArray)):

							distanceTemp=(det.resultsArray[x].positionFaceX-cx)**2 +(det.resultsArray[x].positionFaceY-cy)**2
							if distanceTemp<distance:
								distance=distanceTemp
								posMin=x
								# print(x)
							# print(distanceTemp)
					# print('111111111111111111111111111111111111111')
					if(posMin>-1):
						det.resultsArray[posMin].hand=True;
				self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)



	def destroy(self,res):	
		self.cam.release()
		cv2.destroyAllWindows()
		self.loop=False

	def grapImg(self):
			self.ret,self.img_frame = self.cam.read()


	def detectFace(self):



		# loop over frames from the video file stream
		#while True:
			# grab the frame from the threaded video stream
			frame=self.img_frame

			# resize the frame to have a width of 600 pixels (while
			# maintaining the aspect ratio), and then grab the image
			# dimensions
			# frame = imutils.resize(frame, width=600)
			(h, w) = frame.shape[:2]

			# construct a blob from the image
			imageBlob = cv2.dnn.blobFromImage(frame, swapRB=False, crop=False)

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

					# draw the bounding box of the face along with the
					# associated probability
					text = "{}: {:.2f}%".format(name, proba * 100)
					y = startY - 10 if startY - 10 > 10 else startY + 10
					cv2.rectangle(frame, (startX, startY), (endX, endY),
						(0, 0, 255), 2)
					
					self.xx=round((startX+endX)/2)
					self.yy=round((startY+endY)/2)


					test1 = Results()

					test1.positionFaceX=self.xx
					test1.positionFaceY=self.yy
					test1.focus=False
					test1.hand=False
					test1.name=name
					self.resultsArray.append(test1)

					image = cv2.circle(frame, (self.xx,self.yy), radius=12,
						color=(15, 15, 240), thickness=-2)
					
					cv2.putText(frame, text, (startX, startY),
						cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)



			# print('Return false')
			return False

	def contact(self):

		img=self.img_frame
		color_green = (0,255,0)
		line_width = 3
		
		rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

		dets = self.contactdetector(rgb_image)
		for det in dets:
			cv2.rectangle(img,(det.left(), det.top()), (det.right(), det.bottom()), color_green, line_width)
		
			distance=1000000;
			posMin=-1;
			# print('111111111111111111111111111111111111111')
			# print(" en(det.resultsArray)    "+str(len(det.resultsArray)))
			for x in range(len(self.resultsArray)):

					distanceTemp=(self.resultsArray[x].positionFaceX-det.left())**2 +(self.resultsArray[x].positionFaceY-det.right())**2
					if distanceTemp<distance:
						distance=distanceTemp
						posMin=x
						# print(x)
					# print(distanceTemp)
			# print('111111111111111111111111111111111111111')
			if(posMin>-1):
				self.resultsArray[posMin].focus=True;



			
		cv2.imshow('my webcam', img)
		key = cv2.waitKey(1) & 0xFF



	def faceSrv(self,req):
			print (req.text)   
			det.grapImg()
			while self.detectFace()==False:
				print('Pending!')
				det.grapImg()		

			return faceResponse(self.fingerPos)

		

	def fingers(self,req):
			print (req.text)   
			det.grapImg()
			while self.detectFingers()==False:
				print('Pending!')
				det.grapImg()		

			return fingersResponse("Found")


	def recognitionFnc(self,req):
			recognitions=recognitionResponse()
			# pub = rospy.Publisher('Recognition', RecognitionMsg, queue_size=50)

			print ("---------------------------------------------------------"+ str(len(self.resultsArrayPrevious))+" "+str(len(self.resultsArray)))
			for x in range(len(self.resultsArrayPrevious)):
				print ("---------------------------------------------------------")

				rec=RecognitionMsg()
				rec.name=str(self.resultsArrayPrevious[x].name)
				rec.isFocus=str(self.resultsArrayPrevious[x].focus)
				rec.hasRaiseHand=str(self.resultsArrayPrevious[x].hand)

				recognitions.recog.append(rec)
				
			return recognitions
	
	def rosservice(self):
	
		s = rospy.Service('recognitions', recognition,det.recognitionFnc)

		rospy.Service('shutdown', shutdownSrv,det.destroy)
		print('Ready to receive!')

		# rospy.spin()


if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	det=detection(ap,)



	det.resultsArrayPrevious = []
	
	det.rosservice()
	# x.start()
	pub = rospy.Publisher('Recognition', RecognitionMsg, queue_size=50)

	while det.loop:
		det.resultsArray = [] 
		det.grapImg()


		x = threading.Thread(target=det.detectFace())
		y = threading.Thread(target=det.detectFingersNew())
		z = threading.Thread(target=det.contact())

		x.start()
		y.start()
		z.start()

		x.join()
		y.join()
		z.join()

		for x in range(len(det.resultsArray)):
			print("         "+ str(det.resultsArray[x].name)+" "+ str(det.resultsArray[x].positionFaceX)+" "+str(det.resultsArray[x].positionFaceY)+" " +str(det.resultsArray[x].focus) +" " +str(det.resultsArray[x].hand))
			rec=RecognitionMsg()
			rec.name=str(det.resultsArray[x].name)
			rec.isFocus=str(det.resultsArray[x].focus)
			rec.hasRaiseHand=str(det.resultsArray[x].hand)
			pub.publish(rec)
			det.resultsArrayPrevious=det.resultsArray
			



