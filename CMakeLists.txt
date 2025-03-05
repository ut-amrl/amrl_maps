cmake_minimum_required(VERSION 3.0)
project(amrl_maps)

# For compatibility with cmake 3.0 to 3.2
if(POLICY CMP0057)
  cmake_policy(SET CMP0057 NEW)
endif()

if(DEFINED ENV{ROS_ROOT} AND EXISTS "$ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake")
  message(STATUS "Detected ROS1 (rosbuild) environment.")

  include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)
  rosbuild_init()
else()
  #===============================================================
  # ROS2 (ament) Section
  #===============================================================
  message(STATUS "Detected ROS2 (ament) environment.")

  find_package(ament_cmake REQUIRED)

  # If you have a subdirectory with static data:
  install(
    DIRECTORY maps
    DESTINATION share/${PROJECT_NAME}
  )

  ament_package()
endif()
