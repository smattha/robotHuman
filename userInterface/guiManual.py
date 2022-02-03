#!/usr/bin/env python3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

import rospy
from std_msgs.msg import String


class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow,self).__init__()
		self.setGeometry(0,0,600,600)
		self.setWindowTitle("Hello World")
		self.initUI()
		
	def initUI(self):
		self.label=QtWidgets.QLabel(self)
		self.label.setText("Hello")
		self.label.move(50,50)
		
		self.b1=QtWidgets.QPushButton(self)
		self.b1.setText("Click me")
		self.b1.clicked.connect(self.clicked)
			
	def clicked(self):
		print("clicked")
		self.label.setText("Use press the button")
		self.update()
		
	def clickedROS():
		print("clicked")
		pub = rospy.Publisher('chatter', String, queue_size=10)
		rospy.init_node('talker', anonymous=True)
		hello_str = "με λενε στεργιο" 	
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		
	def update(self):
		self.label.adjustSize()





def window():
	app=QApplication(sys.argv)
	win=MyWindow()
	win.show()
	sys.exit(app.exec_())
window()
