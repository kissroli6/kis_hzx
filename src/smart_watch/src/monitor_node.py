import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

class MonitorNode(Node):
    def __init__(self):
        super().__init__('monitor_node')
        self.heart_rate_subscription = self.create_subscription(
            Float32,
            'heart_rate',
            self.heart_rate_callback,
            10
        )
        self.oxygen_level_subscription = self.create_subscription(
            Float32,
            'oxygen_level',
            self.oxygen_level_callback,
            10
        )
        self.alert_publisher = self.create_publisher(String, 'alert', 10)

    def heart_rate_callback(self, msg):
        if msg.data < 60.0 or msg.data > 100.0:
            self.publish_alert(f'Abnormal heart rate detected: {msg.data}')

    def oxygen_level_callback(self, msg):
        if msg.data < 95.0 or msg.data > 100.0:
            self.publish_alert(f'Abnormal oxygen level detected: {msg.data}')

    def publish_alert(self, alert_msg):
        self.alert_publisher.publish(String(data=alert_msg))
        self.get_logger().info(alert_msg)

def main(args=None):
    rclpy.init(args=args)
    node = MonitorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
