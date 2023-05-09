#!/usr/bin/env python3


from PyQt5.QtCore import  pyqtSlot
from threading import Thread
from exersiceController.RootController import RootController
from exersiceController.ControllerType2Data import ControllerType2Data

class ControllerType2(RootController,ControllerType2Data):
    def __init__(self,ros,model):
        super().__init__()
        print("Initialize the controller for Excersice 3 ")
        self._rosInterface=ros
        self.mainPage=3
        self.model=model
        self._exercise3Img=0
        self._feedback=''
        self.step=1
        self.noStep=1
        self._imagesStoryCur=''
        self._answerEx1=''
        self.path=self.model.path


    def readExersice(self):
        print('Read Exercise')
        # self.nextPageLoop()
        self.readTextMainThread()



    def step2Store(self,value):
        self.answerEx3_step2=value
        self._rosInterface.talker('Γιατί;')
        self.answerEx3_step3= self._rosInterface.getText()
    

    def feedback(self):
        print('feedback')
        self.feedbackFN()


    def readAnswers2(self):
        self.playAudio(self.answerEx3)

    def readAnswers3(self):
        self.playAudio("Τι είπε ο ήρωας που διάλεξες που μπορεί να στεναχώρησε ή να θύμωσε κάποιον από τους ήρωες;")


    def step2(self,value):
        self._rosInterface.talker("Τι είπε ο ήρωας που διάλεξες που μπορεί να στεναχώρησε ή να θύμωσε κάποιον από τους ήρωες;")
        self.feedbackStore(self.model.result,value)
        self._counter=0
        self.model.trigger(101)

    @pyqtSlot(int)
    def storeAnswer(self,value):

        if self.noStep==1:
            self.feedbackStore(self.model.result,value)
            self._counter=0
            self.model.trigger(101)
        elif self.noStep==3:
            print("\t\t\Feedback for step1/3")
            self.answerEx3=value
            self.readAnswers3()
            self.model.nextImage='1'    
            self.noStep= self.noStep - 1

    @pyqtSlot(str)
    def nextPage3(self,value):
        print('Change Image step 3 --------------------------------{}',self._counter)
        # self.model.nextPageEx2('2')
        if (len(self._imagesStory)>self._counter):
            self._imagesStoryCur=self._imagesStory[self._counter][0]
            self.model.nextImage=self._imagesStory[self._counter][1]
            self._rosInterface.talker(self._imagesStory[self._counter][0])
            self._counter=self._counter+1

            return 
        
        if self.step==1: 
            self.readAnswers2()

            self.model.nextImage='0'
        if self.step==2: 
            self.readAnswers3()
            self.model.nextImage='1'    
    
    @pyqtSlot(str)
    def nextPage4(self):
        self.nextPage3(0)   


    def updateImages(self):
        counter=1
        self.model.nextImage = self._imagesStory[0][1]
        if self.model.name=='':
            self.model.name=self._rosInterface.getNames()
        self._rosInterface.talker(self.model.name +" "+self._exerciseDscr)
        self._rosInterface.talker(self.model.name+" όταν είσαι ετοιμός να προχωρήσουμε σήκωσε το χέρι")
        self._rosInterface.getHand()
        self._rosInterface.displayImg('/robotApp/faces/smile.jpg')
        while (len(self._imagesStory)>self._counter):
            self.nextPage4()
            if (counter==1):
                counter=0
            print("\t\tthread running.......")
        self.nextPage4()
        self.getTextMainThread()
        

    def readTextMainThread(self):
        thread = Thread(target = self.updateImages,args=(),daemon=True)
        thread.start()
        print("Thread finished...exiting")

    # def nextPageLoop(self):
    #     self.getTextMainThread()


    # def feedbackAnswer(self,value):
    #     print('Feedback {}',value)
    #     self._feedback=value

    # def setupUi(self):
    #     print("main")

        # def feedbackFN(self):
    #     thread = Thread(target=self.stopBeforeShowImageMainF, args=(), daemon=True)
    #     thread.start()

    # def stopBeforeShowImageMainF(self):
    #     self._rosInterface.talker(
    #         'Πόσο εύκολος σου φάνηκε ο γρίφος; Αν σου φάνηκε εύκολος διάλεξε 3 ανθρωπάκια. Αν σου φάνηκε έτσι και έτσι, διάλεξε 2 ανθρωπάκια. Αν σου φάνηκε δύσκολος διάλεξε 1 ανθρωπάκι')
    #     self.model.showButtonsFeedback()

    # def feedbackStore(self,model,value):
    #     self._answerEx1=value
    #     print('feedback Answer store ',value)
    #     self.feedback()


    # def step1(self):
    #     self._rosInterface.talker('Ο Γιωργάκης κρύβει την σοκολάτα του στο ντουλάπι της κουζίνας πριν πάει να παίξει έξω')
    
    # def step2(self):
    #     self._rosInterface.talker('Όταν ο Γιωργάκης βγαίνει στην αυλή, η γιαγιά του βρίσκει την σοκολάτα και την βάζει στο ψυγείο')
    
    # def readAnswers(self):
    #     print('Read Answers')


