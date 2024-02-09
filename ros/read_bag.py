#!/usr/bin/env python3

import rospy
import rosbag



rospy.init_node('read_bag')

bag = rosbag.Bag('/home/elyas/catkin_ws_el/src/pub_sub/bag/test')

for topic, msg, t in bag.read_message(topics ='/sam'):
    if topic == '/sam':
        print("sam's data is:")
        print(msg.data)
        print('and it was recorded at:')
        print(t)