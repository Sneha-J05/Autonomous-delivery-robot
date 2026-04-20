import rclpy
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator
import time

def create_goal(x, y):
    goal = PoseStamped()
    goal.header.frame_id = 'map'
    goal.pose.position.x = x
    goal.pose.position.y = y
    goal.pose.orientation.w = 1.0
    return goal

def main():
    rclpy.init()
    navigator = BasicNavigator()

    print("[INFO] Waiting for Nav2...")
    navigator.waitUntilNav2Active()

    goals = [
        (-3.86, 3.94),   # start room
        (0.0, 0.0),      # corridor
        (4.0, 2.0),      # target room
    ]

    for i, (x, y) in enumerate(goals):
        print(f"[INFO] Going to point {i+1}: ({x}, {y})")
        navigator.goToPose(create_goal(x, y))

        while not navigator.isTaskComplete():
            print("[INFO] Navigating...")
            time.sleep(1)

        print(f"[SUCCESS] Reached point {i+1}")

    print("[DONE] All goals completed!")
    rclpy.shutdown()

if __name__ == '__main__':
    main()
