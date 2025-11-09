#!/usr/bin/env python3

#q1
import rclpy 
from rclpy.node import Node
from std_msgs.msg import String 

class PublishingNode(Node):
   def __init__(self):
      super().__init__("exam_publish")
      self.robot_name_ = "C3P0"
      self.publisher_ = self.create_publisher(String, "/oop_status", 10)
      self.timer_ = self.create_timer(0.5, self.publish_exam)
      self.get_logger().info("Exam Publishing Node has started")

   def publish_exam(self):
      msg = String()
      msg.data = "Hi, this is "+str(self.robot_name_)+" from the exam station."
      self.publisher_.publish(msg)

def main(args=None):
      rclpy.init(args=args)
      node = PublishingNode()
      rclpy.spin(node)
      rclpy.shutdown()

if __name__=="__main__":
   main()