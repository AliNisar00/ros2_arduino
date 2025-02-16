import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class LEDCommandPublisher(Node):
    def __init__(self):
        super().__init__('led_command_publisher')
        self.publisher_ = self.create_publisher(String, 'led_control', 10)

    def send_command(self, command):
        msg = String()
        msg.data = command
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = LEDCommandPublisher()

    while rclpy.ok():
        command = input("Enter 'ON' to turn LED on, 'OFF' to turn LED off: ").strip().upper()
        if command in ["ON", "OFF"]:
            node.send_command(command)
        else:
            print("Invalid command. Enter 'ON' or 'OFF'.")

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()