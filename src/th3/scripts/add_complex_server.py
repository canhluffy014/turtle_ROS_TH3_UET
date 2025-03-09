#!/usr/bin/env python3
import rospy
from th3.srv import addComplex,addComplexResponse
from th3.msg import complex

def handle_add_complex(req):
    output = complex()
    output.re = req.input1.re + req.input2.re
    output.im = req.input1.im + req.input2.im
    rospy.loginfo("(%.2f + %.2fi) + (%.2f + %.2fi) = (%.2f + %.2fi) ",req.input1.re,req.input1.im,req.input2.re,req.input2.im,output.re,output.im)
    return addComplexResponse(output) 
def add_complex_sever():
    rospy.init_node("add_complex_server",anonymous=True)
    s = rospy.Service("add_complex",addComplex,handle_add_complex)
    rospy.loginfo("server ready!!!!!")
    rospy.spin()
if __name__=="__main__":
    add_complex_sever()