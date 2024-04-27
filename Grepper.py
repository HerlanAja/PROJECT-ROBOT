import RPi.GPIO as GPIO
from time import sleep
import cv2
import torch

# Fungsi untuk mengontrol siku
def SetElbowAngle(sudut):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    pwm = GPIO.PWM(11, 50)
    pwm.start(0)
    tugas = sudut / 18 + 2
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(tugas)
    sleep(2)
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(0)

# Fungsi untuk mengontrol pergelangan tangan (wrist)
def SetWristAngle(sudut):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    pwm = GPIO.PWM(7, 50)
    pwm.start(0)
    tugas = sudut / 18 + 2
    GPIO.output(7, True)
    pwm.ChangeDutyCycle(tugas)
    sleep(2)
    GPIO.output(7, True)
    pwm.ChangeDutyCycle(0)

# Fungsi untuk mengontrol gripper
def SetGripperAngle(sudut):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)
    pwm = GPIO.PWM(3, 50)
    pwm.start(0)
    tugas = sudut / 18 + 2
    GPIO.output(3, True)
    pwm.ChangeDutyCycle(tugas)
    sleep(2)
    GPIO.output(3, False)
    pwm.ChangeDutyCycle(0)

# Inisialisasi YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Fungsi deteksi objek menggunakan YOLOv5
def detect_object(img):
    results = model(img)
    labels = results.xyxyn[0][:, -1].cpu().numpy()
    boxes = results.xyxyn[0][:, :-1].cpu().numpy()
    return labels, boxes

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

try:
    while True:
        # Mengambil gambar dari kamera
        ret, frame = cap.read()

        # Deteksi objek menggunakan YOLOv5
        labels, boxes = detect_object(frame)

        # Jika objek terdeteksi, kontrol servo gripper
        if len(labels) > 0:
            # Bergerak ke posisi awal
            SetElbowAngle(130)
            SetWristAngle(70)
            SetGripperAngle(0)

            # Mengambil objek
            SetElbowAngle(110)
            SetGripperAngle(0)
            SetGripperAngle(130)

            # Bergerak kembali
            SetElbowAngle(150)
            SetWristAngle(50)

            # Melepaskan objek
            SetGripperAngle(130)
            SetGripperAngle(0)

        # Menampilkan gambar
        cv2.imshow('Object Detection', frame)

        # Tekan 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Program dihentikan dengan keyboard")

finally:
    cap.release()
    cv2.destroyAllWindows()
    pwm.stop()
    GPIO.cleanup()
    GPIO.setwarnings(False)