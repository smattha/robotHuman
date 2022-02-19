#!/usr/bin/env python3

import sys


class ControllerExersice5(object):
    def __init__(self,ros):
        print("Initialize the controller for Excersice 5")
        self.mainPage=5

        self._rosInterface=ros
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
        self._rosInterface.talker('Σε αυτό το παιχνίδι θα χρειαστώ τη βοήθειά σου. Θέλω να γίνουμε ντεντέκτιβ και να βρούμε κάποια κρυμμένα αντικείμενα στις παρακάτω εικόνες')
        self._rosInterface.talker('Κοίτα προσεκτικά την εικόνα και βρες πόσοι άνθρωποι φοράνε καπέλο.')

    def readAnswers(self):
        print('Read Answers')
        self._rosInterface.talker('Α  1 ,Β  2, Γ  3, Δ  4, Ε  5')

    def reply(self):
        print('Get Reply')
    def feedback(self):
        print('feedback')
        self._rosInterface.talker('Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε ένα ανθρωπάκι. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 3 ανθρωπάκια')


    def continueDialog(self):
        print('continue Dialog')
        self._rosInterface.talker('Είσαι έτοιμος να προχωρήσουμε')





