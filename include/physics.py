'''''
import include.Character
import include.rooms
import numpy as np

G = 150

WIDTH = 576
HEIGHT = int(WIDTH * 2 / 3)


class physics:

    def __init__(self, c: include.Character.Player):
        self.c = c
        self.in_air_time = 0

    def __in_air(self, lat, m: include.rooms.Room, c_bottom):
        h = self.c.status_avatar.get_height()
        w = self.c.status_avatar.get_width()
        # print((int((self.c.x + w)/WIDTH*18-1), (int((self.c.y + h)/HEIGHT*12))))
        # if  m.room_structure.get((int((self.c.x + w) / WIDTH * 18 - 1),\
           # (int((self.c.y + h) / HEIGHT * 12))), None) or 
        if c_bottom:
            self.in_air_time = 0
        else:
            self.in_air_time += lat


    def physic_handling(self, latency: float,m:include.rooms.Room,c_bottom):
        self.__in_air(latency,m,c_bottom)
        return self.c.y + 0.25 * G * (self.in_air_time**2)

'''''
import include.Character
import include.rooms
import numpy as np

G = 9.8
WIDTH = 1000
HEIGHT = int(WIDTH * 2 / 3)


class physics:

    def __init__(self, c: include.Character.Player):
        self.c = c
        self.in_air_time = 0

    def __in_air(self, lat, m: include.rooms.Room):
        h = self.c.status_avatar.get_height()
        w = self.c.status_avatar.get_width()
        # print((int((self.c.x + w)/WIDTH*18-1), (int((self.c.y + h)/HEIGHT*12)-1)))
        if m.room_structure.get((int((self.c.x + w) / WIDTH * 18 - 1), (int((self.c.y + h) / HEIGHT * 12))), None):
            self.in_air_time = 0
        else:
            self.in_air_time += lat
        print(self.in_air_time)

    def physic_handling(self, latency: float,m:include.rooms.Room):
        self.__in_air(latency,m)
        return self.c.y + 0.5 * G * (self.in_air_time**2)