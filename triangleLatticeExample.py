import numpy as np

# six directions for nearest neighbors
x60 = np.cos(np.pi/3)
y60 = np.sin(np.pi/3)
# make numpy arrays, each with one row of two elements each.
unitVector1 = np.array((1.0, 0.0))
unitVector2 = np.array((x60, y60))
unitVector3 = np.array((-x60, y60))
unitVector4 = np.array((-1.0, 0.0))
unitVector5 = np.array((-x60, -y60))
unitVector6 = np.array((x60, -y60))
directionVector = [unitVector1, unitVector2, unitVector3, unitVector4, unitVector5, unitVector6]

for vector in directionVector:
    print(vector)

# initial positions
position = np.array((0.0, 0.0))

# generate an array of 100 random numbers
u = 6.0 * np.random.random_sample(100)
print(u)

# do a random walk
for number in u:
    iDirection = int(number)
    position = position + directionVector[iDirection]
    # access ith element of an array with [i], starting at 0.
    print(iDirection, position[0], position[1])
