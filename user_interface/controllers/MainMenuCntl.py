from PyQt5.QtCore import QObject, pyqtSlot

# import rospy
# from std_msgs.msg import String

class MainMenuCntl(QObject):
    def __init__(self, model,exercisesController):
        super().__init__()
        self._model = model
        self._exercisesController=exercisesController
        self._exercise3Img=0;
        self._exercise4Img=0;
        

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



    def change_text(self, value):
        self._model.amount = value
        rospy.loginfo(value)
        self.pub.publish(str(value))
        self._model.enable_reset = True if value else False
    

    @pyqtSlot(int)
    def storePose(self,value):
        self._exercisesController[self._model.currentExerciseID-1].feedbackStore(self._model.result,value)
        self._model.trigger(2)


    @pyqtSlot(str)
    def setPage(self,value):
        print('Main Page Controller:Set page ',value)
        self._currentExerciseID=value
        self._model.selectedExercise=value
        self._model.trigger(value+1)
        self._exercisesController[value].readExersice()
        self._exercisesController[value].readAnswers()
        self._model.currentExerciseID=value+1


    @pyqtSlot(str)
    def go2Home(self,name,surname,age):
       self._model.trigger(0)
       self._model.name = name
       self._model.surname = surname
       self._model.age = age
       self.printResults()



    @pyqtSlot(str)
    def go2Home1(self):
       self._model.trigger(0)


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
    def feedback(self,value):

        print('\t\tFeedback Main:', value)
        self._model.showButtonFeedback='show'
        self._exercisesController[self._model.currentExerciseID-1].feedbackAnswer(value)

        
    

    def change_text(self, value):
        self._model.amount = value
        rospy.loginfo(value)
        self.pub.publish(str(value))
        self._model.enable_reset = True if value else False

    def printUserData(self):
        print("Print User data :  Name: {},  Surname: {}, Age : {}", self._model.name,self._model.surname,self._model.age)


    def printResults(self):
        newResult=self._model.createNewResultObject()
        newResult.name=self._model.name
        newResult.surname = self._model.surname
        newResult.answerEx1=str(self._exercisesController[0]._answerEx1)
        newResult.answerEx2=str(self._exercisesController[1]._answerEx1)
        newResult.answerEx3=str(self._exercisesController[2]._answerEx1)
        newResult.answerEx4=str(self._exercisesController[3]._answerEx1)
        newResult.answerEx5A = str(self._exercisesController[4]._answerEx1)
        newResult.answerEx5B = str(self._exercisesController[4]._answerEx2)
        newResult.answerEx6A = str(self._exercisesController[5]._answerEx1)
        newResult.answerEx6B = str(self._exercisesController[5].answerEx32)
        newResult.answerEx7 = str(self._exercisesController[6]._answerEx1)
        newResult.answerEx8 = str(self._exercisesController[7]._answerEx1)
        newResult.answerEx9 = str(self._exercisesController[8]._answerEx1)
        newResult.answerEx10 = str(self._exercisesController[9]._answerEx1)
        newResult.answerEx11A = str(self._exercisesController[10]._answerEx1)
        newResult.answerEx11B = str(self._exercisesController[10]._answerEx2)
        newResult.answerEx12A = str(self._exercisesController[11]._answerEx1)
        newResult.answerEx12B = str(self._exercisesController[11].answerEx32)

        newResult.feedbackE1=str(self._exercisesController[0]._feedback)
        newResult.feedbackE2=str(self._exercisesController[1]._feedback)
        newResult.feedbackE3=str(self._exercisesController[2]._feedback)
        newResult.feedbackE4=str(self._exercisesController[3]._feedback)
        newResult.feedbackE5=str(self._exercisesController[4]._feedback)
        newResult.feedbackE6=str(self._exercisesController[5]._feedback)
        newResult.feedbackE7=str(self._exercisesController[6]._feedback)
        newResult.feedbackE8=str(self._exercisesController[7]._feedback)
        newResult.feedbackE9=str(self._exercisesController[8]._feedback)
        newResult.feedbackE10=str(self._exercisesController[9]._feedback)
        newResult.feedbackE11=str(self._exercisesController[10]._feedback)
        newResult.feedbackE12=str(self._exercisesController[11]._feedback)

        self._model.createNewResult(newResult)
        self.printUserData()
        for i in self._exercisesController:
              i.printResult()
              print(self._model.name)
              i.clearResults()

