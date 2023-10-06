class row():


    def __init__(self,number,currentNumber,correct,timer):
        self.number=''
        self.numberAnswers=''
        self.time=0
        self.number=number
        self.currentNumber= currentNumber
        self.correct=correct
        self.timePrint=timer
        self.correctFlag=correct
    
    def print(self,counter):

        print(str(counter)+' Row: Timer '+str(self.timePrint)+' lenth '+str(self.number)+ ' ids '+str(self.currentNumber))


    def getData(self):
        data=[str(self.timePrint),str(self.number),str(self.currentNumber)]  
        return data
    
    def getHeader(self):
        return [' Χρόνος ','Αριθμός ',' Απάντηση']