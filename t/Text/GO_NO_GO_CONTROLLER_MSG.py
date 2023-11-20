class GO_NO_GO_CONTROLLER_MSG:


    WRONG_ANSWER='<h1>Λάθος απάντηση</h1>'

    DESCRIPTION='<h1>Go/No-go task</h1> <br>\
                                                    Σε αυτό το παιχνίδι εμφανίζονται διαδοχικά δυο εικόνες.<br> \
                Πάτα το space όταν εμφανίζετε η εικόνα αριστερά.<br> \
                Μη κάνεις τίποτα όταν το εμφανίζετε η εικόνα δεξιά.\
                                                        Πάτα το space  για να ξεκινήσουμε!<br>\
                    Αν θέλεις να τερματίσεις το παιχνίδι πάτα το ESC'


    def result(self, time, correctCounter,falseCounter):
        return '<h1> Τέλος </h1>\
                Απάντησες σωστά σε '+str(correctCounter)+' σε συνολικά '+str(correctCounter+falseCounter)+\
                '.<br> Mέσος χρόνος ανά απάντηση '+str(time)+'<br>\
                    Πάτα το space  για να ξεκινήσουμε από την αρχή!'