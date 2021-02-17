#!/usr/bin/env python
"""
Created on Wed Nov 11 11:47:26 2020

@author: Martin
"""

import rospy
from mDev import *
from geometry_msgs.msg import Twist

mdev = mDEV()                      

def CmdVel_callback(msg):          
  x = msg.linear.x*1000               
  z =(((-msg.angular.z)+1)*80)+10  
  mdev.move(x, x, z)               
  print ("Motor speed: ", x, "Turn angle: ", z) 
    
rospy.init_node("cmd_vel_subscriber_node")                  
sub = rospy.Subscriber("/cmd_vel", Twist, CmdVel_callback)                                                           
rospy.spin()                                               

