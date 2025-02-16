import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class LEDCommandSubscriber(Node):
    def __init__(self):
        super().__init__('led_command_subscriber')
        self.subscription = self.create_subscription(String, 'led_control', self.callback, 10)
        self.arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Remember to confirm port used by Arduino
        self.get_logger().info("LED Command Subscriber Node Started")

    def callback(self, msg):
        command = msg.data
        self.get_logger().info(f'Received Command: "{command}"')
        
        if command in ["ON", "OFF"]:
            self.arduino.write(command.encode())
            self.get_logger().info(f'Sent to Arduino: "{command}"')

def main(args=None):
    rclpy.init(args=args)
    node = LEDCommandSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()