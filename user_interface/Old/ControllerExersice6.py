#!/usr/bin/env python3

import sys
from PyQt5.QtCore import QObject, pyqtSlot

class ControllerExersice6(object):


    def __init__(self,ros,model):
        print("Initialize the controller for Excersice 6 ")
        self._rosInterface=ros
        self.mainPage=6
        self.model=model

        self._feedback=''
    
    def feedbackAnswer(self,value):
        print('Feedback {}',value)
        self._feedback=value
    

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
        self._rosInterface.talker('Σε αυτό το παιχνίδι θα χρειαστώ τη βοήθειά σου. Θέλω να δεις τις εικόνες και να μου πεις τι δείχνουν.')
        #self._rosInterface.talker('Ένα από τα αντικείμενα στο κάτω μέρος της οθόνης είναι το ίδιο με το αντικείμενο που φαίνεται στο πάνω μέρος της οθόνης. Ποιο;')

    def readAnswers(self):
        print('Read Answers')
        # self._rosInterface.talker('Α  1 ,Β  2, Γ  3, Δ  4, Ε  5')

    def reply(self):
        print('Get Reply')
    def feedback(self):
        print('feedback')
        self._rosInterface.talker('Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε ένα ανθρωπάκι. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 3 ανθρωπάκια')



    def continueDialog(self):
        print('continue Dialog')
        self._rosInterface.talker('Είσαι έτοιμος να προχωρήσουμε')


    def stepA(self,model,value):
        print("Exercise 5 part b")
        valueText=self._rosInterface.getText()
        model.answerEx6A=valueText


    def feedbackStore(self,model,value):
        valueText=self._rosInterface.getText()
        model.answerEx6B=valueText
        print('feedback')
        self._rosInterface.talker('Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε ένα ανθρωπάκι. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 3 ανθρωπάκια')
    
    def printResult(self,model):
        print("Exersice1 :", model.answerEx6B)

    def printResult(self):
        print("Exersice 6 A:{},B:{} :", self.model.result.answerEx6A,self.model.result.answerEx6B)




    @pyqtSlot(int)
    def storeAnswer(self,value):
        self.feedbackStore(self.model.result,value)
        self.model.trigger(7)

    @pyqtSlot(str)
    def nextPageEx6(self,value):
        print('Change Image 6')
        self.stepA(self.model.result,value)
        self.model.nextPageEx6('2')
