#!/usr/bin/env python3


from PyQt5.QtCore import  pyqtSlot
from threading import Thread
from exersiceController.MainController import MainController
from exersiceController.ControllerExersice5Data import  ControllerExersice5Data

class ControllerExersice5(MainController,ControllerExersice5Data):
    def __init__(self,ros,model):
        super().__init__()
        print("Initialize the controller for Excersice 1 ")
        self._rosInterface=ros
        self.mainPage=5
        self.model=model
        self._feedback=''
        self._image2=0
        self._imageAnswerFlag=1
        self._answerEx1=''
        self.path=self.model.path

    



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

        self._counter =1
        self.stopBeforeShowImageMainThread()
    def readAnswers(self):
        print('Read Answers 1')


    def reply(self):
        print('Get Reply 1')

    def feedback(self,model,value):
        model.results.answerEx1=value
        print('feedback 1')
       
    def continueDialog(self):
        print('continue Dialog 1')
        self._rosInterface.talker('||||||||||||||||||||||||||||||||||||||||||||||||||Controller 5 Είσαι έτοιμος να προχωρήσουμε')


    def feedbackStore(self,model,value):
        self._answerEx1=value
        print('\t\t\tfeedback ',value)
      

    def feedbackFN(self):
            thread = Thread(target=self.stopBeforeShowImageMainF, args=(), daemon=True)
            thread.start()

    def stopBeforeShowImageMainF(self):
            self._rosInterface.talker(
                'Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε 3 ανθρωπάκια. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 1 ανθρωπάκι')
            self.model.showButtonsFeedback()



    def printResult(self):
        print("Exersice1 :", self._answerEx1, self._feedback)


    def clearResults(self):
        self._answerEx1=''
        self._feedback=''


    @pyqtSlot(int)
    def storeAnswer(self,value):
        self.feedbackStore(self.model.result,value)
        if self._counter==2:
            self._counter=1
            # self._rosInterface.talker1(self._exersiceDsr2)
            self.playAudio(self._exersiceDsr2)
            self.readAnswers()
        elif  self._counter==1:
            print('--------------------------------------------------------------------------------------------------------------')
            self.model.trigger(self._image2)
            # self._rosInterface.talker(self._part2)
            self.playAudio(self._part2)
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
        self._counter == 1

    def trigger(self):
        self.model.trigger(101)
        self.feedbackFN()


