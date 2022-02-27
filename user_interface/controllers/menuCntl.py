from PyQt5.QtCore import QObject, pyqtSlot

import rospy
from std_msgs.msg import String

class MenuCntl(QObject):
    def __init__(self, model,exercisesController):
        super().__init__()
        self._model = model
        self._exercisesController=exercisesController
        self._exercise3Img=0;
        self._exercise4Img=0;
        
        # self.pub = rospy.Publisher('chatter', String, queue_size=10)
        # rospy.init_node('talker', anonymous=True)
	
    @pyqtSlot(int)
    def clearClicked(self):
        self._model.reset()
        self._model.amount =''
        self._model.name=''
        self._model.surname=''
        self._model.age=''



    
    @pyqtSlot(int)
    def clearClicked(self):
        print('................................')
        print('Main menu clear form previous values' , self._model.name , self._model.surname, self._model.age)
        self._model.name=''
        self._model.surname=''
        self._model.age=''
        self._model.resetFields()

    @pyqtSlot(str,str,str)
    def saveClicked(self,name,surname,age):
        print('Save main menu data  ',name,surname,age)
        self._model.name=name
        self._model.surname=surname
        self._model.age=age
        

    @pyqtSlot(int)
    def selectButtonClicked(self,value):
        print('Save answer :',value)
        self._model.selectedExercise=value
        

    @pyqtSlot(int)
    def clearClicked(self):
        self._model.amount = 'TEST!!!!'
        print ('Press !!')
        self._model.name=''
        self._model.surname=''
        self._model.age=''


        # calculate button enabled state
        # self._model.enable_reset = True if value else False

    def change_text(self, value):
        self._model.amount = value
        rospy.loginfo(value)
        self.pub.publish(str(value))

        # calculate button enabled state
        self._model.enable_reset = True if value else False
    

    @pyqtSlot(int)
    def storeAnswer(self,value):
        self._exercisesController[self._model.currentExerciseID-1].feedbackStore(self._model.result,value)
        self._model.trigger(7)
        # self._model.selectedExercise=value

    @pyqtSlot(int)
    def storePose(self,value):
        self._exercisesController[self._model.currentExerciseID-1].feedbackStore(self._model.result,value)
        self._model.trigger(7)
        # self._model.selectedExercise=value


    @pyqtSlot(int)
    def storeAnswer5(self,value):
        self._exercisesController[4].stepb(self._model.result,value)
        self._model.trigger(11)
        # self._model.selectedExercise=value

    @pyqtSlot(str)
    def setPage(self,value):
        print('Set page ',value)
        # if (value==0):
        pageId=self._exercisesController[value].mainPage
        self._currentExerciseID=value
        self._model.selectedExercise=value
        self._model.trigger(pageId)
        self._exercisesController[value].readExersice()
        self._exercisesController[value].readAnswers()
        self._model.currentExerciseID=value+1

    @pyqtSlot(str)
    def go2Home(self):
       self._model.trigger(0)
       self.printResults()


    @pyqtSlot(str)
    def move2NextPage(self):
        value=self._model.currentExerciseID
        print('Move to next page ',self._model.currentExerciseID)
        # if (value==0):value
        self._model.currentExerciseID=value
        self._model.trigger(int(value)+1)
        self._exercisesController[value].readExersice()
        self._exercisesController[value].readAnswers()
        self._model.currentExerciseID=self._model.currentExerciseID+1
        self._model.showButtonFeedback='hide'


    @pyqtSlot(str)
    def nextPage3(self,value):
        print('Change Image step 3 {}',self._exercise3Img)
        self._model.nextPageEx2('2')
        if self._exercise3Img==0:
            self._exercisesController[self._model.currentExerciseID-1].step2()
        else:   
            self._exercisesController[self._model.currentExerciseID-1].readAnswers2()
        self._exercise3Img=self._exercise3Img+1

    @pyqtSlot(str)
    def nextPage4(self,value):
        if self._exercise4Img==0:
            self._exercisesController[self._model.currentExerciseID-1].step2()
        elif self._exercise4Img==1:
            self._exercisesController[self._model.currentExerciseID-1].step3()
        elif self._exercise4Img==2:
            self._exercisesController[self._model.currentExerciseID-1].step4()
        elif self._exercise4Img==3:
            self._exercisesController[self._model.currentExerciseID-1].step5()
        else:
            self._exercisesController[self._model.currentExerciseID-1].step6()
        self._exercise4Img=self._exercise4Img+1;
        self._model.nextPageEx4('2')



    @pyqtSlot(str)
    def nextPageEx6(self,value):
        print('Change Image 6')
        self._exercisesController[self._model.currentExerciseID-1].stepA(self._model.result,value)
        self._model.nextPageEx6('2')


    @pyqtSlot(str)
    def feedback(self,value):
        print('Feedback {}',value)
        self._model.showButtonFeedback='show'
        self._exercisesController[self._model.currentExerciseID].continueDialog()


        # self._model.nextPageEx6('2')
        
    

    def change_text(self, value):
        self._model.amount = value
        rospy.loginfo(value)
        self.pub.publish(str(value))

        # calculate button enabled state
        self._model.enable_reset = True if value else False

    def printUserData(self):
        print("Print User data :  Name: {},  Surname: {}, Age : {}", self._model.name,self._model.surname,self._model.age)


    def printResults(self):
        self.printUserData()
        self._exercisesController[0].printResult()
        self._exercisesController[1].printResult()
        self._exercisesController[2].printResult()
        self._exercisesController[3].printResult()
        self._exercisesController[4].printResult()
        self._exercisesController[5].printResult()