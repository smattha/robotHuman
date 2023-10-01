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

    def correctAnswer(self):
        if (self.color==self.text and self.pressed)or (self.color!=self.text and not self.pressed):
            return True;
        else :
            return False;
    def print(self):

        print('Row: Timer '+str(self.time)+' text '+str(self.text)+ ' color background '+str(self.color) + ' correct '+str(self.correctAnswer()) )
