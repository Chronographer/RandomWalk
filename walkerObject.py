import numpy as np


class walker:
    def __init__(self, startPosition, walkSize):
        self.walkSize = walkSize
        self.startPosition = startPosition
        self.position = startPosition
        self.positionList = []
        self.displacementSquaredList = []
        self.stepList = []

    def walkUniform(self, minStep, maxStep):
        randomStepList = np.random.uniform(minStep, maxStep, self.walkSize)
        for i in range(0, self.walkSize):
            self.stepList.append(i)
            self.positionList.append(self.position)
            self.displacementSquaredList.append(self.position ** 2)
            self.position = self.position + randomStepList[i]

    def walkRange(self, stepRange):
        for i in range(0, self.walkSize):
            self.stepList.append(i)
            self.positionList.append(self.position)
            self.displacementSquaredList.append(self.position ** 2)
            self.position = self.position + (2.0 * stepRange * (np.random.random_sample() - 0.5))

    def computeAveragePositionForMultipleRuns(self, minStepSize, maxStepSize, numberOfRuns):
        averageList = []
        runList = []
        for i in range(0, numberOfRuns):
            self.walkUniform(minStepSize, maxStepSize)
            average = sum(self.positionList) / len(self.positionList)
            averageList.append(average)
            runList.append(i)
            self.reset()
        returnList = [runList, averageList]
        return returnList

    def reset(self):
        self.positionList.clear()
        self.stepList.clear()
        self.displacementSquaredList.clear()
        self.position = self.startPosition
