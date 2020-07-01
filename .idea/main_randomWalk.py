import numpy as np
import walkerObject
import matplotlib.pyplot as plt

startPosition = 0  # the starting position of the walker (the walkers position is reset to this after each run)
walkLength = 1000  # the number of steps taken by the walker object for each run
numberOfRuns = 5000  # the number of runs the walker will perform
minStepSize = -1  # the lower bound of the possible step size using walkerObject.walkUniform()
maxStepSize = 1   # the upper bound of the possible step size using walkerObject.walkUniform()
stepRange = 1     # the magnitude of the min/max step size using walkerObject.walkRange()

averageList = []  # list containing the average position of the walker for each run
runList = []  # list for holding integers from 0 to numberOfRuns, used for plotting purposes.


drunk = walkerObject.walker(startPosition, walkLength)


for i in range(0, numberOfRuns):
    drunk.walkUniform(minStepSize, maxStepSize)
    positionSum = sum(drunk.positionList)
    average = positionSum / len(drunk.positionList)
    #print("average position for run " + str(i) + " is " + str(average))
    averageList.append(average)
    runList.append(i)
    drunk.reset()

    """
    plt.plot(drunk.stepList, drunk.positionList)
    plt.plot(drunk.stepList, drunk.positionList, 'b.')
    plt.xlabel("Step number")
    plt.ylabel("Walker position")
    plt.show()
    """

"""
plt.plot(runList, averageList)
plt.plot(runList, averageList, "b.")
plt.ylabel("Average run position")
plt.xlabel("Run number")
plt.show()
"""

plt.hist(averageList, 100)
plt.suptitle("histogram of avarage position after each run")
plt.xlabel("average position after run")
plt.ylabel("number of runs in respective range")
plt.show()