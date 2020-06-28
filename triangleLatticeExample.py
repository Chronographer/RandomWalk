import numpy
import numpy.random
pi = numpy.pi

#six directions for nearest neighbors
x60 = numpy.cos(pi/3)
y60 = numpy.sin(pi/3)
#make numpy arrays, each with one row of two elements each.
unitvector1 = numpy.array( (1.0,0.0) )
unitvector2 = numpy.array( (x60,y60) )
unitvector3 = numpy.array( (-x60,y60) )
unitvector4 = numpy.array( (-1.0,0.0) )
unitvector5 = numpy.array( (-x60,-y60) )
unitvector6 = numpy.array( (x60,-y60) )
directionvector = [unitvector1, unitvector2, unitvector3, unitvector4, \
                   unitvector5, unitvector6]
for vector in directionvector:
    print vector

#initial positions
position = numpy.array( (0.0,0.0) )

#generate an array of 100 random numbers
u = 6.0*numpy.random.random_sample(100)
print u

#do a random walk
for number in u:
    idirection = int(number)
    position = position + directionvector[idirection]
    #access ith element of an array with [i], starting at 0.
    print idirection, position[0], position[1]
