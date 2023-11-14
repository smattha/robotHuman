from random import randint
from Text.DIGITAL_SPAN_MSG import DIGITAL_SPAN_MSG
class stateRecord:
    def __init__(self, pauseCicles, label, ui,number='0',color='blue'):
        self.pause=4
        self.pause=pauseCicles
        self.label=label
        self.UI=ui
        self.number=number
        self.color=color

    
class state():
    def __init__(self):
        self.MSG= DIGITAL_SPAN_MSG()
        self.firstStep()


    def restart(self):

        self.firstStep()   
        
    def firstStep(self):

        self.newLoop=True;
        self.current=0;
        self.changeRecord=False
        self.records=[]
        drawUI=stateRecord(100,'','drawUI')
        label2=stateRecord(20,self.MSG.START_MSG,'',str(randint(1, 9)),'red')
        draw1=stateRecord(8,'','draw1',str(randint(1, 9)))

        back=stateRecord(0,'img/sky2.jpg','back',str(randint(1, 9)))

        back1=stateRecord(0,'img/back.png','back',str(randint(1, 9)))
        
        backhide=stateRecord(0,'','backhide',str(randint(1, 9)))
        
        label1=stateRecord(-10,self.MSG.INSTRUNCTIONS,'',0)
                    
        self.records.append(backhide)
        self.records.append(label1)
  
        self.records.append(back1)
        self.records.append(label2)
        
        self.records.append(draw1)
        
        self.records.append(back)
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
        
        label2=stateRecord(60,self.MSG.CORRECT,'',1,'red')
    
        if (wrong):
            label2=stateRecord(60,self.MSG.WRONG,'',1,'red')
            back=stateRecord(0,'img/rain.jpg','back',str(randint(1, 9)))
            self.records.append(back)
        elif(self.changeRecord):
            self.number=self.number+1
        self.changeRecord=not self.changeRecord
            
        self.numberCounter=0;
    
        t2=stateRecord(8+2*wrongCount,'','draw1',nextNumber)
        t1=stateRecord(100,'','drawUI')

        self.records.append(label2)
        if (wrong):
            back=stateRecord(0,'img/sky2.jpg','back',str(randint(1, 9)))
            self.records.append(back)
        self.records.append(t2)
        self.records.append(t1)
        self.current=self.current+1