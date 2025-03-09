#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from th3.srv import goToGoal,goToGoalResponse
import math
current_pose = Pose()
def pose_call_back(msg):
    global current_pose 
    current_pose = msg
def handle_go_to_goal(req):
    global current_pose
    pub =rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    if current_pose is None:
        return goToGoalResponse(False)
    rate = rospy.Rate(10)
    vel_msg = Twist()
    while not rospy.is_shutdown():
        dx = req.x - current_pose.x
        dy = req.y - current_pose.y
        dist = math.sqrt(dx**2+dy**2)
        if dist < 0.1 :
            vel_msg.linear.x = 0
            vel_msg.angular.z = 0
            pub.publish(vel_msg)
            return goToGoalResponse(True)
        angle_goal = math.atan2(dy,dx)
        angle_err = math.atan2(math.sin(angle_goal - current_pose.theta), 
                       math.cos(angle_goal - current_pose.theta))
        vel_msg.linear.x = min(2,dist)
        vel_msg.angular.z = min(2,max(-2,angle_err))
        pub.publish(vel_msg)
        rate.sleep()
def go_to_goal_server():
    rospy.init_node("go_to_goal_server",anonymous=True)
    rospy.Subscriber("/turtle1/pose",Pose,pose_call_back)
    rospy.Service("go_to_goal",goToGoal,handle_go_to_goal)
    rospy.loginfo("server go to goal ready!!!!")
    rospy.spin()
if __name__=="__main__":
    go_to_goal_server()
    
