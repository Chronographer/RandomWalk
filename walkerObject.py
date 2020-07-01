import numpy as np


class walker:
    def __init__(self, startPositionVector, walkSize):
        self.walkSize = walkSize
        self.startPosition = startPositionVector
        self.position = startPositionVector
        self.positionList = []
        self.stepList = []

    def walkUniform(self, minStep, maxStep):
        for i in range(0, self.walkSize):
            self.stepList.append(i)
            self.positionList.append(self.position.x)
            self.position.x = self.position.x + np.random.uniform(minStep, maxStep, 1)

    def walkRange(self, stepRange):
        for i in range(0, self.walkSize):
            self.stepList.append(i)
            self.positionList.append(self.position.x)
            self.position.x = self.position.x + (2.0 * stepRange * (np.random.random_sample() - 0.5))
        #self.positionList = 2.0 * stepRange * (np.random.random_sample(self.walkSize) - 0.5)

    def reset(self):
        self.positionList.clear()
        self.stepList.clear()
        self.position = self.startPosition
