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
  file(GLOB MAP_DIRS RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} "*")
  foreach(MAP_DIR ${MAP_DIRS})
    if(IS_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/${MAP_DIR})
      # Skip hidden directories, utility_scripts, and build directories
      if(NOT MAP_DIR MATCHES "^\\." AND 
         NOT MAP_DIR STREQUAL "utility_scripts" AND
         NOT MAP_DIR STREQUAL "build" AND
         NOT MAP_DIR STREQUAL "install" AND
         NOT MAP_DIR STREQUAL "resource" AND
         NOT MAP_DIR STREQUAL ".git" AND
         NOT MAP_DIR STREQUAL ".github")
        message(STATUS "Installing map directory: ${MAP_DIR}")
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

