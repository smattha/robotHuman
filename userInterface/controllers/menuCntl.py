from PyQt5.QtCore import QObject, pyqtSlot

import rospy
from std_msgs.msg import String

class MenuCntl(QObject):
    def __init__(self, model,exer1Controller):
        super().__init__()
        self._model = model
        self._exer1Controller=exer1Controller
        # self.pub = rospy.Publisher('chatter', String, queue_size=10)
        # rospy.init_node('talker', anonymous=True)
	
    @pyqtSlot(int)
    def clearClicked(self):
        self._model.reset()
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
    def clearClicked(self):
        print('................................')
        print('Main menu clear form previous values' , self._model.name , self._model.surname, self._model.age)
        self._model.name=''
        self._model.surname=''
        self._model.age=''
        self._model.resetFields()

    @pyqtSlot(str,str,str)
    def saveClicked(self,name,surname,age):
        print('S_ave main menu data  ',name,surname,age)
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
    

    @pyqtSlot(str)
    def clickLabel(self,value):
        print('select Answer step1 ',value)
        self._exer1Controller.feedback()
        self._model.trigger(7)
        # self._model.selectedExercise=value

    @pyqtSlot(str)
    def setPage(self,value):
        print('Set page ',value)
        self._model.selectedExercise=value
        self._model.trigger(int(value)+1)
        self._exer1Controller.readExersice()
        self._exer1Controller.readAnswers()
