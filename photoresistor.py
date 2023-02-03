# ----------------------------------
# Photoresistor
# JBCS 2023 IOT Workshop
# ----------------------------------

#!/usr/bin/env python3
import PCF8591 as ADC		# This is the library for the analog to digital converter
import RPi.GPIO as GPIO		# This is the library that makes the pins work
import comm					# MQTT communications library
import time					# Library needed for timekeeping

DO = 17
GPIO.setmode(GPIO.BCM)

def setup():
	ADC.setup(0x48)
	GPIO.setup(DO, GPIO.IN)
	
def loop():
	# YOUR CODE GOES HERE
	pass

# --------------------------------------------
# Main Program Starts Here
# --------------------------------------------
if __name__ == '__main__':
	try:
		setup()
		print("Program Running.  Heading to the Light")
		loop()
	except KeyboardInterrupt: 
		pass	
