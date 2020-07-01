import numpy as np
from vpython import *
import walkerObject
import matplotlib.pyplot as plt

walkLength = 100
minStep = -1
maxStep = 1

startVector = vector(0, 0, 0)
drunk = walkerObject.walker(startVector, walkLength)
drunk.walk(minStep, maxStep)

print(np.average(drunk.positionList))
plt.plot(drunk.stepList, drunk.positionList)
plt.plot(drunk.stepList, drunk.positionList, 'b.')
plt.xlabel("Step number")
plt.ylabel("Walker position")
plt.grid(True)
plt.show()
