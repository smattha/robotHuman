#!/usr/bin/env python3

import sys


class ControllerExersice2(object):
    def __init__(self,ros,model):
        print("Initialize the controller for Excersice 2 ")
        self._rosInterface=ros
        self.mainPage=2
        self.model=model
    
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
        self._rosInterface.talker('Τώρα θα παίξουμε ένα παιχνίδι με γρίφους. Στην οθόνη που είναι δίπλα μου θα εμφανίζονται οι εικόνες των γρίφων. Κάτω από την εικόνα θα εμφανίζονται 5 πιθανές απαντήσεις. Διάλεξε την απάντηση που σου φαίνεται σωστή και προχώρα στον επόμενο γρίφο')
        self._rosInterface.talker('Ένα από τα αντικείμενα στο κάτω μέρος της οθόνης είναι το ίδιο με το αντικείμενο που φαίνεται στο πάνω μέρος της οθόνης. Ποιο;')

    def readAnswers(self):
        print('Read Answers')
        self._rosInterface.talker('Α  1 ,Β  2, Γ  3, Δ  4, Ε  5')

    def reply(self):
        print('Get Reply')
    def feedback(self):
        print('feedback')
        self._rosInterface.talker('Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε ένα ανθρωπάκι. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 3 ανθρωπάκια')
    
    def feedbackStore(self,model,value):
        model.answerEx2=value
        print('feedback')
        self._rosInterface.talker('Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε ένα ανθρωπάκι. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 3 ανθρωπάκια')
    

    def continueDialog(self):
        print('continue Dialog')
        self._rosInterface.talker('Είσαι έτοιμος να προχωρήσουμε')


    def printResult(self):
        print("Exersice2 :", self.model.result.answerEx2)


