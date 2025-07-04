# AMRL Maps

Map files used by UT-AMRL projects.

## Dependencies

[ROS](http://wiki.ros.org/ROS/Installation)

## Usage

1. Clone this repository.
2. **For ROS1**: Add the path to your `~/.bashrc` file for the `ROS_PACKAGE_PATH` environment variable:
    ```bash
    echo "export ROS_PACKAGE_PATH=$(pwd):\$ROS_PACKAGE_PATH" >> ~/.bashrc
    source ~/.bashrc
    ```
3. **For ROS2**: Add the path to your `~/.bashrc` file for the `AMENT_PREFIX_PATH` environment variable:
    ```bash
    echo "export AMENT_PREFIX_PATH=$(pwd)/install:\$AMENT_PREFIX_PATH" >> ~/.bashrc
    source ~/.bashrc
    ```
4. Run `make`. This will automatically build and install (for ROS2) or just work directly (for ROS1). No need to run `catkin_*`, `rosbuild`, etc.

## Updating and Creating Maps

Maps are created with the [vector_display](https://github.com/ut-amrl/vector_display) package.

### Creating Racing Lines
Racing lines are represented as text files noted with the `.racingline` extension.
Each line in the text file represents a point on the racing line and some information about the line segment immediately following that point.
The format is as follows:
```
<node_x> <node_y> <segment_max_speed> <segment_angular_velocity_factor> <segment_acceleration_factor> <segment_deceleration_factor>
```
