from picamera import PiCamera
camera = PiCamera()

import time

from time import sleep
import os

from gpiozero import MotionSensor

pir = MotionSensor(4)

recording = 0
teller = 0


named_tuple = time.localtime()
time_string = time.strftime("%m_%d_%Y_%Hh%M", named_tuple)


#usb mount
os.system("sudo mount /dev/sdb /mnt/USBdrive/")
os.system("sudo mount /dev/sda /mnt/USBdrive/")
print("USB mounted")
sleep(3)

from datetime import datetime

teller = 0
toggle = True


while True:
    if pir.motion_detected:
        if toggle:
            dt_string = datetime.now().strftime("%d%m%Y%H%M%S")
            camera.start_recording('/mnt/USBdrive/movie%s.h264' %dt_string)
            toggle = False 
            print("recording started")
    if pir.motion_detected == False:
        if toggle == False:
            camera.stop_recording()
            print("Stopped recording")
            teller = 0
            toggle = True
    if toggle == False :
        sleep(1)
        teller = teller + 1
        print(teller)
        if teller >= 30:
            camera.stop_recording()
            print("recording stopped")
            teller = 0
            toggle = True

