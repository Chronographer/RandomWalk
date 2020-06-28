import numpy
import numpy.random
pi = numpy.pi

# six directions for nearest neighbors
x60 = numpy.cos(pi/3)
y60 = numpy.sin(pi/3)
# make numpy arrays, each with one row of two elements each.
unitVector1 = numpy.array((1.0, 0.0))
unitVector2 = numpy.array((x60, y60))
unitVector3 = numpy.array((-x60, y60))
unitVector4 = numpy.array((-1.0, 0.0))
unitVector5 = numpy.array((-x60, -y60))
unitVector6 = numpy.array((x60, -y60))
directionVector = [unitVector1, unitVector2, unitVector3, unitVector4, unitVector5, unitVector6]
for vector in directionVector:
    print(vector)

# initial positions
position = numpy.array((0.0, 0.0))

# generate an array of 100 random numbers
u = 6.0 * numpy.random.random_sample(100)
print(u)

# do a random walk
for number in u:
    iDirection = int(number)
    position = position + directionVector[iDirection]
    # access ith element of an array with [i], starting at 0.
    print(iDirection, position[0], position[1])
