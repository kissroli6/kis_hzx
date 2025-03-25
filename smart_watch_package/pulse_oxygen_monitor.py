import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import Float32

class SmartWatchNode(Node):
    def __init__(self):
        super().__init__('smart_watch_node')
        
        self.pulse_publisher = self.create_publisher(Float32, 'pulse_topic', 10)
        self.oxygen_publisher = self.create_publisher(Float32, 'oxygen_topic', 10)

        self.timer = self.create_timer(4.0, self.publish_data)

    def publish_data(self):
        pulse_rate = random.randint(50, 120)
        oxygen_level = random.randint(85, 100)

        pulse_msg = Float32()
        pulse_msg.data = float(pulse_rate)

        oxygen_msg = Float32()
        oxygen_msg.data = float(oxygen_level)

        self.pulse_publisher.publish(pulse_msg)
        self.oxygen_publisher.publish(oxygen_msg)

        self.check_values(pulse_rate, oxygen_level)

    def check_values(self, pulse_rate, oxygen_level):
        if pulse_rate < 60:
            self.get_logger().warn(f"Figyelmeztetés! A pulzus értéked ({pulse_rate} bpm) túl alacsony!")
        elif pulse_rate > 100:
            self.get_logger().warn(f"Figyelmeztetés! A pulzus értéked ({pulse_rate} bpm) túl magas!")
        else:
            self.get_logger().info(f"Pulzus: {pulse_rate} bpm - Minden rendben.")

        if oxygen_level < 90:
            self.get_logger().warn(f"Figyelmeztetés! A véroxigén szinted ({oxygen_level}%) alacsony!")
        else:
            self.get_logger().info(f"Véroxigén szint: {oxygen_level}% - Minden rendben.")

def main(args=None):
    rclpy.init(args=args)

    node = SmartWatchNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

