class row():

    def __init__(self):
        self.currentCorsi=3;
        self.ids=[]
        self.idsAnswer=[]
        self.timer=300
        
        self.timer1sec=1000
        self.first=True
        self.time2Answer=0
    
    def getLenght(self):
        if (self.ids==self.idsAnswer):
            return len(self.ids)
        return 0
        
    def print(self,counter):
        x=0
        y=0
        for i in self.ids:
            x=x*10+i+1
        
        for j in self.idsAnswer:
            y=y*10+j+1
        print(str(counter)+': Χρόνος απάντησεις '+str(self.time2Answer)+' μήκος αλυσίδας '+str(len(self.ids))+ ' σωστή ακολουθεία '+str(x)+' απαντήσεις '+str(y))
