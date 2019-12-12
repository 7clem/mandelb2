#! python3

#~ import threading
from matplotlib import pyplot as plot
import numpy as np

DEPTH = 256
SIZE = 128

def randomColor():
	np.uint32

def suite(c):
	C = complex(c)
	z = complex()
	n = 0
	while (n < DEPTH and (z * z.conjugate()).real < 4.0):
		z = z * z + C
		n += 1
	return n
	
def colorFromN(n):
	return n
	
def screenToComplex(left, top, right, bottom, x, y):
	cx = float(x) / float(SIZE) * float(right - left) + left
	cy = float(y) / float(SIZE) * float(bottom - top) + top 
	return complex(cx, cy)

#~ class FractalRender(threading.Thread):
	#~ def __init__(self, viewRect, spaceRect):
		#~ self.toto = 0
		
	#~ def run(self):
		#~ pass
		
if __name__ == "__main__":
	view = None;
	space = None;

	image = np.empty((SIZE, SIZE), np.uint8)
	for x in range(SIZE):
		for y in range(SIZE):
			c = screenToComplex(-3.0, -2.0, 1.0, 2.0, x, y)
			n = suite(c)
			col = colorFromN(n)
			image[x][y] = col
	plot.imshow(image)
	plot.show()
	print ("not implemented yet")
	
