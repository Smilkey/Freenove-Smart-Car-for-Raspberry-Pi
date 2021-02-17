#!/usr/bin/env python
"""
Created on Thu Nov 19 09:18:35 2020

@author: Marius & Martin
"""

import rospy
import actionlib
from wheeled_robot_rpi.msg import carAction
from dnn_rotate.srv import StringTrigger, StringTriggerRequest
from geometry_msgs.msg import Twist
from sub_echo_distance_class import ListenEcho

class ActionGoal(object):
    def __init__(self):
    
        self.ActionServer = actionlib.SimpleActionServer("/drive_as", carAction, self.goal_callback, False)
        self.cmd_vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)                                
        self.ActionServer.start()

        self.vel_msg = Twist()
        self.echo = ListenEcho()
        self.crash = self.CallService()

    def goal_callback(self, goal):
        running = True

        
        while running:
            
            if(goal.goal == "straight"):
                self.vel_msg.linear.x = 0.38
                self.cmd_vel_pub.publish(self.vel_msg)
                while self.echo._echoData.data > 25.0:
                    rospy.sleep(0.3)
                                                  
            if(goal.goal == "circle"):
                self.vel_msg.linear.x = 0.38
                self.vel_msg.angular.z = 1.0
                self.cmd_vel_pub.publish(self.vel_msg)
                while self.echo._echoData.data > 20.0:
                    rospy.sleep(0.3)
                 
            if(goal.goal == "watch out"):
                self.vel_msg.linear.x = 0.0
                self.cmd_vel_pub.publish(self.vel_msg)
                while self.echo._echoData.data > 25.0:
                    rospy.sleep(0.3)

            self.vel_msg.linear.x = 0.0
            self.cmd_vel_pub.publish(self.vel_msg)
            self.OpenRoad(self.CallService())
            
        self.vel_msg.linear.x = 0
        self.vel_msg.angular.z = 0
        self.cmd_vel_pub.publish(self.vel_msg)
        
################################################################################################################    
    def OpenRoad(self, crash_dir):
        
        if crash_dir.response == "Front":
            self.vel_msg.linear.x = -0.38
            self.vel_msg.angular.z = -0.8
            self.cmd_vel_pub.publish(self.vel_msg)
            rospy.sleep(1)
            self.vel_msg.angular.z = 0.0
            self.cmd_vel_pub.publish(self.vel_msg)
            
        elif crash_dir.response== "Left":
            self.vel_msg.angular.z = 0.8
            self.vel_msg.linear.x = -0.38
            self.cmd_vel_pub.publish(self.vel_msg)
            rospy.sleep(1)
            self.vel_msg.angular.z = 0.0
            self.cmd_vel_pub.publish(self.vel_msg)
            
        elif crash_dir.response== "Right":
            self.vel_msg.angular.z = -0.8
            self.vel_msg.linear.x = -0.38
            self.cmd_vel_pub.publish(self.vel_msg)
            rospy.sleep(1)
            self.vel_msg.angular.z = 0.0
            self.cmd_vel_pub.publish(self.vel_msg)
            
#################################################################################################################
    
       
    def CallService(self):
        rospy.wait_for_service("/crash_detection_service")
        self.service_side = rospy.ServiceProxy("/crash_detection_service", StringTrigger)
        self.request_obj = StringTriggerRequest()
        return self.service_side(self.request_obj)

            
    def Result(self):
        self.result = Twist()  


if __name__ == '__main__':
    rospy.init_node("move_car_action_server_node")
    action_goal = ActionGoal()
    rate = rospy.Rate(1)
    
    ctrl_c = False
    def shutdownhook():
        global ctrl_c
        print("The time for shutdown is....NOW!")
        ctrl_c = True
        
    rospy.on_shutdown(shutdownhook)
    
    while not ctrl_c:
        ag = action_goal.Result()
        rate.sleep()
    
    
    
    
    
    
    
    
    
    