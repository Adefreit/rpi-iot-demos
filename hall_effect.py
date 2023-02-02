# ----------------------------------
# Hall Effect Sensor
# JBCS 2023 IOT Workshop
# ----------------------------------

#!/usr/bin/env python3
import RPi.GPIO as GPIO		# This is the library that makes the pins work
import comm					# MQTT communications library
import time					# Library needed for timekeeping

# This is the pin we are going to use to get readings from the sensor
HallPin = 11


def setup():
	# Numbers GPIOs by physical location
	GPIO.setmode(GPIO.BOARD)       

	# Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.setup(HallPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

	# Tells the Pi to call a function when a magnetic field is detected
	GPIO.add_event_detect(HallPin, GPIO.BOTH, callback=detect, bouncetime=200)


# This function is called whenever 
def SensorChanged(sensorReading):
	# TODO:  YOUR CODE GOES HERE


def detect(chn):
	# When a state change is detected, call the SensorChanged function
	SensorChanged(GPIO.input(HallPin))


def loop():
	# This is just a neverending loop to keep the program running
	while True:
		pass


def destroy():
	GPIO.cleanup() # Release resource


# --------------------------------------------
# Main Program Starts Here
# --------------------------------------------
if __name__ == '__main__':     # Program start from here
	setup()
	try:
		print("Sensor Running.  Waiting for a Magnet")
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

