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
   
    
    def setVariable1(self):
        self._exersiceDsr='Τώρα θα παίξουμε ένα παιχνίδι με γρίφους. Στην οθόνη που είναι δίπλα μου θα εμφανίζονται οι εικόνες των γρίφων. Κάτω από την εικόνα θα εμφανίζονται 5 πιθανές απαντήσεις. Διάλεξε την απάντηση που σου φαίνεται σωστή και προχώρα στον επόμενο γρίφο'
        self._answerDscr='Α  1 ,Β  2, Γ  3, Δ  4, Ε  5'
        self._title="Δραστηριότητα 5!!!!!!!!"
        self._imagePath="./resources/images/ex5/image.png"
    
    def setVariable2(self):
        self._exersiceDsr='Ένα λιοντάρι ζυγίζει το ίδιο με 2 σκυλάκια. Ένα σκυλάκι ζυγίζει το ίδιο με 2 παπάκια. Πόσα παπάκια ζυγίζουν το ίδιο με το λιοντάρι;'
        self._answerDscr='Α  1 ,Β  2, Γ  3, Δ  4, Ε  5'
        self._title="Άσκηση προσοχής"
        self._imagePath="./resources/images/ex2/mainImage.png"
        self._rosInterface.talker('Ένα από τα αντικείμενα στο κάτω μέρος της οθόνης είναι το ίδιο με το αντικείμενο που φαίνεται στο πάνω μέρος της οθόνης. Ποιο;')


    def setVariableB5(self):
        self._exersiceDsr='Τώρα θα παίξουμε ένα παιχνίδι με γρίφους. Στην οθόνη που είναι δίπλα μου θα εμφανίζονται οι εικόνες των γρίφων. Κάτω από την εικόνα θα εμφανίζονται 5 πιθανές απαντήσεις. Διάλεξε την απάντηση που σου φαίνεται σωστή και προχώρα στον επόμενο γρίφο'
        self._answerDscr='Α  1 ,Β  2, Γ  3, Δ  4, Ε  5'
        self._title="Δραστηριότητα 5!!!!!!!!"
        self._imagePath="./resources/images/exB5/1.jpg"

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
        print('feedback--------------------------------------------------')
        self._rosInterface.talker('Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε ένα ανθρωπάκι. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 3 ανθρωπάκια')
   
    def printResult(self):
        print("Exersice1 :", self._answerEx1, self._feedback)


    @pyqtSlot(int)
    def storeAnswer(self,value):
        self.feedbackStore(self.model.result,value)
        self.model.trigger(11)

    def feedbackAnswer(self,value):
        print('Feedback {}',value)
        self._feedback=value
    
    def getImagePath(self):
        return self._imagePath

    def getTitle(self):
        return self._title

    @pyqtSlot(int)
    def storePose(self,value):
        self.feedbackStore(self.model.result,value)
        self.model.trigger(7)
        # self._model.selectedExercise=value
