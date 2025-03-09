#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
current_msg = Pose()
def pose_callback(msg):
    global current_msg 
    current_msg = msg
if __name__=="__main__":
    rospy.init_node("auto_move",anonymous=True)
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    rospy.Subscriber("/turtle1/pose",Pose,pose_callback)
    rate = rospy.Rate(10)
    time_start = rospy.Time.now()
    while rospy.Time.now() - time_start < rospy.Duration(10000):
        
        vel = Twist()
        
        if current_msg.x < 0.4 or current_msg.x > 10.6 or current_msg.y < 0.4 or current_msg.y > 10.6:
            vel.angular.z = 2.0
            vel.linear.x = 2.0
        else:
            vel.angular.z = 0.0
            vel.linear.x = 2.0
        pub.publish(vel)
        rate.sleep()
