import numpy as np
import matplotlib.pyplot as plt
import PIL
import skimage.io as io
from skimage.color import rgb2gray
from skimage.exposure import equalize_hist
from skimage.filters import gaussian
from skimage.segmentation import active_contour
import matplotlib.patches as mpatches
import matplotlib.path as mpath


def main():
	segment_tympanic_membrane('./ear_images/normalTympanic1.jpg') #cone of light throws off
	#segment_tympanic_membrane('./ear_images/noisy1-1.jpg')
	#segment_tympanic_membrane('./ear_images/noisy1-2.jpg')
	segment_tympanic_membrane('./ear_images/normalTympanic2.jpg')
	segment_tympanic_membrane('./ear_images/normalTympanic3.jpg')

	segment_tympanic_membrane('./normal_ear_images/NORMAL1.jpg')
	segment_tympanic_membrane('./normal_ear_images/NORMAL2.jpg') #all black
	segment_tympanic_membrane('./normal_ear_images/NORMAL3.jpg') #too much extra space


#TODO
def segment_tympanic_membrane(filename):
	"""Given image input containing tympanic membrane, segments by masking
	to show only membrane and displays/saves masked image."""
	orig = read_image(filename)

	#make grayscale
	img = rgb2gray(orig)

	#make histogram equalized
	img = equalize_hist(img)

	#initialize search circle in center
	s = np.linspace(0, 2*np.pi, 400)
	#start centered and use search boundary
	x = img.shape[1]/2 + 220*np.cos(s)
	y = img.shape[0]/2 + 220*np.sin(s)
	init = np.array([x, y]).T


	#gaussian filter before contour fit
	snake = active_contour(gaussian(img, 3), init, alpha=0.015, beta=10, gamma=0.001)
	
	fig = plt.figure(figsize=(7, 7))
	ax = fig.add_subplot(111)
	ax.plot(init[:, 0], init[:, 1], '-k', lw=3) #initial search circle
	ax.plot(snake[:, 0], snake[:, 1], '-k', lw=3) #final contour
	
	#want to mask outside of snake
	coords = []
	sx = snake[:, 0]
	sy = snake[:, 1]
	for i in range(len(snake)):
		coords.append((sx[i], sy[i]))
	print coords

	mask_outside_polygon(coords)
	
	ax.set_xticks([]), ax.set_yticks([])
	ax.axis([0, orig.shape[1], orig.shape[0], 0])

	ax.imshow(orig)
	plt.show()
	#fig.savefig(filename + '_segmented.jpg')

	return;



def mask_outside_polygon(perimeter, ax=None):
    """ Plots a mask on the specified axis such that all areas outside of
    perimeter are masked. Perimeter is a list of tuples outlining the crop
    region to maintain. Returns the matplotlib.patches.PathPatch instance
    plotted on the figure."""

    if ax is None:
        ax = plt.gca()

    #get current plot limits
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    #corners of the plot boundaries in clockwise order
    bounds = [(xlim[0], ylim[0]), (xlim[0], ylim[1]),
    	(xlim[1], ylim[1]), (xlim[1], ylim[0]),
    	(xlim[0], ylim[0])]

    # 
    bound_codes = [mpath.Path.MOVETO] + (len(bounds) - 1) * [mpath.Path.LINETO]
    poly_codes = [mpath.Path.MOVETO] + (len(perimeter) - 1) * [mpath.Path.LINETO]

    #plot masking patch
    path = mpath.Path(bounds + perimeter, bound_codes + poly_codes)
    patch = mpatches.PathPatch(path, facecolor='black', edgecolor='none')
    patch = ax.add_patch(patch)

    #reset plot limits to original
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    return patch

#TODO
#def bubble_presence():
	#"""Uses Canny edge detection"""

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
	img = PIL.Image.fromarray(np.uint8(numpyArray*255))
	#Use object method to save
	img.save(outputFile)
	return;

if __name__ == '__main__':
    main()


