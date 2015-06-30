#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from enum import Enum
from robot import message_handler

# MQTT Broker
HOST = "iot.eclipse.org"

# name of client
NAME="JHGKJhskjdhfgksjdhg"

# topic to initialize new game, send <id> as payload
INIT_TOPIC = "botgrid/init"

# robot is sending state JSON-formatted to this topic
STATE_TOPIC = "botgrid/{}/state".format(NAME)

# topic to send commands to robot
CMD_TOPIC = "botgrid/{}/command".format(NAME)

# commands that can be issued to the robot
class Cmd(Enum):
    go_north = "n"
    go_south = "s"
    go_east  = "e"
    go_west  = "w"
    reset    = "r"

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

def cmd(cmd):
    global client
    if not isinstance(cmd, Cmd):
        raise Exception("'cmd' is not an instance of Cmd")
    
    client.publish(CMD_TOPIC, cmd.value)

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
client.loop_forever()

# tidy up
client.disconnect()
