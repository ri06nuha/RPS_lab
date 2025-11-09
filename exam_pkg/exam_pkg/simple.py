#!/usr/bin/env python3

#q2
import rclpy 
from rclpy.node import Node

class SimpleNode(Node):
    def __init__(self):
        super().__init__("simple_node") #node name
        self.create_timer(0.5, self.timer_callback) #(frequency, callback method)

    def timer_callback(self):    
        self.get_logger().info("Hi ROS2")

def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()

