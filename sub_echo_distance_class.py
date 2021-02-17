#!/usr/bin/env python
"""
Created on Fri Nov 13 12:24:37 2020

@author: Martin
"""

import rospy
from mDev import *
from std_msgs.msg import Float32


class ListenEcho (object):
  def __init__(self):
    self._sub = rospy.Subscriber("/echo_distance", Float32, self.echo_callback)
    self._echoData = Float32()
    
    
  def echo_callback(self, msg):
    self._echoData = msg        
    
  def get_echoData(self):
    return self._echoData
    
if __name__ == "__main__":
  rospy.init_node("echo_distance_subscriber", log_level = rospy.INFO)
  listen_echo_object = ListenEcho()
  rate = rospy.Rate(1)
  
  ctrl_c = False
  def shutdownhook():
    global ctrl_c
    print("The time for shutdown is...NOW!")
    ctrl_c = True
    
  rospy.on_shutdown(shutdownhook)
  
  while not ctrl_c:
    data = listen_echo_object.get_echoData()
    rate.sleep