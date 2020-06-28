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

npoints = 100     # nr of steps in walk
steprange = 1.0
nruns = 10000      # nr of walks to do for statistics.
p = 0.5          # prob of moving right.

# Create arrays to store statistics:
sumarray = np.zeros(npoints)
s2array = np.zeros(npoints)

for irun in range(nruns):

    # Start a new random walk
    istep = 0             # start count of number of steps
    x = 0.0               # initial position
    xwalk = []

    # Do the walk -- move x by desired steps.
    while istep < npoints:
        u = np.random.random_sample()
        if u < p:
            x = x + steprange
        else:
            x = x - steprange
        xwalk.append(x)
        istep += 1
    xwalk = np.array(xwalk)

    # accumulate sums needed to do statistics.  Done as array, all at once.
    sumarray = sumarray + xwalk
    s2array = s2array + xwalk**2

# At end of all runs, divide by total number of walks to get average,
# and variance (sigma**2).  This is done for all points all at once.
xaverage = sumarray/nruns
x2average = s2array/nruns
sigmasquared = x2average - xaverage*xaverage

# Make plot to visualize
plt.plot(range(npoints), xaverage, label="average")
plt.plot(range(npoints), sigmasquared, label="variance")
plt.legend()
plt.xlabel("# of steps")
plt.ylabel("displacement")
plt.show()
