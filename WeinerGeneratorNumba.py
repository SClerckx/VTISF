
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import random as random
import math as math
import os
from pyrsistent import v

from sympy import false
from numba import njit

@njit
def generateWeiner(wstart, steps, tend, dt):
    ts = np.linspace(0, tend, steps+1) #items = steps + 1
    ws = np.zeros(len(ts))
    dws = np.zeros(len(ts))
    w = wstart
    for i, t in enumerate(ts):
        ws[i] = w
        dw = random.gauss(0,1)*math.sqrt(dt)
        dws[i] = dw
        #dws.append(dw)
        w += dw
    """
    example:
    ts:  0,    1,     2
    ws:  0,    0.45,  0.67, (0.55 gets calculated but not stored)
    dws: 0.45, 0.22, -0.12 <-- this last value gets used to calculate the 0.55 but is actually useless because the 0.55 is not stored
    """
    #ws = np.array(ws)
    #dws = np.array(dws)
    return ts, ws, dws

def getWeiner(steps, tend, realization, noIO = False):
    """
    new realization index gives a new realization
    """
    dt = tend/steps
    filepath = os.path.join(os.path.join(os.path.abspath(os.getcwd()), "WeinerRealizations"), f"{steps},{tend},{dt:e}")
    filename = str(realization) #+ ".csv"
    fullname = os.path.join(filepath, filename)

    if noIO: 
        ts, ws, dws = generateWeiner(0, steps, tend, dt)
        #saveWeiner(filepath, filename, fullname, ts, ws, dws, dt)
    else:
        if os.path.exists(fullname):
            ts, ws, dws = np.load(fullname, allow_pickle = True)
        else:
            ts, ws, dws = generateWeiner(0, steps, tend, dt)
            saveWeiner(filepath, filename, fullname, ts, ws, dws, dt)

    return ts, ws, dws, dt

def saveWeiner(filepath, filename, fullname, ts, ws, dws, dt):
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    f = open(fullname, 'wb')
    np.save(f, (ts,ws,dws))
    f.close()

def getWeinerSubset(Nth, baseSteps, baseTend, baseRealization):
    """
    No noIO option because that would mean subsets of the same baseRealizaiton would be independent from each other
    to use noIO option, use getWeinerSubsets
    Nth, get every nth item from set
    dt = basedt * Nth
    """
    assert baseSteps%Nth == 0

    baseTs, baseWs, baseDws, baseDt = getWeiner(baseSteps, baseTend, baseRealization)

    subTs = baseTs[0::Nth] #start_from = 0 every_nth = 2 a_list[start_from::every_nth]
    subWs = baseWs[0::Nth]
    subDws = np.diff(subWs) #for i in subWs: subDws.append(subWs[i+1] - subWs[i])
    subDws = np.append(subDws, 0) #add last useless value to dws
    subDt = baseDt * Nth

    return  subTs, subWs, subDws, subDt

def getWeinerSubsets(Nths, baseSteps, baseTend, baseRealization, noIO = False):
    """
    Get lots of subsets for a given baseRealization
    Nth, get every nth item from set
    dt = basedt * Nth
    """
    subsets = []
    for Nth in Nths:
        assert baseSteps%Nth == 0

        baseTs, baseWs, baseDws, baseDt = getWeiner(baseSteps, baseTend, baseRealization, noIO = False)

        subTs = baseTs[0::Nth] #start_from = 0 every_nth = 2 a_list[start_from::every_nth]
        subWs = baseWs[0::Nth]
        subDws = np.diff(subWs) #for i in subWs: subDws.append(subWs[i+1] - subWs[i])
        subDws = np.append(subDws, 0) #add last useless value to dws
        subDt = baseDt * Nth

        subset = {}
        subset['subTs'] = subTs
        subset['subWs'] = subWs
        subset['subDws'] = subDws
        subset['subDt'] = subDt

        subsets.append(subset)

    return  subsets

def constructWeinerSubset(Nth, baseTs, baseWs, baseDws, baseDt):
    assert (len(baseTs)-1)%Nth == 0, f"{len(baseTs)-1} not divisible by {Nth}"

    subTs = baseTs[0::Nth] #start_from = 0 every_nth = 2 a_list[start_from::every_nth]
    subWs = baseWs[0::Nth]
    subDws = np.diff(subWs) #for i in subWs: subDws.append(subWs[i+1] - subWs[i])
    subDws = np.append(subDws, 0) #add last useless value to dws
    subDt = baseDt * Nth

    return  subTs, subWs, subDws, subDt