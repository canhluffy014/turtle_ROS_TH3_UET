#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import curses

def control(stdscr):
    rospy.init_node("keyboard_control")
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    vel = Twist()
    rate = rospy.Rate(10)
    stdscr.nodelay(True)
    while not rospy.is_shutdown():
        key = stdscr.getch()
        if key == ord("w"):
            
            vel.linear.x = 2.0
            vel.angular.z = 0.0
        elif key == ord("s"):
            
            vel.linear.x = -2.0
            vel.angular.z = 0.0
        elif key == ord("a"):
           vel.linear.x = 0.0
           vel.angular.z = 2.0
        elif key == ord("d"):
            vel.linear.x = 0.0
            vel.angular.z = -2.0
        elif key == ord("q"):
            break
        else:
            vel.linear.x = 0.0
            vel.angular.z = 0.0
        pub.publish(vel)
        rate.sleep()
if __name__ == "__main__":
    curses.wrapper(control)

