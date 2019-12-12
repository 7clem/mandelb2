# fractalCw.py

import ctypes

libpath = "/home/clem/prog/mp-fractal/fractallib.so"
_csuite = None

_flib = ctypes.CDLL(libpath)
_flib.suite.argtypes = (ctypes.c_float, ctypes.c_float, ctypes.c_int)
_csuite = _flib.suite
	
def suite(real, imag, depth):
	global _csuite
	re = ctypes.c_float(real)
	im = ctypes.c_float(imag)
	de = ctypes.c_int(depth)
	result = _csuite(re, im, de)
	return int(result)
