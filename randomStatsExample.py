"""Create random walk and demonstrate <x^2(i)> ~ t.

Here I am only using uniform float random numbers on the interval [0,1),
so I only import the routine "random_sample"  It can be used to generate
a single random number or a whole series of them.

Antonio Cancio
Phys 336/536
March 29, 2020
"""
import numpy as np
import matplotlib.pyplot as plt

numberPoints = 100  # number of steps in walk
stepRange = 1.0
numberRuns = 10000  # number of walks to do for statistics.
p = 0.5  # probability of moving right.

# Create arrays to store statistics:
sumArray = np.zeros(numberPoints)
s2array = np.zeros(numberPoints)

for iRun in range(numberRuns):

    # Start a new random walk
    iStep = 0  # start count of number of steps
    x = 0.0  # initial position
    xWalk = []

    # Do the walk -- move x by desired steps.
    while iStep < numberPoints:
        u = np.random.random_sample()
        if u < p:
            x = x + stepRange
        else:
            x = x - stepRange
        xWalk.append(x)
        iStep += 1
    xWalk = np.array(xWalk)

    # accumulate sums needed to do statistics.  Done as array, all at once.
    sumArray = sumArray + xWalk
    s2array = s2array + xWalk ** 2

# At end of all runs, divide by total number of walks to get average,
# and variance (sigma**2).  This is done for all points all at once.
xAverage = sumArray / numberRuns
x2average = s2array / numberRuns
sigmaSquared = x2average - xAverage * xAverage

# Make plot to visualize
plt.plot(range(numberPoints), xAverage, label="average")
plt.plot(range(numberPoints), sigmaSquared, label="variance")
plt.legend()
plt.xlabel("# of steps")
plt.ylabel("displacement")
plt.show()
