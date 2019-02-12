#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " I heard %s", data.data)

def listener():
    rospy.init_node('led_handler')
    rospy.loginfo(rospy.get_caller_id() + " started")
    rospy.Subscriber('toggle_led', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
