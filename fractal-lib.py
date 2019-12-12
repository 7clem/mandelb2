#! python3

import random
from matplotlib import pyplot as plot
import numpy as np
import sys
import fractalCw

DEPTH = 256
SIZE = 128

csuite = fractalCw.suite
	
def suite(c):
	C = complex(c)
	z = complex()
	n = 0
	while (n < DEPTH and (z * z.conjugate()).real < 4.0):
		z = z * z + C
		n += 1
	return n

def linear_interpolate(x, inlow, inhigh, outlow, outhigh):
	return x/(inhigh - inlow) * (outhigh - outlow) + outlow

def screenToComplex(left, top, right, bottom, x, y):
	lin = linear_interpolate
	cx = lin(x, 0, SIZE, left, right)
	cy = lin(y, 0, SIZE, top, bottom)
	return complex(cx, cy)
		
if __name__ == "__main__":

	image = np.empty((SIZE, SIZE), np.uint8)
	
	for x in range(SIZE):
		for y in range(SIZE):
			c = screenToComplex(-3.0, -2.0, 1.0, 2.0, x, y)
			n = csuite(float(c.real), float(c.imag), int(DEPTH))
			n2 = suite(c)
			
			image[x][y] = n
		
	plot.imshow(image, aspect="equal" )
	plot.axis("off")
	plot.show()
	plot.show()
