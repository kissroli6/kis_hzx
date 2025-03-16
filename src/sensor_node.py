import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random
import time

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        self.heart_rate_publisher = self.create_publisher(Float32, 'heart_rate', 10)
        self.oxygen_level_publisher = self.create_publisher(Float32, 'oxygen_level', 10)
        self.timer = self.create_timer(1.0, self.publish_sensor_data)

    def publish_sensor_data(self):
        heart_rate = random.uniform(60.0, 100.0)
        oxygen_level = random.uniform(95.0, 100.0)
        self.heart_rate_publisher.publish(Float32(data=heart_rate))
        self.oxygen_level_publisher.publish(Float32(data=oxygen_level))
        self.get_logger().info(f'Heart Rate: {heart_rate}, Oxygen Level: {oxygen_level}')

def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
