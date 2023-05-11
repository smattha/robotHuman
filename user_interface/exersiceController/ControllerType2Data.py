#!/usr/bin/env python3


from PyQt5.QtCore import  pyqtSlot
from threading import Thread



class ControllerType2Data():
    def __init__(self):
        super().__init__()
        print("Initialize the controller for Excersice 3 ")


    def setVariables3(self):
    
        self._imagesStory=  [
                    ["Ο Γιωργάκης κρύβει την σοκολάτα του στο ντουλάπι της κουζίνας πριν πάει να παίξει έξω", self.path+"/resources/images/ex3/1.png",'1'],
                    ["Όταν ο Γιωργάκης βγαίνει στην αυλή, η γιαγιά του βρίσκει την σοκολάτα και την βάζει στο ψυγείο", self.path+"/resources/images/ex3/2.png",'2']
 
        ]

        self._imagesAnswer=  [
                    ["\nΝτουλάπι\n", self.path+"/resources/images/ex3/3.png",'1'],
                    ["\nΨυγείο\n", self.path+"/resources/images/ex3/4.png",'2']
                    ]
        self._counter=0
        self._exerciseDscr='Στις παρακάτω εικόνες θα δούμε το μικρό Γιωργάκη να κάνει κάποιες σκανταλιές. Αφού ακούσεις προσεκτικά την ιστορία θα μαντέψεις τι θα κάνει ο Γιωργάκης. '
        # self.title_= '3'
        self.title='Ο Γιωργάκης και η σοκολάτα!'
        self.answerEx3='Ο Γιωργάκης γυρνάει στο σπίτι για να φάει με λαχτάρα την σοκολάτα. Που θα ψάξει για την σοκολάτα του;'
        self.results=['Ντουλάπι','Φίλη']

    def setVariables4(self):
        
        self._imagesStory=  [
                    ["Η Μαρία είναι ένα μικρό κοριτσάκι 3 ετών'", self.path+"/resources/images/ex4/1.png",'1'],
                    ["Το κουδούνι χτυπά και η μαμά της Μαρίας ανοίγει την πόρτα'", self.path+"/resources/images/ex4/2.png",'2'],
                    ["Μια φίλη της μαμάς της Μαρίας ήρθε επίσκεψη", self.path+"/resources/images/ex4/3.png",'3'],
                    ["Η μαμά της Μαρίας λέει: «Καλημέρα!", self.path+"/resources/images/ex4/4.png",'3'],
                    ["νομίζω ότι δεν έχω γνωρίσει το γιο σου. Πως τον λένε;'", self.path+"/resources/images/ex4/5.png",'4']
        ]

        self._imagesAnswer=  [
                    ["\nMαρία\n", self.path+"/resources/images/ex4/6.png",'1'],
                    ["\nΜαμά\n", self.path+"/resources/images/ex4/7.png",'2'],
                    ["\nΦίλη\n", self.path+"/resources/images/ex4/8.png",'3']
                    ]
        self._counter=0
        self._exerciseDscr=' Τώρα θα σου πω κάποιες ιστορίες. Άκουσε προσεκτικά τις ιστορίες γιατί σε κάποιες από αυτές κάποιος λέει κάτι που μπορεί να στεναχωρήσει ή να θυμώσει τον ήρωα.'
        self.title= 'Η Μαρία και η μαμά της'
        self.answerEx3="Άκουσες κάποιον να λέει κάτι που μπορεί να στεναχωρήσει ή να θυμώσει κάποιον από τους ήρωες της ιστορίας;"
        self.results=['Mαρία','Μαμά','Φίλη']


    def setVariablesB3(self):
        
        self._imagesStory=  [
                   ["Κατά τη διάρκεια του πολέμου, ο κόκκινος στρατός έπιασε έναν στρατιώτη μέλος του μπλε στρατού", self.path+"/resources/images/exB3/1.png",'1'],
                   ["Ήθελαν να τους πει πού βρίσκονται τα τανκς του στρατού του.\n Τα τανκς μπορεί να είναι είτε στη θάλασσα, είτε στο βουνό.\n ", self.path+"/resources/images/exB3/2.png",'2'],
                   ["Ο φυλακισμένος στρατιώτης είναι πολύ γενναίος και έξυπνος και θέλει να τους ξεγελάσει.\n Tα τανκς είναι στην πραγματικότητα στα βουνά.\n ", self.path + "/resources/images/exB3/2.png", '3'],
        ]

        self.answerEx3="Οι αντίπαλοι στρατιώτες τον ρωτάνε πού είναι τα τανκς; Τι θα απαντήσει ο μπλε στρατιώτης "

        self._imagesAnswer=  [
                    ["\nΒουνό\n", self.path+"/resources/images/exB3/3.png",'1'],
                    ["\nΘάλασσα\n", self.path+"/resources/images/exB3/4.png",'2']
                    ]
        self._counter=0
        self._exerciseDscr='Στις παρακάτω εικόνες θα δούμε την ιστορία ενός μικρού στρατιώτη. Αφού ακούσεις προσεκτικά την ιστορία θα χρειαστεί να απαντήσεις σωστά στην ερώτηση που θα σου κάνω.'
        self.title= 'Ο μικρός στρατιώτης!'
        self.results=['Βουνό','Θάλασσα']

    def setVariablesB4(self):
        
        self._imagesStory=  [
                    ["Η Σοφία είναι μαθήτρια της Γ Δημοτικού", self.path+"/resources/images/exB4/1.png",'1'],
                    ["Η Σοφία είναι πολύ χαρούμενη για τη νέα κασετίνα που της αγόρασε η μαμά της", self.path+"/resources/images/exB4/2.png",'2'],
                    ["Το κουδούνι χτυπά και η φίλης της Σοφίας μπαίνει στην τάξη", self.path+"/resources/images/exB4/3.png",'2'],
                    ["Τι απαίσια κασετίνα.. Ελπίζω σύντομα να πάρεις καινούρια»", self.path+"/resources/images/exB4/3.png",'2']
 
        ]

        self.answerEx3="Άκουσες κάποιον να λέει κάτι που μπορεί να στεναχωρήσει ή να θυμώσει κάποιον από τους ήρωες της ιστορίας;"

        self._imagesAnswer=  [
                    ["\nΣοφία\n", self.path+"/resources/images/exB4/5.png",'1'],
                    ["\nΦίλη\n", self.path+"/resources/images/exB4/6.png",'2']
                    ]
        self._counter=0
        self._exerciseDscr='Τώρα θα σου πω κάποιες ιστορίες. Άκουσε προσεκτικά τις ιστορίες γιατί σε κάποιες από αυτές κάποιος λέει κάτι που μπορεί να στεναχωρήσει ή να θυμώσει τον ήρωα'
        self.title= 'Η μικρή Σοφία!'

        self.results=['Σοφία','Φίλη']