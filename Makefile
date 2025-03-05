SHELL = /bin/bash

# Check if we have a ROS1 (rosbuild) environment:
CHECK_ROS1 = $(shell if [ -n "$$ROS_ROOT" ] && [ -f "$$ROS_ROOT/core/rosbuild/rosbuild.cmake" ]; then echo 1; else echo 0; fi)

# Choose a CMake build type if needed (e.g., Release or Debug)
build_type = Release

.SILENT:

all: build/CMakeLists.txt.copy
	if [ "$(CHECK_ROS1)" = "1" ]; then \
	  echo "Detected ROS1 (rosbuild). Nothing to build for static data. Using ROS_PACKAGE_PATH."; \
	else \
	  echo "Detected ROS2 (ament). Running make in build/ ..."; \
	  $(MAKE) --no-print-directory -C build; \
	fi

clean:
	rm -rf build install

install: build/CMakeLists.txt.copy
	if [ "$(CHECK_ROS1)" = "1" ]; then \
	  echo "Detected ROS1 (rosbuild). 'make install' not needed. Just rely on ROS_PACKAGE_PATH."; \
	else \
	  echo "Detected ROS2 (ament). Installing to ./install ..."; \
	  $(MAKE) --no-print-directory -C build install; \
	fi

# Configure step: run cmake in the build directory, only for ROS2
build/CMakeLists.txt.copy: build CMakeLists.txt package.xml
	if [ "$(CHECK_ROS1)" = "1" ]; then \
	  echo "Detected ROS1 (rosbuild). Skipping CMake configuration (no-op for static files)."; \
	else \
	  echo "Detected ROS2 (ament). Configuring with CMake..."; \
	  cd build && cmake -DCMAKE_BUILD_TYPE=$(build_type) \
	                    -DCMAKE_INSTALL_PREFIX="$(shell pwd)/install" \
	                    ..; \
	  cp ../CMakeLists.txt CMakeLists.txt.copy; \
	fi

build:
	mkdir -p build
