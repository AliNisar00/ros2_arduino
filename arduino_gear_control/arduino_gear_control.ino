// Define the pins
const int pinD7 = 7;  // Pin D7
const int pinD4 = 4;  // Pin D4

// Variable to store the incoming character
char command;

void setup() {
  // Set the pins as outputs
  pinMode(pinD7, OUTPUT);
  pinMode(pinD4, OUTPUT);

  // Ensure both pins start off
  digitalWrite(pinD7, LOW);
  digitalWrite(pinD4, LOW);

  // Initialize serial communication
  Serial.begin(9600);
}

void loop() {
  // Check if data is available on the serial port
  if (Serial.available() > 0) {
    // Read the incoming character
    command = Serial.read();

    // Perform actions based on the command
    switch (command) {
      case '0':
        // Turn both pins off
        digitalWrite(pinD7, LOW);
        digitalWrite(pinD4, LOW);
        break;

      case '1':
        // Turn D7 off and D4 on
        digitalWrite(pinD7, LOW);
        digitalWrite(pinD4, HIGH);
        break;

      case '2':
        // Turn D4 off and D7 on
        digitalWrite(pinD7, HIGH);
        digitalWrite(pinD4, LOW);
        break;

      default:
        // Do nothing for unrecognized commands
        break;
    }
  }
}
