import RPi.GPIO as GPIO
from time import sleep

# Fungsi untuk mengontrol gripper
def SetGripperAngle(sudut):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    pwm = GPIO.PWM(11, 50)
    pwm.start(0)
    tugas = sudut / 18 + 2
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(tugas)
    sleep(2)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(0)

try:
    count = 0  # Inisialisasi variabel penghitung
    while count < 10:  # Loop selama count kurang dari 10
        print(f"Looping ke-{count + 1}")
        
        # Menggerakkan servo untuk membuka gripper
        SetGripperAngle(0)  # Atur sudut untuk membuka gripper
        sleep(2)  # Tunggu 2 detik agar gripper terbuka sepenuhnya
        
        # Menggerakkan servo untuk menutup gripper
        SetGripperAngle(180)  # Atur sudut untuk menutup gripper
        sleep(2)  # Tunggu 2 detik agar gripper tertutup sepenuhnya
        
        count += 1  # Tambahkan nilai count setiap kali loop

except KeyboardInterrupt:
    print("Program dihentikan dengan keyboard")

finally:
    pwm.stop()  # Berhenti PWM
    GPIO.cleanup()  # Membersihkan GPIO
