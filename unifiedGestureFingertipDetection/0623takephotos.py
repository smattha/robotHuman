#!/usr/bin/env python3
import sys
from PyQt5 import QtCore, QtWidgets
import os
import signal
import shutil
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import cv2
import numpy as np
from imutils import paths
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import argparse
import pickle

global hasRun
hasRun = False

# python3 0623takephotos.py --embedding-model /home/stergios/git/src/face_rec/openface_nn4.small2.v1.t7 -d ./photos --outputpath output


class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 
  
        #self.setStyleSheet("background-color: black;")
        self.setWindowTitle(" ") 
#        self.setGeometry(100, 100, 350, 500) 
        self.resize(1000, 1000) 
        
        self.UiComponents() 
        self.show() 
  

    def UiComponents(self): 
        lockButton = QPushButton(self) 
        lockButton.setGeometry(60, 200, 100, 70) 
        #lockButton.setStyleSheet("border-radius : 10; border : 1px solid white; background-color : #3A3535") 
        #lockButton.setIcon(QIcon('1.jpg'))              # ! 'lock.png'
        size = QSize(40, 40) 
        lockButton.setIconSize(size)
        lockButton.clicked.connect(self.clickme) 
        label = QLabel(self)
        label.setGeometry(30, 10, 350, 121)
        label.setText("<h1>ΕΦΑΡΜΟΓΗ MCTEST</h1>")
        

    def clickme(self): 
        print("pressed") 
        self.close()

class EmittingStream(QtCore.QObject):

    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))
 
 
class Ui_Dialog(object):
 
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        #Dialog.resize(448, 300)
        Dialog.resize(700, 600)                                                 

 
        self.take_photo = QtWidgets.QPushButton(Dialog)
        self.take_photo.setGeometry(QtCore.QRect(300, 90, 360, 58))   
        self.take_photo.setFont(QFont('Arial', 18))
        self.take_photo.setObjectName("take_photo")
        self.take_photo.setCheckable(True)
        self.take_photo.clicked.connect(self.take_photoFnc)
        #self.v.setHidden(True)F
        
        self.save_photos = QtWidgets.QPushButton(Dialog)
        self.save_photos.setGeometry(QtCore.QRect(300, 190, 360, 58))   
        self.save_photos.setFont(QFont('Arial', 18))
        self.save_photos.setObjectName("take_photo")
        #self.save_photos.setCheckable(True)
        self.save_photos.clicked.connect(self.play_videoFnc)
        
        self.recognize = QtWidgets.QPushButton(Dialog)
        self.recognize.setGeometry(QtCore.QRect(300, 280, 360, 58))   
        self.recognize.setFont(QFont('Arial', 18))
        self.recognize.setObjectName("recognize")
        #self.save_photos.setCheckable(True)
        self.recognize.clicked.connect(recognize)

        
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(300, 480, 61, 28))
        self.exit.setCheckable(True)
        self.exit.clicked.connect(self.clos)
        
        self.insert_dir = QtWidgets.QLabel(Dialog)
        self.insert_dir.setGeometry(QtCore.QRect(30, 220, 250, 21))
        self.insert_dir.setObjectName("insert_dir")
        
        self.insert_dir1 = QtWidgets.QLineEdit(Dialog)
        self.insert_dir1.setGeometry(QtCore.QRect(30, 250, 250, 21))            # left, up, base, height
        #self.lineEdit_name.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        self.insert_dir1.setObjectName("insert_dir1")
        

        self.cap = cv2.VideoCapture(0)      
        
        self.currentframe = 0          
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
       
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
 
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ΑΝΑΓΝΩΡΙΣΗ ΜΑΘΗΤΩΝ"))
        # self.play_video.setText(_translate("Dialog", "ΕΚΚΙΝΗΣΗ ΚΑΜΕΡΑΣ"))
        self.take_photo.setText(_translate("Dialog", "ΛΗΨΗ ΦΩΤΟΓΡΑΦΙΑΣ"))
        self.save_photos.setText(_translate("Dialog", "ΑΠΟΘΗΚΕΥΣΗ ΦΩΤΟΓΡΑΦΙΑΣ"))
        self.insert_dir.setText(_translate("Dialog", "ΔΩΣΤΕ ΟΝΟΜΑ ΜΑΘΗΤΗ"))
        self.recognize.setText(_translate("Dialog", "ΕΚΠΑΙΔΕΥΣΗ ΜΟΝΤΕΛΟΥ"))
        self.exit.setText(_translate("Dialog", "ΕΞΟΔΟΣ"))
        #self.recognize1.setText(_translate("Dialog", "ΑΝΑΓΝΩΡΙΣΗ ΜΑΘΗΤΗ"))
        #self.test_button.setText(_translate("Dialog", "test button"))
 
    def play_videoFnc(self):



        

        self.hasRun = False
        if self.hasRun == False:
            

                #cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
                #if hasRun == True:
                    #print('button clicked')
                    #hasRun == False
                if True:
                        from os import rename, listdir
                        from pathlib import Path
                        import os
                        from os import path
                                        

                        
                        x = ui.insert_dir1.text()   
                        if x == "":
                            print('warning')
                            show_warning_messagebox()
                            self.hasRun=True

                        #print('Enter your name:')
                        #x = input()
                        print('Hello, ' + x)
                        directory = x

                        # Parent Directory path
                        parent_dir = dataset
                        pathFile=os.path.join(parent_dir, directory)
                        if path.exists(os.path.join(parent_dir, directory))==False:
                            os.mkdir(pathFile)    
                        #print('pressed button video')
                        fileName=pathFile+'/'+str(self.currentframe)+'.jpg'
                        cv2.imwrite(fileName, self.frame  )
                        self.currentframe += 1
                        time.sleep(.5)

                

                

    def clos(self):
        Dialog.close()
        hasRun = True
        cv2.destroyAllWindows()

    def take_photoFnc(self):

            window_name = 'ΜΑΘΗΤΗΣ'
            cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
            cv2.moveWindow(window_name, 1400,50)

            print('take_photo')
            # while(cap.isOpened() and self.hasRun == False):

            ret, frame = self.cap.read()
            ret, frame = self.cap.read()
            ret, frame = self.cap.read()
            ret, frame = self.cap.read()
            ret, frame = self.cap.read()
            
            name = './data2/0000' + str(self.currentframe) + '.jpg'
            
            scale_percent = 50 # percent of original size
            width = int(frame.shape[1] * scale_percent / 100)
            height = int(frame.shape[0] * scale_percent / 100)
            dim = (width, height)
            #resize image
            self.frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
            

            scale_percent = 50 # percent of original size
            width = int(self.frame.shape[1] * scale_percent / 100)
            height = int(self.frame.shape[0] * scale_percent / 100)
            dim = (width, height)
            #resize image
            self.frame = cv2.resize(self.frame, dim, interpolation = cv2.INTER_AREA)
            cv2.imshow(window_name, self.frame)
            self.currentframe=self.currentframe+1
            cv2.waitKey(25)

