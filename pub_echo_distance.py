#!/usr/bin/env python
"""
Created on Wed Nov 11 15:11:48 2020

@author: Martin
"""

import rospy
from std_msgs.msg import Float32
from mDev import *


rospy.init_node("echo_distance")
pub = rospy.Publisher("/echo_distance", Float32, queue_size = 1)

rate = rospy.Rate(10)                                           
distance = Float32()                                            

mdev = mDEV()                                                   

while not rospy.is_shutdown():                                  
  distance = mdev.getSonic()                                    
  pub.publish(distance)                  
  rate.sleep()                                                   

  
  
  
  
  
  
  
  
  
  
  
  
  
