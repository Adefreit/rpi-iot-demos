# ----------------------------------
# Button Sensor
# JBCS 2023 IOT Workshop
# ----------------------------------

#!/usr/bin/env python3
import RPi.GPIO as GPIO		# This is the library that makes the pins work
import comm					# MQTT communications library
import time					# Library needed for timekeeping


# This is the input pin
BtnPin = 11


def setup():
	# Numbers GPIOs by physical location
	GPIO.setmode(GPIO.BOARD)       

	# Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    

	# Tells the Pi to call a function when a button event is detected
	GPIO.add_event_detect(BtnPin, GPIO.BOTH, callback=detect, bouncetime=200)


def OnStateChange(buttonPin):
	# YOUR CODE GOES HERE
	pass


def detect(chn):
	# When a state change is detected, call the OnStateChange function
	OnStateChange(GPIO.input(BtnPin))


def loop():
	# This is just a neverending loop to keep the program running
	while True:
		pass


def destroy():
	GPIO.cleanup() # Release resource


# --------------------------------------------
# Main Program Starts Here
# --------------------------------------------
if __name__ == '__main__':
	setup()
	try:
		print("Program Running.  Waiting for a Button Press")
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

