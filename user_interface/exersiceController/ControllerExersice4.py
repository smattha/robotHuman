#!/usr/bin/env python3

import sys


class ControllerExersice4(object):
    def __init__(self,ros,model):
        print("Initialize the controller for Excersice 4 ")
        self._rosInterface=ros
        self.mainPage=4
        self.model=model
    
    def setupUi(self):
        print("main")

    def steps(self):
        self.readExersice() 
        # self.readAnswers()
        # self.reply()
        # # self.feedback()
        # self.continueDialog()

    def readExersice(self):
        print('Read Exercise')
        # self._rosInterface.talker('Τώρα θα σου πω κάποιες ιστορίες. Άκουσε προσεκτικά τις ιστορίες γιατί σε κάποιες από αυτές κάποιος λέει κάτι που μπορεί να στεναχωρήσει ή να θυμώσει τον ήρωα.')
        #self._rosInterface.talker('Ένα από τα αντικείμενα στο κάτω μέρος της οθόνης είναι το ίδιο με το αντικείμενο που φαίνεται στο πάνω μέρος της οθόνης. Ποιο;')
    
    def step1(self):
        self._rosInterface.talker('Η Μαρία είναι ένα μικρό κοριτσάκι 3 ετών')

    def step2(self):
        self._rosInterface.talker('Το κουδούνι χτυπά και η μαμά της Μαρίας ανοίγει την πόρτα')
    
    def step3(self):
        self._rosInterface.talker('Μια φίλη της μαμάς της Μαρίας ήρθε επίσκεψη.»')
    
    def step4(self):
        self._rosInterface.talker('Η μαμά της Μαρίας λέει: «Καλημέρα!')

    def step5(self):
        self._rosInterface.talker('Ω νομίζω ότι δεν έχω γνωρίσει το γιο σου. Πως τον λένε;')

    def step6(self):
        self._rosInterface.talker('Άκουσες κάποιον να λέει κάτι που μπορεί να στεναχωρήσει ή να θυμώσει κάποιον από τους ήρωες της ιστορίας;')

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




