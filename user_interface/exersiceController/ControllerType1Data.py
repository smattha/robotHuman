#!/usr/bin/env python3

class ControllerType1Data():
    def __init__(self):
        super().__init__()



    def setVariable1(self):
        self._exersiceDsr='Ένα λιοντάρι ζυγίζει το ίδιο με 2 σκυλάκια. Ένα σκυλάκι ζυγίζει το ίδιο με 2 παπάκια. Πόσα παπάκια ζυγίζουν το ίδιο με το λιοντάρι;'

        self._exersiceTitleDsr='Ένα λιοντάρι ζυγίζει το ίδιο με 2 σκυλάκια. Ένα σκυλάκι ζυγίζει το ίδιο με 2 παπάκια.'
        self._answerDsr='Πόσα παπάκια ζυγίζουν το ίδιο με το λιοντάρι;'

        self._answerDscr='1, 2, 3, 4 ή 5;'
        self._title="Το λιοντάρι και τα παπάκια!"
        self._imagePath=self.path+"/resources/images/ex1/mainImage.png"

        self._imageAnswer1=self.path+'/resources/images/ex1/answer1.png'
        self._imageAnswer2=self.path+'/resources/images/ex1/answer2.png'
        self._imageAnswer3=self.path+'/resources/images/ex1/answer3.png'
        self._imageAnswer4=self.path+'/resources/images/ex1/answer4.png'
        self._imageAnswer5=self.path+'/resources/images/ex1/answer5.png'

        self._answerEx1Descr='\nΈνα παπάκι\n'
        self._answerEx2Descr='\nΔύο παπάκια\n'
        self._answerEx3Descr='\nΤρία παπάκια\n'
        self._answerEx4Descr='\nΤεσσερά Παπάκια\n'
        self._answerEx5Descr='\nΠέντε Παπάκια\n'

    def setVariable2(self):
        self._exersiceDsr='Τώρα θα παίξουμε ένα παιχνίδι με γρίφους.\n Με ποιο αντικείμενο μοιάζει η κεντρική εικόνα;'

        self._exersiceTitleDsr='Τώρα θα παίξουμε ένα παιχνίδι με γρίφους.\n Με ποιο αντικείμενο μοιάζει η κεντρική εικόνα;'
        self._answerDsr=' Διάλεξε την απάντηση που σου φαίνεται σωστή και προχώρα στον επόμενο γρίφο;'

        self._answerDscr='Α   ,Β  , Γ  , Δ  , Ε  '
        self._title="Άσκηση προσοχής"
        self._imagePath=self.path+"/resources/images/ex2/mainImage.png"
        self._imageAnswer1=self.path+'/resources/images/ex2/answer1.png'
        self._imageAnswer2=self.path+'/resources/images/ex2/answer2.png'
        self._imageAnswer3=self.path+'/resources/images/ex2/answer3.png'
        self._imageAnswer4=self.path+'/resources/images/ex2/answer4.png'
        self._imageAnswer5=self.path+'/resources/images/ex2/answer5.png'

        self._answerEx1Descr='\nA\n'
        self._answerEx2Descr='\nB\n'
        self._answerEx3Descr='\nΓ\n'
        self._answerEx4Descr='\nΔ\n'
        self._answerEx5Descr='\nΕ\n'



    def setVariableB1(self):
        self._exersiceDsr='Η μαμά καγκουρό ζυγίζει με το μωρό της 60 κιλά. Η μαμά ζυγίζει μόνη της 52 κιλά. Πόσα κιλά ζυγίζει το μωρό της;'
        self._exersiceTitleDsr='Η μαμά καγκουρό ζυγίζει με το μωρό της 60 κιλά. Η μαμά ζυγίζει μόνη της 52 κιλά. .'
        self._answerDsr=' Πόσα κιλά ζυγίζει το μωρό της;'

        self._answerDscr='4, 8, 30, 56 ή 112'
        self._title="Άσκηση προσοχής"
        self._imagePath=self.path+"/resources/images/exB1/1.png"
        self._imageAnswerFlag=1


        self._answerEx1Descr='\n4\n'
        self._answerEx2Descr='\n8\n'
        self._answerEx3Descr='\n30\n'
        self._answerEx4Descr='\n56\n'
        self._answerEx5Descr='\n112\n'
        #self._rosInterface.talker('Ένα από τα αντικείμενα στο κάτω μέρος της οθόνης είναι το ίδιο με το αντικείμενο που φαίνεται στο πάνω μέρος της οθόνης. Ποιο;')



    def setVariableB2(self):
        self._exersiceDsr='Ο Μάξιμος έκοψε ένα φύλλο χαρτί σε 2 κομμάτια. Το ένα κομμάτι εμφανίζεται στο πάνω μέρος της οθόνης. Ποιο από τα κομμάτια στο κάτω μέρος της οθόνης είναι το άλλο;'
        self._answerDscr='Α ,  Β , Γ , Δ , Ε '
        self._title="Άσκηση προσοχής"
        self._imagePath=self.path+"/resources/images/exB2/mainImage.png"

        self._exersiceTitleDsr='Ο Μάξιμος έκοψε ένα φύλλο χαρτί σε 2 κομμάτια.Το ένα κομμάτι εμφανίζεται στο πάνω μέρος της οθόνης.'
        self._answerDsr=' Ποιο από τα κομμάτια στο κάτω μέρος της οθόνης είναι το άλλο;'


        self._imageAnswer1=self.path+'/resources/images/exB2/answer1.png'
        self._imageAnswer2=self.path+'/resources/images/exB2/answer2.png'
        self._imageAnswer3=self.path+'/resources/images/exB2/answer3.png'
        self._imageAnswer4=self.path+'/resources/images/exB2/answer4.png'
        self._imageAnswer5=self.path+'/resources/images/exB2/answer5.png'

        self._answerEx1Descr='\nA\n'
        self._answerEx2Descr='\nB\n'
        self._answerEx3Descr='\nΓ\n'
        self._answerEx4Descr='\nΔ\n'
        self._answerEx5Descr='\nΕ\n'









