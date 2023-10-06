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

    def restart(self):

        self.firstStep()        
        # self.newLoop=True;
        # self.current=0;
        # self.changeRecord=False
        # self.records=[]
        
        # recordslen=len( self.records)
        # drawUI=stateRecord(100,'','drawUI')
        # label2=stateRecord(-10,'Ξεκινάμε από την αρχή\n\nΠάτα το s ή το space όταν είσαι έτοιμος.?','',str(randint(1, 9)))
        # draw1=stateRecord(8,'','draw1',str(randint(1, 9)))
        
        # label1=stateRecord(-10,'Digit span - verbal working memory\n\n\n'+\
        #     'Θα παρουσιαστεί μια ακολουθία ψηφίων.\n\
        #         Μετά θα πρέπει να επαναλάβεις την ακολουθία. Αφού επαναλάβεις την ακολουθία θα παρουσιάστει μια μεγαλύτερη ακολουθία.\n'+
        #         ' Αυτό συνεχίζεται μέχρι το άτομο να μην μπορεί πλέον να επαναλάβει την ακολουθία. \n\nΠάτα το s ή το space για να ξεκινήσουμε.','',str(randint(1, 9)))

        # # self.records.append(label1)
        # self.records.append(label2)
        
        # self.records.append(draw1)

        # self.records.append(drawUI)
        # self.number=1
        # self.numberCounter=0;
        # self.current=recordslen
        
    def firstStep(self):

        self.newLoop=True;
        self.current=0;
        self.changeRecord=False
        self.records=[]
        drawUI=stateRecord(100,'','drawUI')
        label2=stateRecord(20,'Ξεκινάμε','',str(randint(1, 9)))
        draw1=stateRecord(8,'','draw1',str(randint(1, 9)))
        
        label1=stateRecord(-10,'<b>Digit span - verbal working memory<b><br><br>'+\
            'Θα παρουσιαστεί μια ακολουθία ψηφίων.<br>\
                Μετά θα πρέπει να επαναλάβεις την ακολουθία.<br> Αφού επαναλάβεις την ακολουθία θα παρουσιάστει μια μεγαλύτερη ακολουθία.\n'+
                '<br>Αυτό συνεχίζεται μέχρι να μην μπορεί πλέον να επαναλάβει την ακολουθία και να κάνεις δυο διαδοχικά λάθη. <br>\
                Πάτα το space για να ξεκινήσουμε.<br> \
                    Αν θέλεις να τερματίσεις το παιχνίδι πάτα το ESC','',str(randint(1, 9)))
                    

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
        # label3=stateRecord(30,'Ξεκινάμε','',str(randint(1, 9)))
    
        if (wrong):
            label2=stateRecord(60,'Λάθος','',str(randint(1, 9)))
        elif(self.changeRecord):
            self.number=self.number+1
        self.changeRecord=not self.changeRecord
            
        self.numberCounter=0;
    
        t2=stateRecord(8+2*wrongCount,'','draw1',nextNumber)
        t1=stateRecord(100,'','drawUI')
        # self.records.append(t0)
        self.records.append(label2)
        # self.records.append(label3)
        self.records.append(t2)
        self.records.append(t1)
        self.current=self.current+1