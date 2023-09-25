class row():


    def __init__(self,number,currentNumber,correct,timer):
        self.number=''
        self.numberAnswers=''
        self.time=0
        self.number=number
        self.currentNumber= currentNumber
        self.correct=correct
        self.timePrint=timer
    
    def print(self):

        print('Row: Timer '+str(self.timer)+' lenth '+str(self.number)+ ' ids '+str(self.currentNumber))
