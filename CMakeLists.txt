CMAKE_MINIMUM_REQUIRED(VERSION 3.8)
PROJECT(amrl_maps)

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

  # Copy maps into the install directory
  install(DIRECTORY AHG_Apartment DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY AHG1 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY AHG2 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY AHG2v2 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY AHGHallway DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY AHGM DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY Airsim-Neighborhood DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY ASE1 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY ASE4 DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY Briefcase DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY Briefcase_Obstacles DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY EmptyMap DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY freiburg_parkinglot DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY GDC_Track DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY GDC1 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY GDC2 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY GDC3 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY GDC4 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY GDC5 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY GDC6 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY GDC7 DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY GHC_Elevators DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY GHC1 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY GHC2 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY GHC3 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY GHC4 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY GHC5 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY GHC6 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY GHC7 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY GHC8 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY GHC9 DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY ICRA2022_F1Tenth_Track DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY Joydeepb-Driveway DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY Joydeepb-Home DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY LGRC_Parking DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY LGRC1 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY LGRC2 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY LGRC3 DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY Mit_ReadingRoom DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY NSH1 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY NSH2 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY NSH3 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY NSH4 DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY NSHA DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY NSHB DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY NYU19 DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY Obstacle_Hallway DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY orebro DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY resource DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY Slalom_Course DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY Social-Navigation DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY SXSW2024 DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY UT_AUTOmata_Track DESTINATION share/${PROJECT_NAME})

  install(DIRECTORY UT_Campus DESTINATION share/${PROJECT_NAME})

  ament_package()
else()
  message(FATAL_ERROR "Unknown ROS_VERSION ${ROS_VERSION}")
endif()

