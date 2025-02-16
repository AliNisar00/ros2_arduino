import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class GearCommandPublisher(Node):
    def __init__(self):
        super().__init__('gear_command_publisher')
        self.publisher_ = self.create_publisher(String, 'gear_control', 10)

    def send_command(self, command):
        msg = String()
        msg.data = command
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = GearCommandPublisher()

    while rclpy.ok():
        command = input("Enter '0' (Neutral - All OFF), '1' (Forward - D4 ON, D7 OFF), '2' (Reverse - D7 ON, D4 OFF): ").strip()
        if command in ["0", "1", "2"]:
            node.send_command(command)
        else:
            print("Invalid command. Enter '0', '1', or '2'.")

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
