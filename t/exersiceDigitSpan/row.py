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
