#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from enum import Enum

# MQTT Broker
HOST = "iot.eclipse.org"

# name of client
NAME="JHGKJhskjdhfgksjdhg"

# topic to initialize new game, send <id> as payload
INIT_TOPIC = "botgrid/init"

# robot is sending state JSON-formatted to this topic
STATE_TOPIC = "botgrid/{}/state"

# topic to send commands to robot
CMD_TOPIC = "botgrid/{}/command"

# commands that can be issued to the robot
class Cmd(Enum):
    go_north = "n"
    go_south = "s"
    go_east  = "e"
    go_west  = "w"
    reset    = "r"

###############################################

def message_handler(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    state = STATE_TOPIC.format(NAME)
    print("subscribing to {}".format(state))
    client.subscribe(state)

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

# start background loop
client.loop_start()

while True:
    try:
        pass
    except:
        break

# tidy up when finished
client.loop_stop()
client.disconnect()
