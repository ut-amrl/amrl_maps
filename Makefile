SHELL = /bin/bash

# Use the same detection logic as CMakeLists.txt
ROS_VERSION := $(shell echo $$ROS_VERSION)

#acceptable build_types: Release/Debug/Profile
build_type=Release
# build_type=Debug

.SILENT:

all: build-only install

# Install target - handles ROS version differences
install: build/CMakeLists.txt.copy
	if [ "$(ROS_VERSION)" = "1" ]; then \
	  echo "ROS1 detected, no install needed (use ROS_PACKAGE_PATH)"; \
	elif [ "$(ROS_VERSION)" = "2" ]; then \
	  echo "ROS2 detected, installing to ./install ..."; \
	  $(MAKE) --no-print-directory -C build install; \
	else \
	  echo "Warning: ROS_VERSION not set, assuming ROS2"; \
	  $(MAKE) --no-print-directory -C build install; \
	fi

# Build-only target (no install)
build-only: build build/CMakeLists.txt.copy
	$(info Build_type is [${build_type}])
	if [ "$(ROS_VERSION)" = "1" ]; then \
	  echo "ROS1 detected, nothing to build for static data"; \
	else \
	  $(MAKE) --no-print-directory -C build; \
	fi

clean:
	rm -rf build install

build/CMakeLists.txt.copy: build CMakeLists.txt package.xml
	cd build && cmake -DCMAKE_BUILD_TYPE=$(build_type) -DCMAKE_INSTALL_PREFIX=../install ..
	cp CMakeLists.txt build/CMakeLists.txt.copy

build:
	mkdir -p build 