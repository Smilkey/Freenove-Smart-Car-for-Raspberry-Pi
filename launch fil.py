<launch>
  <node pkg="wheeled_robot_rpi" type="pub_echo_distance.py" name="echo_distance" output="screen">
  </node>
  <node pkg="wheeled_robot_rpi" type="service_crash_detection.py" name="crash_detection_service_node" output="screen">
  </node>
  <node pkg="wheeled_robot_rpi" type="sub_pan_cam.py" name="cam_pan_subscriber" output="screen">
  </node>
  <node pkg="wheeled_robot_rpi" type="sub_cmd_vel.py" name="cmd_vel_subscriber_node" output="screen">
  </node>
  <node pkg="wheeled_robot_rpi" type="action_server.py" name="move_car_action_server_node" output="screen">
  </node>
  <node pkg="wheeled_robot_rpi" type="sub_echo_distance_class.py" name="echo_distance_subscriber" output="screen">
  </node>
</launch>