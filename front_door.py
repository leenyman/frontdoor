#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import picamera
import slack_api

sensor = 4
camera = picamera.PiCamera()

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

while True:
	current_state = GPIO.input(sensor)
	if current_state and slack_api.check() =="away":
		camera.capture('capture.jpg')
		slack_api.upload()
		time.sleep(60)
	else:
                time.sleep(.5)
