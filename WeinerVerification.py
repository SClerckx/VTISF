import numpy as np
import matplotlib.pyplot as plt
from WeinerGenerator import getWeiner

def plotWeiner(steps, tend, maxsteps):
    ts, ws, dws, dt = getWeiner(steps, tend)

    #fig, (fig1, fig2) = plt.subplots(1, 2)	# subplots(row, columns)

    plt.plot(ts, ws, color=((maxsteps-steps)/maxsteps, 0, steps/maxsteps))
    #fig2.scatter(ts, dws)

maxsteps = 1000
for steps in range(maxsteps):
    plotWeiner(maxsteps-steps, 10, maxsteps)

plt.show()