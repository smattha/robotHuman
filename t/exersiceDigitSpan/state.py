import time
from random import *
class stateRecord:
    def __init__(self, pauseCicles, label, ui,number='0'):
        self.pause=4
        self.pause=pauseCicles
        self.label=label
        self.UI=ui
        self.number=number

    

class state():
    def __init__(self):

        self.firstStep()

    def firstStep(self):

        self.newLoop=True;
        self.current=0;
        self.changeRecord=False
        self.records=[]
        drawUI=stateRecord(100,'','drawUI')
        label2=stateRecord(20,'Ξεκινάμε','',str(randint(1, 9)))
        draw1=stateRecord(8,'','draw1',str(randint(1, 9)))
        
        label1=stateRecord(-10,'Digit span - verbal working memory\n\n\n'+\
            'Θα παρουσιάστει μια ακολουθία ψηφίων.\n\
                Μετά θα πρέπει να επαναλάβες την ακολουθία. Αν επαναλάβεις την ακολουθία θα παρουσιάστει μια μεγαλύτερη ακολουθία.\n'+
                ' Αυτό συνεχίζεται μέχρι το άτομο να μην μπορεί πλέον να επαναλάβει την ακολουθία. \n\nΠάτα το s ή το space για να ξεκινήσουμε.','',str(randint(1, 9)))

        self.records.append(label1)
        self.records.append(label2)
        
        self.records.append(draw1)

        self.records.append(drawUI)
        self.number=1
        self.numberCounter=0;
        


    def getCurrentRecord(self):
        return self.records[self.current]
    
    def changeState(self,numbers):
        if self.records[self.current].UI=='draw1':
            if self.numberCounter<self.number:
                nextNumber=str(randint(1, 9))
                while( nextNumber in numbers):
                    nextNumber=str(randint(1, 9))
        
                self.records[self.current].number=nextNumber 
                self.numberCounter=self.numberCounter+1
                return
            else:
                self.numberCounter=0
        if (self.current< (len(self.records)-1)):
            self.current=self.current+1

    def addChangeState(self,wrong,wrongCount,numbers):

        nextNumber=str(randint(1, 9))
        while( nextNumber in numbers):
            nextNumber=str(randint(1, 9))
        
        label2=stateRecord(60,'Σωστά','',str(randint(1, 9)))
        label3=stateRecord(30,'Ξεκινάμε','',str(randint(1, 9)))
    
        if (wrong):
            label2=stateRecord(20,'Λάθος','',str(randint(1, 9)))
        elif(self.changeRecord):
            self.number=self.number+1
        self.changeRecord=not self.changeRecord
            
        self.numberCounter=0;
    
        t2=stateRecord(8+2*wrongCount,'','draw1',nextNumber)
        t1=stateRecord(100,'','drawUI')
        # self.records.append(t0)
        self.records.append(label2)
        self.records.append(label3)
        self.records.append(t2)
        self.records.append(t1)
        self.current=self.current+1