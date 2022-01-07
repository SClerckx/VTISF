
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import random as random
import math as math
import os

def generateWeiner(wstart, steps, tend, dt):
    ts = np.linspace(0, tend, steps)
    ws = []
    dws = []
    w = wstart
    for t in ts:
        ws.append(w)
        dw = random.gauss(0,1)*math.sqrt(dt)
        dws.append(dw)
        w += dw
    ws = np.array(ws)
    dws = np.array(dws)
    return ts, ws, dws

def getWeiner(steps, tend, realization = 0):
    """
    n gives a new realization
    """
    dt = tend/steps
    filepath = os.path.join(os.path.join(os.path.abspath(os.getcwd()), "WeinerRealizations"), f"{steps},{tend},{dt:e}")
    filename = str(realization)
    fullname = os.path.join(filepath, filename)
    if os.path.exists(fullname):
        ts, ws, dws = np.loadtxt(fullname)
    else:
        ts, ws, dws = generateWeiner(0, steps, tend, dt)
        saveWeiner(filepath, filename, fullname, ts, ws, dws, dt)

    return ts, ws, dws, dt

def saveWeiner(filepath, filename, fullname, ts, ws, dws, dt):
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    f = open(fullname, 'wb')
    np.savetxt(f, (ts,ws,dws))
    f.close()
