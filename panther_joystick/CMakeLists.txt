cmake_minimum_required(VERSION 2.8.3)
project(panther_joystick)

find_package(catkin REQUIRED COMPONENTS rospy sound_play sensor_msgs rosservice)

catkin_python_setup()

catkin_package()

include_directories()

catkin_install_python(PROGRAMS scripts/joystick_bridge.py
                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

# Install config and launch folders
install(DIRECTORY launch config
DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})