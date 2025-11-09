#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String

#q3
class Question3(Node):
    def __init__(self):
        super().__init__("exam_pub") #gives the node its name
        self.publisher_ = self.create_publisher(String, '/exam_status', 10) #message_type, topic_name, queue_size 
        self.timer_ = self.create_timer(0.5, self.msg_callback) #time_in_seconds, callback
        self.get_logger().info("Exam publisher node active")

    def msg_callback(self):
        """creates the message to be published"""
        msg = String()
        msg.data = "Lab Exam in Progress"
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Question3()
    rclpy.spin(node) #call the callbacks continuously
    rclpy.shutdown() 

if __name__ == '__main__':
    main()
