#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math
import random


if __name__== "__main__" :
    rospy.init_node("random_move")
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        vel = Twist()
        vel.linear.x = random.uniform(0,2)
        vel.linear.y = random.uniform(0,2)
        vel.angular.z = random.uniform(-2,2)
        pub.publish(vel)
        rate.sleep()
    
