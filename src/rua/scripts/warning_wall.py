#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
def call_back(msg):
    x = msg.x
    y = msg.y
    if x < 0.4 or x > 10.6 or y < 0.4 or y > 10.6:
        rospy.logwarn("Warning_Wall!!!!!!!")
if __name__=="__main__":
    rospy.init_node("Warning_Wall",anonymous=True)
    rospy.Subscriber("/turtle1/pose",Pose,call_back)
    rospy.spin()