
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import random as random
import math as math
import os

def generateWeiner(wstart, steps, tend, dt):
    ts = np.linspace(0, tend, steps)
    ws = []
    w = wstart
    for t in ts:
        ws.append(w)
        w += random.gauss(0,1)*math.sqrt(dt)
    ws = np.array(ws)
    return ts, ws

def getWeiner(steps, tend, n = 0):
    """
    n gives a new realization
    """
    dt = tend/steps
    filepath = os.path.join(os.path.abspath(os.getcwd()), f"{steps},{tend},{dt:e}")
    filename = str(n)
    fullname = os.path.join(filepath, filename)
    if os.path.exists(fullname):
        ts,ws = np.loadtxt(fullname)
    else:
        ts, ws = generateWeiner(0, steps, tend, dt)
        saveWeiner(filepath, filename, fullname, ts, ws, dt)

    return ts, ws, dt

def saveWeiner(filepath, filename, fullname, ts, ws, dt):
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    f = open(fullname, 'wb')
    np.savetxt(f, (ts,ws))
    f.close()
