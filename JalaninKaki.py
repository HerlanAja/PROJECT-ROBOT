import board
import busio
import time
from adafruit_pca9685 import PCA9685

# Inisialisasi bus I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Inisialisasi objek PCA9685 dengan alamat I2C yang sesuai
pca = PCA9685(i2c)
pca.frequency = 50

# Fungsi untuk menggerakkan servo ke posisi tertentu
def set_servo_position(channel, position):
    pulse_width = int(position * 40.96)  # Konversi sudut ke lebar pulsa (0.5 ms - 2.5 ms)
    pca.channels[channel].duty_cycle = pulse_width

# Fungsi untuk menggerakkan satu kaki
def move_leg(leg, servo1_pos, servo2_pos, servo3_pos):
    # Tentukan channel servo untuk setiap servo di kaki
    servo1_channel = leg * 3
    servo2_channel = leg * 3 + 1
    servo3_channel = leg * 3 + 2

    # Atur posisi setiap servo pada kaki
    set_servo_position(servo1_channel, servo1_pos)
    set_servo_position(servo2_channel, servo2_pos)
    set_servo_position(servo3_channel, servo3_pos)

# Fungsi untuk menggerakkan keenam kaki secara bersamaan
def move_legs(leg1, leg2, leg3, leg4, leg5, leg6):
    move_leg(0, leg1[0], leg1[1], leg1[2])
    move_leg(1, leg2[0], leg2[1], leg2[2])
    move_leg(2, leg3[0], leg3[1], leg3[2])
    move_leg(3, leg4[0], leg4[1], leg4[2])
    move_leg(4, leg5[0], leg5[1], leg5[2])
    move_leg(5, leg6[0], leg6[1], leg6[2])

# Pola gerakan maju
def walk_forward():
    move_legs([90, 90, 90], [45, 90, 45], [90, 90, 90], [45, 90, 45], [90, 90, 90], [45, 90, 45])  # Gerakan kaki 1, 3, dan 5 maju
    time.sleep(0.5)
    move_legs([45, 90, 45], [90, 90, 90], [45, 90, 45], [90, 90, 90], [45, 90, 45], [90, 90, 90])  # Gerakan kaki 2, 4, dan 6 maju
    time.sleep(0.5)

# Pola gerakan mundur
def walk_backward():
    move_legs([45, 90, 45], [90, 90, 90], [45, 90, 45], [90, 90, 90], [45, 90, 45], [90, 90, 90])  # Gerakan kaki 2, 4, dan 6 mundur
    time.sleep(0.5)
    move_legs([90, 90, 90], [45, 90, 45], [90, 90, 90], [45, 90, 45], [90, 90, 90], [45, 90, 45])  # Gerakan kaki 1, 3, dan 5 mundur
    time.sleep(0.5)

# Pola gerakan kiri
def walk_left():
    move_legs([90, 90, 45], [45, 90, 90], [90, 90, 45], [45, 90, 90], [90, 90, 45], [45, 90, 90])  # Gerakan kaki 1, 3, dan 5 kiri
    time.sleep(0.5)
    move_legs([45, 90, 90], [90, 90, 45], [45, 90, 90], [90, 90, 45], [45, 90, 90], [90, 90, 45])  # Gerakan kaki 2, 4, dan 6 kiri
    time.sleep(0.5)

# Pola gerakan kanan
def walk_right():
    move_legs([45, 90, 90], [90, 90, 45], [45, 90, 90], [90, 90, 45], [45, 90, 90], [90, 90, 45])  # Gerakan kaki 2, 4, dan 6 kanan
    time.sleep(0.5)
    move_legs([90, 90, 45], [45, 90, 90], [90, 90, 45], [45, 90, 90], [90, 90, 45], [45, 90, 90])  # Gerakan kaki 1, 3, dan 5 kanan
    time.sleep(0.5)

try:
    while True:
        # Pola gerakan yang diinginkan
        walk_forward()
        time.sleep(1)
        walk_backward()
        time.sleep(1)
        walk_left()
        time.sleep(1)
        walk_right()
        time.sleep(1)

except KeyboardInterrupt:
    # Hentikan servo saat program berakhir
    for i in range(16):
        pca.channels[i].duty_cycle = 0
    print("Program dihentikan dengan keyboard")