def test_button(self):
    print('a')
    if ui.test_button.isChecked():
        print('t')
        
def btnstate(self):
   #if ui.test_button.isChecked():
      #print ("button pressed")
   #else:
      #print( "button released")
    global hasRun
    hasRun = True
    #time.sleep(2)
    #hasRun = False
      
#def test():
    #btnstate(self)
    #print('george')
    
def savephoto(self):
    from os import rename, listdir
    from pathlib import Path
    import os
    from os import path

    ## create Directory

    x = ui.insert_dir1.text()
    
    if x == "":
        print('warning')
        show_warning_messagebox()
    
    #print('Enter your name:')
    #x = input()
    print('Hello, ' + x)
    directory = x
    
    # Parent Directory path
    parent_dir = "photos/"
    if path.exists(os.path.join(parent_dir, directory)):
        show_warning_messagebox1()
    
    # Path
    path = os.path.join(parent_dir, directory)
    print('path  ', path)

    os.mkdir(path)
    print("Directory '% s' created" % directory)
    dst = path + '/'
    print('dst ', dst)


    ## move files
    
    src = "/home/g/test/"
    files = os.listdir(src)
    files.sort()
    print('files  ', files)
    for f in files:
        src1 = src+f
        dst1 = dst+f
        shutil.move(src1,dst1)
        # readNetFromTorch  
