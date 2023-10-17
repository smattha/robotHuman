class msg:

    INSTRUNCTIONS="<h1>SART</h1> <br>\
        Θα εμφανιζόνται εικόνες στην οθόνη.<br> <br> \
        Θέλω να πατάς το space για κάθε εικόνα. <br>\
            <b><U><I>Eκτός</I></U></b> αν η εικόνα είναι ένα μήλο. <br><br><br>\
            Πάτα το s ή το space  για να ξεκινήσουμε!<br>\
            Πάτα το ESC για να τερματίσουμε το παιχνίδι."

    INSTRUNCTIONS2="Aγγίξε τα μπλοκ που  με την ίδια σειρά που εμφανίστηκαν."

    
    WRONG="Λάθος.\n Tώρα τα κουτάκια θα αλλάζουν χρώμα για περισσότερη ώρα για να σε βοηθήσω."

    CORRECT="Σωστά"

    FINISHED="Τέλος"

    TIMEOUT="Ο χρόνος έληξε!"

    CLEAR="Καθαρισμός"

    CONTINUE="Συνέχεια"
    
    def countDown(self,level,countdown):
       if (int(countdown)<1):
           return '    '
       return 'Είσαι στο επίπεδο '+str(level)+'!!!\n\n\n Ξεκινάμε σε  '+str(countdown)
    
    def finishedMsg(self,time,maxC):
        return 'Αποτελέσματα \n Χρόνος: '+ str(time)+ ' μήκος μέγιστης αλυσίδα '+ str(maxC)
    