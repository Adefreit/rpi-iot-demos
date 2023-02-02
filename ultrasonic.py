# ----------------------------------
# Ultrasonic Sensor (Sonar)
# JBCS 2023 IOT Workshop
# ----------------------------------

#!/usr/bin/env python3
import RPi.GPIO as GPIO		# This is the library that makes the pins work
import comm					# MQTT communications library
import time					# Library needed for timekeeping

# These are the pins used by this sensor
TRIG = 11
ECHO = 12

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)


def getDistance():
	# This is so freaking cool
	# It basically sends out a sound signal here
	GPIO.output(TRIG, 0)
	time.sleep(0.000002)

	GPIO.output(TRIG, 1)
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)

	# . . . and Listens for it here . . .
	while GPIO.input(ECHO) == 0:
		a = 0
	time1 = time.time()
	while GPIO.input(ECHO) == 1:
		a = 1
	time2 = time.time()

	# And calculates distance based on the time elapsed
	during = time2 - time1
	return during * 340 / 2 * 100


def loop():
	# TODO:  YOUR CODE GOES HERE
	pass


def destroy():
	GPIO.cleanup()


# --------------------------------------------
# Main Program Starts Here
# --------------------------------------------
if __name__ == "__main__":
	setup()
	try:
		comm.connect()
		print("Ultrasonic starts now!")
		loop()
	except KeyboardInterrupt:
		destroy()
