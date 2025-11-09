# RPS_lab
Contains the workspace for Robot Programming and Simulation laboratory


## Pre-Setup Instructions
Ensure you have ROS2 and Gazebo setup in your system following the official documentation.

Further install the following ros2 packages:
- sudo apt-get install ros-humble-ros2-control
- sudo apt-get install ros-humble-ros2-controllers
- sudo apt-get install ros-humble-xacro
- sudo apt-get install ros-humble-*-ros2-control
- sudo apt-get install ros-humble-joint-state-publisher-gui
- sudo apt-get install ros-humble-turtlesim
- sudo apt-get install ros-humble-robot-localization
- sudo apt-get install ros-humble-joy
- sudo apt-get install ros-humble-joy-teleop
- sudo apt-get install ros-humble-tf-transformations
- sudo apt-get install ros-humble-plotjuggler
- sudo apt-get install ros-humble-plotjuggler-ros
---
## Setup Instructions

1. Clone the repository in a folder
```bash
git clone https://github.com/ri06nuha/RPS_lab.git
cd <folder_name>
```

2. Build the workspace
```bash
colcon build
```

3. Source the setup script
```bash
. install/setup.bash
```
---

## Commands to run
- ros2 run <pkg_name> <node_name as defined in setup.py>
- ros2 launch <pkg_name> <launch_file_name>

To make the robot move in a straight line/circle, run the following the command by modifying it with the appropriate linear and angular values (for straight line linear x:0.5, for circle linear x:0.5, angular z:0.5):
```
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "linear:
  x: 0.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0"
```
