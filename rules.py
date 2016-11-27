""" Rules for Conway's Game of Life"""
import numpy as np

def advance(state):
	""" Takes a state and returns the next state"""
	width = len(state[0])
	height = len(state)

	next = np.zeros((width,height), np.uint8)
	for y in xrange(1,height-1):
		for x in xrange(1,width-1):
			neighbors = sumAllNeighbors(state,x,y)
			next[y][x] = isAlive(state[y][x], neighbors)
	
	return next

def sumAllNeighbors(state, x, y):
	""" Sums the number of alive neighbors"""

	sum = 0
	for i in range(-1,2):
		for j in range(-1,2):
			sum +=  state[y+j][x+i]
	return sum


def sumNeighbors(state, x, y, width, height):
	""" Sums the number of alive neighbors"""

	sum = 0
	for i in range(-1,2):
		for j in range(-1,2):
			if (((i != 0) | (j != 0)) & isValidIndex(x+i,y+j,width,height)):
				sum +=  state[y+j][x+i]
	return sum


def isValidIndex(x,y,width,height):
	return ((x>=0) & (x<width) & (y>=0) & (y<height))


def isAlive(current, neighbors):
	if current:
		if (neighbors == 2) | (neighbors == 3):
			return 1
		else:
			return 0
	else:
		if (neighbors == 3):
			return 1
		else:
			return 0
