import vector
from vector import *

import tingbot
from tingbot import screen

class Orbiter:
    def __init__(self, _centerX, _centerY, _radius, _size, _phase, _speed):
        self.centerCoordinates = Vector(_centerX, _centerY)
        self.orbiterCoordinates = rotateVector(Vector(_radius,0),_phase)
        self.size = _size
        self.speed = _speed
        
    def plot(self):
        
        pos = addVectors(self.centerCoordinates, self.orbiterCoordinates)
        
        screen.circle(
            xy = (pos.x, pos.y),
            size = tuple([self.size]*2),
            color = 'white',
            align = 'center',
        )
        
    def update(self):
        self.orbiterCoordinates.rotate(self.speed)