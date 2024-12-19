import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.subscription = self.create_subscription(Int32, 'input_value', self.listener_callback, 10)
        self.get_logger().info('Subscriber Node is running...')

    def listener_callback(self, msg):
        value = msg.data
        self.get_logger().info(f'Received value: {value}. Printing "Hello World" {value} times.')
        for i in range(value):
            print(f"Hello World {i + 1}")

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
