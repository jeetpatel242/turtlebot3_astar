# Project 3 - Phase 3
## Part-2

# Implementation of A* algorithm on a differential drive (non-holonomic) TurtleBot robot - ROS+Gazebo

## Overview


## Installing Dependencies
This program works on a device running Ubuntu 18.04 and ROS Melodic.

To install ROS Melodic in Ubuntu 18.04, follow the steps in this [link](http://wiki.ros.org/melodic/Installation/Ubuntu).

To install catkin, follow the installation steps in this [link](http://wiki.ros.org/catkin).

## How to build
Open a terminal window and run the following commands

```
mkdir -p ~/turtlebot3_ws/src
cd ~/turtlebot3_ws
catkin_make
source devel/setup.bash
cd src
git clone https://github.com/jeetpatel242/Turtlebot3-Astar-ROS

cd ..
catkin_make
```
(Alternatively, copy the turtlebot3_astar package into the 'turtlebot3_ws/src' directory and write 'catkin_make' in terminal)

## How to run Simulation
Open a terminal window and run the following commands

```
cd ~/catkin_ws
source devel/setup.bash
roslaunch turtlebot3_astar turtlebot3_gazebo_astar.launch x_pos:=-4 y_pos:=-4

```
This launches the gazebo environment. In the same terminal, program will ask the user for following inputs:
* Clearance (in meters) from the obstacles, provide input in 'float' format. For eg: 0.2.
* Choose the initial position, provide input in [x,y,theta] format. For eg: [1, 1, 0]
* Choose the goal position, provide input in [x,y] format. For eg. [9, 9]
* Enter the two RPM's for the wheels, provide input in [rpm1,rpm2] format, For eg: [6,4]
* Turtlebot will follow the planned path from start to goal avoiding the obstacles.

## Maintainers ##
### Group-10

Jeet Patel (jeetpatel242@gmail.com)

Mrugesh Shah (mrugesh.shah92@gmail.com)




