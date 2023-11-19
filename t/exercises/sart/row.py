from utilities.stats import stats
class row():


    def __init__(self):
        self.greenGo='green';
        self.time=0
        self.correct=False;
        self.timeout=False;
        self.stats=stats()
        self.stats.startTimer()
        self.pressed=False

    def stopTimer(self):
        self.stats.stopTimer()
        self.time=self.stats.timePrint()
        if self.greenGo=='green' and self.pressed:
            self.correct=True
            self.correctGR='Σωστά'
        else:
            self.correct=False
            self.correctGR='Λάθος'
    
    def print(self):

        print('Row: Timer '+str(self.time)+' greenGo '+str(self.greenGo)+ ' correct '+str(self.correct)+' timeout '+ str(self.timeout))

    def getData(self):
        color='Ξεκίνα'
        if (self.greenGo!='green'):
            color='Στοπ'
        correctGR='Σωστά'
        if(not self.correct):
            correctGR='Λάθος'
        data=[str(self.time),str(color),str(correctGR)]  
        return data
    
    def getHeader(self):
        return [' Χρόνος απάντησεις ','Χρώμα ',' Απάντησεs']