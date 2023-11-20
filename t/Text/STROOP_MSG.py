class STROOP_MSG:


    INSTRUNCTIONS="<h1>Stroop</h1> <br> <br>\
                    Στην οθόνη θα εμφανίζονται λέξεις. <br><br>\
                        Πάτα το space όταν το χρώμα της λέξης και το νόημα της είναι το ίδιο.<br><br><br>\
                    Πάτα το space  για να ξεκινήσουμε!<br>\
                    Αν θέλεις να τερματίσεις το παιχνίδι πάτα το ESC"
    
    FINISHED= '<h1>Τέλος</h1>\
                    Πάτα το space  για να ξεκινήσουμε από την αρχή!<br>'
    

    CORRECT='Σωστά'

    WRONG='Λάθος'


    def result(self, time, correctCounter,falseCounter):
        return '<h1> Τέλος </h1>\
                Απάντησες σωστά σε '+str(correctCounter)+' σε συνολικά '+str(correctCounter+falseCounter)+\
                '.<br> Mέσος χρόνος ανά απάντηση '+str(time)+'<br>\
                    Πάτα το space  για να ξεκινήσουμε από την αρχή!'