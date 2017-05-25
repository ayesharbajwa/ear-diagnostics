import numpy as np
import matplotlib.pyplot as plt
import PIL
from skimage.util import random_noise
from skimage.transform import rotate
from image_processing_funcs import read_image
from image_processing_funcs import save_image
import random

#read in original image from which to create noisy images

for num in range(70):

	path = './ear_normal_square/NORMAL' + str(num) + '.jpg'
	orig = read_image(path)

	for i in range(5):
		
		#modify image
		new = random_noise(orig, mode='gaussian', clip=False)
		rot_angle = random.choice([0, 90, 180, 270])
		new = rotate(new, rot_angle)

		"""
		#for visualizing image
		plt.gray()
		fig = plt.figure(figsize=(7, 7))
		ax = fig.add_subplot(111)
		ax.imshow(new)
		ax.set_xticks([]), ax.set_yticks([])
		ax.axis([0, new.shape[1], new.shape[0], 0])
		plt.show()
		"""

		#save noisy image
		save_image(new, './noisy_ear_normal_square/noisy' + str(num) + '-' + str(i) + '.jpg')