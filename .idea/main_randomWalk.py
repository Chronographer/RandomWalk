import numpy as np
from vpython import *
import walkerObject
import matplotlib.pyplot as plt

walkLength = 100
minStepSize = -1
maxStepSize = 1
stepRange = 1

startVector = vector(0, 0, 0)
drunk = walkerObject.walker(startVector, walkLength)

drunk.walkUniform(minStepSize, maxStepSize)
print("uniform")
print(np.average(drunk.positionList))
plt.plot(drunk.stepList, drunk.positionList)
plt.plot(drunk.stepList, drunk.positionList, 'b.')
plt.xlabel("Step number")
plt.ylabel("Walker position")
plt.grid(True)
plt.show()

drunk.reset()

drunk.walkRange(stepRange)
print("range")
print(np.average(drunk.positionList))
plt.plot(drunk.stepList, drunk.positionList)
plt.plot(drunk.stepList, drunk.positionList, 'b.')
plt.xlabel("Step number")
plt.ylabel("Walker position")
plt.grid(True)
plt.show()