#!/usr/bin/env python3

from ast import Store
import sys
from typing import Counter
from PyQt5.QtCore import QObject, pyqtSlot
from threading import Thread
import time


class ControllerType2(object):
    def __init__(self,ros,model):
        print("Initialize the controller for Excersice 3 ")
        self._rosInterface=ros
        self.mainPage=3
        self.model=model
        self._exercise3Img=0
        self._feedback=''
        self.step=1
        self.nostep=1
        self._imagesStoryCur=''
        self._answerEx1=''
        self.path=self.model.path

    def feedbackAnswer(self,value):
        print('Feedback {}',value)
        self._feedback=value

    def setVariables3(self):
    
        self._imagesStory=  [
                    ["Ο Γιωργάκης κρύβει την σοκολάτα του στο ντουλάπι της κουζίνας πριν πάει να παίξει έξω", self.path+"/resources/images/ex3/1.png",'1'],
                    ["Όταν ο Γιωργάκης βγαίνει στην αυλή, η γιαγιά του βρίσκει την σοκολάτα και την βάζει στο ψυγείο", self.path+"/resources/images/ex3/2.png",'2']
 
        ]

        self._imagesAnswer=  [
                    ["\nΝτουλάπι\n", self.path+"/resources/images/ex3/3.png",'1'],
                    ["\nΨυγείο\n", self.path+"/resources/images/ex3/4.png",'2']
                    ]
        self._counter=0
        self._exerciseDscr='Στις παρακάτω εικόνες θα δούμε το μικρό Γιωργάκη να κάνει κάποιες σκανταλιές. Αφού ακούσεις προσεκτικά την ιστορία θα μαντέψεις τι θα κάνει ο Γιωργάκης. '
        # self.title_= '3'
        self.title='Ο Γιωργάκης και η σοκολάτα!'
        self.answerEx3='Ο Γιωργάκης γυρνάει στο σπίτι για να φάει με λαχτάρα την σοκολάτα. Που θα ψάξει για την σοκολάτα του;'

    def setVariables4(self):
        
        self._imagesStory=  [
                    ["Η Μαρία είναι ένα μικρό κοριτσάκι 3 ετών'", self.path+"/resources/images/ex4/1.png",'1'],
                    ["Το κουδούνι χτυπά και η μαμά της Μαρίας ανοίγει την πόρτα'", self.path+"/resources/images/ex4/2.png",'2'],
                    ["Μια φίλη της μαμάς της Μαρίας ήρθε επίσκεψη", self.path+"/resources/images/ex4/3.png",'3'],
                    ["Η μαμά της Μαρίας λέει: «Καλημέρα!", self.path+"/resources/images/ex4/4.png",'3'],
                    ["Ω νομίζω ότι δεν έχω γνωρίσει το γιο σου. Πως τον λένε;'", self.path+"/resources/images/ex4/5.png",'4']
        ]

        self._imagesAnswer=  [
                    ["\nMαρία\n", self.path+"/resources/images/ex4/6.png",'1'],
                    ["\nΜαμά\n", self.path+"/resources/images/ex4/7.png",'2'],
                    ["\nΦίλη\n", self.path+"/resources/images/ex4/8.png",'3']
                    ]
        self._counter=0
        self._exerciseDscr=' Τώρα θα σου πω κάποιες ιστορίες. Άκουσε προσεκτικά τις ιστορίες γιατί σε κάποιες από αυτές κάποιος λέει κάτι που μπορεί να στεναχωρήσει ή να θυμώσει τον ήρωα.'
        self.title= 'Η Μαρία και η μαμά της'
        self.answerEx3="Άκουσες κάποιον να λέει κάτι που μπορεί να στεναχωρήσει ή να θυμώσει κάποιον από τους ήρωες της ιστορίας;"


    def setVariablesB3(self):
        
        self._imagesStory=  [
                   ["Κατά τη διάρκεια του πολέμου, ο κόκκινος στρατός έπιασε έναν στρατιώτη μέλος του μπλε στρατού", self.path+"/resources/images/exB3/1.png",'1'],
                   ["Ήθελαν να τους πει πού βρίσκονται τα τανκς του στρατού του.\n Τα τανκς μπορεί να είναι είτε στη θάλασσα, είτε στο βουνό.\n ", self.path+"/resources/images/exB3/2.png",'2'],
                   ["Ο φυλακισμένος στρατιώτης είναι πολύ γενναίος και έξυπνος και θέλει να τους ξεγελάσει.\n Tα τανκς είναι στην πραγματικότητα στα βουνά.\n ", self.path + "/resources/images/exB3/2.png", '3'],
        ]

        self.answerEx3="Οι αντίπαλοι στρατιώτες τον ρωτάνε πού είναι τα τανκς; Τι θα απαντήσει ο μπλε στρατιώτης "

        self._imagesAnswer=  [
                    ["\nΒουνό\n", self.path+"/resources/images/exB3/3.png",'1'],
                    ["\nΘάλασσα\n", self.path+"/resources/images/exB3/4.png",'2']
                    ]
        self._counter=0
        self._exerciseDscr='Στις παρακάτω εικόνες θα δούμε την ιστορία ενός μικρού στρατιώτη. Αφού ακούσεις προσεκτικά την ιστορία θα χρειαστεί να απαντήσεις σωστά στην ερώτηση που θα σου κάνω.'
        self.title= 'Ο μικρός στρατιώτης!'


    def setVariablesB4(self):
        
        self._imagesStory=  [
                    ["Η Σοφία είναι μαθήτρια της Γ Δημοτικού", self.path+"/resources/images/exB4/1.png",'1'],
                    ["Η Σοφία είναι πολύ χαρούμενη για τη νέα κασετίνα που της αγόρασε η μαμά της", self.path+"/resources/images/exB4/2.png",'2'],
                    ["Το κουδούνι χτυπά και η φίλης της Σοφίας μπαίνει στην τάξη", self.path+"/resources/images/exB4/3.png",'2'],
                    ["Τι απαίσια κασετίνα.. Ελπίζω σύντομα να πάρεις καινούρια»", self.path+"/resources/images/exB4/3.png",'2']
 
        ]

        self.answerEx3="Άκουσες κάποιον να λέει κάτι που μπορεί να στεναχωρήσει ή να θυμώσει κάποιον από τους ήρωες της ιστορίας;"

        self._imagesAnswer=  [
                    ["\nΣοφία\n", self.path+"/resources/images/exB4/5.png",'1'],
                    ["\nΦίλη\n", self.path+"/resources/images/exB4/6.png",'2']
                    ]
        self._counter=0
        self._exerciseDscr='ώρα θα σου πω κάποιες ιστορίες. Άκουσε προσεκτικά τις ιστορίες γιατί σε κάποιες από αυτές κάποιος λέει κάτι που μπορεί να στεναχωρήσει ή να θυμώσει τον ήρωα'
        self.title= 'Η μικρή Σοφία!'
        # self.nostep=3


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

        # self.nextPage3(0)
        self.nextPageLoop()
        # self.step1()

    def step1(self):
        self._rosInterface.talker('Ο Γιωργάκης κρύβει την σοκολάτα του στο ντουλάπι της κουζίνας πριν πάει να παίξει έξω')
    
    def step2(self):
        self._rosInterface.talker('Όταν ο Γιωργάκης βγαίνει στην αυλή, η γιαγιά του βρίσκει την σοκολάτα και την βάζει στο ψυγείο')
    

    def step2Store(self,value):
        self.answerEx3_step2=value
        self._rosInterface.talker('Γιατί;')
        self.answerEx3_step3= self._rosInterface.getText()
    
    def readAnswers(self):
        print('Read Answers')

        # self._rosInterface.talker('Α  1 ,Β  2, Γ  3, Δ  4, Ε  5')

    def reply(self):
        print('Get Reply')
    def feedback(self):
        print('feedback')
        self.feedbackFN()
        # self._rosInterface.talker1('Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε 3 ανθρωπάκια. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 1 ανθρωπάκι')

    def feedbackFN(self):
        thread = Thread(target=self.stopBeforeShowImageMainF, args=(), daemon=True)
        thread.start()

    def stopBeforeShowImageMainF(self):
        self._rosInterface.talker(
            'Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε 3 ανθρωπάκια. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 1 ανθρωπάκι')
        self.model.showButtonsFeedback()

    def feedbackStore(self,model,value):
        self._answerEx1=value
        print('feedback Answer store ',value)
        # self._rosInterface.talker('Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε 3 ανθρωπάκια. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 1 ανθρωπάκι')
    


    def continueDialog(self):
        print('continue Dialog')
        self._rosInterface.talker('Είσαι έτοιμος να προχωρήσουμε')

    def readAnswers2(self):
        self._rosInterface.talker(self.answerEx3)



    def readAnswers3(self):
        self._rosInterface.talker("Τι είπε ο ήρωας που διάλεξες που μπορεί να στεναχώρησε ή να θύμωσε κάποιον από τους ήρωες;")



    def printResult(self):
        print("Exersice 3:", self._answerEx1,self._feedback)

    def clearResults(self):
        self._answerEx1=''
        self._feedback=''


    def step2(self,value):
        self._rosInterface.talker("Τι είπε ο ήρωας που διάλεξες που μπορεί να στεναχώρησε ή να θύμωσε κάποιον από τους ήρωες;")
        self.feedbackStore(self.model.result,value)
        self._counter=0
        self.model.trigger(101)

    @pyqtSlot(int)
    def storeAnswer(self,value):

        if self.nostep==1:
            self.feedbackStore(self.model.result,value)
            self._counter=0
            self.model.trigger(101)
        elif self.nostep==3:
            print("\t\t\Feedback for step1/3")
            self.answerEx3=value
            self.readAnswers3()
            self.model.nextImage='1'    
            self.nostep=self.nostep-1



    @pyqtSlot(str)
    def nextPage3(self,value):
        print('Change Image step 3 --------------------------------{}',self._counter)
        # self.model.nextPageEx2('2')
        if (len(self._imagesStory)>self._counter):

            self._imagesStoryCur=self._imagesStory[self._counter][0]
            self.model.nextImage=self._imagesStory[self._counter][1]
            self._rosInterface.talker(self._imagesStory[self._counter][0])
            self._counter=self._counter+1

            return 
        
        if self.step==1: 
            self.readAnswers2()
            self.model.nextImage='0'
        if self.step==2: 
            self.readAnswers3()
            self.model.nextImage='1'    
    
    @pyqtSlot(str)
    def nextPage4(self):
        self.nextPage3(0)   


    def updateImages(self):
        # while (len(self._imagesStory)>=self._counter):
        #     time.sleep(5)
        #     thread = Thread(target = self.nextPage4,args=(),daemon=True)
        #     thread.start()
        counter=1

        #self._imagesStoryCur = self._imagesStory[self._counter][0]
        self.model.nextImage = self._imagesStory[0][1]

        self._rosInterface.talker(self._exerciseDscr)
        while (len(self._imagesStory)>self._counter):
            self.nextPage4()
            if (counter==1):
                #time.sleep(self.model.sleepForAnswer2)
                counter=0
            #time.sleep(self.model.sleepForNextImage)
            print("\t\tthread running.......")  
        self.nextPage4()

    def getTextMainThread(self):
        thread = Thread(target = self.updateImages,args=(),daemon=True)
        thread.start()
        print("Thread finished...exiting")   

        


    def nextPageLoop(self):
        self.getTextMainThread()
            # self.getTextMainThread()
            # self.sleepThread()
            