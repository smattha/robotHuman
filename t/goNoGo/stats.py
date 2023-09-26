import time
class stats():
    def __init__(self):
        self.level=2
        self.time=300
        self.number=''
        self.wrong=0
        self.currentNumber=''

    def startTimer(self):
        self.tick=time.time()
    
    def stopTimer(self):
        self.tock=time.time()
        return round(self.timePrint(),2)

    def timePrint(self):
        return round(self.tock-self.tick,2)