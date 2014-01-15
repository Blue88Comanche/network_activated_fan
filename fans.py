# Media Center Fan Controler
# version 1
#
# Importing
import os
import time
import RPi.GPIO as GPIO
import fan_conf
from fan_conf import *
#
# GPIO Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
#
# Make sure those relays are off
GPIO.output(11, GPIO.HIGH)
GPIO.output(12, GPIO.HIGH)
GPIO.output(15, GPIO.HIGH)
GPIO.output(16, GPIO.HIGH)
#
# Start 
while True:
	import fan_conf
	from fan_conf import *
	reload(fan_conf)
# XBOX 360
	if xbox360 is 0:
		print 'XBOX 360 fan OFF'
		GPIO.output(11, GPIO.HIGH)
		GPIO.output(12, GPIO.HIGH)
	elif xbox360 is 1:
		print 'XBOX 360 fan ON'
		GPIO.output(11, GPIO.LOW)
		GPIO.output(12, GPIO.LOW)
        else:
                print 'XBOX 360 fan OFF'
                GPIO.output(11, GPIO.HIGH)
                GPIO.output(12, GPIO.HIGH)
# PS3
        if ps3 is 0:
                print 'PS3 fan OFF'
                GPIO.output(15, GPIO.HIGH)
                GPIO.output(16, GPIO.HIGH)
        elif ps3 is 1:
                print 'PS3 fan ON'
                GPIO.output(15, GPIO.LOW)
                GPIO.output(16, GPIO.LOW)
        else:             
                print 'PS3 fan OFF'
                GPIO.output(15, GPIO.HIGH)
                GPIO.output(16, GPIO.HIGH)
	time.sleep(5)
