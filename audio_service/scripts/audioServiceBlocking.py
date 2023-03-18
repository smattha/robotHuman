#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from gtts import gTTS
from playsound import playsound
from audio_service.srv import *
import os

NAME = 'speechToTextBlocking'








class ControllerExersice5(object):

	def __init__(self):
		rospy.init_node(NAME)
		s = rospy.Service('textToSpeechBlocking', text2Speech, self.text2SpeechFnct)
		print ("Service waiting ...")
	def text2SpeechFnct(self,req):
		rospy.loginfo('Msg received: "%s" ', req.text)
		# Language in which you want to convert
		language = 'el'

		# Passing the text and language to the engine,
		# here we have marked slow=False. Which tells
		# the module that the converted audio should
		# have a high speed
		myobj = gTTS(text=req.text, lang=language, slow=False)
		
		print("Audio saved")
		# Saving the converted audio in a mp3 file named
		# welcome
		myobj.save("audio.mp3")

		# Playing the converted file
		#os.system("mpg321 welcome.mp3")
		# for playing note.wav file
		playsound('audio.mp3', block=True)
		os.remove('audio.mp3')
		text='true'
		return text2SpeechResponse(text)
	
def destroy(req):
	print ("destroy")
	rospy.signal_shutdown("test")
	print ("Done")
	return shutdownSrvResponse("")

if __name__ == '__main__':
 
    
    app= ControllerExersice5()
    rospy.Service('shutdownT2S', shutdownSrv,destroy)


    rospy.spin()






