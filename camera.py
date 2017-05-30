import numpy as np
import cv2
import datetime
from time import gmtime, strftime
camera_port=0
camera = cv2.VideoCapture(camera_port)

def get_image():
	retval, im = camera.read()
	return im

def current_time():
	return strftime("%Y_%m_%d_%H_%M_%S", gmtime())

def main():
	camera_port=0 #input port

	camera = cv2.VideoCapture(camera_port)
	a=0
	while(True):
		if(a==115):
			break
		print ("Press 'c' to capture and 's' to stop")
		while(True):

			a=cv2.waitKey(10)
			# Capture frame-by-frame
			ret, frame = camera.read()
			# Display the resulting frame
			cv2.imshow('frame',get_image())
				
			if(a==99):
				saving=get_image()
				file = "./saved_images/image.jpg"
				cv2.imwrite(file, get_image())
				print("")
				print("Image Captured")	
				print("")		
				break
			if(a==115):
				print('Program terminating')
				break

    # When everything done, release the capture
	camera.release()
	cv2.destroyAllWindows()


if __name__ == '__main__':
        main() 
