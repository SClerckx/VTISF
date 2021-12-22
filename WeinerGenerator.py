
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import matplotlib.cm as cm
import random as random
import math as math
import os


b = -0.05

t0 = 0
tend = 1
steps = 100000
dt = (tend-t0)/steps
h = 1.0
threshold = h/2
Kbar = 1.0

def generateWeiner(wstart, steps, tend):
    dt = tend/steps
    ts = np.linspace(0, tend, steps)
    ws = []
    w = wstart
    for t in ts:
        ws.append(w)
        w += random.gauss(0,1)*math.sqrt(dt)
    ws = np.array(ws)
    return ts, ws

def getWeiner(steps, tend, n):
    filepath = os.path.join(os.path.abspath(os.getcwd()), str(steps) + "," + str(tend))
    filename = str(n)
    fullname = os.path.join(filepath, filename)
    if os.path.exists(fullname):
        ts,ws = np.loadtxt(fullname)
    else:
        ts, ws = generateWeiner(0, steps, tend)
        saveWeiner(filepath, filename, fullname, ts, ws)

    return ts, ws

def saveWeiner(filepath, filename, fullname, ts, ws):
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    f = open(fullname, 'wb')
    np.savetxt(f, (ts,ws))
    f.close()

def plotRealization(n):
    ts, ws = getWeiner(100000, 10, n)
    
    plt.plot(ts,ws)

for i in range(10):
    plotRealization(i)

plt.legend()
plt.show()
