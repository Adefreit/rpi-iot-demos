# ----------------------------------
# Active Buzzer
# JBCS 2023 IOT Workshop
# ----------------------------------

#!/usr/bin/env python3
import RPi.GPIO as GPIO		# This is the library that makes the pins work
import comm					# MQTT communications library
import time					# Library needed for timekeeping


# This is the pin we are going to use to control the buzzer
Buzzer = 11    

# This is a flag variable used to control whether to run the buzzer
active = True


def setup(pin):
	global BuzzerPin
	BuzzerPin = pin

	# Numbers GPIOs by physical location
	GPIO.setmode(GPIO.BOARD)       

	# This is where we configure the Buzzer
	GPIO.setup(BuzzerPin, GPIO.OUT)
	GPIO.output(BuzzerPin, GPIO.HIGH)


def on():
	# This tells the buzzer to start making noise
	GPIO.output(BuzzerPin, GPIO.LOW)


def off():
	# This tells the buzzer to stop making noise
	GPIO.output(BuzzerPin, GPIO.HIGH)


def loop():
	# TODO:  YOUR CODE GOES HERE
	pass


def destroy():
	GPIO.output(BuzzerPin, GPIO.HIGH)  # Turns off the buzzer
	GPIO.cleanup()                     # Release resource


# --------------------------------------------
# Main Program Starts Here
# --------------------------------------------
if __name__ == '__main__': 
	    
	setup(Buzzer)
	try:
		print("Buzzer Running")
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

