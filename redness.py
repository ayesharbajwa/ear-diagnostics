import numpy as np
import cv2
import matplotlib.pylab as plt

class Image(object):
    
    def __init__(self,image):
        self.img=np.array(image)
        self.width,self.height=np.shape(self.img)[0:2]
    
    def display(self):
        cv2.imshow('image',self.img)
        
    def gray(self):
        return cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        
    def edges(self,low_thresh):
        high_thresh=low_thresh*2
        return cv2.Canny(tm.img,low_thresh,high_thresh)
        
    def equal(self):
        return cv2.equalizeHist(self.gray())

def redness(img):
	tm=Image(cv2.imread('./{}'.format(img)))
	return ((np.mean(tm.img[:,:,2]))/(np.mean(tm.img)))

def main():
    print (redness('ear_normal/NORMAL4.jpg'))

if __name__ == '__main__':
    main()
