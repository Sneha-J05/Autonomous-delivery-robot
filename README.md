# Autonomous Delivery Robot

A ROS2-based autonomous indoor delivery robot capable of mapping, localization, and goal-based navigation in a simulated environment.

---

## Project Overview

This project implements a fully autonomous delivery robot that navigates between rooms in an indoor environment without human intervention. The robot builds a map of its surroundings, estimates its own position, and plans safe paths to target delivery locations — all within a Gazebo simulation.

**Course:** Mobile and Autonomous Robots (UE23CS343BB7)  

---

## Problem Statement

Autonomous robots are increasingly used in indoor environments such as hospitals, warehouses, and offices for performing tasks like delivery, monitoring, and assistance. This project addresses the challenge of enabling a robot to navigate autonomously in an unknown environment while avoiding obstacles.

The robot must be capable of:
- Mapping its surroundings
- Determining its position within that map
- Planning a safe and efficient path to target locations
- Adapting to new delivery goals in real time

---

## Objectives

- Design and implement an autonomous mobile robot capable of indoor navigation
- Generate a map of an unknown environment using SLAM
- Enable accurate robot localization within the environment
- Perform goal-based navigation between different rooms
- Automate delivery tasks using a Python script

---

## Methodology

### 1. Environment Setup
A virtual indoor environment was created in Gazebo, consisting of rooms, walls, and obstacles. The TurtleBot was spawned at a defined starting position, and sensor plugins (LiDAR and wheel odometry) were verified.

### 2. Mapping (SLAM)
The robot was manually controlled via teleoperation to explore the environment. SLAM Toolbox was used to construct a real-time occupancy grid map by fusing LiDAR scans with odometry data. The final map was saved in image and YAML formats.

### 3. Localization (AMCL)
An initial pose estimate was provided through RViz to seed the particle filter. The robot was moved briefly to allow particle convergence, enabling accurate position estimation on the saved map.

### 4. Navigation (Nav2)
The Nav2 framework planned globally optimal paths and executed smooth, obstacle-aware motion control. The robot dynamically adjusted its trajectory based on real-time sensor data.

### 5. Automation
A Python script automated the delivery process by sending goal coordinates to the Nav2 action server, completing the fully autonomous pipeline from map loading to goal execution.

---

## Key Algorithms

### SLAM (Simultaneous Localization and Mapping)
- **Tool:** SLAM Toolbox
- **Function:** Constructs an occupancy grid map while tracking the robot's position
- **Technique:** LiDAR data fusion with loop closure for improved accuracy

### AMCL (Adaptive Monte Carlo Localization)
- **Method:** Particle filter-based localization
- **Function:** Maintains multiple pose hypotheses (particles) that converge to the robot's actual position
- **Advantage:** Robust localization even under sensor noise

### Nav2 Navigation Stack
- **Function:** Global and local path planning with obstacle avoidance
- **Features:** Dynamic replanning, smooth trajectory execution, costmap-based navigation

---

## Tools and Technologies

**Software:**
- ROS2 – Middleware for robot communication
- Python – Scripting and automation
- RViz – Visualization and debugging
- Gazebo – Simulation environment

**Libraries/Frameworks:**
- Nav2 – Navigation framework
- SLAM Toolbox – Mapping
- AMCL – Localization

**Sensors (Simulated):**
- LiDAR – Obstacle detection and mapping
- Wheel Odometry – Motion tracking

---

## Results

### Key Achievements
- Successfully generated an accurate map using SLAM
- Achieved stable localization using AMCL particle filter
- Navigated between multiple rooms with obstacle avoidance
- Automated delivery tasks via Python script
- Demonstrated dynamic replanning when delivery targets changed mid-session


---



## Future Work

- Extend to dynamic environments with moving obstacles
- Implement multi-robot coordination for collaborative delivery
- Deploy on real TurtleBot hardware
- Integrate task scheduling layer for priority-based deliveries
- Add elevator navigation for multi-floor delivery scenarios

---

## Conclusion

This project successfully demonstrated an autonomous indoor delivery robot using ROS2. The integration of SLAM, AMCL, and Nav2 created a robust navigation system capable of real-time decision-making and path planning. The modular ROS2 architecture enabled independent development and testing of each component, resulting in a maintainable and scalable solution.

The simulation-first approach in Gazebo allowed rapid iteration and validation, providing a strong foundation for future deployment in real-world applications such as warehouse automation, hospital logistics, and service robotics.

---

