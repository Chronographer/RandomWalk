"""Create random walk and demonstrate <x^2(i)> ~ t.

Here I am only using uniform float random numbers on the interval [0,1),
so I only import the routine "random_sample"  It can be used to generate
a single random number or a whole series of them.

Antonio Cancio
Phys 336/536
March 28, 2015
"""
from vpython import *
#need this to call random number generator and do array math
import numpy

nsteps = 1000
nruns = 10000
print ("#Measurement of <x> and <x^2> versus step i for 3D random walk.")
print ("# number of steps, number of averaging runs: ", nsteps, nruns)
print ("#i, <r>, <r^2>")

##make visual plot
random_plot = canvas (xtitle='i',
                      ytitle='average',
                      width=600, height=350,
                      background=color.white, foreground=color.black)
random_dots = gdots(color=color.red)
other_random_dots = gdots(color=color.blue)
theory = gcurve(color=color.black)

#Intialize statistics arrays to zero.
s2walk = numpy.zeros(nsteps)
swalk = numpy.zeros(nsteps)

def integer1Dwalk( nsteps ):
    """1D integer random walk of nsteps steps"""

    #get set of integers -- if u<1/2 take - move, else take + move
    steps = numpy.sign( numpy.random.random_sample(nsteps) - 0.5 )

    # measure position x for each step and place in xwalk
    xwalk = numpy.zeros(nsteps)
    istep = 0
    x = 0
    while ( istep < nsteps ):
        xwalk[istep] = x
        x = x + int(steps[istep])
        istep += 1

    return xwalk

def uniform1Dwalk( nsteps, steprange=1.0 ):
    """1D uniform random walk of length nsteps on [-steprange,steprange)"""

    #get random set numbers from -steprange to steprange.
    steps = 2.0*steprange*( numpy.random.random_sample(nsteps) - 0.5 )

    # measure position x for each step and place in xwalk
    xwalk = 0.0*numpy.zeros(nsteps)    #make sure this is a float.
    istep = 0
    x = 0.0
    while ( istep < nsteps ):
        xwalk[istep] = x
        x = x + steps[istep]
        istep += 1

    return xwalk

#Do nrun runs:
irun = 0
while ( irun < nruns ):
    # Do this line to have integer steps.
    #xwalk = integer1Dwalk( nsteps )
    # Add this to do in 3 D
    ##ywalk = integer1Dwalk( nsteps )
    ##zwalk = integer1Dwalk( nsteps )
    # Do this to have uniform steps.
    xwalk = uniform1D( nsteps )

    # add xwalk to statistics sum used to get an average of x versus step
    swalk = swalk + xwalk  ### shortcut notations used below
    # add xwalk**2 to statistics sum used to get an average of x^2 versus step
    s2walk += xwalk*xwalk
    #s2walk += xwalk*xwalk + ywalk*ywalk + zwalk*zwalk

    irun += 1

#average of x = sum of x_i / N, N = number of runs you are averaging over
xaverage = swalk/nruns
x2average = s2walk/nruns

#plot averages
for i in range(nsteps):
    print (i, xaverage[i], x2average[i])
    random_dots.plot( pos=(i, x2average[i]) )
    other_random_dots.plot( pos=(i, xaverage[i]) )
    theory.plot( pos=(i,i) )

