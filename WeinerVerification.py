from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
from WeinerGenerator import getWeiner, getWeinerSubset
from scipy.stats import norm
import math

from tqdm import tqdm
import time

def plotWeinerSteps(steps, tend, maxsteps):
    ts, ws, dws, dt = getWeiner(steps, tend)

    #fig, (fig1, fig2) = plt.subplots(1, 2)	# subplots(row, columns)

    plt.plot(ts, ws, color=((maxsteps-steps)/maxsteps, 0, steps/maxsteps))
    #fig2.scatter(ts, dws)

def plotRealizationDistribution(steps, realizations):
    fig, (fig1, fig2) = plt.subplots(1, 2)	# subplots(row, columns)
    endpoints = []
    for realization in range(realizations):
        ts, ws, dws, dt = getWeiner(steps, 10, realization = realization)
        fig1.plot(ts, ws)
        endpoints.append(ws[-1])

    mu, std = norm.fit(endpoints)
    sigma = math.sqrt(std)
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    y = norm.pdf(x, mu, sigma)
    fig2.plot(x, y)

    return x,y

def getRealizationDistribution(steps, realizations):
    endpoints = []
    for realization in range(realizations):
        ts, ws, dws, dt = getWeiner(steps, 10, realization = realization)
        endpoints.append(ws[-1])

    mu, std = norm.fit(endpoints)
    sigma = math.sqrt(std)
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    y = norm.pdf(x, mu, sigma)

    return x,y
    
maxsteps = 50
#for steps in range(maxsteps):
   # plotWeinerSteps(maxsteps-steps, 10, maxsteps)


#x2,y2 = plotRealizationDistribution(100, 1000)

fig3 = plt.figure()

start = time.time()
for steps in tqdm(np.arange(2,maxsteps)):
    x,y = getRealizationDistribution(steps, 5000)
    plt.plot(x, y, color=((maxsteps-steps)/maxsteps, 0, steps/maxsteps), label = steps)
    print(steps)

print(f"runtime {start - time.time()}")
#plt.plot(x2, y2, label = "100")

plt.legend()
plt.show()