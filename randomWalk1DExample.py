"""Create random walk and demonstrate <x^2(i)> ~ t.

Here I am only using uniform float random numbers on the interval [0,1),
so I only import the routine "random_sample"  It can be used to generate
a single random number or a whole series of them.

Antonio Cancio
Phys 336/536
March 28, 2015
"""
from vpython import *
import numpy

numberSteps = 1000
numberRuns = 10000
print("#Measurement of <x> and <x^2> versus step i for 3D random walk.")
print("# number of steps, number of averaging runs: ", numberSteps, numberRuns)
print("#i, <r>, <r^2>")

# make visual plot
randomPlot = canvas(xtitle='i', ytitle='average', width=600, height=350, background=color.white, foreground=color.black)
randomDots = gdots(color=color.red)
otherRandomDots = gdots(color=color.blue)
theory = gcurve(color=color.black)

# Initialize statistics arrays to zero.
s2walk = numpy.zeros(numberSteps)
swalk = numpy.zeros(numberSteps)


def integer1Dwalk(numberSteps):
    """1D integer random walk of numberSteps steps"""

    # get set of integers -- if u<1/2 take - move, else take + move
    steps = numpy.sign(numpy.random.random_sample(numberSteps) - 0.5)

    # measure position x for each step and place in xWalk
    xwalk = numpy.zeros(numberSteps)
    iStep = 0
    x = 0
    while iStep < numberSteps:
        xwalk[iStep] = x
        x = x + int(steps[iStep])
        iStep += 1

    return xwalk


def uniform1Dwalk(nsteps, stepRange=1.0):
    """1D uniform random walk of length numberSteps on [-stepRange, stepRange)"""

    # get random set numbers from -stepRange to stepRange.
    steps = 2.0 * stepRange * (numpy.random.random_sample(nsteps) - 0.5)

    # measure position x for each step and place in xWalk
    xwalk = 0.0*numpy.zeros(nsteps)  # make sure this is a float.
    iStep = 0
    x = 0.0
    while iStep < nsteps:
        xwalk[iStep] = x
        x = x + steps[iStep]
        iStep += 1

    return xwalk


# Do nrun runs:
iRun = 0
while iRun < numberRuns:
    # Do this line to have integer steps.
    #xWalk = integer1Dwalk(numberSteps)
    # Add this to do in 3 D
    #ywalk = integer1Dwalk(numberSteps)
    #zwalk = integer1Dwalk(numberSteps)
    # Do this to have uniform steps.
    xwalk = uniform1D(numberSteps)

    # add xWalk to statistics sum used to get an average of x versus step
    swalk = swalk + xwalk  # shortcut notations used below
    # add xWalk**2 to statistics sum used to get an average of x^2 versus step
    s2walk += xwalk*xwalk
    #s2walk += xWalk*xWalk + ywalk*ywalk + zwalk*zwalk

    iRun += 1

# average of x = sum of x_i / N, N = number of runs you are averaging over
xAverage = swalk / numberRuns
x2average = s2walk / numberRuns

# plot averages
for i in range(numberSteps):
    print(i, xAverage[i], x2average[i])
    randomDots.plot(pos=(i, x2average[i]))
    otherRandomDots.plot(pos=(i, xAverage[i]))
    theory.plot(pos=(i, i))

