# fractalCw.py

import ctypes
import os, sys
cwd = os.path.abspath(os.path.dirname(sys.argv[0]))
print(cwd)

lib = "fractallib.so"
libFullPath = "{}/{}".format(cwd, lib)
print(libFullPath)
_csuite = None

_flib = ctypes.CDLL(libFullPath)
_flib.suite.argtypes = (ctypes.c_float, ctypes.c_float, ctypes.c_int)
_csuite = _flib.suite
	
def suite(real, imag, depth):
	global _csuite
	re = ctypes.c_float(real)
	im = ctypes.c_float(imag)
	de = ctypes.c_int(depth)
	result = _csuite(re, im, de)
	return int(result)