def recognize(self):
            # load the face detector from disk
        print("Loading Caffe based face detector to localize faces in an image")
        protoPath = os.path.sep.join(["/robotApp/face_detection_model", "deploy.prototxt"])
        modelPath = os.path.sep.join(["/robotApp/face_detection_model",
            "res10_300x300_ssd_iter_140000.caffemodel"])
        detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

        # load the face embedding model from disk
        print("Loading Openface imlementation of Facenet model")
        embedder = cv2.dnn.readNetFromTorch(pathEmb)

        # grab the paths to the input images in our dataset
        print("Load image dataset..")
        imagePaths = list(paths.list_images(dataset))

        # initialize our lists of extracted facial embeddings and
        # corresponding people names
        knownEmbeddings = []
        knownNames = []

        # initialize the total number of faces processed
        total = 0

        # loop over the image paths
        for (i, imagePath) in enumerate(imagePaths):
            # extract the person name from the image path
            name = imagePath.split(os.path.sep)[-2]

            # load the image, resize it to have a width of 600 pixels (while
            # maintaining the aspect ratio), and then grab the image
            # dimensions
            image = cv2.imread(imagePath)
            image = imutils.resize(image, width=600)
            (h, w) = image.shape[:2]

            # construct a blob from the image
            imageBlob = cv2.dnn.blobFromImage(
                cv2.resize(image, (300, 300)), 1.0, (300, 300),
                (104.0, 177.0, 123.0), swapRB=False, crop=False)

            # apply OpenCV's deep learning-based face detector to localize
            # faces in the input image
            detector.setInput(imageBlob)
            detections = detector.forward()

            # ensure at least one face was found
            if len(detections) > 0:
                # we're making the assumption that each image has only ONE
                # face, so find the bounding box with the largest probability
                i = np.argmax(detections[0, 0, :, 2])
                confidence = detections[0, 0, i, 2]

                # ensure that the detection with the 50% probabilty thus helping filter out weak detections
                if confidence > 0.5:
                    # compute the (x, y)-coordinates of the bounding box for
                    # the face
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")

                    # extract the face ROI and grab the ROI dimensions
                    face = image[startY:endY, startX:endX]
                    (fH, fW) = face.shape[:2]

                    # ensure the face width and height are sufficiently large
                    if fW < 20 or fH < 20:
                        continue

                    # construct a blob for the face ROI, then pass the blob
                    # through our face embedding model to obtain the 128-d
                    # quantification of the face
                    faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
                        (96, 96), (0, 0, 0), swapRB=True, crop=False)
                    embedder.setInput(faceBlob)
                    vec = embedder.forward()

                    # add the name of the person + corresponding face
                    # embedding to their respective lists
                    knownNames.append(name)
                    knownEmbeddings.append(vec.flatten())
                    total += 1

        # dump the facial embeddings + names to disk
        data = {"embeddings": knownEmbeddings, "names": knownNames}
        f = open(outputpath+"/embeddings.pickle", "wb")
        f.write(pickle.dumps(data))
        f.close()




        # load the face embeddings
        print("Loading face embeddings of the dataset")
        data = pickle.loads(open(outputpath+"/embeddings.pickle", "rb").read())

        # encode the labels
        print("Encoding image labels")
        le = LabelEncoder()
        labels = le.fit_transform(data["names"])

        # train the model used to accept the 128-d embeddings of the face and
        # then produce the actual face recognition
        print("Training the model usng SVM...")
        recognizer = SVC(C=1.0, kernel="linear", probability=True)
        recognizer.fit(data["embeddings"], labels)

        # write the actual face recognition model to disk
        f = open(outputpath+"/recognizer.pickle", "wb")
        f.write(pickle.dumps(recognizer))
        f.close()

        # write the label encoder to disk
        f = open(outputpath+"/le.pickle", "wb")
        f.write(pickle.dumps(le))
        f.close()
    

    
def show_warning_messagebox():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
  
    # setting message for Message Box
    msg.setText("ΚΕΝΟ ΟΝΟΜΑ ΜΑΘΗΤΗ")
      
    # setting Message box window title
    msg.setWindowTitle("ΠΡΟΣΟΧΗ!")
      
    # declaring buttons on Message Box
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
      
    # start the app
    retval = msg.exec_()
    
def show_warning_messagebox1():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
  
    # setting message for Message Box
    msg.setText("ΤΟ ΟΝΟΜΑ ΜΑΘΗΤΗ ΥΠΑΡΧΕΙ")
      
    # setting Message box window title
    msg.setWindowTitle("ΠΡΟΣΟΧΗ!")
      
    # declaring buttons on Message Box
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
      
    # start the app
    retval = msg.exec_()

def show_warning_messagebox2():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
  
    # setting message for Message Box
    msg.setText("Η ΕΚΠΑΙΔΕΥΣΗ ΟΛΟΚΛΗΡΩΘΗΚΕ")
      
    # setting Message box window title
    msg.setWindowTitle("ΠΛΗΡΟΦΟΡΙΑ")
      
    # declaring buttons on Message Box
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
      
    # start the app
    retval = msg.exec_()

pathEmb=""
dataset=""
outputpath=""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    ap = argparse.ArgumentParser()
    ap.add_argument("-m", "--embedding-model", required=True,
        help="path to OpenCV's deep learning face embedding model")
    ap.add_argument("-d", "--dataset", required=True,
        help="path to OpenCV's deep learning face embedding model")
    ap.add_argument("-o", "--outputpath", required=True,
        help="path to OpenCV's deep learning face embedding model")
    # ap.add_argument("-r", "--recognizer", required=True,
    #   help="path to output model trained to recognize faces")
    # ap.add_argument("-l", "--le", required=True,
    #   help="path to output label encoder")

    argsTemp, unknown = ap.parse_known_args()
    args = vars(argsTemp)

    pathEmb=args["embedding_model"]
    
    dataset=args["dataset"]
        
    outputpath=args["outputpath"]
    #t = threading.Thread(target=ui.play_video)
    #t.start()
    sys.exit(app.exec_())
