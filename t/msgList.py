class msg:

    INSTRUNCTIONS="Corsi memory tasks\n	Θα εμφανιστούν στην οθόνη εννέα μπλοκ \n 'Επειτα θα φωτιστεί μια ακολουθία μπλοκ,\n	Έπειτα θα πρέπει να αγγίξει τα μπλοκ που  με την ίδια σειρά.\nΠάτα το s ή το space  για να ξεκινήσουμε!"

    INSTRUNCTIONS2="Corsi memory tasks\nAγγίξε τα μπλοκ που  με την ίδια σειρά που εμφανίστηκαν."


    WRONG="Corsi memory tasks\nΛάθος.\n Tώρα τα κουτάκια θα αλλάζουν χρώμα για περισσότερη ώρα για να σε βοηθήσω."

    CORRECT="Corsi memory tasks\nΣωστά"

    FINISHED="Corsi memory tasks\nΤέλος"

    TIMEOUT="Corsi memory tasks\nΟ χρόνος έληξε!"
    
    def countDown(self,level,countdown):
       if (int(countdown)<1):
           return 'Corsi memory tasks\n'
       return 'Corsi memory tasks\nΕίσαι στο επίπεδο '+str(level)+'!!!\n\n\n Ξεκινάμε σε  '+str(countdown)
    
    def finishedMsg(self,time,maxC):
        return 'Αποτελέσματα \n Χρόνος: '+ str(time)+ ' μήκος μέγιστης αλυσίδα '+ str(maxC)
    