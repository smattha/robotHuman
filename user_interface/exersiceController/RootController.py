#!/usr/bin/env python3


from threading import Thread , Event
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
        self.model.feedback(value)

    def continueDialog(self):
        print('--------------------------------------MainController: Eίσαι έτοιμος να προχωρήσουμε;')
        if self.model.name!='':
            print("test")
            isFocus=self._rosInterface.focus(self.model.name)
            if isFocus==False:
                self._rosInterface.talker( self.model.name +'παρατήρησα ότι δεν ήσουν προσεκτικός κατά την διάρκεια της άσκησης. Προσπάθησε να προσέχεις περισσότερο.')
                self._rosInterface.displayImg('/robotApp/faces/anger.jpg')
                self._rosInterface.moveRobotFromFile('/robotApp/positions/displayImg.txt')
        self._rosInterface.talker('Είσαι έτοιμος να προχωρήσουμε;')

    def feedbackStore(self, model1, value):
        self._answerEx1=value
        self.feedbackFN()

    def feedbackFN(self):
        thread = Thread(target=self.stopBeforeShowImageMainF, args=(), daemon=True)
        thread.start()

    def stopBeforeShowImageMainF(self):
        # self._rosInterface.moveRobotFromFile('/robotApp/positions/voice.txt')
        self._rosInterface.talker(
            'Πόσο εύκολος σου φάνηκε ο γρίφος; Εύκολος,έτσι και έτσι ή δύσκολος;')
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
        if hasattr(self, "event"):
            self.event.set()

    def feedbackAnswer(self, value):
        print('Feedback Robot Controller', value)
        if (value=='1'):
            print("Value is 1")
            self._rosInterface.displayImg('/robotApp/faces/smile1.jpg')
        elif value=='2' :
            print("Value is 2")
            self._rosInterface.displayImg('/robotApp/faces/smile.jpg')
        elif(value=='3'):    
            print("Value is 3")
            self._rosInterface.displayImg('/robotApp/faces/surprise.jpg')
        self._feedback=value

        self.continueDialog()

    def getImagePath(self):
        return self._imagePath

    def getTitle(self):
        return self._title

    def stopBeforeShowImageMainThread(self):
        thread = Thread(target=self.stopBeforeShowImageMain, args=(), daemon=True)
        thread.start()


    def stopBeforeShowImageMain(self):
        
        while self.model.name=='':
            self.model.name=self._rosInterface.getNames()
        self._rosInterface.talker(self.model.name+" όταν είσαι ετοιμός να προχωρήσουμε σήκωσε το χέρι")
        self._rosInterface.getHand()
        self._rosInterface.displayImg('/robotApp/faces/smile.jpg')
        self._rosInterface.talker(self._exersiceDsr + self._answerDscr)
        self.thread=self.getTextMainThread()
        self.model.showAnswerButtonsFunction()


    def playAudio(self,msg):
        print("Text to speech: Thread Starting!!!")
        self.msg = msg
        thread = Thread(target=self.playAudioThread, args=(), daemon=True)
        thread.start()
        print("Text to speech: Thread finished!!!")

    def playAudioThread(self):
        print("\t\tthread running.......")
        self._rosInterface.talker(self.msg)
        # self._rosInterface.talker(self._answerDsr)
    
    def getText (self,event: Event) -> None:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Get Text!!!!")
        self.text=self._rosInterface.getText()
        self.storeAnswer(self.text)


    def getTextMainThread(self):
        self.event=Event()
        thread = Thread(target = self.getText,args=(self.event,),daemon=True)
        thread.start()

        print("thread finished...exiting")
        return thread
    
    