PROJECT(amrl_maps)
CMAKE_MINIMUM_REQUIRED(VERSION 3.8)

if(DEFINED ENV{ROS_VERSION})
  set(ROS_VERSION $ENV{ROS_VERSION})
else()
  message(FATAL_ERROR "ROS_VERSION is not defined")
endif()


if(${ROS_VERSION} EQUAL "1")
  message(STATUS "Compiling with ROS1 ROSBUILD")
  INCLUDE($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)
  ROSBUILD_INIT()
elseif(${ROS_VERSION} EQUAL "2")
  message(STATUS "Compiling with ROS2 COLCON")
  find_package(ament_cmake REQUIRED)

  ament_package()

  SET(maps_list CDL_Ground EmptyMap UT_Campus ASE1 ASE4 AHG1 AHG2 AHGM GDC1 GDC2 GDC3 GDC4 GDC5 GDC6 GDC7 GHC1 GHC2 GHC3 GHC5 GHC6)
  foreach(map_name ${maps_list})
    INSTALL(DIRECTORY ${map_name}/ DESTINATION share/${PROJECT_NAME}/${map_name}/)
  endforeach()

else()
  message(FATAL_ERROR "Unknown ROS_VERSION ${ROS_VERSION}")
endif()

