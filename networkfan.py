# Console Ping
#Version 1
#
# Importing
import os
import time
import subprocess
#
# Start
f = open("fan_conf.py", "w")
f.write('xbox360 = 0\n')
f.write('ps3 = 0')
f.close()
while True:
# XBOX 360
	print 'Looking for XBOX 360'
	xbox360address = "192.168.0.11"
	os.system("sudo arp-scan 192.168.0.11 > stdout.txt")
	c = open('stdout.txt', 'r+')
	data = c.read()
	xbox = int(data[data.find('responded')-3:data.find('responded')].strip())
	if xbox == 1:
		print "ping to", xbox360address, "ok"
		print 'xbox 360 fan on'
		f = open("fan_conf.py", "r+")
		f.seek(10)
		f.write('1')
		f.close()
		c.close()
	elif xbox == 0:
		print "ping to", xbox360address, "no response from"
		print 'Xbox 360 fan off'
                f = open("fan_conf.py", "r+")
                f.seek(10) 
                f.write('0')
                f.close()
		c.close()
	else:
		print "ping to", xbox360address, "failed"
		print 'Xbox 360 fan off'
                f = open("fan_conf.py", "r+")
                f.seek(10)
                f.write('0')
                f.close()
		c.close()
	print
	print
# PS3
	print 'Looking for PS3'
        ps3address = "192.168.0.17"
        res = subprocess.call(['ping', '-c', '3', ps3address])
        if res == 0:
                print "ping to", ps3address, "ok"
		print "PS3 fan on"
                f = open("fan_conf.py", "r+")
                f.seek(18) 
                f.write('1')
                f.close()
        elif res == 2:
                print "ping to", ps3address, "no response from"
		print 'PS3 fan off'
                f = open("fan_conf.py", "r+")
                f.seek(18)
                f.write('0')
                f.close()
        else:   
                print "ping to", ps3address, "failed"
		print 'PS3 fan off'
                f = open("fan_conf.py", "r+")
                f.seek(18)
                f.write('0')
                f.close()
	print
	print
	time.sleep(5)
