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
        
    def edges(self):
        return cv2.Canny(tm.img,100,200,apertureSize = 3)

def img_display(img):
    cv2.imshow('image',img)
    
    
filename='./test_images/test_ear_segmented.png'
filename2='./test_images/download.jpg' 
filename3='./ear_images/normalTympanic3.jpg'   
tm=Image(cv2.imread(filename))
#img_display(tm.edges())
minLineLength = 600
maxLineGap = 10
lines = cv2.HoughLinesP(tm.edges(),1,np.pi/180,30,minLineLength,maxLineGap)
print(lines[1])
print(np.shape(lines))
cimg=tm.img
for i in range(np.shape(lines)[0]):
    for x1,y1,x2,y2 in lines[i]:
        cv2.line(cimg,(x1,y1),(x2,y2),(0,255,0),2)
    


    cv2.line(cimg,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('houghlines3.jpg',cimg)

cv2.waitKey(0)
cv2.destroyAllWindows()

    
        