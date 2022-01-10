import numpy as np
import matplotlib.pyplot as plt
from WeinerGenerator import getWeiner
from scipy.stats import norm
import math

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
        endpoints.append(dws[len(dws)-1])

    mu, std = norm.fit(endpoints)
    sigma = math.sqrt(std)
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    fig2.plot(x, norm.pdf(x, mu, sigma))
    
maxsteps = 1000
for steps in range(maxsteps):
    plotWeinerSteps(maxsteps-steps, 10, maxsteps)

plotRealizationDistribution(5, 1000000)
plotRealizationDistribution(100, 1000)

plt.show()