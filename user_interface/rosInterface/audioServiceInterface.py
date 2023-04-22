from time import sleep

import rospy
from std_msgs.msg import String
from audio_service.srv import *
from motors_controller.srv import *
from robot_face.srv import *
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import String
import rospy
from unifiedGestureFingertipDetection.srv import *


class Ros_Audio_Service(object):
    def __init__(self):
        self.flag = 'run'
        try:
            rate=0.1
            print('Initialize ROS service,Rate',rate)
            self._pub = rospy.Publisher('chatter', String, queue_size=10)
            rospy.init_node('talker', anonymous=True)
            self._rate = rospy.Rate(rate) # 10hz
            rospy.Service('shutdownUI', shutdownSrv,self.destroy)
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
        
        self.moveRobotFromFile('/robotApp/positions/speech2Txt.txt')
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

        req= GetAudioRequest();
        req.parameter=['a','b','c']
            
        resp2 = getText_ROS.call(req)

        print(" Replied {}",resp2.text)


        return resp2
    

    def moveRobotFromFile(self,name):
        # sleep(1)
        # return 'test'
        if self.flag == 'test':
            sleep(10)
            return 'TEST'
        print("Waiting for the server!!!")
        rospy.wait_for_service('motors_controller_ros_intf_srv_file')

        print("Found!!!")
        rosProxy = rospy.ServiceProxy('motors_controller_ros_intf_srv_file', moveRobotFile)

        print("Send Request")
        req= moveRobotFileRequest();
        req.name=name
        print("Called with file name "+name+"")
        resp2 = rosProxy.call(req)

        print(" Finished ")

        return resp2


    def talker(self,msg):

        self.moveRobotFromFile('/robotApp/positions/voice.txt')
        print("Call text to speech with msg :\t\t"+msg)
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



    def displayImg(self,name):
        
        # if self.flag == 'test':
        #     sleep(1)
        #     return 'TEST'

        rospy.wait_for_service('robot_face_srv')

        # create a handle to the add_two_ints service
        getText_ROS = rospy.ServiceProxy('robot_face_srv', imageName)

        s1=imageNameRequest()
        s1.name=name

        resp2 = getText_ROS.call(  s1 )

        print(" Replied {}", resp2.sum)

        return resp2


    def getFace(self):

        # if self.flag == 'test':
        #     sleep(1)
        #     return 'TEST'

        rospy.wait_for_service('face')

        # create a handle to the add_two_ints service
        getText_ROS = rospy.ServiceProxy('face', face)

        s1=faceRequest()
        s1.text='/home/stergios/Downloads/1.jpeg'

        resp2 = getText_ROS.call(  s1 )

        print(" Replied {}", resp2.text)

        return resp2


    def getFinger(self):

        # if self.flag == 'test':
        #     sleep(1)
        #     return 'TEST'

        rospy.wait_for_service('fingers')

        # create a handle to the add_two_ints service
        getText_ROS = rospy.ServiceProxy('fingers', fingers)

        s1=fingersRequest()
        #s1.text='/home/stergios/Downloads/1.jpeg'

        resp2 = getText_ROS.call(  s1 )

        print(" Replied {}", resp2.text)

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
        # rospy.loginfo('!!Msg received!: "%s" ', type(data.data))
        d=data.data
        x=d.split(":")
        rospy.loginfo('!!Msg received!: "%s", "%s" ', x[0],x[1])

        # Language in which you want to convert
    def getName(self):

        if self.flag == 'test':
            sleep(10)
            return 'TEST'

        data=rospy.wait_for_message("face", String, timeout=None)
        d=data.data
        x=d.split(":")
        rospy.loginfo('!!Msg received!: "%s", "%s" ', x[0],x[1])
        return x[0]

    def getPalm(self):
        if self.flag == 'test':
            sleep(10)
            return 'TEST'
        data=rospy.wait_for_message("fingers", Float32MultiArray, timeout=None)
        d=data.data
        rospy.loginfo('Msg received: "%s" ', data.data[0])


    def listener(self):

        #rospy.Subscriber('fingers', Float32MultiArray, self.callback)
        rospy.Subscriber('face', String, self.callback1)
        # rospy.Subscriber('fingers', String, self.callback)
        rospy.spin()

    def callback(self,data):
        # rospy.loginfo('Msg received: "%s" ', len(data.data))
        rospy.loginfo('Msg received: "%s" ', data.data[0])
        
	    # Language in which you want to convert


    def getRecognitionResult(self):
        print("Calling Recognition Service !!!")
        # if self.flag == 'test':
        #     sleep(1)
        #     return 'TEST'

        rospy.wait_for_service('recognitions')

        getText_ROS = rospy.ServiceProxy('recognitions', recognition)

        s1=recognitionRequest()
        #s1.text='/home/stergios/Downloads/1.jpeg'

        resp2 = getText_ROS.call(  s1 )

        for x in range(len(resp2.recog)):
            print("         "+ str(resp2.recog[x].name)+" " +str(resp2.recog[x].isFocus) +" " +str(resp2.recog[x].hasRaiseHand))
        return resp2


    def destroy(self,req):
        import signal
        import os
        import psutil

        print ("destroy")


        os.kill(os.getpid(), signal.SIGINT)
        print ("destroy")


        current_system_pid = os.getpid()

        ThisSystem = psutil.Process(current_system_pid)
        ThisSystem.terminate()
        ThisSystem.kill()
        print ("destroy")
        return shutdownSrvResponse("")
        print ("destroy")
        print ("destroy")

        print ("Done")

        
    def getNames(self):
        print("Calling Recognition Service For Names of the children!!!")
        # if self.flag == 'test':
        #     sleep(1)
        #     print("Calling Recognition service is completed !!!")
        #     return 'TEST'

        resp2=self.getRecognitionResult()
        name=""
        for x in range(len(resp2.recog)):
            name= name+" "+str(resp2.recog[x].name)
        print("Calling Recognition service is completed !!!")
        return name

    def getHand(self):
        print("Calling Recognition Service For Hand of the children!!!")
        if self.flag == 'test':
            sleep(1)
            print("Calling Recognition service is completed !!!")
            return 'TEST'
        
        while True:
            resp2=self.getRecognitionResult()
            name=""
            for x in range(len(resp2.recog)):
                if  str(resp2.recog[x].hasRaiseHand)=='True':
                    print("cc")
                    print("Calling Recognition service is completed !!!")
                    return str(resp2.recog[x].name)
        return resp2
    
    def focus(self,name):
        print("Calling Recognition Service For Hand of the children!!!")
        if self.flag == 'test':
            sleep(1)
            print("Calling Recognition service is completed !!!")
            return 'TEST'
        
        resp2=self.getRecognitionResult()
        name=""
        for x in range(len(resp2.recog)):
            # if resp2.recog[x].hasRaiseHand==name:
                if  str(resp2.recog[x].isFocus)=='True':
                    return True
                else :
                    return False
        return False