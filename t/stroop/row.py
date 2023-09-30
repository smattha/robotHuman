from goNoGo.stats import stats
class row():

    def __init__(self,text,color):
        self.text=text
        self.color=color       
        self.stats=stats()
        self.stats.startTimer()
        self.pressed=False;

    def stopTimer(self):
        self.stats.stopTimer()
        self.time=self.stats.timePrint()

    def print(self):

        print('Row: Timer '+str(self.time)+' text '+str(self.text)+ ' color background '+str(self.color))
