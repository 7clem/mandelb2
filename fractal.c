/* fractal.c */

#include "fractal.h"

const int DEPTH = 255;

int suite(float real, float imag) {
	float zr = 0;
	float zi = 0;
	int n = 0;
	while (n++ < DEPTH && (zr * zr + zi * zi < 4.0)) {
		zr = zr * zr - zi * zi + real;
		zi = 2.0 * zi * zr + imag;
	}
	return(n);
}

