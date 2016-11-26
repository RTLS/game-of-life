import sys
import os
#import getopt
import numpy as np
import timing
from rules import advance
import imageio
import pdb


def main(argv): 

	state = np.zeros((30,30), np.uint8)
	state[0][1] = 1
	state[1][2] = 1
	state[2][0] = 1
	state[2][1] = 1
	state[2][2] = 1

	name = "nptest.gif"
	writer = imageio.get_writer(name, None, 'I')

	num = 100
	for i in xrange(num):
#		pdb.set_trace()
		writer.append_data(255*state,{})
		state = advance(state)
	
	writer.close()


def generateName(seed):
	return

def generateSeed(state):
	return

if __name__ == '__main__':
	main(sys.argv[1:])
