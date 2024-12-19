import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(Int32, 'input_value', 10)
        self.timer = self.create_timer(2.0, self.publish_input)
        self.get_logger().info('Publisher Node is running...')

    def publish_input(self):
        try:
            user_input = int(input("Enter a number: "))
            msg = Int32()
            msg.data = user_input
            self.publisher_.publish(msg)
            self.get_logger().info(f'Published: {user_input}')
        except ValueError:
            self.get_logger().warn('Invalid input! Please enter an integer.')

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
