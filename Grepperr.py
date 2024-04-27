from gpiozero import Servo
from time import sleep

# Inisialisasi servo tangan kiri pada pin GPIO 17
servo_kiri = Servo(17)

# Inisialisasi servo tangan kanan pada pin GPIO 27
servo_kanan = Servo(27)

try:
    while True:
        # Membuka kedua gripper (sudut 0 derajat)
        servo_kiri.min()
        servo_kanan.min()
        print("Kedua gripper terbuka")
        sleep(2)

        # Menutup kedua gripper (sudut 90 derajat)
        servo_kiri.max()
        servo_kanan.max()
        print("Kedua gripper tertutup")
        sleep(2)

except KeyboardInterrupt:
    print("Program dihentikan dengan keyboard")

finally:
    # Mengembalikan kedua servo ke posisi tengah (sudut 45 derajat)
    servo_kiri.mid()
    servo_kanan.mid()
    print("Kedua servo dikembalikan ke posisi tengah")