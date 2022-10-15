#!/usr/bin/env python3


from PyQt5.QtCore import  pyqtSlot
from threading import Thread

from exersiceController.MainController import MainController

class ControllerExersice5Data():
    def __init__(self):
        super().__init__()

    
    def setVariable1(self):
        self._exersiceDsr='Τώρα θα παίξουμε ένα παιχνίδι με γρίφους. Στην οθόνη που είναι δίπλα μου θα εμφανίζονται οι εικόνες των γρίφων. \n Κάτω από την εικόνα θα εμφανίζονται 5 πιθανές απαντήσεις.\n Διάλεξε την απάντηση που σου φαίνεται σωστή και προχώρα στον επόμενο γρίφο'
        self._answerDscr='Κοίτα προσεκτικά την εικόνα και βρες πόσοι άνθρωποι φοράνε καπέλο'
        self._answerDsr='Κοίτα προσεκτικά την εικόνα και βρες πόσοι άνθρωποι φοράνε καπέλο'
        self._title=""
        path=self.model.path
        self._imagePath=path+"/resources/images/ex5/image.png"
        self._exersiceDsr2 = "Κοίτα προσεκτικά την εικόνα και δείξε μου που είναι το λαγουδάκι."
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        print (""+path + " " +self._imagePath)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        self._counter=1
        self._part2="Κοίτα προσεκτικά την εικόνα και δείξε μου που είναι το μικρό σκυλάκι."

        self._imageAnswer1=''
        self._imageAnswer2=''
        self._imageAnswer3=''
        self._imageAnswer4=''
        self._imageAnswer5=''

        self._answerEx1Descr='\n1\n'
        self._answerEx2Descr='\n2\n'
        self._answerEx3Descr='\n3\n'
        self._answerEx4Descr='\n4\n'
        self._answerEx5Descr='\n5\n'

        self._exersiceTitleDsr='Τώρα θα παίξουμε ένα παιχνίδι με γρίφους. \nΣτην οθόνη που είναι δίπλα μου θα εμφανίζονται οι εικόνες των γρίφων. \n Κάτω από την εικόνα θα εμφανίζονται 5 πιθανές απαντήσεις.'

    
    


    
    def setVariable2(self):
        self._exersiceDsr='Άσκηση προσοχής'
        self._exersiceDsr2="Κοίτα προσεκτικά την εικόνα και βρες πόσα είναι τα (γκρι) περιστέρια."
        self._answerDscr='Κοίτα προσεκτικά την εικόνα και βρες πόσα είναι τα (γκρι) περιστέρια.'
        self._answerDsr='Κοίτα προσεκτικά την εικόνα και βρες πόσα είναι τα (γκρι) περιστέρια.'
        self._title="Άσκηση προσοχής"
        self._imagePath=self.path+"/resources/images/exB5/1.jpg"
        self._counter=1
        self._part2="Κοίτα προσεκτικά την εικόνα και δείξε μου που είναι το κάστρο"

        self._imageAnswer1=''
        self._imageAnswer2=''
        self._imageAnswer3=''
        self._imageAnswer4=''
        self._imageAnswer5=''

        self._answerEx1Descr='1'
        self._answerEx2Descr='2'
        self._answerEx3Descr='3'
        self._answerEx4Descr='4'
        self._answerEx5Descr='5'

        self._exersiceTitleDsr='Τώρα θα παίξουμε ένα παιχνίδι με γρίφους. Στην οθόνη που είναι δίπλα μου θα εμφανίζονται οι εικόνες των γρίφων. \n Κάτω από την εικόνα θα εμφανίζονται 5 πιθανές απαντήσεις.'

    


    def setVariableB5(self):
        self._exersiceDsr='Τώρα θα παίξουμε ένα παιχνίδι με γρίφους. Στην οθόνη που είναι δίπλα μου θα εμφανίζονται οι εικόνες των γρίφων.'
        self._answerDscr='Α  1 ,Β  2, Γ  3, Δ  4, Ε  5'
        self._title=""
        self._imagePath=self.path+"/resources/images/exB5/1.jpg"
        self._imagePath2=self.path+"/resources/images/exB5/1.jpg"

        self._imageAnswer1=''
        self._imageAnswer2=''
        self._imageAnswer3=''
        self._imageAnswer4=''
        self._imageAnswer5=''

        self._answerEx1Descr='1'
        self._answerEx2Descr='2'
        self._answerEx3Descr='3'
        self._answerEx4Descr='4'
        self._answerEx5Descr='5'

        self._exersiceTitleDsr='Τώρα θα παίξουμε ένα παιχνίδι με γρίφους. Στην οθόνη που είναι δίπλα μου θα εμφανίζονται οι εικόνες των γρίφων. \n Κάτω από την εικόνα θα εμφανίζονται 5 πιθανές απαντήσεις.'

    

