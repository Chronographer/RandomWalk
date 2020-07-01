import numpy as np


class walker:
    def __init__(self, startPositionVector, walkSize):
        self.position = startPositionVector
        self.walkSize = walkSize

        self.positionList = []
        self.stepList = []

    def walk(self, minStep, maxStep):
        for i in range(0, self.walkSize):
            self.stepList.append(i)
            self.positionList.append(self.position.x)
            self.position.x = self.position.x + np.random.uniform(minStep, maxStep, 1)
