#!/usr/bin/env python3

from enum import Enum

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
    nop      = "nop"

###############################################

def command(client, cmd):
    if not isinstance(cmd, Cmd):
        raise Exception("'cmd' is not an instance of Cmd")

    client.publish(CMD_TOPIC, cmd.value)

###############################################

if __name__ == "__main__":
    print('This file should be imported')
