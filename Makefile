#! make
CC = gcc

fractallib.so : fractal.o
	cc -shared -o fractallib.so fractal.o

