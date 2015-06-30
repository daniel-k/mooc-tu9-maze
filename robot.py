#!/usr/bin/env python3

import json
from enum import Enum
from config import Cmd, command, STATE_TOPIC

class Field(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []
        self.pending_visits = [Cmd.go_north, Cmd.go_south, Cmd.go_east, Cmd.go_west]

    def next_visit(self):
        try:
            return self.pending_visits.pop()
        except:
            return Cmd.nop

class Maze(object):

    def __init__(self):
        self.maze = {}

    def get_field(self, x, y):
        try:
            return self.maze[(x, y)]
        except:
            return None

    def add_field(self, x, y):
        field = Field(x,y)
        self.maze[(x, y)] = field
        return field


maze = Maze()

def message_handler(client, userdata, msg):

    if msg.topic == STATE_TOPIC:
        payload = msg.payload.decode("utf-8")
        state = json.loads(payload)
        position = state['position']
        x = int(position['x'])
        y = int(position['y'])

        print("x: {} y: {}".format(x, y))

        current = maze.get_field(x, y)
        if current is None:
            current = maze.add_field(x, y)

        next = current.next_visit()
        if next is not Cmd.nop:
            command(client, next)
        else:
            # backtracking here
            print("Preliminary end")

    else:
        print("Unknown topic {}".format(msg.topic))

if __name__ == "__main__":
    print("This file should be imported")
