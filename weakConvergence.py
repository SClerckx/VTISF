
import numpy as np
import matplotlib.pyplot as plt
import random as random
import math as math

b = -0.05

t0 = 0
tend = 1
steps = 100000
dt = (tend-t0)/steps
h = 1.0
threshold = h/2
Kbar = 1.0

def K(z):
    if z <= threshold:
        K = z*(h-2*z)*Kbar
    else:
        K = (h-z)*(-h+2*z)*Kbar
    return K

def dKdz(z):
    if z <= threshold:
        dKdz = h-4*z
    else:
        dKdz = 3*h-4*z
    return dKdz

class Particle():
    def __init__(self, z):
        self.z = z

    def simulate(self, dt):
        z0 = self.z
        z1 = z0 + dKdz(z0)*dt + math.sqrt(2*K(z0))*random.gauss(0,1)*math.sqrt(dt)#*randomFactor
        if z1 < 0:
            z1 = -z1
        if z1 > h:
            z1 = 2*h-z1
        self.z = z1 
        return z1

def plotRealization(startloc):
    s0 = 1
    s1 = 0
    ts = np.linspace(t0, tend, steps)
    Ss = []
    for t in ts:
        if t == t0:
            particle = Particle(startloc)
        else:
            s1 = particle.simulate(dt)
        Ss.append(s1)

    plt.plot(ts,Ss)

for i in range(20):
    plotRealization(1)

plt.legend()
plt.show()
