void setup() {
    pinMode(13, OUTPUT); // LED on pin 13
    Serial.begin(9600);
}

void loop() {
    if (Serial.available()) {
        String command = Serial.readStringUntil('\n');
        command.trim(); // Remove any newline characters

        if (command == "ON") {
            digitalWrite(13, HIGH);
        } else if (command == "OFF") {
            digitalWrite(13, LOW);
        }
    }
}
