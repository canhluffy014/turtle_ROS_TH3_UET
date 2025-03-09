#!/usr/bin/env python3
import rospy
from th3.srv import addComplex
from th3.msg import complex
def add_complex_client(re1,im1,re2,im2):
    rospy.wait_for_service("add_complex")
    try:
        add_complex = rospy.ServiceProxy("add_complex",addComplex)
        input1 = complex(re = re1, im = im1)
        input2 = complex(re = re2, im = im2)
        s = add_complex(input1,input2)
        rospy.loginfo("ket qua la: %.2f + %.2fi",s.output.re,s.output.im)
        return s
    except rospy.ServiceException as e:
        rospy.loginfo("Service call fail: %s",e)
if __name__ == "__main__":
    rospy.init_node("add_complex_client")
    re1 = float(input("re1: "))
    im1 = float(input("im1: "))
    re2 = float(input("re2: "))
    im2 = float(input("im2: "))
    add_complex_client(re1, im1, re2, im2)