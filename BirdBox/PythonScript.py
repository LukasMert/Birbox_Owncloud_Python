from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
import datetime
import os

pir = MotionSensor(4)
camera = PiCamera()
recording = 0
vervolg = 0
teller = 0
h264_video = ".h264"
mp4_video = ".mp4"

# mount  USB
os.system("sudo mount /dev/sda1 /mnt/USBdrive")
os.system("sudo mount /dev/sda /mnt/USBdrive")
print("mounted")
sleep(3)

while True:
	while pir.motion_detected == True:
		if recording == 0:
			print( "Motion detected!")
			timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
			camera.start_recording("/mnt/USBdrive/video" + "_" + timestamp + "_" + format(vervolg) + ".h264")
			recording = 1
			print( "  video" + "_" + timestamp + "_" + format(vervolg) + ".h264")
			sleep(1)

		if recording == 1:
			sleep(1)
			teller = teller + 1
			print(teller)
		if teller >= 5 and recording == 1:
			camera.stop_recording()
			print("stop recording")
			os.system("MP4Box -add " + "/mnt/USBdrive/video" +  "_" + timestamp + "_" + format(vervolg) + ".h264" + " " +  "/mnt/USBdrive/video" + "_" + timestamp + "_" + format(vervolg) + mp4_video)
			os.system("rm " + "/mnt/USBdrive/video" +  "_" + timestamp + "_" + format(vervolg) + h264_video)
			footage = "/mnt/USBdrive/video" + "_" + timestamp + "_" + format(vervolg) + mp4_video
			vervolg += 1
			camera.start_recording("/mnt/USBdrive/video" + "_" + timestamp + "_" + format(vervolg) + ".h264")
			print("start rec")
			teller = 0

	if pir.motion_detected == False and recording == 1:
		print("geen detectie")
		camera.stop_recording()
		os.system("MP4Box -add " + "/mnt/USBdrive/video" + "_" + timestamp + "_" + format(vervolg) + ".h264" + " " +  "/mnt/USBdrive/video" + "_" + timestamp + "_" + format(vervolg) + mp4_video)
		os.system("rm " + "/mnt/USBdrive/video" + "_" + timestamp + "_" + format(vervolg) + h264_video)
		footage = "/mnt/USBdrive/video" + "_" + timestamp + "_" + format(vervolg) + mp4_video
		recording = 0
		teller = 0
		vervolg = 0
