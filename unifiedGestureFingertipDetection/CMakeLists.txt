cmake_minimum_required(VERSION 3.0.2)
project(unifiedGestureFingertipDetection)

find_package(catkin REQUIRED COMPONENTS message_generation std_msgs )

add_message_files(DIRECTORY msg FILES RecognitionMsg.msg)
add_service_files(DIRECTORY srv FILES face.srv fingers.srv recognition.srv  shutdownSrv.srv)

generate_messages(DEPENDENCIES std_msgs)



catkin_package(CATKIN_DEPENDS message_runtime std_msgs)



# do not wildcard install files since the root folder of the package will contain a debian folder for releasing
catkin_install_python(PROGRAMS
  0623takephotos.py
 DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
install(FILES
  README
  #talker_listener.launch
 DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

