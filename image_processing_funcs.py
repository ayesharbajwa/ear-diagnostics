import numpy as np
import matplotlib.pyplot as plt
import PIL
import skimage.io as io


#TODO
#def increase_contrast():
	#"""Increases contrast by histogram equalization"""

#TODO
#def segment_tympanic_membrane():
	#"""Segments tympanic membrane from image"""

def rgb_array_separation(inputArr):
	"""Given a numpy array representing an image file, returns separated RGB color channels as three numpy arrays"""

	# separate channels
	redArr, greenArr, blueArr = inputArr.copy(), inputArr.copy(), inputArr.copy()

	redArr[:,:,(1,2)] = 0
	greenArr[:,:,(0,2)] = 0
	blueArr[:,:,(0,1)] = 0

	return redArr, greenArr, blueArr;


def rgb_aray_addition(redArr, greenArr, blueArr):
	"""Given the RGB color channels of image as three numpy arrays, returns numpy array representing RGB file"""

	# add channels and normalize 
	redArr *= (255/redArr.max())
	greenArr *= (255/greenArr.max())
	blueArr *= (255/blueArr.max())

	sumArr = np.add(redArr, np.add(greenArr, blueArr))

	return sumArr;


def read_image(inputFile):
	"""Given an image file, returns numpy array representation"""
	#use Skimage conversion
	array = io.imread(inputFile)
	return array;


def save_image(numpyArray, outputFile):
	"""Given a numpy array representing an RGB image, saves to image file"""
	#Use PIL conversion to Image type
	img = PIL.Image.fromarray(np.uint8(numpyArray))
	#Use object method to save
	img.save(outputFile)
	return;


