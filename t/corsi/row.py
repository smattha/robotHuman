class row():

    def __init__(self):
        self.currentCorsi=3;
        self.ids=[]
        self.idsAnswer=[]
        self.timer=6
        
        self.timer1sec=1000
        self.first=True
        self.time2Answer=0
        self.counterPause=3
    
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
        print(str(counter)+': Χρόνος απάντησεις '+str(self.time2Answer)+' μήκος '+str(len(self.ids))+ ' σωστό νούμερο '+str(x)+' απαντήση '+str(y))


    def getData(self):
        x=0
        y=0
        for i in self.ids:
            x=x*10+i+1
        
        for j in self.idsAnswer:
            y=y*10+j+1
        data=[str(self.time2Answer),str(len(self.ids)),str(x),str(y)]  
        return data
    
    def getHeader(self):
        return [' Χρόνος',' Μήκος αλυσίδας ',' Σωστή ακολουθία ',' Απαντήση χρήστη ',]
