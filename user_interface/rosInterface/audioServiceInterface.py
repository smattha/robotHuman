from time import sleep

import rospy
from std_msgs.msg import String
from audio_service.srv import *
from motors_controller.srv import *
from robot_face.srv import *
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import String
import rospy


class Ros_Audio_Service(object):
    def __init__(self):
        self.flag = 'run'
        try:
            rate=0.1
            print('Initialize ROS service,Rate',rate)
            self._pub = rospy.Publisher('chatter', String, queue_size=10)
            rospy.init_node('talker', anonymous=True)
            self._rate = rospy.Rate(rate) # 10hz
        except rospy.ROSInterruptException:
            print('Exception Occured in ros audio service')
            pass

    def talker1(self,msg):
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

        if self.flag == 'test':
            sleep(10)
            return 'TEST'

        rospy.wait_for_service('add_two_ints')

            # create a handle to the add_two_ints service
        getText_ROS = rospy.ServiceProxy('add_two_ints', GetAudio)
            
            
            # simplified style
        resp1 = getText_ROS()

            # formal style
        resp2 = getText_ROS.call(GetAudioRequest())
            


        print(" Replied {}",resp2.text)


        return resp2

    def talker(self,msg):

        if self.flag == 'test':
            sleep(1)
            return 'TEST'

        rospy.wait_for_service('textToSpeechBlocking')

        # create a handle to the add_two_ints service
        getText_ROS = rospy.ServiceProxy('textToSpeechBlocking', text2Speech)

        s1=text2SpeechRequest()
        s1.text=msg

        resp2 = getText_ROS.call(  s1 )

        print(" Replied {}", resp2.text)

        return resp2



    def displayImg(self):

        # if self.flag == 'test':
        #     sleep(1)
        #     return 'TEST'

        rospy.wait_for_service('robot_face_srv')

        # create a handle to the add_two_ints service
        getText_ROS = rospy.ServiceProxy('robot_face_srv', imageName)

        s1=imageNameRequest()
        s1.name='/home/stergios/Downloads/1.jpeg'

        resp2 = getText_ROS.call(  s1 )

        print(" Replied {}", resp2.sum)

        return resp2



    def moveRobot(self,a,b,c,d,e,f):

        if self.flag == 'test':
            print('Running robot in test mode! Sleep for 1 sec to simulate the robot motion.')
            sleep(1)
            return 'TEST'

        rospy.wait_for_service('motors_controller_ros_intf_srv_abs')

        # create a handle to the add_two_ints service
        getText_ROS = rospy.ServiceProxy('motors_controller_ros_intf_srv_abs', motors_controller)

        position=motors_controllerRequest()
        position.a=a
        position.b=b
        position.c=c
        position.d=d
        position.e=e
        position.f=f

        resp2 = getText_ROS.call(  position )
        print(" Replied {}", resp2.sum)

        return resp2

    def callback1(self,data):
        rospy.loginfo('!!Msg received!: "%s" ', type(data.data))
        d=data.data
        # Language in which you want to convert
        

    def listener(self):

        # rospy.Subscriber('fingers', Float32MultiArray, self.callback)
        rospy.Subscriber('face', String, self.callback1)
        rospy.spin()

    def callback(self,data):
        rospy.loginfo('Msg received: "%s" ', len(data.data))
        rospy.loginfo('Msg received: "%s" ', data.data[0])
        
	    # Language in which you want to convert
