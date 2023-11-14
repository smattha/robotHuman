class DIGITAL_SPAN_MSG:

    START_MSG='Ξεκινάμε'

    INSTRUNCTIONS='<h1>Digit span - verbal working memory</h1><br><br>\
            Θα παρουσιαστεί μια ακολουθία ψηφίων.<br><br>\
                Μετά θα πρέπει να επαναλάβεις την ακολουθία.<br><br> Αφού επαναλάβεις την ακολουθία θα παρουσιάστει μια μεγαλύτερη ακολουθία.<br>\
                <br>Αυτό συνεχίζεται μέχρι  να κάνεις δυο διαδοχικά λάθη. <br><br><br>\
                Πάτα το space για να ξεκινήσουμε.<br> \
                    Αν θέλεις να τερματίσεις το παιχνίδι πάτα το ESC.<br>\
                        Αν θέλεις να τερματίσεις την εφαρμογή πάτα το τ. '

    INSTRUNCTIONS2="Aγγίξε τα μπλοκ που  με την ίδια σειρά που εμφανίστηκαν."

    ZERO_CORRECT_DATA="<h1>Tέλος</h1> <br> Digital span 0"
    WRONG="Λάθος."

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
    