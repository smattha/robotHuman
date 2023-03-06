#!/usr/bin/env python3


from threading import Thread
from PyQt5.QtCore import QObject, pyqtSlot


class RootController(QObject):
    def __init__(self):
        super().__init__()

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

        self.stopBeforeShowImageMainThread()

    def readAnswers(self):
        print('Read Answers 1')

    def reply(self):
        print('Get Reply 1')

    def feedback(self, model, value):
        model.results.answerEx1 = value
        print('feedback 1')
        self.model.feedback()

    def continueDialog(self):
        print('--------------------------------------MainController: Eίσαι έτοιμος να προχωρήσουμε ')
        self._rosInterface.talker('Είσαι έτοιμος να προχωρήσουμε')

    def feedbackStore(self, model1, value):
        self._answerEx1 = value
        print('\t\tFeedback:', value)
        self.feedbackFN()

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
        self._answerEx1 = ''
        self._feedback = ''

    @pyqtSlot(int)
    def storeAnswer(self, value):
        self.feedbackStore(self.model.result, value)
        self.model.trigger(101)

    def feedbackAnswer(self, value):
        print('Feedback {}', value)

        self.continueDialog()

    def getImagePath(self):
        return self._imagePath

    def getTitle(self):
        return self._title

    def stopBeforeShowImageMainThread(self):
        thread = Thread(target=self.stopBeforeShowImageMain, args=(), daemon=True)
        thread.start()
        print("Thread finished...exiting")

    def stopBeforeShowImageMain(self):
        
        
        name=self._rosInterface.getNames()
        
        self._rosInterface.talker("Καλημέρα "+name+" όταν είσαι ετοιμός να προχωρήσουμε σήλωσε το χέρι")

        self._rosInterface.talker("Καλημέρα "+name+" όταν είσαι ετοιμός να προχωρήσουμε σήλωσε το χέρι")

        self._rosInterface.getPalm()

        self._rosInterface.talker(self._exersiceDsr + self._answerDscr)
        self.model.showAnswerButtonsFunction()


    def playAudio(self,msg):
        self.msg = msg
        thread = Thread(target=self.playAudioThread, args=(), daemon=True)
        thread.start()
        print("Thread finished...exiting")

    def playAudioThread(self):
        print("\t\tthread running.......")
        self._rosInterface.talker(self.msg)
        # self._rosInterface.talker(self._answerDsr)