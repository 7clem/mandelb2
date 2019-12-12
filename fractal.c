/* fractal.c */

#include "fractal.h"

float sqrZre(float , float );
float sqrZre(float re, float im) {
	return re * re - im * im;
}

float sqrZim(float , float );
float sqrZim(float re, float im) {
	return 2 * re * im;
}

float abs2(float re, float im){
	return re * re + im * im;
}

int suite(float cr, float ci, int depth) {
	float zr = 0;
	float zi = 0;
	int n = 0;
	while (n < depth && abs2(zr, zi) < 4.0) {
		zr = sqrZre(zr, zi) + cr;
		zi = sqrZim(zr, zi) + ci;
		n++;
	}
	return(n);
}

