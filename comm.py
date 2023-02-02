# -------------------------------------------
# comm.py
# MQTT Library
# -------------------------------------------
from threading import Thread
import paho.mqtt.client as mqtt
import datetime
import time

DEBUG = True
MQTT_BROKER_IP = "96.66.89.56"
CHANNELS = [ ]
MESSAGE_HANDLER = None

# MQTT Client
client = mqtt.Client()

# Specifies the amount of time before the client is forced to reconnect
# Only used when listening to channels
PERSISTENCE_CHECK_DURATION = 60.0 * 15
RECEIVED_RECENT_MESSAGE = False


# ----------------------------------------------
# Event Hander for When the Client Connects
# ----------------------------------------------
def on_connect(client, userdata, flags, rc):
    if DEBUG:
        print("MQTT CONNECTED. Subscribing to channels:", CHANNELS)
    
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    if len(CHANNELS) > 0:
        client.subscribe(CHANNELS)


# ----------------------------------------------
# Event Hander for When the Client Disconnects
# ----------------------------------------------
def on_disconnect(client, userdata, rc):
    if DEBUG:
        print("MQTT DISCONNECT:", client, userdata, rc, "\n")


# ----------------------------------------------
# Event Hander for When the Client Disconnects
# ----------------------------------------------
def on_message(client, userdata, msg):
    global RECEIVED_RECENT_MESSAGE
    
    if DEBUG:
        print()
        print(datetime.datetime.now(), "::", "[" + msg.topic + "]: ", str(len(decode(msg.payload))) + " bytes")
    
    # Sets Flag to Indicate that a Message Was Received Recently
    RECEIVED_RECENT_MESSAGE = True
    
    # Forwards the Message to a Custom Handler
    if MESSAGE_HANDLER != None:
        MESSAGE_HANDLER(client, userdata, decode(msg.payload))


# ----------------------------------------------
# Connects to the MQTT Broker
# ----------------------------------------------
def connect(destination=MQTT_BROKER_IP, channels=None):
    global CHANNELS
    
    print("Connecting to", destination, "- Channels:", channels)
    
    # Updates the Channels if Needed
    if channels != None:
        CHANNELS = channels
    
    client.on_connect = on_connect
    client.connect(destination, keepalive=int(PERSISTENCE_CHECK_DURATION))


# ----------------------------------------------
# Sends an MQTT Message to the Broker
# This automatically wraps it with the standard
# headers
# ----------------------------------------------
def send(channel, payload, qos=0):

    print("Sending:", payload)
    message = payload
    
    # Sends the message on the desired channel
    client.publish(channel, message)
    
    if DEBUG:
        print("Sent Message to Broker:")
        print("  Channel:", channel)
        print("  Message:", message, "\n")


# ----------------------------------------------
# Disconnects the MQTT Client from the Broker
# ----------------------------------------------
def disconnect():
    client.disconnect()


# ----------------------------------------------
# Converts a Message (encoded in bytes)
# to a string
# ----------------------------------------------
def decode(message_in_bytes):
    return bytes.decode(message_in_bytes)


# ----------------------------------------------
# Checks to see if the connection is working
# ----------------------------------------------
def persistence_check_task():
    global RECEIVED_RECENT_MESSAGE
    
    # Assumes that the connection fails if it does not receive a message since the last persistence check
    while RECEIVED_RECENT_MESSAGE:
        print("Persistence Check PASS:  Received Message in the Past", PERSISTENCE_CHECK_DURATION, "Seconds")
        RECEIVED_RECENT_MESSAGE = False
        time.sleep(PERSISTENCE_CHECK_DURATION)
    
    print("Persistence Check FAIL:  No Message Received in the Past", PERSISTENCE_CHECK_DURATION, "Seconds")
    
    print("  - Halting Listening Loop")
    client.loop_stop()
    
    print("  - Disconnecting from the Broker")
    disconnect()
    
    print("  - Reconnecting to the Broker")
    connect()
    
    print("  - Restarting Listening Service(s)")
    listen()
            

# ----------------------------------------------
# Creates a Thread to Listen Forever
# ----------------------------------------------
def listen_continuously_task():
    global RECEIVED_RECENT_MESSAGE
    
    # Make sure to set this so that you don't fail the test the first time
    RECEIVED_RECENT_MESSAGE = True
    
    # Tells the Listener to Listen Forever
    client.loop_forever()


# ----------------------------------------------
# Listens indefinitely for messages from the
# specified MQTT topics/channels
# ----------------------------------------------
def listen(message_handler_function = None):
    global CHANNELS, MESSAGE_HANDLER
        
    # Updates the Message Handler Function
    if message_handler_function != None:
        MESSAGE_HANDLER = message_handler_function
    
    # Creates a Thread that Listens
    listen_thread = Thread(target=listen_continuously_task)
    listen_thread.start()
    
    # Creates a Thread to Checks on the Health of the Connection
    persistence_thread = Thread(target=persistence_check_task)
    persistence_thread.start()
    

# ----------------------------------------------
# Main Script
# Initiaizates Default Values
# ----------------------------------------------

# Sets Up Event Handlers
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

if DEBUG:
    print("MQTT Comm Initiaized.  Waiting for connect()")
