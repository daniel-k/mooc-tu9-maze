#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
from robot import message_handler
from config import HOST, NAME, INIT_TOPIC, STATE_TOPIC

###############################################

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    print("subscribing to {}".format(STATE_TOPIC))
    client.subscribe(STATE_TOPIC)

    # send initialization command
    client.publish(INIT_TOPIC, NAME)
    
###############################################

# connect to game
client = mqtt.Client()

# subscribe in on_connect method
client.on_connect = on_connect

# connect message handler
client.on_message = message_handler

# connect to to broker
client.connect(HOST)

# main loop
client.loop_start()
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break
client.loop_stop()

# tidy up
client.disconnect()
