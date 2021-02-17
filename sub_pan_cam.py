#!/usr/bin/env python
"""
Created on Wed Nov 11 22:08:47 2020

@author: Martin
"""

import rospy
from mDev import *
from std_msgs.msg import Float32


mdev = mDEV()                                         

def pan_callback(msg):                                 
  angel = ((-msg.data+1)*90)+5                         
  mdev.setServo("2", angel)                                               


rospy.init_node("cam_pan_subscriber")
sub = rospy.Subscriber("/cam_pan", Float32, pan_callback)
rospy.spin()