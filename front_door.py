#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import picamera
import presencecheck

sensor = 4
camera = picamera.PiCamera()

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

while True:
	current_state = GPIO.input(sensor)
	if current_state and presencecheck.pres_chk() =="away":
		camera.capture('capture.jpg')
		execfile("apiupload.py")
		time.sleep(60)
	else:
                time.sleep(.5)
