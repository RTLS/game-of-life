""" Rules for Conway's Game of Life"""

def advance(state):
	""" Takes a state and returns the next state"""
	width = len(state[0])
	height = len(state)

	next = [[0 for w in range(width)] for h in range(height)]
	for y in xrange(height):
		for x in xrange(width):
			neighbors = sumNeighbors(state,x,y,width,height)
			next[y][x] = isAlive(state[y][x], neighbors)
	
	return next


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
