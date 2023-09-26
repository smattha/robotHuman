class msg:

    INSTRUNCTIONS="Ξεκινάμε!!!!!!\n	Θα εμφανιστούν στην οθόνη εννέα μπλοκ \n 'Επειτα θα φωτιστεί μια ακολουθία μπλοκ,\n	Έπειτα θα πρέπει να αγγίξει τα μπλοκ που  με την ίδια σειρά.\nΠάτα το s ή το space  για να ξεκινήσουμε!"

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
    