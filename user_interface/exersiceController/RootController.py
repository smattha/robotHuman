#!/usr/bin/env python3


from threading import Thread , Event
from PyQt5.QtCore import QObject, pyqtSlot


class RootController(QObject):
    def __init__(self):
        super().__init__()
        self.correct=True;


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

#meta to feedback
    def continueDialog(self):
        print('--------------------------------------MainController: Eίσαι έτοιμος να προχωρήσουμε;')
        # if self.model.name!='':
        #     print("test")
        #     isFocus=self._rosInterface.focus(self.model.name)
        #     if isFocus==False:
                #1
        self._rosInterface.moveRobotFromFile('/robotApp/positions/focus.csv')
                #self._rosInterface.moveRobotFromFile('/robotApp/positions/feedback.txt')
        #         self._rosInterface.talker( self.model.name +'παρατήρησα ότι δεν ήσουν προσεκτικός κατά την διάρκεια της άσκησης. Προσπάθησε να προσέχεις περισσότερο.')
        #         # self._rosInterface.displayImg('/robotApp/faces/anger.jpg')

        if (self.correct==True):
            self._rosInterface.talker('Μπράβο το πέτυχες!!! Είσαι έτοιμος να προχωρήσουμε;')
        else:
            self._rosInterface.talker('Καλή προσπάθεια! Aλλά δεν το πέτυχες! Είσαι έτοιμος να προχωρήσουμε;')
        self.getTextMainThreadContinue()

    def feedbackStore(self, model1, value):
        self._answerEx1=value
        self.feedbackFN()

    def feedbackFN(self):
        thread = Thread(target=self.stopBeforeShowImageMainF, args=(), daemon=True)
        thread.start()

    #prin to feedback
    def stopBeforeShowImageMainF(self):
        #2
        self._rosInterface.moveRobotFromFile('/robotApp/positions/userFeedback.csv')
        # self._rosInterface.talker(
        #     'Πόσο εύκολος σου φάνηκε ο γρίφος; Εύκολος,έτσι και έτσι ή δύσκολος;')
        # # self.model.showButtonsFeedback()
        # self.getTextMainThreadFeedback()
        self.continueDialog()

    def printResult(self):
        print("Exersice1 :", self._answerEx1, self._feedback)

    def clearResults(self):
        self._answerEx1 = ''
        self._feedback = ''

    @pyqtSlot(int)
    def storeAnswer(self, value):
        self.feedbackStore(self.model.result, value)
        self.model.changeFeedbackLabelWrong()
        print("value :"+str(value))
        for x in self.correctAnswer:
            if (x.casefold()==str(value).casefold()):  
                self.model.changeFeedbackLabelCorrect()
                self.correct=True
            else:
                self.correct=False;
        self.model.trigger(101)
        if hasattr(self, "event"):
            self.event.set()

    def feedbackAnswer(self, value):
        print('Feedback Robot Controller', value)
        if (value=='1'):
            print("Value is 1")
            # self._rosInterface.displayImg('/robotApp/faces/smile1.jpg')
        elif value=='2' :
            print("Value is 2")
            # self._rosInterface.displayImg('/robotApp/faces/smile.jpg')
        elif(value=='3'):    
            print("Value is 3")
            # self._rosInterface.displayImg('/robotApp/faces/surprise.jpg')
        self._feedback=value
        if hasattr(self, "event"):
            self.event.set()

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
        #3
        self._rosInterface.moveRobotFromFile('/robotApp/positions/handRaise.csv')
        self._rosInterface.talker("Παιδάκι όταν είσαι ετοιμό να προχωρήσουμε σήκωσε το χέρι")
        self._rosInterface.getHand()
        # self._rosInterface.displayImg('/robotApp/faces/smile.jpg')
        #self._rosInterface.moveRobotFromFile('/robotApp/positions/read.txt')
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
        print("Call speech to text!")
        self.text=self._rosInterface.getText(self.results)
        if self.text=='timeout':
            return
        self.storeAnswer(self.text)


    def getTextMainThread(self):
        self.event=Event()
        thread = Thread(target = self.getText,args=(self.event,),daemon=True)
        thread.start()

        print("thread finished...exiting")
        return thread
    
    

    def getTextFeedback (self,event: Event) -> None:

        # print("!Get Text!")
        # self.text=self._rosInterface.getText(['Εύκολος','Έτσι και έτσι','δύσκολος','Εύκολο','Έτσι','δύσκολο'])

        if(self.text=='Εύκολο'):
            self.feedbackAnswer('1')
        elif(self.text=='Έτσι και έτσι'):
            self.feedbackAnswer( '2')
        else:
            self.feedbackAnswer( '3')
        
        self.model.showButtonFeedback='show'

    def getTextMainThreadFeedback(self):
        self.event=Event()
        thread = Thread(target = self.getTextFeedback,args=(self.event,),daemon=True)
        thread.start()

        print("thread finished...exiting")
        return thread

    def getTextContinue (self,event: Event) -> None:
        print("Check ")
        self.text=self._rosInterface.getText(['Ναι','όχι','τερματισμός','συνέχεια','επόμενο'])
        print("--------------------------------------"+self.text)
        if(self.text=='όχι'or self.text=='τερματισμός'):
            self.model.trigger(0)
            self.model.name = ''
            self.model.surname =''
            self.model.age = ''
        elif(self.text.casefold()=='Ναι'.casefold() or self.text.casefold()=='ναι'.casefold() or self.text.casefold()=='συνέχεια'.casefold() or self.text.casefold()=='επόμενο'.casefold()):
            self.model.mainController.move2NextPage()
        

        self.model.showButtonFeedback='show'

    def getTextMainThreadContinue(self):
        self.event=Event()
        thread = Thread(target = self.getTextContinue,args=(self.event,),daemon=True)
        thread.start()
        print("thread finished...exiting")
        return thread