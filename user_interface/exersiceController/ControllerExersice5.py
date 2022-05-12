#!/usr/bin/env python3

import sys

from PyQt5.QtCore import QObject, pyqtSlot

class ControllerExersice5(object):
    def __init__(self,ros,model):
        print("Initialize the controller for Excersice 1 ")
        self._rosInterface=ros
        self.mainPage=5
        self.model=model
        self._feedback=''
        self._image2=0
        self._imageAnswerFlag=1
   
    
    def setVariable1(self):
        self._exersiceDsr='Τώρα θα παίξουμε ένα παιχνίδι με γρίφους. Στην οθόνη που είναι δίπλα μου θα εμφανίζονται οι εικόνες των γρίφων. \n Κάτω από την εικόνα θα εμφανίζονται 5 πιθανές απαντήσεις.\n Διάλεξε την απάντηση που σου φαίνεται σωστή και προχώρα στον επόμενο γρίφο'
        self._answerDsr='Κοίτα προσεκτικά την εικόνα και βρες πόσοι άνθρωποι φοράνε καπέλο'
        self._title="Δραστηριότητα 5"
        self._imagePath="./resources/images/ex5/image.png"
        self._counter=1
        self._part2="Κοίτα προσεκτικά την εικόνα και δείξε μου που είναι το μικρό σκυλάκι."

        self._imageAnswer1=''
        self._imageAnswer2=''
        self._imageAnswer3=''
        self._imageAnswer4=''
        self._imageAnswer5=''

        self._answerEx1Descr='\n1\n'
        self._answerEx2Descr='\n2\n'
        self._answerEx3Descr='\n3\n'
        self._answerEx4Descr='\n4\n'
        self._answerEx5Descr='\n5\n'

        self._exersiceTitleDsr='Τώρα θα παίξουμε ένα παιχνίδι με γρίφους. \nΣτην οθόνη που είναι δίπλα μου θα εμφανίζονται οι εικόνες των γρίφων. \n Κάτω από την εικόνα θα εμφανίζονται 5 πιθανές απαντήσεις.'

    
    


    
    def setVariable2(self):
        self._exersiceDsr='Κοίτα προσεκτικά την εικόνα και βρες πόσες γάτες υπάρχουν;'
        self._exersiceDsr2="Κοίτα προσεκτικά την εικόνα και βρες πόσα είναι τα (γκρι) περιστέρια."
        self._answerDsr='Κοίτα προσεκτικά την εικόνα και βρες πόσα είναι τα (γκρι) περιστέρια.'
        self._title="Άσκηση προσοχής"
        self._imagePath="./resources/images/exB5/1.jpg"
        self._counter=2
        self._part2="Κοίτα προσεκτικά την εικόνα και δείξε μου που είναι το κάστρο"

        self._imageAnswer1=''
        self._imageAnswer2=''
        self._imageAnswer3=''
        self._imageAnswer4=''
        self._imageAnswer5=''

        self._answerEx1Descr='1'
        self._answerEx2Descr='2'
        self._answerEx3Descr='3'
        self._answerEx4Descr='4'
        self._answerEx5Descr='5'

        self._exersiceTitleDsr='Τώρα θα παίξουμε ένα παιχνίδι με γρίφους. Στην οθόνη που είναι δίπλα μου θα εμφανίζονται οι εικόνες των γρίφων. \n Κάτω από την εικόνα θα εμφανίζονται 5 πιθανές απαντήσεις.'

    


    def setVariableB5(self):
        self._exersiceDsr='Τώρα θα παίξουμε ένα παιχνίδι με γρίφους. Στην οθόνη που είναι δίπλα μου θα εμφανίζονται οι εικόνες των γρίφων. Κάτω από την εικόνα θα εμφανίζονται 5 πιθανές απαντήσεις. Διάλεξε την απάντηση που σου φαίνεται σωστή και προχώρα στον επόμενο γρίφο'
        self._answerDsr='Α  1 ,Β  2, Γ  3, Δ  4, Ε  5'
        self._title="Δραστηριότητα 5!!!!!!!!"
        self._imagePath="./resources/images/exB5/1.jpg"
        self._imagePath2="./resources/images/exB5/1.jpg"

        self._imageAnswer1=''
        self._imageAnswer2=''
        self._imageAnswer3=''
        self._imageAnswer4=''
        self._imageAnswer5=''

        self._answerEx1Descr='1'
        self._answerEx2Descr='2'
        self._answerEx3Descr='3'
        self._answerEx4Descr='4'
        self._answerEx5Descr='5'

        self._exersiceTitleDsr='Τώρα θα παίξουμε ένα παιχνίδι με γρίφους. Στην οθόνη που είναι δίπλα μου θα εμφανίζονται οι εικόνες των γρίφων. \n Κάτω από την εικόνα θα εμφανίζονται 5 πιθανές απαντήσεις.'

    


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
    def readAnswers(self):
        print('Read Answers 1')
        self._rosInterface.talker(self._answerDsr)

    def reply(self):
        print('Get Reply 1')

    def feedback(self,model,value):
        model.results.answerEx1=value
        print('feedback 1')
        # self._rosInterface.talker('Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε ένα ανθρωπάκι. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 3 ανθρωπάκια')
    
    def continueDialog(self):
        print('continue Dialog 1')
        self._rosInterface.talker('Είσαι έτοιμος να προχωρήσουμε')


    def feedbackStore(self,model,value):
        self._answerEx1=value
        print('\t\t\tfeedback ',value)
        # self._rosInterface.talker('Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε ένα ανθρωπάκι. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 3 ανθρωπάκια')
   
    def printResult(self):
        print("Exersice1 :", self._answerEx1, self._feedback)


    @pyqtSlot(int)
    def storeAnswer(self,value):
        self.feedbackStore(self.model.result,value)
        if self._counter==2:
            self._counter=1
            self._rosInterface.talker(self._exersiceDsr2)
            self.readAnswers()
        elif  self._counter==1:
            print('--------------------------------------------------------------------------------------------------------------')
            self._rosInterface.talker(self._part2)
            self.model.trigger(self._image2)
            self._counter=0

    def feedbackAnswer(self,value):
        print('Feedback {}',value)
        self._feedback=value
    
    def getImagePath(self):
        return self._imagePath

    def getTitle(self):
        return self._title

    @pyqtSlot(int)
    def storePose(self,value):
        self._answerEx2=value
        print('\t\t\tfeedback 2',value)
        self.model.trigger(101)
        self._rosInterface.talker('Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε ένα ανθρωπάκι. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 3 ανθρωπάκια')
        # self._model.selectedExercise=value
