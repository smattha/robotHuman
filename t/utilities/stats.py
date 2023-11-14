import time
class stats():
    def __init__(self):
        self.level=3
        self.time=300

        #2
        self.number=''
        self.wrong=0
        self.currentNumber=''

    def startTimer(self):
        self.tick=time.time()
    
    def stopTimer(self):
        self.tock=time.time()
        return round(self.timePrint(),2)

    def timePrint(self):
        print( self.tock-self.tick)
        return round(self.tock-self.tick,2)