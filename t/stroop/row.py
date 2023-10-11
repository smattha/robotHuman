from goNoGo.stats import stats
class row():


    def __init__(self,text,color):
        self.text=text
        self.color=color       
        self.stats=stats()
        self.stats.startTimer()
        self.pressed=False;

    def stopTimer(self,pressed):
        self.pressed=pressed
        self.stats.stopTimer()
        self.time=self.stats.timePrint()



    def correctAnswer(self):
        if (self.color==self.text and self.pressed)or (self.color!=self.text and not self.pressed):
            return True;
        else :
            return False;
    def print(self):

        print('Row: Timer '+str(self.time)+' text '+str(self.text)+ ' color background '+str(self.color) + ' correct '+str(self.correctAnswer()) )


    def getData(self):
        self.textGR=''
        if (self.text=='green'):
            self.textGR='Πράσινο'
        elif (self.text=='blue'):
            self.textGR='Μπλε'
        elif (self.text=='red'):
            self.textGR='Κόκκινο'
        elif (self.text=='yellow'):
            self.textGR='Κίτρινο'   

        self.colorGR=''
        if (self.color=='green'):
            self.colorGR='Πράσινο'
        elif (self.color=='blue'):
            self.colorGR='Μπλε'
        elif (self.color=='red'):
            self.colorGR='Κόκκινο'
        elif (self.color=='yellow'):
            self.colorGR='Κίτρινο'           

        answerGR='Σωστά'
        if(not self.correctAnswer()):
            answerGR='Λάθος'

        data=[str(self.time),str((self.textGR)),str(self.colorGR), str(answerGR)]  
        return data
    
    def getHeader(self):
        return [' Χρόνος','Λέξη ','Χρώμα','Απάντησε']