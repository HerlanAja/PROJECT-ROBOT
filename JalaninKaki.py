import RPi.GPIO as GPIO
import time

# Atur pin PWM (Pulse Width Modulation)
servo_pin = 18  # Atur pin GPIO yang digunakan untuk servo
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Inisialisasi objek PWM
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz (20 ms periode)
pwm.start(0)  # Mulai PWM dengan siklus tugas 0 (servo diam)

# Fungsi untuk menggerakkan servo ke posisi maju
def move_forward():
    duty = 2  # Siklus tugas untuk posisi maju (sesuaikan jika perlu)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)  # Tunggu 1 detik untuk servo bergerak
    pwm.ChangeDutyCycle(0)  # Berhenti mengirimkan sinyal PWM

# Fungsi untuk menggerakkan servo ke posisi mundur
def move_backward():
    duty = 12  # Siklus tugas untuk posisi mundur (sesuaikan jika perlu)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)  # Tunggu 1 detik untuk servo bergerak
    pwm.ChangeDutyCycle(0)  # Berhenti mengirimkan sinyal PWM

try:
    while True:
        # Bergerak maju
        move_forward()
        time.sleep(2)  # Tunggu 2 detik sebelum bergerak mundur

        # Bergerak mundur
        move_backward()
        time.sleep(2)  # Tunggu 2 detik sebelum bergerak maju
except KeyboardInterrupt:
    pwm.stop()  # Berhenti PWM
    GPIO.cleanup()  # Bersihkan pin GPIO
