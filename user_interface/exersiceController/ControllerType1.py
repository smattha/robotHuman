#!/usr/bin/env python3

from pickle import TRUE
import sys
from threading import Thread
import time
from PyQt5.QtCore import QObject, pyqtSignal

from PyQt5.QtCore import QObject, pyqtSlot

class ControllerType1(QObject):
    def __init__(self,ros,model):
        super().__init__()
        print("Initialize the controller for Excersice 1 ")
        self._rosInterface=ros
        self.mainPage=1
        self.model=model
        self._feedback=''
        self._imageAnswerFlag=0
    

    
    def setVariable1(self):
        # self._exersiceDsr='Τώρα θα παίξουμε ένα παιχνίδι με γρίφους. Στην οθόνη που είναι δίπλα μου θα εμφανίζονται οι εικόνες των γρίφων. Κάτω από την εικόνα θα εμφανίζονται 5 πιθανές απαντήσεις. Διάλεξε την απάντηση που σου φαίνεται σωστή και προχώρα στον επόμενο γρίφο'
        self._exersiceDsr='Ένα λιοντάρι ζυγίζει το ίδιο με 2 σκυλάκια. Ένα σκυλάκι ζυγίζει το ίδιο με 2 παπάκια. Πόσα παπάκια ζυγίζουν το ίδιο με το λιοντάρι;'
        
        self._exersiceTitleDsr='Ένα λιοντάρι ζυγίζει το ίδιο με 2 σκυλάκια. Ένα σκυλάκι ζυγίζει το ίδιο με 2 παπάκια.'
        self._answerDsr='Πόσα παπάκια ζυγίζουν το ίδιο με το λιοντάρι;'
        
        self._answerDscr='Α  1 ,Β  2, Γ  3, Δ  4, Ε  5'
        self._title="Το λιοντάρι και τα παπάκια!"
        self._imagePath="./resources/images/ex1/mainImage.png"
        
        self._imageAnswer1='./resources/images/ex1/answer1.png'
        self._imageAnswer2='./resources/images/ex1/answer2.png'
        self._imageAnswer3='./resources/images/ex1/answer3.png'
        self._imageAnswer4='./resources/images/ex1/answer4.png'
        self._imageAnswer5='./resources/images/ex1/answer5.png'

        self._answerEx1Descr='\nΈνα παπάκι\n'
        self._answerEx2Descr='\nΔύο παπάκια\n'
        self._answerEx3Descr='\nΤρία παπάκια\n'
        self._answerEx4Descr='\nΤεσσερά Παπάκια\n'
        self._answerEx5Descr='\nΠέντε Παπάκια\n'
    
    def setVariable2(self):
        self._exersiceDsr='Τώρα θα παίξουμε ένα παιχνίδι με γρίφους. \n Στην οθόνη που είναι δίπλα μου θα εμφανίζονται οι εικόνες των γρίφων.\n Κάτω από την εικόνα θα εμφανίζονται 5 πιθανές απαντήσεις.\n Διάλεξε την απάντηση που σου φαίνεται σωστή και προχώρα στον επόμενο γρίφο'
        # self._exersiceDsr='Ένα λιοντάρι ζυγίζει το ίδιο με 2 σκυλάκια. Ένα σκυλάκι ζυγίζει το ίδιο με 2 παπάκια. Πόσα παπάκια ζυγίζουν το ίδιο με το λιοντάρι;'
        
        self._exersiceTitleDsr='Τώρα θα παίξουμε ένα παιχνίδι με γρίφους.\n Στην οθόνη που είναι δίπλα μου θα εμφανίζονται οι εικόνες των γρίφων. \n  Κάτω από την εικόνα θα εμφανίζονται 5 πιθανές απαντήσεις.'
        self._answerDsr=' Διάλεξε την απάντηση που σου φαίνεται σωστή και προχώρα στον επόμενο γρίφο;'
        
        self._answerDscr='Α   ,Β  , Γ  , Δ  , Ε  '
        self._title="Άσκηση προσοχής"
        self._imagePath="./resources/images/ex2/mainImage.png"
        #self._rosInterface.talker('Ένα από τα αντικείμενα στο κάτω μέρος της οθόνης είναι το ίδιο με το αντικείμενο που φαίνεται στο πάνω μέρος της οθόνης. Ποιο;')
        self._imageAnswer1='./resources/images/ex2/answer1.png'
        self._imageAnswer2='./resources/images/ex2/answer2.png'
        self._imageAnswer3='./resources/images/ex2/answer3.png'
        self._imageAnswer4='./resources/images/ex2/answer4.png'
        self._imageAnswer5='./resources/images/ex2/answer5.png'
        
        self._answerEx1Descr='\nA\n'
        self._answerEx2Descr='\nB\n'
        self._answerEx3Descr='\nΓ\n'
        self._answerEx4Descr='\nΔ\n'
        self._answerEx5Descr='\nΕ\n'



    def setVariableB1(self):
        self._exersiceDsr='Η μαμά καγκουρό ζυγίζει με το μωρό της 60 κιλά. Η μαμά ζυγίζει μόνη της 52 κιλά. Πόσα κιλά ζυγίζει το μωρό της'
        # self._exersiceDsr='Ένα λιοντάρι ζυγίζει το ίδιο με 2 σκυλάκια. Ένα σκυλάκι ζυγίζει το ίδιο με 2 παπάκια. Πόσα παπάκια ζυγίζουν το ίδιο με το λιοντάρι;'
        self._exersiceTitleDsr='Η μαμά καγκουρό ζυγίζει με το μωρό της 60 κιλά. Η μαμά ζυγίζει μόνη της 52 κιλά. .'
        self._answerDsr=' Πόσα κιλά ζυγίζει το μωρό της;'

        self._answerDscr='Α 4,  Β 8, Γ 30, Δ 56, Ε 112'
        self._title="Άσκηση προσοχής"
        self._imagePath="./resources/images/exB1/1.png"
        self._imageAnswerFlag=1
        

        self._answerEx1Descr='\n1\n'
        self._answerEx2Descr='\n2\n'
        self._answerEx3Descr='\n3\n'
        self._answerEx4Descr='\n4\n'
        self._answerEx5Descr='\n5\n'
        #self._rosInterface.talker('Ένα από τα αντικείμενα στο κάτω μέρος της οθόνης είναι το ίδιο με το αντικείμενο που φαίνεται στο πάνω μέρος της οθόνης. Ποιο;')



    def setVariableB2(self):
        self._exersiceDsr='Ο Μάξιμος έκοψε ένα φύλλο χαρτί σε 2 κομμάτια. Το ένα κομμάτι εμφανίζεται στο πάνω μέρος της οθόνης. Ποιο από τα κομμάτια στο κάτω μέρος της οθόνης είναι το άλλο;'
        # self._exersiceDsr='Ένα λιοντάρι ζυγίζει το ίδιο με 2 σκυλάκια. Ένα σκυλάκι ζυγίζει το ίδιο με 2 παπάκια. Πόσα παπάκια ζυγίζουν το ίδιο με το λιοντάρι;'
        self._answerDscr='Α ,  Β , Γ , Δ , Ε '
        self._title="Άσκηση προσοχής"
        self._imagePath="./resources/images/exB2/mainImage.png"
        #self._rosInterface.talker('Ένα από τα αντικείμενα στο κάτω μέρος της οθόνης είναι το ίδιο με το αντικείμενο που φαίνεται στο πάνω μέρος της οθόνης. Ποιο;')

        self._exersiceTitleDsr='Ο Μάξιμος έκοψε ένα φύλλο χαρτί σε 2 κομμάτια.Το ένα κομμάτι εμφανίζεται στο πάνω μέρος της οθόνης.'
        self._answerDsr=' Ποιο από τα κομμάτια στο κάτω μέρος της οθόνης είναι το άλλο;'
        

        #self._rosInterface.talker('Ένα από τα αντικείμενα στο κάτω μέρος της οθόνης είναι το ίδιο με το αντικείμενο που φαίνεται στο πάνω μέρος της οθόνης. Ποιο;')
        self._imageAnswer1='./resources/images/exB2/answer1.png'
        self._imageAnswer2='./resources/images/exB2/answer2.png'
        self._imageAnswer3='./resources/images/exB2/answer3.png'
        self._imageAnswer4='./resources/images/exB2/answer4.png'
        self._imageAnswer5='./resources/images/exB2/answer5.png'
        
        self._answerEx1Descr='\nA\n'
        self._answerEx2Descr='\nB\n'
        self._answerEx3Descr='\nΓ\n'
        self._answerEx4Descr='\nΔ\n'
        self._answerEx5Descr='\nΕ\n'


    def setupUi(self):
        print("main")

    def steps(self):
        self.readExersice() 
        self.readAnswers()
        self.reply()
        self.feedback()
        self.continueDialog()

    def readExersice(self):
        print('Read Exercise 1')
        self._rosInterface.talker(self._exersiceDsr)
        self.stopBeforeShowImageMainThread()

    def readAnswers(self):
        print('Read Answers 1')
        self._rosInterface.talker(self._answerDscr)

    def reply(self):
        print('Get Reply 1')

    def feedback(self,model,value):
        model.results.answerEx1=value
        print('feedback 1')
        self._rosInterface.talker('Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε ένα ανθρωπάκι. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 3 ανθρωπάκια')
    
    def continueDialog(self):
        print('continue Dialog 1')
        self._rosInterface.talker('Είσαι έτοιμος να προχωρήσουμε')


    def feedbackStore(self,model,value):
        self._answerEx1=value
        print('\t\tFeedback:',value)
        self._rosInterface.talker('Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε ένα ανθρωπάκι. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 3 ανθρωπάκια')
   
    def printResult(self):
        print("Exersice1 :", self._answerEx1, self._feedback)


    @pyqtSlot(int)
    def storeAnswer(self,value):
        self.feedbackStore(self.model.result,value)
        self.model.trigger(101)

    def feedbackAnswer(self,value):
        print('Feedback {}',value)
        self._feedback=value
    
    def getImagePath(self):
        return self._imagePath

    def getTitle(self):
        return self._title

        

    showAnswerButtons = pyqtSignal(str, name='showAnswerButtons')
   
    def stopBeforeShowImageMainThread(self):
        thread = Thread(target = self.stopBeforeShowImageMain,args=(),daemon=True)
        thread.start()
        print("Thread finished...exiting")  


    # #Exercise 6
    # showAnswerButtons = pyqtSignal(str, name='showAnswerButtons')
    # showAnswerButtons.emit(self._description)

    def stopBeforeShowImageMain(self):
        # while (len(self._imagesStory)>=self._counter):
        #     time.sleep(5)
        #     thread = Thread(target = self.nextPage4,args=(),daemon=True)
        #     thread.start()
        # while (len(self._imagesStory)>self._counter):
        # self.nextPage4()
        time.sleep(5)
        print("\t\tthread running.......")  
        
        self.showAnswerButtons.emit("")
        # self.nextPage4()