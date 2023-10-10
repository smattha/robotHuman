class msg:

    INSTRUNCTIONS="<b><h1>Corsi memory tasks<h1></b> <br><br> \
    Θα εμφανιστούν στην οθόνη εννέα τετραγωνάκια. <br>\
    Έπειτα θα φωτιστεί μια ακολουθία από τετραγωνάκια,<br>\
    Στο τέλος θα πρέπει να πατήσεις τα τετραγωνάκια με τη ίδια σειρά.<br><br>\
    Πάτα το space  για να ξεκινήσουμε!<br><br><br>\
    Αν θέλεις να τερματίσεις το παιχνίδι πάτα το ESC"

    INSTRUNCTIONS2="<b>Corsi memory tasks</b><br>Aγγίξε τα μπλοκ που  με την ίδια σειρά που εμφανίστηκαν."


    WRONG="<b>Corsi memory tasks</b><br><br>\
    Λάθος.<br><br>\
    Tώρα τα τετραγωνάκια θα αλλάζουν χρώμα για περισσότερη ώρα για να σε βοηθήσω."

    CORRECT="<b>Corsi memory tasks</b><br><br>\
    Σωστά"

    FINISHED="<b>Corsi memory tasks</b><br><br>\
    Τέλος"

    TIMEOUT="<br>Corsi memory tasks</b><br><br>\
    Ο χρόνος έληξε!"
    
    def countDown(self,level,countdown):
       if (int(countdown)<1):
           return '<b>Corsi memory tasks</b><br>'
       return '<b>Corsi memory tasks</b><br><br>Είσαι στο επίπεδο '+str(level)+'.<br><br><br> Ξεκινάμε σε  '+str(countdown)
    
    def finishedMsg(self,time,maxC):
        return 'Αποτελέσματα <br><br>\
        Μέσος χρόνος ανά αλυσίδα: '+ str(time)+ \
        ' Μήκος μέγιστης αλυσίδα '+ str(maxC)+\
        '<br><br>Πάτα το space  για να ξεκινήσουμε πάλι!"'
    
    