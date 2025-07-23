
### Receiver
import json, zmq, rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoyNode(Node):
    def __init__(self):
        super().__init__("joy_bridge")
        ctx = zmq.Context()
        self.sub= ctx.socket(zmq.SUB)
        self.sub.connect("tcp://localhost:5556")
        self.sub.setsockopt_string(zmq.SUBSCRIBE, "")
        self.pub= self.create_publisher(Twist, "/joy_teleop/cmd_vel", 10)
        self.create_timer(0.001, self.tick)

        self.seq = 0

    def tick(self):
        try:
            tw = Twist()
            msg = self.sub.recv_json(flags=zmq.NOBLOCK)
            
            speed = 0.5
            if msg["buttons"][5]: speed = 1.0

            tw.linear.x = msg["axes"][1] * speed
            tw.angular.z = msg["axes"][3]

            self.pub.publish(tw)

        except zmq.Again:
            pass

def main():
    rclpy.init()
    rclpy.spin(JoyNode())

if __name__ == "__main__":
    main()
