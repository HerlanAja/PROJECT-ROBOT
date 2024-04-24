import time
import Adafruit_PCA9685
import Adafruit_Servo

# Buat objek PCA9685
pca = Adafruit_PCA9685.PCA9685()

# Atur frekuensi PCA9685
pca.set_pwm_freq(60)  # Frekuensi 60Hz

# Buat objek servo untuk setiap kaki
servo1_1 = Adafruit_Servo.PWM(pca.get_channel(0))
servo1_2 = Adafruit_Servo.PWM(pca.get_channel(1))
servo1_3 = Adafruit_Servo.PWM(pca.get_channel(2))

servo2_1 = Adafruit_Servo.PWM(pca.get_channel(3))
servo2_2 = Adafruit_Servo.PWM(pca.get_channel(4))
servo2_3 = Adafruit_Servo.PWM(pca.get_channel(5))

servo3_1 = Adafruit_Servo.PWM(pca.get_channel(6))
servo3_2 = Adafruit_Servo.PWM(pca.get_channel(7))
servo3_3 = Adafruit_Servo.PWM(pca.get_channel(8))

servo4_1 = Adafruit_Servo.PWM(pca.get_channel(9))
servo4_2 = Adafruit_Servo.PWM(pca.get_channel(10))
servo4_3 = Adafruit_Servo.PWM(pca.get_channel(11))

servo5_1 = Adafruit_Servo.PWM(pca.get_channel(12))
servo5_2 = Adafruit_Servo.PWM(pca.get_channel(13))
servo5_3 = Adafruit_Servo.PWM(pca.get_channel(14))

servo6_1 = Adafruit_Servo.PWM(pca.get_channel(15))
servo6_2 = Adafruit_Servo.PWM(pca.get_channel(16))
servo6_3 = Adafruit_Servo.PWM(pca.get_channel(17))

# Atur posisi awal servo
servo1_1.setAngle(90)
servo1_2.setAngle(90)
servo1_3.setAngle(90)

servo2_1.setAngle(90)
servo2_2.setAngle(90)
servo2_3.setAngle(90)

servo3_1.setAngle(90)
servo3_2.setAngle(90)
servo3_3.setAngle(90)

servo4_1.setAngle(90)
servo4_2.setAngle(90)
servo4_3.setAngle(90)

servo5_1.setAngle(90)
servo5_2.setAngle(90)
servo5_3.setAngle(90)

servo6_1.setAngle(90)
servo6_2.setAngle(90)
servo6_3.setAngle(90)

# Import library ultrasonik
import RPi.GPIO as GPIO
import time
import datetime

# Atur pin GPIO untuk sensor ultrasonik
trig = 23
echo = 24

# Setting pin GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def get_distance():
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == 0:
        pass
    start_time = time.time()

    while GPIO.input(echo) == 1:
        pass
    stop_time = time.time()

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2

    return distance

# Loop utama
while True:
    # Baca jarak dari sensor ultrasonik
    distance = get_distance()

    # Jika jarak kurang dari 10cm, robot
