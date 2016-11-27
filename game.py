import sys
import os
#import getopt
import numpy as np
import timing
from rules import advance
import imageio
import pdb


def main(argv): 

	state = np.zeros((100,100), np.uint8)
	for x in xrange(10):
		state[50][45+x] = 1

	name = "nptest.gif"
	writer = imageio.get_writer(name, None, 'I')

	num = 1000
	for i in xrange(num):
#		pdb.set_trace()
		writer.append_data(255*state,{})
		state = advance(state)
	
	writer.close()

if __name__ == '__main__':
	main(sys.argv[1:])
