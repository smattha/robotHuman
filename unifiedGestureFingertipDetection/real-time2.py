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
import cv2
import os
from unifiedGestureFingertipDetection.srv import *
from  threading import Thread

class detection():
	def __init__(self,ap):
		self.found=False

					
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
		ap.add_argument("-t", "--topic", required=True,
			help="offline")

		argsTemp, unknown = ap.parse_known_args()
		args = vars(argsTemp)
		self.topicFlag=('True'==args["topic"])
		self.offline=('True'==args["offline"])


        #./real-time2.py --detector face_detection_model --embedding-model /home/stergios/git/src/face_rec/openface_nn4.small2.v1.t7 --recognizer output2/recognizer.pickle --le output2/le.pickle --hand_detection_method yolo --hand_detection_method_weight /home/stergios/git/src/weights/yolo.h5 --fingertips /home/stergios/git/src/weights/fingertip.h5
		self.fingertips = Fingertips(weights=args["fingertips"])
		self.hand_detection_method = args["hand_detection_method"]
		self.hand_detection_method_weight = args["hand_detection_method_weight"]

		if self.hand_detection_method == 'solo':
			self.hand = SOLO(weights=self.hand_detection_method_weight, threshold=0.8)
		elif self.hand_detection_method == 'yolo':
			self.hand = YOLO(weights=self.hand_detection_method_weight, threshold=0.8)
		else:
			assert False, "'" + self.hand_detection_method + \
					"' hand detection does not exist. use either 'solo' or 'yolo' as hand detection method"

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



		if self.offline==False:
			try:
				rate=0.1
				print('Initialize ROS service,Rate',rate)
				self._pub = rospy.Publisher('fingers', Float32MultiArray, queue_size=10)
				self._pub_name = rospy.Publisher('face',String, queue_size=10)
				rospy.init_node('talker', anonymous=True)
				self._rate = rospy.Rate(rate) # 10hz
			except rospy.ROSInterruptException:
				print('Exception Occured in ros audio service')
				pass
		
		self.cam = cv2.VideoCapture(0)

		rospy.logerr("---------------------------------------------args[topicFlag]|%s|-----------------", self.topicFlag)
		rospy.logerr("---------------------------------------------=args[offline] |%s|-----------------", self.offline)

	def talker1(self,msg):
		print('Audio S2T:',msg,' ')
		self._pub.publish(msg)
		# self._rate.sleep()


	def detectFingers(self):
			print('Unified Gesture & Fingertips Detection')
			# ret, image = self.cam.read()
			image=self.img_frame

			#if ret is False:
			#	return
			# hand detection
			tl, br = self.hand.detect(image=image)

			if tl and br is not None:
				cropped_image = image[tl[1]:br[1], tl[0]: br[0]]
				height, width, _ = cropped_image.shape

				# gesture classification and fingertips regression
				prob, pos = self.fingertips.classify(image=cropped_image)
				pos = np.mean(pos, 0)

				self.propability=0.3
				# post-processing
				prob = np.asarray([(p >= self.propability) * 1.0 for p in prob])
				for i in range(0, len(pos), 2):
					pos[i] = pos[i] * width + tl[0]
					pos[i + 1] = pos[i + 1] * height + tl[1]

				counter=0
				self.fingersCounter=0
				for c, p in enumerate(prob):
					if p > self.propability:
						counter=counter+2
						self.fingersCounter=self.fingersCounter+1
				posSend = np.empty(shape= counter)

				# drawing
				index = 0
				counter=0
				color = [(15, 15, 240), (15, 240, 155), (240, 155, 15), (240, 15, 155), (240, 15, 240)]
				image = cv2.rectangle(image, (tl[0], tl[1]), (br[0], br[1]), (235, 26, 158), 2)
				for c, p in enumerate(prob):
					if p > self.propability:
						image = cv2.circle(image, (int(pos[index]), int(pos[index + 1])), radius=12,
											color=color[c], thickness=-2)
						print(pos[index])
						print(pos[index+1])
						posSend[counter]=pos[index]
						posSend[counter+1]=pos[index+1]
						counter=counter+2
						if self.offline==False:
							if self.topicFlag==True:
								if (self.fingersCounter>3):
									self._pub.publish(Float32MultiArray(data=posSend))
							else:
								self.fingerPos=posSend
								return True;

					
					self.found=True
					index = index + 2
				print (index)
				data = [0.0, 1.0]

				#self._pub.publish(Float32MultiArray(data=posSend))
			#return False
			# cv2.waitKey(1)
				#if cv2.waitKey(1) & 0xff == 27:
				#break

				# display image
			cv2.imshow('Unified Gesture & Fingertips Detection', image)
			return False
			

	def destroy(self):	
		self.cam.release()
		cv2.destroyAllWindows()

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

					# draw the bounding box of the face along with the
					# associated probability
					text = "{}: {:.2f}%".format(name, proba * 100)
					y = startY - 10 if startY - 10 > 10 else startY + 10
					cv2.rectangle(frame, (startX, startY), (endX, endY),
						(0, 0, 255), 2)
					cv2.putText(frame, text, (startX, y),
						cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
					if self.offline==False:
						if self.topicFlag==True:
							self._pub_name.publish(text)
						else:
							self.faceTxt=text
							print('Found!!!!!!!!!!!!!!!!!!!!!!!')
							return True;


			# show the output frame
			cv2.imshow("Frame", frame)
			key = cv2.waitKey(1) & 0xFF
			print('Return false')
			return False


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




if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	det=detection(ap,)
	# det.found=False


	rospy.logerr("---------------------------------------------det.topicFlag|%s|-----------------", det.topicFlag)

     
	if det.topicFlag==True:
		while True:
			det.grapImg()
			
			det.detectFace()
			det.detectFingers()

	else :
		s = rospy.Service('face', face,det.faceSrv)
		print('Ready to receive!')
		
		s = rospy.Service('fingers', fingers,det.fingers)
		print('Ready to receive!')

		rospy.spin()



	det.destroy()
