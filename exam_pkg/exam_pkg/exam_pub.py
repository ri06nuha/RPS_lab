#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String

#q3
class Question3(Node):
    def __init__(self):
        super().__init__("exam_pub")
        self.publisher_ = self.create_publisher(String, '/exam_status', 10)
        self.timer_ = self.create_timer(0.5, self.msg_callback)
        self.get_logger().info("Exam publisher node active")

    def msg_callback(self):
        msg = String()
        msg.data = "Lab Exam in Progress"
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Question3()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
