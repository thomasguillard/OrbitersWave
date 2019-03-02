import math
from math import sqrt, cos, sin

class Vector:
    '''
        Home made 2D Vector library
        Errors are more than likely, use wisely
    '''
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
    
    def info(self):
        return [self.x, self.y]
        
    def add(self, other):
        self.x += other.x
        self.y += other.y

    def sub(self, other):
        self.x -= other.x
        self.y -= other.y
            
    def mul(self, factor):
        self.x *= factor
        self.y *= factor

    def div(self, divisor):
        self.x /= divisor
        self.y /= divisor
           
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def mag2(self):
        return pow(self.x, 2) + pow(self.y, 2)
    
    def mag(self):
        return sqrt(self.mag2())
    
    def norm(self):
        v = divVector(self, self.mag())
        self.x = v.x
        self.y = v.y
        
    def rotate(self, angle):
        cs = cos(angle)
        sn = sin(angle)
        nx = self.x * cs - self.y * sn
        ny = self.x * sn + self.y * cs
        self.x = nx
        self.y = ny

def subVectors(v1, v2):
    newx = v1.x - v2.x
    newy = v1.y - v2.y
    return Vector(newx, newy)

def addVectors(v1, v2):
    newx = v1.x + v2.x
    newy = v1.y + v2.y
    return Vector(newx, newy)

def mulVector(v, factor):
    newx = factor * v.x
    newy = factor * v.y
    return Vector(newx, newy)

def divVector(v, divisor):
    newx = v.x / divisor
    newy = v.y / divisor
    return Vector(newx, newy)
    
def rotateVector(v, angle):
    cs = cos(angle)
    sn = sin(angle)
    nx = v.x * cs - v.y * sn
    ny = v.x * sn + v.y * cs
    return Vector(nx, ny)