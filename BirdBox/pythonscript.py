from picamera import PiCamera
from gpiozero import MotionSensor
from time import sleep
import datetime

camera = PiCamera()
pir = MotionSensor(4)
teller = 0
recording = 0

while True:
	while pir.motion_detected == True:
		print("Motion detected!")
		if recording == 0:
			camera.start_recording("/home/pi/Birdhouse/videos/video"+"{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())+".h264")
			print("Recording...")
			recording = 1
		if recording == 1:
			sleep(1)
			teller = teller + 1
			print(teller)
		if teller == 300 and recording == 1:
			camera.stop_recording()
			print("Stopped recording door teller")
			camera.start_recording("/home/pi/Birdhouse/videos/video"+"{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())+".h264")
			print("Recording again...")
			teller = 0
	if pir.motion_detected == False:
		print("NO motion detected")
		sleep(1)
		if recording == 1:
			camera.stop_recording()
			print("Stopped recording")
			recording = 0
			teller = 0
