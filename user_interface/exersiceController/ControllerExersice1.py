#!/usr/bin/env python3

import sys

from PyQt5.QtCore import QObject, pyqtSlot

class ControllerExersice1(object):
    def __init__(self,ros,model):
        print("Initialize the controller for Excersice 1 ")
        self._rosInterface=ros
        self.mainPage=1
        self.model=model
        self._feedback=''

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
        self._rosInterface.talker('Ένα λιοντάρι ζυγίζει το ίδιο με 2 σκυλάκια. Ένα σκυλάκι ζυγίζει το ίδιο με 2 παπάκια. Πόσα παπάκια ζυγίζουν το ίδιο με το λιοντάρι;')

    def readAnswers(self):
        print('Read Answers 1')
        self._rosInterface.talker('Α  1 ,Β  2, Γ  3, Δ  4, Ε  5')

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
        model.answerEx1=value
        print('feedback')
        self._rosInterface.talker('Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε ένα ανθρωπάκι. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 3 ανθρωπάκια')
   
    def printResult(self):
        print("Exersice1 :", self.model.result.answerEx1, self._feedback)


    @pyqtSlot(int)
    def storeAnswer(self,value):
        self.feedbackStore(self.model.result,value)
        self.model.trigger(7)

    def feedbackAnswer(self,value):
        print('Feedback {}',value)
        self._feedback=value