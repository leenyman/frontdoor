#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import picamera

sensor = 4
camera = picamera.PiCamera()

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

while True:
	time.sleep(0.1)
	previous_state = current_state
	current_state = GPIO.input(sensor)
	if current_state != previous_state:
		new_state = "HIGH" if current_state else "LOW"
		print("GPIO pin %s is %s" % (sensor, new_state))
		if current_state:
			#camera.start_preview()
			camera.capture('capture.jpg')
		#else:
			#camera.stop_preview()