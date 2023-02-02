# ----------------------------------
# RGB LED
# JBCS 2023 IOT Workshop
# ----------------------------------

#!/usr/bin/env python3
import RPi.GPIO as GPIO		# This is the library that makes the pins work
import comm					# MQTT communications library
import time					# Library needed for timekeeping

# Colors as RGB
#  0xFF0000 = RED
#  0x00FF00 = GREEN
#  0x0000FF = BLUE
colors = [0xFF0000]

# These are the pins for Red, Green, and Blue
R = 11
G = 12
B = 13


def setup(Rpin, Gpin, Bpin):
	global pins
	global p_R, p_G, p_B
	pins = {'pin_R': Rpin, 'pin_G': Gpin, 'pin_B': Bpin}
	
	# Numbers GPIOs by physical location
	GPIO.setmode(GPIO.BOARD)       

	for i in pins:
		GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
		GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led
	
	p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
	p_G = GPIO.PWM(pins['pin_G'], 1999)
	p_B = GPIO.PWM(pins['pin_B'], 5000)
	
	p_R.start(100)      # Initial duty Cycle = 0(leds off)
	p_G.start(100)
	p_B.start(100)


def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def off():
	GPIO.setmode(GPIO.BOARD)
	for i in pins:
		GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
		GPIO.output(pins[i], GPIO.HIGH)    # Turn off all leds


def setColor(colorAsHex):   
	# This extracts the specific colors and draws them
	R_val = (colorAsHex & 0xff0000) >> 16
	G_val = (colorAsHex & 0x00ff00) >> 8
	B_val = (colorAsHex & 0x0000ff) >> 0

	R_val = map(R_val, 0, 255, 0, 100)
	G_val = map(G_val, 0, 255, 0, 100)
	B_val = map(B_val, 0, 255, 0, 100)
	
	p_R.ChangeDutyCycle(100-R_val)
	p_G.ChangeDutyCycle(100-G_val)
	p_B.ChangeDutyCycle(100-B_val)


def loop():
	# TODO:  YOUR CODE GOES HERE
	pass


def destroy():
	# Turns off all of the lights
	p_R.stop()
	p_G.stop()
	p_B.stop()
	off()

	# Releases the Resource
	GPIO.cleanup()


# --------------------------------------------
# Main Program Starts Here
# --------------------------------------------
if __name__ == "__main__":
	try:
		setup(R, G, B)
		print("RGB Running.  Enjoy the light show!")
		loop()
	except KeyboardInterrupt:
		destroy()
