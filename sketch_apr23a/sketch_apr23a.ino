#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// Address PCA9685
#define PCA9685_ADDRESS 0x40

// Number of PCA9685 PWM channels
#define NUM_PCA_CHANNELS 16

// Servo min-max pulse width in microseconds
#define SERVO_MIN_PW 150
#define SERVO_MAX_PW 600

// Create instance of Adafruit_PWMServoDriver class
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

// Function to set PWM signal for a servo on a specific channel
void setServo(uint8_t channel, uint16_t pulseWidth) {
  pwm.setPWM(channel, 0, pulseWidth);
}

void setup() {
  Serial.begin(9600);

  // Initialize PWM driver
  pwm.begin();
  
  // Set PWM frequency (default is 50 Hz)
  pwm.setPWMFreq(60); // 60 Hz is typical for most servos
  
  // Set servo positions
  // You can adjust these values according to your servo's range
  setServo(0, SERVO_MIN_PW); // Servo 1
  setServo(1, SERVO_MIN_PW); // Servo 2
  setServo(2, SERVO_MIN_PW); // Servo 3
  // Set more servos if needed...
}

void loop() {
  // Move servo 1 to different positions
  for (int i = SERVO_MIN_PW; i <= SERVO_MAX_PW; i += 10) {
    setServo(0, i);
    delay(50);
  }
  delay(1000);

  // Move servo 2 to different positions
  for (int i = SERVO_MIN_PW; i <= SERVO_MAX_PW; i += 10) {
    setServo(1, i);
    delay(50);
  }
  delay(1000);

  // Move servo 3 to different positions
  for (int i = SERVO_MIN_PW; i <= SERVO_MAX_PW; i += 10) {
    setServo(2, i);
    delay(50);
  }
  delay(1000);
}
