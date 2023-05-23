#!/usr/bin/env python3

import sys
from typing import Counter
from PyQt5.QtCore import QObject, pyqtSlot
from threading import Thread
import time
from PyQt5.QtCore import QObject
import time
from exersiceController.RootController import RootController
class ControllerExersice6(RootController,QObject):
    def __init__(self,ros,model):
        super().__init__()
        print("Initialize the controller for Excersice 3 ")
        self._rosInterface=ros
        self.mainPage=3
        self.model=model
        self._exercise3Img=0
        self._feedback=''
        self.step=0
        self._imagesStoryCur=''
        self._answerEx1=''
        self.answerEx3=''
        self.answerEx32=''
        self.path=self.model.path
    
    # def feedbackAnswer(self,value):
    #     print('Feedback Robot Controller', value)
    #     if (value=='1'):
    #         print("Value is 1")
    #         self._rosInterface.displayImg('/robotApp/faces/smile1.jpg')
    #     elif value=='2' :
    #         print("Value is 2")
    #         self._rosInterface.displayImg('/robotApp/faces/smile.jpg')
    #     elif(value=='3'):    
    #         print("Value is 3")
    #         self._rosInterface.displayImg('/robotApp/faces/surprise.jpg')
        
        # self._feedback=value
        # self.continueDialog()

    def setVariable6(self):
        
        self._imagesStory=  [                 
                    ["", self.path+"/resources/images/ex6/1.png",'2'],
                    ["", self.path+"/resources/images/ex6/2.png",'1']
        ]

        self._imagesAnswer=  [
                    ["A", self.path+"/resources/images/ex3/3.png",'1'],
                    ["B", self.path+"/resources/images/ex3/4.png",'2']
                    ]
        self._counter=0
        self._exerciseDscr='Σε αυτό το παιχνίδι θα χρειαστώ τη βοήθειά σου. Θέλω να δεις τις εικόνες και να μου πεις τι δείχνουν.'
        self.title= 'Τι δείχνουν οι εικόνες'

        self.results=['άλογο','πορτοκάλι']


        self.correctAnswer=['άλογο','πορτοκάλι','αλογο','πορτοκαλι']

        #PATH# Exercise 6
        self.moveRobot='/robotApp/positions/speech2Text.txt'


    def setVariable6B(self):
        
        self._imagesStory=  [                 
                    ["", self.path+"/resources/images/exB6/1.jpeg",'2'],
                    ["", self.path+"/resources/images/exB6/2.png",'1']
        ]

        self._imagesAnswer=  [
                    ["A", self.path+"/resources/images/ex3/3.png",'1'],
                    ["B", self.path+"/resources/images/ex3/4.png",'2']
                    ]
        self._counter=0
        self._exerciseDscr='Σε αυτό το παιχνίδι θα χρειαστώ τη βοήθειά σου. Θέλω να δεις τις εικόνες και να μου πεις τι δείχνουν.'
        self.title= 'Τι δείχνουν οι εικόνες;'
        self.results=['σκυλί','μήλο']


        #PATH# Exercise 12
        self.moveRobot='/robotApp/positions/voice.txt'


        self.correctAnswer=['σκυλί','μήλο','σκυλί','μήλο']


    def setVariables4(self):
        
        self._imagesStory=  [
                    ["Η Μαρία είναι ένα μικρό κοριτσάκι 3 ετών'", self.path+"/resources/images/ex4/1.png",'1'],
                    ["Το κουδούνι χτυπά και η μαμά της Μαρίας ανοίγει την πόρτα'", self.path+"/resources/images/ex4/2.png",'2'],
                    ["Η μαμά της Μαρίας λέει: «Καλημέρα!", self.path+"/resources/images/ex4/3.png",'3'],
                    ["Ω νομίζω ότι δεν έχω γνωρίσει το γιο σου. Πως τον λένε;'", self.path+"/resources/images/ex4/4.png",'4'],
                    ["Άκουσες κάποιον να λέει κάτι που μπορεί να στεναχωρήσει ή να θυμώσει κάποιον από τους ήρωες της ιστορίας;", self.path+"/resources/images/ex4/5.png",'5']
        ]

        self._imagesAnswer=  [
                    ["A", self.path+"/resources/images/ex4/6.png",'1'],
                    ["B", self.path+"/resources/images/ex4/7.png",'2'],
                    ["Γ", self.path+"/resources/images/ex4/8.png",'3']
                    ]
        self._counter=0
        self._exerciseDscr='Στις παρακάτω εικόνες θα δούμε το μικρό Γιωργάκη να κάνει κάποιες σκανταλιές. Αφού ακούσεις προσεκτικά την ιστορία θα μαντέψεις τι θα κάνει ο Γιωργάκης. Κάτω από τις εικόνες θα υπάρχουν 2 απαντήσεις. Διάλεξε αυτή που νομίζεις ότι είναι η σωστή'
        self.title= 'Τι δείχνουν οι εικόνες'
        self.results=['σκυλί','μήλο']




    def setupUi(self):
        print("main")

    def steps(self):
        self.readExersice() 
        self.readAnswers()
        self.reply()
        self.feedback()
        self.continueDialog()

    def readExersice(self):
        # print('Read Exercise')
        self.model.nextImage='0'
        # self.nextPage3(0)
        
        self._imagesStoryCur=self._imagesStory[self._counter][0]
        self.model.nextImage=self._imagesStory[self._counter][1]
        
        # self.model.nextImage=self._imagesStory[0][0]
        # self._rosInterface.talker(self._exerciseDscr)
        thread = Thread(target=self.readExersiceThread, args=(), daemon=True)
        thread.start()

        # # self.playAudio(self._exerciseDscr)
        # self.step1()

    def readExersiceThread(self):
        print('Read Exercise')
        if self.model.name=='':
            self.model.name=self._rosInterface.getNames()
        self._rosInterface.talker(self.model.name +" "+self._exerciseDscr)
        self._rosInterface.talker(self.model.name+" όταν είσαι ετοιμός να προχωρήσουμε σήκωσε το χέρι")
        self._rosInterface.moveRobotFromFile('/robotApp/positions/speech2Text.txt')
        self._rosInterface.getHand()
        self._rosInterface.displayImg('/robotApp/faces/smile.jpg')
        self.nextPage3(0)
        # self.playAudio(self._exerciseDscr)
        self.step1()

    def step1(self):
        print("Step first")
        # self._rosInterface.talker('Ο Γιωργάκης κρύβει την σοκολάτα του στο ντουλάπι της κουζίνας πριν πάει να παίξει έξω')
    
    def step2(self):
        self._rosInterface.talker('Όταν ο Γιωργάκης βγαίνει στην αυλή, η γιαγιά του βρίσκει την σοκολάτα και την βάζει στο ψυγείο')
    

    def readAnswers(self):
        print('Read Answers')

    def reply(self):
        print('Get Reply')
    def feedback(self):
        print('feedback')
        self.feedbackFN()
        time.sleep(0.4)
        
    def feedbackFN(self):
        thread = Thread(target=self.stopBeforeShowImageMainF, args=(), daemon=True)
        thread.start()
        # thread.sleep(1)

    # def stopBeforeShowImageMainF(self):
    #     self._rosInterface.talker(
    #         'Πόσο εύκολος σου φάνηκε ο γρίφος; Εύκολος,έτσι και έτσι ή δύσκολος;')
    #     self.model.showButtonsFeedback()

    def feedbackStore(self,model,value):
        self._answerEx1=value
        print('feedback')
        self.model.currentExerciseID=0
        self.model.changeFeedbackLabelWrong()
        print("value :"+str(value))
        for x in self.correctAnswer:
            if (x.casefold()==str(value).casefold()):  
                self.model.changeFeedbackLabelCorrect()


    # def continueDialog(self):
    #     print('--------------------------------------MainController: Eίσαι έτοιμος να προχωρήσουμε ')
    #     if self.model.name!='':
    #         print("test")
    #         isFocus=self._rosInterface.focus(self.model.name)
    #         if isFocus==False:
    #             self._rosInterface.talker( self.model.name +'παρατήρησα ότι δεν ήσουν προσεκτικός κατά την διάρκεια της άσκησης. Προσπάθησε να προσέχεις περισσότερο.')
    #             self._rosInterface.displayImg('/robotApp/faces/anger.jpg')
    #             self._rosInterface.moveRobotFromFile('/robotApp/positions/displayImg.txt')
    #     self._rosInterface.talker('Είσαι έτοιμος να προχωρήσουμε;')

    def readAnswers2(self):
        self._rosInterface.talker('Ο Γιωργάκης γυρνάει στο σπίτι για να φάει με λαχτάρα την σοκολάτα. Που θα ψάξει για την σοκολάτα του;')


    def printResult(self):
        print("Exersice 3:", self._answerEx1," ",self.answerEx32," ",self._feedback)


    def clearResults(self):
        self._answerEx1=''
        self._feedback=''




    @pyqtSlot(int)
    def storeAnswer(self,value):
        self.feedbackStore(self.model.result,value)
        self._counter=0
        self._model.currentExerciseID=0
        self.model.trigger(8)



    def getText(self):
        if self.step==0:
            self._answerEx1=self._rosInterface.getText(self.results)
            print('reply!!!!!!!!!!!!!!')
        else:
            self.answerEx32=self._rosInterface.getText(self.results)
            print('reply!!!!!!!!!!!!!!')
        self.step=self.step+1
        self.nextPage3(0)


    def getTextMainThread(self):
        thread = Thread(target = self.getText,args=(),daemon=True)
        thread.start()
        print("thread finished...exiting")
        return thread
       
    
    def nextPage3(self,value):
        print('Change Image step  {}',self._counter)
        # self.model.nextPageEx2('2')
        if (len(self._imagesStory)>self._counter):
            # self._rosInterface.talker()
            # self.playAudio(self._imagesStory[self._counter][0])
            self._imagesStoryCur=self._imagesStory[self._counter][0]
            self.model.nextImage=self._imagesStory[self._counter][1]
            self._counter=self._counter+1
            self.thread=self.getTextMainThread()

        else: 

            self.feedback()
            self.model.trigger(101)


    def playAudio(self,msg):
        self.msg = msg
        thread = Thread(target=self.playAudioThread, args=(), daemon=True)
        thread.start()
        print("Thread finished...exiting")

    def playAudioThread(self):
        print("\t\tthread running.......")
        self._rosInterface.talker(self.msg)
        # self._rosInterface.talker(self._answerDsr)