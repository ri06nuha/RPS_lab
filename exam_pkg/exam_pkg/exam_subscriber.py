#!/usr/bin/env python3 

import rclpy
from rclpy.node import Node
from std_msgs.msg import String 

class ExamSub(Node):
    def __init__(self):
        super().__init__("exam_sub")
        self.subscriber_ = self.create_subscription(String, "/oop_status", self.callback_exam, 10)
        self.get_logger().info("Exam subscriber started")
    
    def callback_exam(self,msg):
        self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = ExamSub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()