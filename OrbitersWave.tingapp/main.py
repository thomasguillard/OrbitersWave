import tingbot
from tingbot import *

import orbiter
from orbiter import *

import math
from math import pi


orbitersSpeed = pi/10
orbitersSize=4
orbitersRadius=10
orbitersRows=10
orbitersCols=15

orbiters=[]

for i in xrange(orbitersCols):
    for j in xrange(orbitersRows):
        orbiters.append(Orbiter(i*screen.width/(orbitersCols-1), j*screen.height/(orbitersRows-1), orbitersRadius, orbitersSize, (i+j)*.5, orbitersSpeed))

@every(seconds=1.0/30)
def loop():
    screen.fill(color='black')
    
    for orbiter in orbiters:
        orbiter.update()
        orbiter.plot()

tingbot.run()