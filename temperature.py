# ----------------------------------
# Temperature Sensor (Thermistor)
# JBCS 2023 IOT Workshop
# ----------------------------------

#!/usr/bin/env python3
import RPi.GPIO as GPIO		# This is the library that makes the pins work
import comm					# MQTT communications library
import time					# Library needed for timekeeping

# This variable stores the temperature sensor's name
ds18b20 = ''

def setup():
    # This function essentially looks for the temperature sensor drivers
    # and loads them.  
    global ds18b20
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = str(i)


def read():
    # This functions returns the temperature in celsius
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    temperature = temperature / 1000
    return temperature


def loop():
    while True:
        # YOUR CODE GOES HERE
	    pass


def destroy():
    pass


# --------------------------------------------
# Main Program Starts Here
# --------------------------------------------
if __name__ == '__main__':
    try:
        setup()
        print("Temperature sensor started.")
        loop()
    except KeyboardInterrupt:
        destroy()