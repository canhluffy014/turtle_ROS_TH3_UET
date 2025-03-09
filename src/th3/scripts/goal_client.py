#!/usr/bin/env python3
import rospy
from th3.srv import goToGoal

def go_to_goal_client(x,y):
    rospy.wait_for_service("go_to_goal")
    try:
        proxy = rospy.ServiceProxy("go_to_goal",goToGoal)
        s = proxy(x,y)
        return s.success
    except rospy.ServiceException as e:
        rospy.loginfo("Service bao loi!!")
        return False
if __name__ == "__main__":
    rospy.init_node("go_to_goal_client")
    x = float(input("nhap toa do x:  "))
    y = float(input("nhap toa do y:  "))
    success = go_to_goal_client(x, y)
    if success:
        rospy.loginfo("Rua da den noi!!")
    else:
        rospy.loginfo("Rua khong the den dich!!")