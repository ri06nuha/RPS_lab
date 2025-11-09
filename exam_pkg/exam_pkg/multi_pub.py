#!/usr/bin/env python3

#q1
import rclpy 
from rclpy.node import Node
from std_msgs.msg import String, Int32

#q5
class Publishing2Node(Node):
   def __init__(self):
      super().__init__("exam_publish")
      self.robot_name_ = "C3P0"
      self.counter=0
      self.publisher1_ = self.create_publisher(String, "/exam_text", 10)
      self.publisher2_ = self.create_publisher(Int32, "/exam_number", 10)
      self.timer_ = self.create_timer(0.5, self.publish_exam)
      self.get_logger().info("Exam Publishing Node has started")

   def publish_exam(self):
      msg1 = String()
      msg1.data = "Hi, this is "+str(self.robot_name_)+" from the exam station."
      self.publisher1_.publish(msg1)

      msg2 = Int32()
      self.counter +=1
      msg2.data = self.counter
      self.publisher2_.publish(msg2)

def main(args=None):
      rclpy.init(args=args)
      node = Publishing2Node()
      rclpy.spin(node)
      rclpy.shutdown()

if __name__=="__main__":
   main()