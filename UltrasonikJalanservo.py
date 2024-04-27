import time
import Adafruit_PCA9685  # Pastikan sudah terinstal dengan pip
import RPi.GPIO as GPIO

# Buat objek PCA9685
pca = Adafruit_PCA9685.PCA9685()

# Atur frekuensi PCA9685 untuk servos
pca.set_pwm_freq(60)  # Frekuensi 60Hz cocok untuk servos

# Fungsi untuk menghitung nilai PWM berdasarkan sudut servo
def servo_pulse(angle):
    pulse_length = 4096    # 12-bit resolution
    pulse = int((angle * 2.275 + 102) / 1000000 * 60 * pulse_length)
    return pulse

# Mengatur posisi awal servo di setiap channel
channels = list(range(18))
initial_angle = 90
for channel in channels:
    pca.set_pwm(channel, 0, servo_pulse(initial_angle))

# Konfigurasi pin GPIO untuk sensor ultrasonik
trig = 23
echo = 24
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
    distance = (time_elapsed * 34300) / 2  # kecepatan suara 34300 cm/s

    return distance

# Loop utama
try:
    while True:
        distance = get_distance()
        print("Distance:", distance, "cm")
        if distance < 10:
            print("Obstacle detected! Stopping or reversing...")
            for channel in channels:
                pca.set_pwm(channel, 0, servo_pulse(90))  # Mengatur semua servo ke posisi netral
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Program stopped by User")
    GPIO.cleanup()  # Membersihkan semua setting GPIO
