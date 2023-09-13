class row():

    def __init__(self):
        self.currentCorsi=3;
        self.ids=[]
        self.idsAnswer=[]
        self.timer=300
        
        self.timer1sec=1000
        self.first=True
        self.time2Answer=0
    
    def print(self):
        x=0
        y=0
        for i in self.ids:
            x=x*10+i+1
        
        for j in self.idsAnswer:
            y=y*10+j+1
        print('Row: Timer '+str(self.time2Answer)+' lenth '+str(len(self.ids))+ ' ids '+str(x)+' idsAnswered '+str(y))
