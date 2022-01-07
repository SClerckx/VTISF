
import numpy as np
import matplotlib.pyplot as plt
from WeinerGenerator import getWeiner

def plotWeiner(steps, tend, realization):
    ts, ws, dws, dt = getWeiner(steps, tend, n=realization)

    fig, (fig1, fig2) = plt.subplots(1, 2)	# subplots(row, columns)

    fig1.plot(ts, ws)
    fig2.scatter(ts, dws)

plotWeiner(10, 10, 1)
plotWeiner(100, 10, 1)
plt.show()