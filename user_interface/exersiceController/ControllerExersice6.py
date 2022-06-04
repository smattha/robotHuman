#!/usr/bin/env python3

import sys
from typing import Counter
from PyQt5.QtCore import QObject, pyqtSlot
from threading import Thread
import time
from PyQt5.QtCore import QObject, pyqtSignal

class ControllerExersice6(QObject):
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
    
    def feedbackAnswer(self,value):
        print('Feedback {}',value)
        self._feedback=value

    def setVariable6(self):
        
        self._imagesStory=  [                 
                    ["", "/home/stergios/git/src/robotHuman/user_interface/resources/images/ex6/1.png",'2'],
                    ["", "/home/stergios/git/src/robotHuman/user_interface/resources/images/ex6/2.png",'1']
        ]

        self._imagesAnswer=  [
                    ["A", "/home/stergios/git/src/robotHuman/user_interface/resources/images/ex3/3.png",'1'],
                    ["B", "/home/stergios/git/src/robotHuman/user_interface/resources/images/ex3/4.png",'2']
                    ]
        self._counter=0
        self._exerciseDscr='Σε αυτό το παιχνίδι θα χρειαστώ τη βοήθειά σου. Θέλω να δεις τις εικόνες και να μου πεις τι δείχνουν.'
        self.title= '6'



    def setVariable6B(self):
        
        self._imagesStory=  [                 
                    ["", "/home/stergios/git/src/robotHuman/user_interface/resources/images/exB6/1.jpeg",'2'],
                    ["", "/home/stergios/git/src/robotHuman/user_interface/resources/images/exB6/2.png",'1']
        ]

        self._imagesAnswer=  [
                    ["A", "/home/stergios/git/src/robotHuman/user_interface/resources/images/ex3/3.png",'1'],
                    ["B", "/home/stergios/git/src/robotHuman/user_interface/resources/images/ex3/4.png",'2']
                    ]
        self._counter=0
        self._exerciseDscr='Σε αυτό το παιχνίδι θα χρειαστώ τη βοήθειά σου. Θέλω να δεις τις εικόνες και να μου πεις τι δείχνουν.'
        self.title= '6'






    def setVariables4(self):
        
        self._imagesStory=  [
                    ["Η Μαρία είναι ένα μικρό κοριτσάκι 3 ετών'", "/home/stergios/git/src/robotHuman/user_interface/resources/images/ex4/1.png",'1'],
                    ["Το κουδούνι χτυπά και η μαμά της Μαρίας ανοίγει την πόρτα'", "/home/stergios/git/src/robotHuman/user_interface/resources/images/ex4/2.png",'2'],
                    ["Η μαμά της Μαρίας λέει: «Καλημέρα!", "/home/stergios/git/src/robotHuman/user_interface/resources/images/ex4/3.png",'3'],
                    ["Ω νομίζω ότι δεν έχω γνωρίσει το γιο σου. Πως τον λένε;'", "/home/stergios/git/src/robotHuman/user_interface/resources/images/ex4/4.png",'4'],
                    ["Άκουσες κάποιον να λέει κάτι που μπορεί να στεναχωρήσει ή να θυμώσει κάποιον από τους ήρωες της ιστορίας;", "/home/stergios/git/src/robotHuman/user_interface/resources/images/ex4/5.png",'5']
        ]

        self._imagesAnswer=  [
                    ["A", "/home/stergios/git/src/robotHuman/user_interface/resources/images/ex4/6.png",'1'],
                    ["B", "/home/stergios/git/src/robotHuman/user_interface/resources/images/ex4/7.png",'2'],
                    ["Γ", "/home/stergios/git/src/robotHuman/user_interface/resources/images/ex4/8.png",'3']
                    ]
        self._counter=0
        self._exerciseDscr='Στις παρακάτω εικόνες θα δούμε το μικρό Γιωργάκη να κάνει κάποιες σκανταλιές. Αφού ακούσεις προσεκτικά την ιστορία θα μαντέψεις τι θα κάνει ο Γιωργάκης. Κάτω από τις εικόνες θα υπάρχουν 2 απαντήσεις. Διάλεξε αυτή που νομίζεις ότι είναι η σωστή'
        self.title= 'Titlos2111111111'





    def setupUi(self):
        print("main")

    def steps(self):
        self.readExersice() 
        self.readAnswers()
        self.reply()
        self.feedback()
        self.continueDialog()

    def readExersice(self):
        print('Read Exercise')
        self.model.nextImage='0'
        self.nextPage3(0)
        self._rosInterface.talker(self._exerciseDscr)
        self.step1()

    def step1(self):
        print("Step first")
        # self._rosInterface.talker('Ο Γιωργάκης κρύβει την σοκολάτα του στο ντουλάπι της κουζίνας πριν πάει να παίξει έξω')
    
    def step2(self):
        self._rosInterface.talker('Όταν ο Γιωργάκης βγαίνει στην αυλή, η γιαγιά του βρίσκει την σοκολάτα και την βάζει στο ψυγείο')
    

    def readAnswers(self):
        print('Read Answers')

        # self._rosInterface.talker('Α  1 ,Β  2, Γ  3, Δ  4, Ε  5')

    def reply(self):
        print('Get Reply')
    def feedback(self):
        print('feedback')
        self._rosInterface.talker('Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε ένα ανθρωπάκι. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 3 ανθρωπάκια')

    def feedbackStore(self,model,value):
        self._answerEx1=value
        print('feedback')
        self.model.currentExerciseID=0
        self._rosInterface.talker('Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε ένα ανθρωπάκι. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 3 ανθρωπάκια')
    


    def continueDialog(self):
        print('continue Dialog')
        self._rosInterface.talker('Είσαι έτοιμος να προχωρήσουμε')

    def readAnswers2(self):
        self._rosInterface.talker('Ο Γιωργάκης γυρνάει στο σπίτι για να φάει με λαχτάρα την σοκολάτα. Που θα ψάξει για την σοκολάτα του;')


    def printResult(self):
        print("Exersice 3:", self._answerEx1)


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
            self._answerEx1=self._rosInterface.getText()
            print('reply!!!!!!!!!!!!!!')
        else:
            self.answerEx32=self._rosInterface.getText()
            print('reply!!!!!!!!!!!!!!')
        self.step=self.step+1
        self.nextPage3(0)


    def getTextMainThread(self):
        thread = Thread(target = self.getText,args=(),daemon=True)
        thread.start()
        print("thread finished...exiting") 
       
    
    def nextPage3(self,value):
        print('Change Image step  {}',self._counter)
        # self.model.nextPageEx2('2')

        if (len(self._imagesStory)>self._counter):
            self._rosInterface.talker(self._imagesStory[self._counter][0])
            self._imagesStoryCur=self._imagesStory[self._counter][0]
            self.model.nextImage=self._imagesStory[self._counter][1]
            self._counter=self._counter+1
            self.getTextMainThread()
        else: 
            self.getTextMainThread()
            self.model.trigger(101)