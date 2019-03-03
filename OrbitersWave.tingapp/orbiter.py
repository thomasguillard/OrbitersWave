import vector
from vector import *

import tingbot
from tingbot import screen

import remap
from remap import *

import colorConverter
from colorConverter import *

import math
from math import sqrt, atan2, pi

class Orbiter:
    def __init__(self, _centerX, _centerY, _radius, _size, _phase, _speed):
        self.centerCoordinates = Vector(_centerX, _centerY)
        self.orbiterCoordinates = rotateVector(Vector(_radius,0),_phase)
        self.size = _size
        self.speed = _speed
        #self.hue = remap(atan2(screen.height/2-_centerY,screen.width/2-_centerX),-pi,pi,0,360)
        self.hue = remap(_centerX+_centerY,0,screen.width+screen.height,0,360)
        self.hueOffset = 0
        self.color = HSVToRGB(self.hue + self.hueOffset, 1, 1)
        
    def plot(self):
        
        pos = addVectors(self.centerCoordinates, self.orbiterCoordinates)
        
        screen.circle(
            xy = (pos.x, pos.y),
            size = tuple([self.size]*2),
            color = self.color,
            align = 'center',
        )
        
    def update(self):
        self.orbiterCoordinates.rotate(self.speed)
        self.hueOffset = (self.hueOffset+5)%360
        self.color = HSVToRGB(self.hue+self.hueOffset, 1, 1)
        #self.hue = (self.hue+10)%360