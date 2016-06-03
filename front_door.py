#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import picamera
import slack_api
from sys import argv

#default start and end times
start = 8
end = 18

#checking for args and setting the vaules correctly with a check for military time
if len(argv) >=3:
	start = int(argv[1])
	end = int(argv[2])
	if end < 12:
		end +=12
else:
	print("Invalid args, falling back on default 8am to 6pm behaviour.")
	
#sensor setup
sensor = 4
camera = picamera.PiCamera()

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

#main logic
while True:
	#set state to false and only update between the start and end times of day
	current_state = False
	if start <= time.localtime().tm_hour < end:
		current_state = GPIO.input(sensor)

	#check status of user and upload photos if target user is away
	if current_state and slack_api.check() =="away":
		camera.capture('capture.jpg')
		print("captured")
		slack_api.upload()
		print("uploaded")
		time.sleep(60)
		print("slept")
	else:
                time.sleep(1)
