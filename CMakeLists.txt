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

  # Install all map directories from root level (maintaining ROS1 backward compatibility)
  # Get all directories that contain map files
  file(GLOB MAP_DIRS "*")
  foreach(MAP_DIR ${MAP_DIRS})
    if(IS_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/${MAP_DIR})
      # Skip hidden directories, utility_scripts, and build directories
      get_filename_component(DIR_NAME ${MAP_DIR} NAME)
      if(NOT DIR_NAME MATCHES "^\\." AND 
         NOT DIR_NAME STREQUAL "utility_scripts" AND
         NOT DIR_NAME STREQUAL "build" AND
         NOT DIR_NAME STREQUAL "install" AND
         NOT DIR_NAME STREQUAL "resource")
        install(
          DIRECTORY ${MAP_DIR}
          DESTINATION share/${PROJECT_NAME}
        )
      endif()
    endif()
  endforeach()

  # Install package metadata
  install(FILES package.xml 
    DESTINATION share/${PROJECT_NAME}
  )

  # Install the resource marker file to register the package with ament index
  install(
    DIRECTORY resource
    DESTINATION share/${PROJECT_NAME}
  )

  ament_package()
else()
  message(FATAL_ERROR "Unknown ROS_VERSION ${ROS_VERSION}")
endif()

