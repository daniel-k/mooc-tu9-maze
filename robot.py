#!/usr/bin/env python3


def message_handler(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


if __name__ == "__main__":
    print("This file should be imported")
