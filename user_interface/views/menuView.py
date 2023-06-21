from PyQt5.QtCore import pyqtSlot
from views.ui.menu import Ui_menuWindow
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import ( QMainWindow)
from views.DisplayImage import DisplayImageWidget
from views.page1View import page1View
from views.page2View import page2View
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import tty
import sys
import termios
from threading import Thread
from time import sleep
import random
path_of_image = '/home/stergios/Desktop/a.png'
import time


class MenuView(QMainWindow):
    
    def keyPressEvent(self, event):
        if(self.lock==True):
            return
        print('...........')
        self.tock=time.time()

        print("You pressed"+ event.text()+ " mode "+ self.mode+ " time " +str(self.tock-self.tick))

        
        if (self.mode=='fish'):
            print ("Mode Fish")
            self.correctFish=self.correctFish+1
            self.totalTime=self.totalTime+ self.tock-self.tick
        elif (self.mode=='sharck') :
            print('Else')
            self.errorFish=self.errorFish+1
            self.totalTime=self.totalTime+ self.tock-self.tick
       

    def __init__(self, model, main_controller):
        super().__init__()




        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_menuWindow()
        self._ui.setupUi(self)
        self.counter=0
        self.tick=0
        self.tock=0
        self.mode="idle"
        self.path=self._model.path
        self.lock=True

        #self._dialog.hide()
        self.move(model.poseX,model.poseY)
        self.resize(model.sizeY, model.sizeY)
        self._ui.selectExercise.addItems(self._model.listAvailableExersice)
        # self._ui.comboBox.addItems(self._model.result.listWithNames)
        #self._ui.easy.setPixmap(QtGui.QPixmap(self._model.easyFeedbackImg ))
        #self._ui.normal.setPixmap(QtGui.QPixmap(self._model.normalFeedback))
        #self._ui.hard.setPixmap(QtGui.QPixmap(self._model.difficultFeedback))

        # self._ui.easy.setMaximumSize(QtCore.QSize(480/model.i, 480/model.i))
        # self._ui.easy.setScaledContents(True)

        # self._ui.normal.setMaximumSize(QtCore.QSize(480/model.i, 480/model.i))
        # self._ui.normal.setScaledContents(True)

        # self._ui.hard.setMaximumSize(QtCore.QSize(480/model.i, 480/model.i))
        # self._ui.hard.setScaledContents(True)

        # self._ui.mainImageHome.setMaximumSize(QtCore.QSize(480/model.i, 480/model.i))
        # self._ui.mainImageHome.setScaledContents(True)

        # self._ui.mainImageHome.setPixmap(QtGui.QPixmap(self.path+"/resources/images/mainScreen.jpg"))

        self._ui.stackedWidget.setCurrentIndex(0)


        self._ui.terminateButton.setDisabled(True)
        self._ui.nextExersice.setDisabled(True)




        ################################################################################################
        # # connect widgets to controller
        # self._ui.clearMenu.clicked.connect(lambda: self._main_controller.clearClicked())
        # self._ui.saveMenu.clicked.connect(lambda:  self._main_controller.saveClicked(self._ui.name.text(), self._ui.surname.text(), self._ui.ageTextBox.text()))
        self._ui.selectExersiceButton.clicked.connect( lambda: self._main_controller.setPage(self._ui.selectExercise.currentIndex()) )        

        self._ui.pushButtonMainResults.clicked.connect( lambda: self.setPage(103) )

        self._ui.pushButtonResultsNext.clicked.connect( lambda: self.loadResultsByIDCounter(1) )

        self._ui.pushButtoResultPrevius.clicked.connect( lambda: self.loadResultsByIDCounter(-1) )


        i=0
        self._ui.ex1.clicked.connect( lambda: self._main_controller.setPage(0))        
        self._ui.ex2.clicked.connect( lambda: self._main_controller.setPage(1))
        self._ui.ex3.clicked.connect( lambda: self._main_controller.setPage(2))
        self._ui.ex4.clicked.connect( lambda: self._main_controller.setPage(3))
        self._ui.ex5.clicked.connect( lambda: self._main_controller.setPage(4))
        self._ui.ex6.clicked.connect( lambda: self._main_controller.setPage(5))

        self._ui.ex7.clicked.connect( lambda: self._main_controller.setPage(6))        
        self._ui.ex8.clicked.connect( lambda: self._main_controller.setPage(7))
        self._ui.ex9.clicked.connect( lambda: self._main_controller.setPage(8))
        self._ui.ex10.clicked.connect( lambda: self._main_controller.setPage(9))
        self._ui.ex11.clicked.connect( lambda: self._main_controller.setPage(10))
        self._ui.ex12.clicked.connect( lambda: self._main_controller.setPage(11))

        self._ui.l1.setPixmap(QtGui.QPixmap("/robotApp/resources/mainPage/1"))
        self._ui.l2.setPixmap(QtGui.QPixmap("/robotApp/resources/mainPage/2"))
        self._ui.l3.setPixmap(QtGui.QPixmap("/robotApp/resources/mainPage/3"))
        self._ui.l4.setPixmap(QtGui.QPixmap("/robotApp/resources/mainPage/4"))
        self._ui.l5.setPixmap(QtGui.QPixmap("/robotApp/resources/mainPage/5"))
        self._ui.l6.setPixmap(QtGui.QPixmap("/robotApp/resources/mainPage/6"))
        self._ui.l7.setPixmap(QtGui.QPixmap("/robotApp/resources/mainPage/7"))
        self._ui.l8.setPixmap(QtGui.QPixmap("/robotApp/resources/mainPage/8"))
        self._ui.l9.setPixmap(QtGui.QPixmap("/robotApp/resources/mainPage/9"))
        self._ui.l10.setPixmap(QtGui.QPixmap("/robotApp/resources/mainPage/10"))
        self._ui.l11.setPixmap(QtGui.QPixmap("/robotApp/resources/mainPage/11"))
        self._ui.l12.setPixmap(QtGui.QPixmap("/robotApp/resources/mainPage/12"))




        self._ui.l1.setScaledContents(True)
        self._ui.l2.setScaledContents(True)
        self._ui.l3.setScaledContents(True)
        self._ui.l4.setScaledContents(True)
        self._ui.l5.setScaledContents(True)
        self._ui.l6.setScaledContents(True)
        self._ui.l7.setScaledContents(True)
        self._ui.l8.setScaledContents(True)
        self._ui.l9.setScaledContents(True)
        self._ui.l10.setScaledContents(True)
        self._ui.l11.setScaledContents(True)
        self._ui.l12.setScaledContents(True)

        self._ui.l1.setAlignment(QtCore.Qt.AlignHCenter)       
        self._ui.l2.setAlignment(QtCore.Qt.AlignHCenter)
        self._ui.l3.setAlignment(QtCore.Qt.AlignHCenter)
        self._ui.l4.setAlignment(QtCore.Qt.AlignHCenter)
        self._ui.l5.setAlignment(QtCore.Qt.AlignHCenter)
        self._ui.l6.setAlignment(QtCore.Qt.AlignHCenter)
        self._ui.l7.setAlignment(QtCore.Qt.AlignHCenter)
        self._ui.l8.setAlignment(QtCore.Qt.AlignHCenter)
        self._ui.l9.setAlignment(QtCore.Qt.AlignHCenter)
        self._ui.l10.setAlignment(QtCore.Qt.AlignHCenter)
        self._ui.l11.setAlignment(QtCore.Qt.AlignHCenter)
        self._ui.l12.setAlignment(QtCore.Qt.AlignHCenter)


        self._ui.l1.setAlignment(QtCore.Qt.AlignVCenter)       
        self._ui.l2.setAlignment(QtCore.Qt.AlignVCenter)
        self._ui.l3.setAlignment(QtCore.Qt.AlignVCenter)
        self._ui.l4.setAlignment(QtCore.Qt.AlignVCenter)
        self._ui.l5.setAlignment(QtCore.Qt.AlignVCenter)
        self._ui.l6.setAlignment(QtCore.Qt.AlignVCenter)
        self._ui.l7.setAlignment(QtCore.Qt.AlignVCenter)
        self._ui.l8.setAlignment(QtCore.Qt.AlignVCenter)
        self._ui.l9.setAlignment(QtCore.Qt.AlignVCenter)
        self._ui.l10.setAlignment(QtCore.Qt.AlignVCenter)
        self._ui.l11.setAlignment(QtCore.Qt.AlignVCenter)
        self._ui.l12.setAlignment(QtCore.Qt.AlignVCenter)


        i=1.1
        k=250
        l=220
        self._ui.l1.setMaximumSize(QtCore.QSize(k/i, l/i))
        self._ui.l2.setMaximumSize(QtCore.QSize(k/i, l/i))
        self._ui.l3.setMaximumSize(QtCore.QSize(k/i, l/i))
        self._ui.l4.setMaximumSize(QtCore.QSize(k/i, l/i))
        self._ui.l5.setMaximumSize(QtCore.QSize(k/i, l/i))
        self._ui.l6.setMaximumSize(QtCore.QSize(k/i, l/i))
        self._ui.l7.setMaximumSize(QtCore.QSize(k/i, l/i))
        self._ui.l8.setMaximumSize(QtCore.QSize(k/i, l/i))
        self._ui.l9.setMaximumSize(QtCore.QSize(k/i, l/i))
        self._ui.l10.setMaximumSize(QtCore.QSize(k/i, l/i))
        self._ui.l11.setMaximumSize(QtCore.QSize(k/i, l/i))
        self._ui.l12.setMaximumSize(QtCore.QSize(k/i, l/i))
        #Exersice 1
        self._ui.selectExercise.currentIndexChanged.connect(lambda:  self._main_controller.selectButtonClicked(self._ui.selectExercise.currentIndex()) )        
        self._ui.selectExercise.hide()
        self._ui.selectExersiceButton.hide()
        self._ui.pushButtonMainResults.hide()

        self._ui.go2Home_2.clicked.connect(lambda: self.go2Home1())
        self._ui.nextExersice.clicked.connect(lambda: self._main_controller.move2NextPage())


        self._ui.terminateButton.clicked.connect(lambda: self._main_controller.go2Home1(   ) )
        # self._ui.feedbackEasyButton.clicked.connect(lambda: self._main_controller.feedback('1'))
        # self._ui.feedbackNormalButton.clicked.connect(lambda: self._main_controller.feedback('2'))
        # self._ui.feedbackHardButton.clicked.connect(lambda: self._main_controller.feedback('3'))


        #################################################################################################xml
        # # listen for model event signals
        self._model.changeDscrSingal.connect(self.changeDscrChanged)
        self._model.resetFieldSingal.connect(self.resetField)
        self._model.setPageSignal.connect(self.setPage)
        self._model.changeFeedbackLabel.connect(self.changeFeedbackLabel)
        self._model.showButtons.connect(self.showButtons)

        #Feedback
        self._model.feedbackShowButton.connect(self.feedbackShowButton)

        self._ui.pushButtonHome.clicked.connect( lambda: self.setPage(0) )
        
        self._ui.fishButton.clicked.connect( lambda: self.setPage(105) )
        
        self._ui.startFish.clicked.connect(lambda: self.startFish())
        self._ui.stopFish.clicked.connect(lambda: self.stopFish())

        self.showMaximized()
        msg="Τώρα θα παίξουμε τους ψαράδες!<br />Στην οθόνη θα εμφανίζονται διάφορα ψαράκια.<br />Άλλα είναι κόκκινα, άλλα πρόσινα και άλλα μπλέ.<br />Κάθε φορά που θα βγαίνει ένα ψαράκι, θα πρέπει να πατάς όσο πιο γρήγορα μπορείς το μεγάλο κουμπί (δείχνεις το πλήκτρο space) για να το ψαρεύεις.<br />Πρόσεχε, όμως! Πού και πού θα εμφανίζεται και ένας πεινασμένος καρχαρίας σαν και αυτόν. Όταν βλέπεις τον καρχαρία δεν πρέπει να πατάς το κουμπί γιατί ο καρχαρίας θα φάει όλα τα ψαράκια που έχεις ψαρέψει!!!<br /><br />Πάμε να κάνουμε μια δοκιμή για να δούμε αν το κατάλαβες; <br />Βάλε το δαχτυλάκι πάνω στο κουμπί να είσαι έτοιμος/η<br />(τοποθετείς το χεράκι του στο space). <br />Μόλις εμφανιστεί κάποιο ψαράκι πρέπει να πατήσεις όσο πιο γρήγορα μπορείς! <br />Πρόσεχε τους καρχαρίες!!!!<br />(Πάτα ένα πλήκτρο)"
        self._ui.fish.setText(msg)
        



    @pyqtSlot(str)
    def changeDscrChanged(self, value):
        # print('Set Text!!!!!!!!! ',value)
        self._ui.descriptionTxt.setText(value)


    @pyqtSlot(str)
    def resetField(self, value):
        print('Empty field ',value)
        self._ui.name.setText('')
        self._ui.ageTextBox.setText('')
        self._ui.surname.setText('')

    def go2Home1( self ):
        self._main_controller.go2Home1()
        self.tick=0
        self.timer.stop()

    def startFish(self):
        print('Timer!!')

        self.showedFish=0;
        self.showedSharck=0;
        self.correctFish=0;
        self.errorFish=0;
        self.totalTime=0;
        msg="Τώρα θα παίξουμε τους ψαράδες!<br />Στην οθόνη θα εμφανίζονται διάφορα ψαράκια.<br />Άλλα είναι κόκκινα, άλλα πρόσινα και άλλα μπλέ.<br />Κάθε φορά που θα βγαίνει ένα ψαράκι, θα πρέπει να πατάς όσο πιο γρήγορα μπορείς το μεγάλο κουμπί (δείχνεις το πλήκτρο space) για να το ψαρεύεις.<br />Πρόσεχε, όμως! Πού και πού θα εμφανίζεται και ένας πεινασμένος καρχαρίας σαν και αυτόν. Όταν βλέπεις τον καρχαρία δεν πρέπει να πατάς το κουμπί γιατί ο καρχαρίας θα φάει όλα τα ψαράκια που έχεις ψαρέψει!!!<br /><br />Πάμε να κάνουμε μια δοκιμή για να δούμε αν το κατάλαβες; <br />Βάλε το δαχτυλάκι πάνω στο κουμπί να είσαι έτοιμος/η<br />(τοποθετείς το χεράκι του στο space). <br />Μόλις εμφανιστεί κάποιο ψαράκι πρέπει να πατήσεις όσο πιο γρήγορα μπορείς! <br />Πρόσεχε τους καρχαρίες!!!!<br />(Πάτα ένα πλήκτρο)"
        self._ui.fish.setText(msg)
        self.counterdown=5
        
        self.timerCountdown = QtCore.QTimer(self)
        self.timerCountdown.stop()
        self.timerCountdown.start(1000)
        self.timerCountdown.timeout.connect(self.countdown)
 


    def countdown(self):
        print('Counter')
        if self.counterdown==0:
            self.counterdown=10
            self.timerCountdown.stop()

            self.timer = QtCore.QTimer(self)
            self.timer.timeout.connect(self.update_image)
            self.timer.stop()
            self.timer.start(1000)
            self.update_image()
            self._ui.stopFish.show()
            self._ui.startFish.hide()

        else:

            self._ui.fish.setText(str(self.counterdown))
            self.counterdown=self.counterdown-1
        

    def stopFish(self):
        # print('Timer!!')
        self._ui.fish.setPixmap(QtGui.QPixmap())
        self._ui.fish.setText("......")
        self._ui.startFish.show()
        self._ui.stopFish.hide()
        self.mode='idle'
        self.tick=0
        self.timer.stop()

        accurancy=(self.correctFish+0.01)/(self.errorFish+self.showedFish)
        time=(self.totalTime/(self.correctFish+self.errorFish))

        accurancy=round(accurancy,2)
        time=round(time,2)

        if(accurancy>1):
            accurancy=1
        self._ui.fish.setText("Αποτελέσματα!\n\n Ακρίβεια "+ str(accurancy)+'\n Μέσος χρόνος:'+str(time))

        print (str(self.showedFish)+' '+str(self.showedSharck)+' accurancy '+str(accurancy)+' time '+str(time))



    @pyqtSlot(int)
    def setPage(self, value):
        print('\t\t\t\tActivate Widget',value)

        if value==105:
            msg="Τώρα θα παίξουμε τους ψαράδες!<br />Στην οθόνη θα εμφανίζονται διάφορα ψαράκια.<br />Άλλα είναι κόκκινα, άλλα πρόσινα και άλλα μπλέ.<br />Κάθε φορά που θα βγαίνει ένα ψαράκι, θα πρέπει να πατάς όσο πιο γρήγορα μπορείς το μεγάλο κουμπί (δείχνεις το πλήκτρο space) για να το ψαρεύεις.<br />Πρόσεχε, όμως! Πού και πού θα εμφανίζεται και ένας πεινασμένος καρχαρίας σαν και αυτόν. Όταν βλέπεις τον καρχαρία δεν πρέπει να πατάς το κουμπί γιατί ο καρχαρίας θα φάει όλα τα ψαράκια που έχεις ψαρέψει!!!<br /><br />Πάμε να κάνουμε μια δοκιμή για να δούμε αν το κατάλαβες; <br />Βάλε το δαχτυλάκι πάνω στο κουμπί να είσαι έτοιμος/η<br />(τοποθετείς το χεράκι του στο space). <br />Μόλις εμφανιστεί κάποιο ψαράκι πρέπει να πατήσεις όσο πιο γρήγορα μπορείς! <br />Πρόσεχε τους καρχαρίες!!!!<br />(Πάτα ένα πλήκτρο)"
        #     self.stopFish()
            self._ui.fish.setText(msg)
            

        if value==1:
            j=self._ui.stackedWidget.count()
            self.page1=page1View(self._model,self._main_controller._exercisesController[0])
            self._ui.stackedWidget.addWidget(self.page1)
            self._ui.stackedWidget.setCurrentIndex(j)
        
        elif value==2:
            j=self._ui.stackedWidget.count()
            self.page2=page1View(self._model,self._main_controller._exercisesController[1])
            self._ui.stackedWidget.addWidget(self.page2)
            self._ui.stackedWidget.setCurrentIndex(j)
        
        elif value==3:
            j=self._ui.stackedWidget.count()
            self.page3=page2View(self._model,self._main_controller._exercisesController[2])
            self._ui.stackedWidget.addWidget(self.page3._ui.stackedWidget)
            self._ui.stackedWidget.setCurrentIndex(j)
        
        elif value==4:
            j=self._ui.stackedWidget.count()
            self.page4=page2View(self._model,self._main_controller._exercisesController[3])
            self._ui.stackedWidget.addWidget(self.page4._ui.stackedWidget)
            self._ui.stackedWidget.setCurrentIndex(j)

        elif value==5:
            j=self._ui.stackedWidget.count()
            self._ui.stackedWidget.setCurrentIndex(15)    
            self.test3=page1View(self._model,self._main_controller._exercisesController[4])
            self._ui.stackedWidget.addWidget(self.test3._ui.widget)
            self._ui.stackedWidget.setCurrentIndex(j)        

            j=self._ui.stackedWidget.count()
            self._main_controller._exercisesController[4]._image2 = j+100
            self.test=(DisplayImageWidget(self._main_controller._exercisesController[4]._imagePath,self._model.displayImageRatio))
            self.test.setController(self._main_controller._exercisesController[4])
            self._ui.stackedWidget.addWidget(self.test)
            self._ui.stackedWidget.ali

        elif value==6:
            j=self._ui.stackedWidget.count()
            self.test4=page2View(self._model,self._main_controller._exercisesController[5])
            self.test4.answer51.show()
            self._ui.stackedWidget.addWidget(self.test4._ui.widget)
            self._ui.stackedWidget.setCurrentIndex(j)
            self._ui.stackedWidget.setCurrentIndex(0)
            self._ui.stackedWidget.setCurrentIndex(j)
            


        elif value==7:
            j=self._ui.stackedWidget.count()

            self.page7=page1View(self._model,self._main_controller._exercisesController[6])
            self._ui.stackedWidget.addWidget(self.page7)
            self._ui.stackedWidget.setCurrentIndex(j)

        elif value==8:
            j=self._ui.stackedWidget.count()
            self.page8=page1View(self._model,self._main_controller._exercisesController[7])
            self._ui.stackedWidget.addWidget(self.page8)
            self._ui.stackedWidget.setCurrentIndex(j)

        elif value==9:
            j=self._ui.stackedWidget.count()
            self.page9=page2View(self._model,self._main_controller._exercisesController[8])
            self._ui.stackedWidget.addWidget(self.page9._ui.stackedWidget)
            self._ui.stackedWidget.setCurrentIndex(j)

        elif value==10:
            j=self._ui.stackedWidget.count()
            self.page10=page2View(self._model,self._main_controller._exercisesController[9])
            self._ui.stackedWidget.addWidget(self.page10._ui.stackedWidget)
            self._ui.stackedWidget.setCurrentIndex(j)

        elif value==11:
            j=self._ui.stackedWidget.count()
            self._ui.stackedWidget.setCurrentIndex(15)    
            self.test11=page1View(self._model,self._main_controller._exercisesController[10])
            self._ui.stackedWidget.addWidget(self.test11._ui.widget)

            self._ui.stackedWidget.setCurrentIndex(j)        
            j=self._ui.stackedWidget.count()
            self._main_controller._exercisesController[10]._image2 = j+100
            self.test10B=(DisplayImageWidget(self._main_controller._exercisesController[10]._imagePath,self._model.displayImageRatio))
            self.test10B.setController(self._main_controller._exercisesController[10])
            self._ui.stackedWidget.addWidget(self.test10B)


        elif value==12:
            j=self._ui.stackedWidget.count()
            self.test12=page2View(self._model,self._main_controller._exercisesController[11])
            self._ui.stackedWidget.addWidget(self.test12._ui.widget)
            self.test12.answer51.show()
            self._ui.stackedWidget.setCurrentIndex(j)
            self._ui.stackedWidget.setCurrentIndex(0)
            self._ui.stackedWidget.setCurrentIndex(j)

        else:
            if value>100:
                value=value-100
            self._ui.stackedWidget.setCurrentIndex(value)
            if value==3:
                self._ui.pushButtoResultPrevius.hide()
                self.loadResultsByID(0)
            if value==1:
                self.hideButtons()


    @pyqtSlot(str)
    def feedbackShowButton(self,value):   
        if value=='show':
            self._ui.terminateButton.setDisabled(False)
            self._ui.nextExersice.setDisabled(False)
            self._ui.feedbackEasyButton.setDisabled(True)
            self._ui.feedbackNormalButton.setDisabled(True)
            self._ui.feedbackHardButton.setDisabled(True)
        else:
            self._ui.terminateButton.setDisabled(True)
            self._ui.nextExersice.setDisabled(True)
            
            self._ui.feedbackEasyButton.setDisabled(False)
            self._ui.feedbackNormalButton.setDisabled(False)
            self._ui.feedbackHardButton.setDisabled(False)
    
    @pyqtSlot(str)
    def changeFeedbackLabel(self,value):   
        print("!!!!! changeFeedbackLabel")
        self._ui.label_6.setText(value)
        
    @pyqtSlot(str)
    def nextPageSignalEx6(self, value):
        self.test6.openImage(value)
        self.test6.resize()     

    def hideButtons(self):
        # self._ui.feedbackEasyButton.setDisabled(True)
        # self._ui.feedbackNormalButton.setDisabled(True)
        # self._ui.feedbackHardButton.setDisabled(True)
        self._ui.terminateButton.setDisabled(False)
        self._ui.nextExersice.setDisabled(False)
     

    def showButtons(self,str):
        # time.sleep(self._model.sleepForAnswer)
        self._ui.feedbackEasyButton.setDisabled(False)
        self._ui.feedbackNormalButton.setDisabled(False)
        self._ui.feedbackHardButton.setDisabled(False)

    def loadResults(self,results):
        # time.sleep(5)
        self._ui.checkBox.setChecked(False)
        self._ui.checkBox2.setChecked(False)
        self._ui.checkBox3.setChecked(False)
        self._ui.checkBox4.setChecked(False)
        self._ui.checkBox5.setChecked(False)
        self._ui.checkBox6.setChecked(False)
        self._ui.checkBox7.setChecked(False)
        self._ui.checkBox8.setChecked(False)
        self._ui.checkBox9.setChecked(False)
        self._ui.checkBox10.setChecked(False)
        self._ui.checkBox11.setChecked(False)
        self._ui.checkBox12.setChecked(False)
        self._ui.checkBox13.setChecked(False)
        self._ui.checkBox14.setChecked(False)
        self._ui.checkBox15.setChecked(False)
        self._ui.checkBox16.setChecked(False)
        self._ui.checkBox17.setChecked(False)
        self._ui.checkBox18.setChecked(False)
        self._ui.checkBox19.setChecked(False)
        self._ui.checkBox20.setChecked(False)
        self._ui.checkBox21.setChecked(False)
        self._ui.checkBox22.setChecked(False)
        self._ui.checkBox23.setChecked(False)
        self._ui.checkBox24.setChecked(False)
        self._ui.checkBox25.setChecked(False)
        self._ui.checkBox26.setChecked(False)
        self._ui.checkBox27.setChecked(False)
        self._ui.checkBox28.setChecked(False)
        self._ui.checkBox29.setChecked(False)
        self._ui.checkBox30.setChecked(False)
        self._ui.checkBox31.setChecked(False)
        self._ui.checkBox32.setChecked(False)
        self._ui.checkBox33.setChecked(False)
        self._ui.checkBox34.setChecked(False)
        self._ui.checkBox35.setChecked(False)
        self._ui.checkBox36.setChecked(False)

        self._ui.lineResultsEx1.setText(results.answerEx1)
        self._ui.lineResultsEx2.setText(results.answerEx2)
        self._ui.lineResultsEx3.setText(results.answerEx3)
        self._ui.lineResultsEx4.setText(results.answerEx4)
        self._ui.lineResultsEx5.setText(results.answerEx5A)
        self._ui.lineResultsEx6.setText(results.answerEx6A)
        self._ui.lineResultsEx7.setText(results.answerEx7)
        self._ui.lineResultsEx8.setText(results.answerEx8)
        self._ui.lineResultsEx9.setText(results.answerEx9)
        self._ui.lineResultsEx10.setText(results.answerEx10)
        self._ui.lineResultsEx11.setText(results.answerEx11A)
        self._ui.lineResultsEx12.setText(results.answerEx12A)
        self._ui.lineResultName.setText(results.name)
        self._ui.lineResultsSurname.setText(results.surname)

        if(results.feedbackE1=='1'):
            self._ui.checkBox.setChecked(True)
        elif (results.feedbackE1=='2'):
            self._ui.checkBox13.setChecked(True)
        elif (results.feedbackE1=='3'):
            self._ui.checkBox25.setChecked(True)
        if(results.feedbackE2=='1'):
            self._ui.checkBox2.setChecked(True)
        elif (results.feedbackE2=='2'):
            self._ui.checkBox14.setChecked(True)
        elif (results.feedbackE2=='3'):
            self._ui.checkBox26.setChecked(True)

        if(results.feedbackE3=='1'):
            self._ui.checkBox3.setChecked(True)
        elif (results.feedbackE3=='2'):
            self._ui.checkBox15.setChecked(True)
        elif (results.feedbackE2=='3'):
            self._ui.checkBox27.setChecked(True)

        if(results.feedbackE4=='1'):
            self._ui.checkBox4.setChecked(True)
        elif (results.feedbackE4=='2'):
            self._ui.checkBox16.setChecked(True)
        elif (results.feedbackE4=='3'):
            self._ui.checkBox28.setChecked(True)

        if(results.feedbackE5=='1'):
            self._ui.checkBox5.setChecked(True)
        elif (results.feedbackE5=='2'):
            self._ui.checkBox17.setChecked(True)
        elif (results.feedbackE5=='3'):
            self._ui.checkBox29.setChecked(True)

        if(results.feedbackE6=='1'):
            self._ui.checkBox6.setChecked(True)
        elif (results.feedbackE5=='2'):
            self._ui.checkBox18.setChecked(True)
        elif (results.feedbackE6=='3'):
            self._ui.checkBox30.setChecked(True)


        if(results.feedbackE7=='1'):
            self._ui.checkBox7.setChecked(True)
        elif (results.feedbackE7=='2'):
            self._ui.checkBox19.setChecked(True)
        elif (results.feedbackE7=='3'):
            self._ui.checkBox31.setChecked(True)


        if(results.feedbackE8=='1'):
            self._ui.checkBox8.setChecked(True)
        elif (results.feedbackE8=='2'):
            self._ui.checkBox20.setChecked(True)
        elif (results.feedbackE8=='3'):
            self._ui.checkBox32.setChecked(True)


        if(results.feedbackE9=='1'):
            self._ui.checkBox9.setChecked(True)
        elif (results.feedbackE9=='2'):
            self._ui.checkBox21.setChecked(True)
        elif (results.feedbackE9=='3'):
            self._ui.checkBox33.setChecked(True)

        if(results.feedbackE10=='1'):
            self._ui.checkBox10.setChecked(True)
        elif (results.feedbackE10=='2'):
            self._ui.checkBox22.setChecked(True)
        elif (results.feedbackE10=='3'):
            self._ui.checkBox34.setChecked(True)

        if(results.feedbackE11=='1'):
            self._ui.checkBox11.setChecked(True)
        elif (results.feedbackE11=='2'):
            self._ui.checkBox23.setChecked(True)
        elif (results.feedbackE11=='3'):
            self._ui.checkBox35.setChecked(True)


        if(results.feedbackE12=='1'):
            self._ui.checkBox11.setChecked(True)
        elif (results.feedbackE12=='2'):
            self._ui.checkBox23.setChecked(True)
        elif (results.feedbackE10=='3'):
            self._ui.checkBox35.setChecked(True)



    def loadResultsByID(self,i):
        self.loadResults(self._model.result.listResults[i])

    def loadResultsByIDCounter(self,value):
        print(" change ",value)
        self.counter=self.counter+value
        print(" counter ",self.counter)
        self.loadResults(self._model.result.listResults[self.counter])

        if ( ( self.counter +1 )==len(self._model.result.listResults)):
            self._ui.pushButtonResultsNext.hide()
        else:
            self._ui.pushButtonResultsNext.show()


        if ( 0== len(self._model.result.listResults)):
            self._ui.pushButtoResultPrevius.hide()
        else:
            self._ui.pushButtoResultPrevius.show()


    def update_image(self):
        self.tick=time.time()
        self.lock=False
        # print('Update !!!!'+str(self.tick))
        if(self.showedFish>100):
            self.stopFish()
            return
        if(random.randint(0,99)>80):
            self.path_of_image='/robotApp/fish/sharck.png'
            self.mode='sharck'
            self.showedSharck=self.showedSharck+1
        else:
            self.mode='fish'
            self.showedFish=self.showedFish+1
            if self.counter==0:
                self.path_of_image='/robotApp/fish/fish.png'
                self.counter=self.counter+1
            else:
                self.counter=0
                self.path_of_image= '/robotApp/fish/fish-yellow.png'   
        self._ui.fish.setPixmap(QtGui.QPixmap(self.path_of_image))

    