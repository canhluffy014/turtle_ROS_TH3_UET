#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math
Turtle_names = ["turtle1","turtle2"]
Turtle_poisitions = {"turtle1":None,"turtle2": None}
def pose_callback(data, turtle_name):
    Turtle_poisitions[turtle_name] = (data.x,data.y)
def get_distance():
    if None in Turtle_poisitions.values():
        return float("inf")
    x1,y1 = Turtle_poisitions["turtle1"]
    x2,y2 = Turtle_poisitions["turtle2"]
    return math.sqrt((x1-x2)**2+(y1-y2)**2)
def spawn_auto_move():
    rospy.init_node("spawn_auto_move")
    rospy.Subscriber("/turtle1/pose",Pose,pose_callback,"turtle1") 
    rospy.Subscriber("/turtle2/pose",Pose,pose_callback,"turtle2")
    pub1 = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    pub2 = rospy.Publisher("/turtle2/cmd_vel",Twist,queue_size=10)
    rate = rospy.Rate(10)
    Vel = Twist()
    while not rospy.is_shutdown():
        if get_distance() <0.3:
            Vel.linear.x = 0
            Vel.angular.z = 3.14
            pub1.publish(Vel)
            pub2.publish(Vel)
            rospy.sleep(1)
            Vel.linear.x = 2
            Vel.angular.z = 0.0
            pub1.publish(Vel)
            pub2.publish(Vel)
            rospy.sleep(1)
        if Turtle_poisitions["turtle1"] is not None:
            x, y = Turtle_poisitions["turtle1"]
            if x < 0.4 or x > 10.6 or y < 0.4 or y > 10.6:
                Vel.angular.z = 2.0
                Vel.linear.x = 2.0
            else:
                Vel.angular.z = 0.0
                Vel.linear.x = 2.0
            pub1.publish(Vel)
        if Turtle_poisitions["turtle2"] is not None:
            x, y = Turtle_poisitions["turtle2"]
            if x < 0.4 or x > 10.6 or y < 0.4 or y > 10.6:
                Vel.angular.z = 2.0
                Vel.linear.x = 2.0
            else:
                Vel.angular.z = 0.0
                Vel.linear.x = 2.0
            pub2.publish(Vel)
        rate.sleep()        
if __name__ == "__main__":
    spawn_auto_move()