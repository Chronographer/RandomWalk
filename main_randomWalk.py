import matplotlib.pyplot as plt
import walkerObject


startPosition = 0  # the starting position of the walker (the walkers position is reset to this after each run)
walkLength = 1000   # the number of steps taken by the walker object for each run
numberOfRuns = 1000  # the number of runs the walker will perform
minStepSize = -1  # the lower bound of the possible step size using walkerObject.walkUniform()
maxStepSize = 1   # the upper bound of the possible step size using walkerObject.walkUniform()
stepRange = 1     # the magnitude of the min/max step size using walkerObject.walkRange()
numberOfHistogramBins = 500  # the number of bins to be used in function plotHistogramAveragePosition()

walker1 = walkerObject.walker(startPosition, walkLength)
walker2 = walkerObject.walker(startPosition, walkLength)


def compareMultipleWalkers(drunk1, drunk2):  # Plots the position of two walkers over time on the same graph.
    drunk1.reset()  # Always reset the information held in a walker before using it to remove any possibility of influencing...
    drunk2.reset()  # ... the current walk with a previous one.
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


def plotAverageDisplacementVsTime(drunk):
    runList = []  # list to hold integers from 0 to numberOfRuns, used for plotting purposes
    meanDisplacementSquaredList = []
    for i in range(0, walkLength):
        meanDisplacementSquaredList.append(0)
        runList.append(i)
    for i in range(0, numberOfRuns):
        drunk.walkUniform(minStepSize, maxStepSize)
        for index in range(0, walkLength):
            meanDisplacementSquaredList[index] = (meanDisplacementSquaredList[index] + drunk.displacementSquaredList[index])
        drunk.reset()
    for i in range(0, walkLength):
        meanDisplacementSquaredList[i] = meanDisplacementSquaredList[i] / numberOfRuns
    plt.plot(runList, meanDisplacementSquaredList, 'b.')
    plt.suptitle("Average displacement squared vs time\nfor multiple runs")
    plt.xlabel("Step number")
    plt.ylabel("Displacement squared")
    print("step_number", "average_displacement_squared")
    for i in range(0, len(runList)):
        print(runList[i], meanDisplacementSquaredList[i])
    plt.ylim(0, 1000)  # manually setting the y axis range provides a more intuitive sense of the graphs behavior than matplotlib's default auto-scaling in this particular case.
    plt.grid(True)
    plt.show()


def plotAveragePositionEachRun(drunk):  # Plots the average position of a walker at the end of its walk for numberOfRuns walks.
    masterList = drunk.computeAveragePositionForMultipleRuns(minStepSize, maxStepSize, numberOfRuns)
    runList = masterList[0]
    averageList = masterList[1]
    plt.plot(runList, averageList)
    plt.plot(runList, averageList, 'b.')
    plt.suptitle("Average position of the walker at the end of each walk")
    plt.ylabel("Average run position")
    plt.xlabel("Run number")
    plt.grid(True)
    plt.show()


def plotHistogramAveragePosition(drunk, numberOfBins):  # Plots the average position of a walker at the end of its walk as a histogram for a number of walks.
    masterList = drunk.computeAveragePositionForMultipleRuns(minStepSize, maxStepSize, numberOfRuns)
    averageList = masterList[1]
    plt.hist(averageList, numberOfBins)
    plt.suptitle("histogram of average position after each run")
    plt.xlabel("average position after run")
    plt.ylabel("number of runs in respective range")
    plt.grid(False)
    plt.show()


def plotPositionAtEndOfEachRun(drunk):  # Plots the final position of the walker at the end of each run.
    finalPositionList = []
    runList = []
    for i in range(0, numberOfRuns):
        drunk.walkUniform(minStepSize, maxStepSize)
        finalPositionList.append(drunk.position)
        runList.append(i)
        drunk.reset()
    plt.plot(runList, finalPositionList)
    plt.plot(runList, finalPositionList, 'b.')
    plt.suptitle("Final position of the walker at the end of each walk")
    plt.ylabel("Final run position")
    plt.xlabel("Run number")
    plt.grid(True)
    plt.show()


def plotPositionAtEndOfRunHistogram(drunk, numberOfBins):  # Plots the final position of the walker at the end of each walk as a histogram for a number of runs.
    finalPositionList = []
    runList = []
    for i in range(0, numberOfRuns):
        drunk.walkUniform(minStepSize, maxStepSize)
        finalPositionList.append(drunk.position)
        runList.append(i)
        drunk.reset()
    plt.hist(finalPositionList, numberOfBins)
    plt.suptitle("histogram of final position after each run")
    plt.xlabel("final position after run")
    plt.ylabel("number of runs in respective range")
    plt.grid(False)
    plt.show()


compareMultipleWalkers(walker1, walker2)
plotAverageDisplacementVsTime(walker1)
# plotAveragePositionEachRun(walker1)
# plotHistogramAveragePosition(walker1, numberOfHistogramBins)
# plotPositionAtEndOfEachRun(walker1)
# plotPositionAtEndOfRunHistogram(walker1, numberOfHistogramBins)
