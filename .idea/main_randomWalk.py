import matplotlib.pyplot as plt
import numpy as np
import walkerObject


startPosition = 0  # the starting position of the walker (the walkers position is reset to this after each run)
walkLength = 100   # the number of steps taken by the walker object for each run
numberOfRuns = 1000  # the number of runs the walker will perform
minStepSize = -1  # the lower bound of the possible step size using walkerObject.walkUniform()
maxStepSize = 1   # the upper bound of the possible step size using walkerObject.walkUniform()
stepRange = 1     # the magnitude of the min/max step size using walkerObject.walkRange()
averageList = []  # list containing the average position of the walker for each run

drunk1 = walkerObject.walker(startPosition, walkLength)
drunk2 = walkerObject.walker(startPosition, walkLength)

def compareMultipleWalkers(drunk1, drunk2):
    drunk1.reset()
    drunk2.reset()
    drunk1.walkUniform(minStepSize, maxStepSize)
    drunk2.walkUniform(minStepSize, maxStepSize)
    plt.plot(drunk1.stepList, drunk1.positionList)
    plt.plot(drunk1.stepList, drunk1.positionList, 'b.')
    plt.plot(drunk2.stepList, drunk2.positionList)
    plt.plot(drunk2.stepList, drunk2.positionList, 'r.')
    plt.grid(True)
    plt.suptitle("Two random walkers in 1 dimension\nPosition vs time")
    plt.xlabel("Step number")
    plt.ylabel("Position")
    plt.show()

    plt.plot(drunk1.stepList, drunk1.displacementSquaredList)
    plt.plot(drunk1.stepList, drunk1.displacementSquaredList, 'b.')
    plt.plot(drunk2.stepList, drunk2.displacementSquaredList)
    plt.plot(drunk2.stepList, drunk2.displacementSquaredList, 'r.')
    plt.grid(True)
    plt.suptitle("Two random walkers in 1 dimension\nDisplacement squared vs time")
    plt.xlabel("Step number")
    plt.ylabel("Displacement squared")
    plt.show()

def plotAverageDisplacementVsTime(drunk):
    runList = []  # list to hold integers from 0 to numberOfRuns, used for plotting purposes
    meanDisplacementSquaredList = []
    for i in range(0, walkLength):
        meanDisplacementSquaredList.append(0)
        runList.append(i)
    for i in range(0, numberOfRuns):
        drunk.walkUniform(minStepSize, maxStepSize)
        for index in range(0, walkLength):
            meanDisplacementSquaredList[index] = (meanDisplacementSquaredList[index] + drunk.displacementSquared[index])
        drunk.reset()
    for i in range(0, walkLength):
        meanDisplacementSquaredList[i] = meanDisplacementSquaredList[i] / numberOfRuns
    plt.plot(runList, meanDisplacementSquaredList)
    plt.suptitle("Average displacement squared vs time\nfor multiple runs")
    plt.xlabel("Step number")
    plt.ylabel("Displacement squared")
    plt.grid(True)
    plt.show()


#compareMultipleWalkers(drunk1, drunk2)
plotAverageDisplacementVsTime(drunk1)



"""
for i in range(0, numberOfRuns):
    drunk.walkUniform(minStepSize, maxStepSize)
    #drunk.walkRange(stepRange)
    average = sum(drunk.positionList) / len(drunk.positionList)
    #print("average position for run " + str(i) + " is " + str(average))
    averageList.append(average)
    runList.append(i)
    drunk.reset()
"""
"""  ### uncomment to plot the average position at the end of each run for each run in the order the runs occured.
plt.plot(runList, averageList)
plt.plot(runList, averageList, "b.")
plt.ylabel("Average run position")
plt.xlabel("Run number")
plt.grid(True)
plt.show()
"""
"""  ### uncomment to plot a histogram of the average position of a walker for each run for numberOfRuns runs. 
plt.hist(averageList, 500)
plt.suptitle("histogram of avarage position after each run")
plt.xlabel("average position after run")
plt.ylabel("number of runs in respective range")
plt.grid(False)
plt.show()"""