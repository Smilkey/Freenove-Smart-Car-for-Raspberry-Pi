#!/usr/bin/env python
"""
Created on Wed Nov 18 13:03:46 2020

@author: Martin
"""

import rospy
from std_msgs.msg import Float32
from dnn_rotate.srv import StringTrigger, StringTriggerResponse
import time


class CrashDetectService(object):
    def __init__(self, srv_name = "/crash_detection_service"):
        self.srv_name = srv_name
        self.service_server = rospy.Service(self.srv_name, StringTrigger, self.crash_callback)
        self.echo_distance_sub = rospy.Subscriber("/echo_distance", Float32, self.echo_distance_callback)
        self.cam_pan_pub = rospy.Publisher("/cam_pan", Float32, queue_size = 1)
        
        self.echo_type = Float32()
        self.turn = Float32()

        
    def crash_callback(self, msg):
        message = self.echo_type
        response = StringTriggerResponse()
        self.turn_right()
        self.turn_left()
        self.turn_front()
        response.response = (self.crash_detected()) 
        return response
     
    def echo_distance_callback(self, msg):
        self.echo_type = msg
    
    def turn_front(self):
        self.turn = 0.0
        print("Distance front: ")
        self.cam_pan_pub.publish(self.turn)
        time.sleep(1)
        self.front = self.echo_type
        print(self.echo_type)
        
    def turn_right(self):
        self.turn = 1.0
        print("Distance right: ")
        self.cam_pan_pub.publish(self.turn)
        time.sleep(1)
        self.right = self.echo_type
        print(self.echo_type)
        
    def turn_left(self):
        self.turn = -1.0
        print("Distance left: ")
        self.cam_pan_pub.publish(self.turn)
        time.sleep(1)
        self.left = self.echo_type
        print(self.echo_type)

    def crash_detected(self):
        if(self.front.data < self.right.data and self.left.data > self.front.data):
            print("Potential crash straight ahead")
            return "Front"
        if(self.right.data < self.front.data and self.left.data > self.right.data):
            print("Potential crash detected right side")
            return "Right"
        if(self.left.data < self.front.data and self.right.data > self.left.data):
            print("Potential crash detected left side")
            return "Left"
            
                        
if __name__ == "__main__":
    rospy.init_node("crash_detection_service_node")
    subscriberObject = CrashDetectService()
    time.sleep(1)   
    rospy.spin()
    
    
    


