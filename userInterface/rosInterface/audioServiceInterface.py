import rospy
from std_msgs.msg import String

class Ros_Audio_Service(object):
    def __init__(self):
        try:
            rate=0.1
            print('Initialize ROS service,Rate',rate)
            self._pub = rospy.Publisher('chatter', String, queue_size=10)
            rospy.init_node('talker', anonymous=True)
            self._rate = rospy.Rate(rate) # 10hz
        except rospy.ROSInterruptException:
            print('Exception Occured in ros audio service')
            pass

    def talker(self,msg):
        print('Send Message ',msg,' ')
        self._pub.publish(msg)
        # self._rate.sleep()

