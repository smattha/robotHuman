class row():

    def __init__(self,number,currentNumber,correct,timePrint):

        self.number=number
        self.answer=currentNumber
        self.correrctFlag=correct
        self.time=timePrint
    
        
    def print(self,counter):

        print(str(counter)+': Αριθμός '+str(self.number)+' απάντηση '+self.answer+ ' σωστά  '+str(self.correrctFlag)+' χρόνος '+str(self.time))
