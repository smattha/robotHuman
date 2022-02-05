from PyQt5.QtCore import QObject, pyqtSlot

import rospy
from std_msgs.msg import String

class MenuCntl(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model
        # self.pub = rospy.Publisher('chatter', String, queue_size=10)
        # rospy.init_node('talker', anonymous=True)
	
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
    def clearClicked(self):
        print('................................')
        print('Main menu clear form previous values' , self._model.name , self._model.surname, self._model.age)
        self._model.name=''
        self._model.surname=''
        self._model.age=''

    @pyqtSlot(str,str,str)
    def saveClicked(self,name,surname,age):
        print('Save main menu data ',name,surname,age)
        self._model.name=name
        self._model.surname=surname
        self._model.age=age
        

    @pyqtSlot(str)
    def selectButtonClicked(self,value):
        print('Save main menu data ',value)
        self._model.selectedExercise=value