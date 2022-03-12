import rospy
from std_msgs.msg import String
from audio_service.srv import *

# from audio_service.srv import *
import rospy 

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
        print('Audio S2T:',msg,' ')
        self._pub.publish(msg)
        # self._rate.sleep()

    def add_two_ints_client(self):

        # NOTE: you don't have to call rospy.init_node() to make calls against
        # a service. This is because service clients do not have to be
        # nodes.

        # block until the add_two_ints service is available
        # you can optionally specify a timeout
        rospy.wait_for_service('add_two_ints')
        
        try:
            # create a handle to the add_two_ints service
            add_two_ints = rospy.ServiceProxy('add_two_ints', GetAudio)
            
            
            
            # simplified style
            resp1 = add_two_ints()

            # formal style
            resp2 = add_two_ints.call(GetAudioRequest())
            
            print(" replied {}",resp2)

        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

    def getText(self):

        # NOTE: you don't have to call rospy.init_node() to make calls against
        # a service. This is because service clients do not have to be
        # nodes.

        # block until the add_two_ints service is available
        # you can optionally specify a timeout
        rospy.wait_for_service('add_two_ints')

            # create a handle to the add_two_ints service
        add_two_ints = rospy.ServiceProxy('add_two_ints', GetAudio)
            
            
            # simplified style
        resp1 = add_two_ints()

            # formal style
        resp2 = add_two_ints.call(GetAudioRequest())
            
            
        print(" replied {}",resp2.text)




