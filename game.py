import sys
import os
#import getopt
from PIL import Image
import timing
from rules import advance
import imageio
import pdb


def main(argv): 


	state = [[0 for x in range (30)] for y in range(30)]
	state[0][1] = 1
	state[1][2] = 1
	state[2][0] = 1
	state[2][1] = 1
	state[2][2] = 1

	name = "glider"

	filenames = []
	num = 100
	for i in xrange(num):
		filenames.append(addFile(state, name, i))
		#pdb.set_trace()
		state = advance(state)
	
	generateGIF(name,filenames)


def generateName(seed):
	return

def generateSeed(state):
	return

def generateGIF(name, filenames):
	""" Generates a gif with name"""

	images = []
	for filename in filenames:
		images.append(imageio.imread(filename))

	path = os.path.join(name, name+".gif")
	imageio.mimsave(path, images)

def addFile(state, name, ext):
	""" Saves 2D list to JPEG in current folder and returns file name """
	
	dir = name
	if not os.path.exists(dir):
		os.makedirs(dir)

	im = Image.new("1", (len(state[0]), len(state)))
	sequence = [state[x][y] for x in range(len(state)) for y in range(len(state[0]))]
	im.putdata(sequence)
	type = ".jpeg"

	filename = "{}{}{}".format(name, ext, type)
	path = os.path.join(dir, filename)
	im.save(path)
	return path

if __name__ == '__main__':
	main(sys.argv[1:])
