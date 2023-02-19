
COMPILER = g++

all:
	- ${COMPILER} huffmanencoding.cpp -o out
	- ./out