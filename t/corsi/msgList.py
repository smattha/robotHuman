class msg:

    INSTRUNCTIONS="<b><h1>Corsi memory tasks<h1></b> <br> \
    Θα εμφανιστούν στην οθόνη εννέα τετραγωνάκια. <br>\
    Έπειτα ένα πιθηκάκι θα μετακινείται από τετραγώνακι σε τετραγωνάκι.<br>\
    Στο τέλος θα πρέπει να πατήσεις τα τετραγωνάκια στα οποία εμφανίστηκε, με τη ίδια σειρά .<br><br>\
    Πάτα το space  για να ξεκινήσουμε!<br><br><br>\
    Αν θέλεις να τερματίσεις το παιχνίδι πάτα το ESC<br>\
    Αν θέλεις να τερματίσεις την εφαρμογή πάτα το τ "
    

    INSTRUNCTIONS2="<b><h1>Corsi memory tasks</h1></b>\
        Άγγιξε τα μπλοκ που με την ίδια σειρά που εμφανίστηκε το πιθικάκι σε αυτά."


    WRONG="<b><h1>Corsi memory tasks</h1></b><br><br>\
    Λάθος.<br><br>\
    Για να σε βοηθήσω,τo πιθηκάκι θα μένει περισσοτέρη ώρα σε κάθε πλακάκι. "

    CORRECT="<b><h1>Corsi memory tasks</h1></b><br><br>\
    Σωστά"

    FINISHED="<b><h1>Corsi memory tasks</h1></b><br><br>\
    Τέλος"

    TIMEOUT="<br>Corsi memory tasks</b><br><br>\
    Ο χρόνος έληξε!"
    
    def countDown(self,level,countdown):
       if (int(countdown)<1):
           return '<b><h1>Corsi memory tasks</h1></b><br>'
       return '<b><h1>Corsi memory tasks</h1></b><br><br>Είσαι στο επίπεδο '+str(level)+'.<br><br><br> Ξεκινάμε σε  '+str(countdown)
    
    def finishedMsg(self,time,maxC):
        return '<h1>Αποτελέσματα<h1><br>\
        Μέσος χρόνος ανά αλυσίδα: '+ str(time)+ \
        ' Μήκος μέγιστης αλυσίδα '+ str(maxC)+\
        '<br><br>Πάτα το space  για να ξεκινήσουμε το παιχνίδι από την αρχή!'
    
    