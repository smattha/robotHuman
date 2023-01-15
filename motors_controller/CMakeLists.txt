cmake_minimum_required(VERSION 3.0.2)
project(motors_controller)

find_package(catkin REQUIRED COMPONENTS message_generation std_msgs)

#add_message_files(DIRECTORY msg FILES Floats.msg HeaderString.msg)
#add_service_files(DIRECTORY srv FILES GetAudio.srv)

#generate_messages(DEPENDENCIES std_msgs)
add_service_files(DIRECTORY srv FILES motors_controller.srv )
generate_messages(DEPENDENCIES std_msgs)


catkin_package(CATKIN_DEPENDS message_runtime std_msgs)

#catkin_install_python(PROGRAMS
 # motors_controller_ros.py
 #  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
#)

# do not wildcard install files since the root folder of the package will contain a debian folder for releasing
#catkin_install_python(PROGRAMS
  #mainMenu.py
# DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
#)
install(FILES
  README
  #talker_listener.launch
 DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)





