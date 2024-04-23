import RPi.GPIO as GPIO
import time

# Atur pin servo
J1Pin = 17
J2Pin = 18
J3Pin = 19

# Inisialisasi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(J1Pin, GPIO.OUT)
GPIO.setup(J2Pin, GPIO.OUT)
GPIO.setup(J3Pin, GPIO.OUT)

# Fungsi untuk mengatur posisi servo
def set_servo_angle(pin, angle):
    duty = angle / 18 + 2
    GPIO.output(pin, True)
    pwm = GPIO.PWM(pin, 50)
    pwm.start(0)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(pin, False)
    pwm.ChangeDutyCycle(0)
    pwm.stop()

# Fungsi untuk gerakan maju dan mundur
def move_forward():
    set_servo_angle(J1Pin, 0)
    set_servo_angle(J2Pin, 50)
    set_servo_angle(J3Pin, 30)
    time.sleep(1)

def move_backward():
    set_servo_angle(J1Pin, 0)
    set_servo_angle(J2Pin, 20)
    set_servo_angle(J3Pin, 20)
    time.sleep(1)

# Fungsi utama
def main():
    try:
        while True:
            move_forward()
            move_backward()
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
