#!/usr/bin/env python
# Console Ping
# Version 1.02
#
# Importing
import os
import time
import subprocess
import RPi.GPIO as GPIO
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
f = open("fan_conf.py", "w")
f.write('xbox360 = 0\n')
f.write('ps3 = 0')
f.close()
while True:
# XBOX 360
	print '--------------------'
	print
	print 'Looking for XBOX 360'
	xbox360address = "192.168.0.11"
	os.system("sudo arp-scan 192.168.0.11 > stdout.txt")
	x = open('stdout.txt', 'r+')
	data = x.read()
	xbox = int(data[data.find('responded')-3:data.find('responded')].strip())
	if xbox == 1:
		print "ping to", xbox360address, "ok"
		print 'xbox 360 fan on'
		GPIO.output(11, GPIO.LOW)
                GPIO.output(12, GPIO.LOW)
		f = open("fan_conf.py", "r+")
		f.seek(10)
		f.write('1')
		f.close()
		x.close()
	elif xbox == 0:
		print "ping to", xbox360address, "no response from"
		print 'Xbox 360 fan off'
                GPIO.output(11, GPIO.HIGH)
                GPIO.output(12, GPIO.HIGH)
                f = open("fan_conf.py", "r+")
                f.seek(10) 
                f.write('0')
                f.close()
		x.close()
	else:
		print "ping to", xbox360address, "failed"
		print 'Xbox 360 fan off'
                GPIO.output(11, GPIO.HIGH)
                GPIO.output(12, GPIO.HIGH)
                f = open("fan_conf.py", "r+")
                f.seek(10)
                f.write('0')
                f.close()
		x.close()
	print
# PS3
	print '--------------------'
        print
	print 'Looking for PS3'
        ps3address = "192.168.0.17"
        res = subprocess.call(['ping', '-c', '3', ps3address])
        if res == 0:
                print "ping to", ps3address, "ok"
                print "PS3 fan on"
                GPIO.output(15, GPIO.LOW)
                GPIO.output(16, GPIO.LOW)
                f = open("fan_conf.py", "r+")
                f.seek(18) 
                f.write('1')
                f.close()
        elif res == 2:
                print "ping to", ps3address, "no response from"
                print 'PS3 fan off'
                GPIO.output(15, GPIO.HIGH)
                GPIO.output(16, GPIO.HIGH)
                f = open("fan_conf.py", "r+")
                f.seek(18)
                f.write('0')
                f.close()
        else:   
                print "ping to", ps3address, "failed"
                print 'PS3 fan off'
                GPIO.output(15, GPIO.HIGH)
                GPIO.output(16, GPIO.HIGH)
                f = open("fan_conf.py", "r+")
                f.seek(18)
                f.write('0')
                f.close()
        print
        time.sleep(5)
