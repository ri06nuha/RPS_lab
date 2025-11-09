#!/usr/bin/env python3

#q2 requiring 0.5 hz 
import rclpy 
from rclpy.node import Node

class SimpleNode(Node):
    def __init__(self):
        super().__init__("simple_node") #node name
        freq = 0.5
        timer_period = 1/freq
        self.create_timer(timer_period, self.timer_callback) #(frequency, callback method)

    def timer_callback(self):    
        self.get_logger().info("Hi ROS2")

def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()

