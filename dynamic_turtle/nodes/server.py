#!/usr/bin/env python
import rospy
from dynamic_reconfigure.server import Server
from dynamic_turtle.cfg import TutorialsConfig

def callback(config,level):
    rospy.loginfo("Config set to {int_param}, {double_param}, {str_param}, {bool_param}, {size}".format(**config))
    return config
if __name__=="__main__":
    
    rospy.init_node("dynamic_tutorials",anonymous=False)
    srv=Server(TutorialsConfig,callback)
    rospy.spin()