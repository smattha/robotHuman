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
        self.current=0;

        self.records=[]

        drawUI=stateRecord(100,'','drawUI')
        draw1=stateRecord(20,'','draw1',str(randint(1, 9)))
        label=stateRecord(-10,'Digit span - verbal working memory','',str(randint(1, 9)))
        label1=stateRecord(100,'Παρουσιάζεται μια ακολουθία δύο ψηφίων.\nΤο άτομο πρέπει να επαναλάβει την ακολουθία. Εάν το άτομο μπορεί να επαναλάβει την ακολουθία, παρουσιάζεται μια μεγαλύτερη ακολουθία.\n Αυτό συνεχίζεται μέχρι το άτομο να μην μπορεί πλέον να επαναλάβει την ακολουθία. ','',str(randint(1, 9)))

        self.records.append(label)
        self.records.append(label1)

        self.records.append(draw1)
        self.records.append(drawUI)
        self.number=2
        self.numberCounter=1;
        


    def getCurrentRecord(self):
        return self.records[self.current]
    
    def changeState(self):
        if self.records[self.current].UI=='draw1':
            if self.numberCounter<self.number:
                self.records[self.current].number=str( randint(1, 9) )
                self.numberCounter=self.numberCounter+1
                return
            else:
                self.numberCounter=0
        if (self.current< (len(self.records)-1)):
            self.current=self.current+1

    def addChangeState(self,wrong,wrongCount):
        if (wrong==False):
            print('Addd')
            self.number=self.number+1
        self.numberCounter=0;
        t2=stateRecord(10*(wrongCount+1),'','draw1',str(randint(1, 9)))
        t1=stateRecord(100,'','drawUI')
        # self.records.append(t0)
        self.records.append(t2)
        self.records.append(t1)
        self.current=self.current+1