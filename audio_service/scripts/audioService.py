#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from gtts import gTTS
from playsound import playsound
import os

def callback(data):
	rospy.loginfo('Msg received: "%s" ', data.data)
	# Language in which you want to convert
	language = 'el'

	# Passing the text and language to the engine,
	# here we have marked slow=False. Which tells
	# the module that the converted audio should
	# have a high speed
	myobj = gTTS(text=data.data, lang=language, slow=False)
	
	print("Audio saved")
	# Saving the converted audio in a mp3 file named
	# welcome
	myobj.save("audio.mp3")

	# Playing the converted file
	#os.system("mpg321 welcome.mp3")
	# for playing note.wav file
	playsound('audio.mp3', block=True)
	os.remove('audio.mp3')
	

def listener():

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
