import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class GearCommandSubscriber(Node):
    def __init__(self):
        super().__init__('gear_command_subscriber')
        self.subscription = self.create_subscription(String, 'gear_control', self.callback, 10)

        try:
            self.arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Confirm Arduino port before running
            self.get_logger().info("Connected to Arduino on /dev/ttyUSB0")
        except serial.SerialException:
            self.get_logger().error("Failed to connect to Arduino. Check the port.")
            self.arduino = None

    def callback(self, msg):
        command = msg.data
        self.get_logger().info(f'Received Command: "{command}"')

        if self.arduino and command in ["0", "1", "2"]:
            self.arduino.write(command.encode())  # Send character to Arduino
            self.get_logger().info(f'Sent to Arduino: "{command}"')

def main(args=None):
    rclpy.init(args=args)
    node = GearCommandSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
