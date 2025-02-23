import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Joy  # Import Joy message

class GearCommandPublisher(Node):
    def __init__(self):
        super().__init__('gear_command_publisher')
        self.publisher_ = self.create_publisher(String, 'gear_control', 10)
        self.state_publisher_ = self.create_publisher(String, 'gear_state', 10)  # topic for public gear state
        self.subscription = self.create_subscription(Joy, 'joy', self.joy_callback, 10)
        
        self.current_gear = "1"  # Default to Forward
        self.previous_lb_state = False  # Track previous state of LB button
        self.get_logger().info('Xbox Controller Gear Control Initialized')
        
        # Publish initial gear state
        self.publish_gear()

    def joy_callback(self, msg):
        lb_pressed = msg.buttons[4] == 1  # LB button index in Joy message
        
        if lb_pressed and not self.previous_lb_state:
            # Toggle gear when LB is pressed
            self.current_gear = "2" if self.current_gear == "1" else "1"
            self.publish_gear()
        
        self.previous_lb_state = lb_pressed  # Update state tracking

    def publish_gear(self):
        msg = String()
        msg.data = self.current_gear
        self.publisher_.publish(msg)
        self.state_publisher_.publish(msg)  # Publish to gear_state as well
        self.get_logger().info(f'Published Gear Command: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = GearCommandPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
