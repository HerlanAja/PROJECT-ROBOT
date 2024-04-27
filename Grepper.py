import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

# Inisialisasi GPIO untuk servo
GPIO.setmode(GPIO.BCM)
servo_pins = [18, 19, 20]  # Contoh pin untuk servo motor, sesuaikan dengan pengaturan Anda
servo_objects = []

# Inisialisasi servo motor untuk setiap sendi
for pin in servo_pins:
    GPIO.setup(pin, GPIO.OUT)
    servo = GPIO.PWM(pin, 50)  # frekuensi 50Hz
    servo.start(0)
    servo_objects.append(servo)

# Fungsi untuk menggerakkan servo ke sudut tertentu
def move_servo(servo, angle):
    duty = angle / 18 + 2
    servo.ChangeDutyCycle(duty)
    time.sleep(1)

# Fungsi untuk mendeteksi objek menggunakan YOLOv3
def detect_object(frame):
    # Lakukan deteksi objek di sini menggunakan YOLOv3
    # Lalu kembalikan koordinat objek yang terdeteksi
    # Contoh sederhana:
    object_coordinates = [(100, 100)]  # Koordinat objek yang dideteksi
    return object_coordinates

# Main program
if __name__ == "__main__":
    try:
        while True:
            # Ambil frame dari kamera atau video
            # frame = cv2.VideoCapture().read()
            
            # Deteksi objek menggunakan YOLOv3
            object_coordinates = detect_object(frame)
            
            # Jika objek terdeteksi, gerakkan servo ke posisi tertentu
            if len(object_coordinates) > 0:
                # Ambil koordinat objek pertama
                x, y = object_coordinates[0]
                
                # Lakukan perhitungan sudut berdasarkan posisi objek
                # Disesuaikan dengan sudut yang diperlukan untuk menggerakkan servo
                angle1 = 90  # Sudut yang diperlukan sesuai dengan posisi objek
                angle2 = 45
                
                # Gerakkan servo ke sudut yang diperlukan untuk setiap sendi
                move_servo(servo_objects[0], angle1)
                move_servo(servo_objects[1], angle2)
            
            # Tampilkan frame dengan kotak deteksi objek
            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        pass

    finally:
        for servo in servo_objects:
            servo.stop()
        GPIO.cleanup()

