from PyQt5.QtCore import QObject, pyqtSlot

import rospy
from std_msgs.msg import String

class Ex1Cntrl(QObject):
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
    

    @pyqtSlot(str)
    def clickLabel(self,value):
        print('Save main menu data ',value)
        # self._model.selectedExercise=value
