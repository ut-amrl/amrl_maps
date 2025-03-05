# AMRL Maps

Map files used by UT-AMRL projects.

## Dependencies

[ROS](http://wiki.ros.org/ROS/Installation)

## Usage

1. Clone this repository.

### ROS1 Usage

2. Add it to your `ROS_PACKAGE_PATH` environment variable:
    ```
    export ROS_PACKAGE_PATH=`pwd`:$ROS_PACKAGE_PATH
    ```
    (Optional, reccomended) Add this to your `.bashrc`

### ROS2 Usage
2. Build and install the package
```
make 
make install
```

3. Add it to your `AMENT_PREFIX_PATH` environment variable: 
    ```
    export AMENT_PREFIX_PATH="$(pwd)/install:$AMENT_PREFIX_PATH"
    ```
    (Optional, reccomended) Add this to your `.bashrc`

## Updating and Creating Maps

Maps are created with the [vector_display](https://github.com/ut-amrl/vector_display) package.

### Creating Racing Lines
Racing lines are represented as text files noted with the `.racingline` extension.
Each line in the text file represents a point on the racing line and some information about the line segment immediately following that point.
The format is as follows
```
<node_x> <node_y> <segment_max_speed> <segment_angular_velocity_factor> <segment_acceleration_factor> <segment_deceleration_factor>
```
