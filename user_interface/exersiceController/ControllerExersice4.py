#!/usr/bin/env python3

import sys
from PyQt5.QtCore import QObject, pyqtSlot

class ControllerExersice4(object):
    def __init__(self,ros,model):
        print("Initialize the controller for Excersice 4 ")
        self._rosInterface=ros
        self.mainPage=4
        self.model=model
        self._exercise4Img=0
        self._feedback=''
    
    def feedbackAnswer(self,value):
        print('Feedback {}',value)
        self._feedback=value

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




    def feedbackStore(self,model,value):
        model.answerEx4=value
        print('feedback')
        self._rosInterface.talker('Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε ένα ανθρωπάκι. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 3 ανθρωπάκια')
    

    def printResult(self):
        print("Exersice4 :", self.model.result.answerEx4)



    @pyqtSlot(int)
    def storeAnswer(self,value):
        self.feedbackStore(self.model.result,value)
        self.model.trigger(7)

    @pyqtSlot(str)
    def nextPage4(self,value):
        if self._exercise4Img==0:
            self.step2()
        elif self._exercise4Img==1:
            self.step3()
        elif self._exercise4Img==2:
            self.step4()
        elif self._exercise4Img==3:
            self.step5()
        else:
            self.step6()
        self._exercise4Img=self._exercise4Img+1;
        self.model.nextPageEx4('2')
