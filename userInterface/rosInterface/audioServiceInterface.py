import rospy
from std_msgs.msg import String

class Ros_Audio_Service(object):
    def __init__(self):
        try:
            print('init')
            self._pub = rospy.Publisher('chatter', String, queue_size=10)
            rospy.init_node('talker', anonymous=True)
            self._rate = rospy.Rate(0.1) # 10hz
        except rospy.ROSInterruptException:
            pass

    def talker(self,msg):
        print('talker',msg,' ')
        # if rospy.is_shutdown():
        rospy.loginfo(msg)
        self._pub.publish(msg)
        # self._rate.sleep()

