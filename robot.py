#!/usr/bin/env python3

from config import Cmd, command


def message_handler(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    command(client, Cmd.go_north)

if __name__ == "__main__":
    print("This file should be imported")
