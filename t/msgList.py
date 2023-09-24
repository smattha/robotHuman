class msg:

    INSTRUNCTIONS="Corsi memory tasks\n\n\n\n\n\n\n\n\
    Θα εμφανιστούν στην οθόνη εννέα τετραγωνάκια. \n\
    Έπειτα θα φωτιστεί μια ακολουθία από τετραγωνάκια,\n\
    Στο τέλος θα πρέπει να πατήσεις τα τετραγωνάκια με τη ίδια σειρά.\n\
    Πάτα το s ή το space  για να ξεκινήσουμε!"

    INSTRUNCTIONS2="Corsi memory tasks\nAγγίξε τα μπλοκ που  με την ίδια σειρά που εμφανίστηκαν."


    WRONG="Corsi memory tasks\n\n\
    Λάθος.\n\n\
    Tώρα τα τετραγωνάκια θα αλλάζουν χρώμα για περισσότερη ώρα για να σε βοηθήσω."

    CORRECT="Corsi memory tasks\n\n\
    Σωστά"

    FINISHED="Corsi memory tasks\n\n\
    Τέλος"

    TIMEOUT="Corsi memory tasks\n\n\
    Ο χρόνος έληξε!"
    
    def countDown(self,level,countdown):
       if (int(countdown)<1):
           return 'Corsi memory tasks\n'
       return 'Corsi memory tasks\nΕίσαι στο επίπεδο '+str(level)+'.\n\n\n Ξεκινάμε σε  '+str(countdown)
    
    def finishedMsg(self,time,maxC):
        return 'Αποτελέσματα \n\n\
        Μέσος χρόνος ανά αλυσίδα: '+ str(time)+ \
        ' Μήκος μέγιστης αλυσίδα '+ str(maxC)+\
        '\n\nΠάτα το s ή το space  για να ξεκινήσουμε πάλι!"'
    
    