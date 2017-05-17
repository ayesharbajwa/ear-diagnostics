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
        #high_thresh, thresh_im = cv2.threshold(self.gray(), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        #low_thresh = 0.5*high_thresh
        #th=0.66
        #low_thresh=np.median(self.equal())*th
        #low_thresh=38
        high_thresh=low_thresh*2
        return cv2.Canny(tm.img,low_thresh,high_thresh)
        
    def equal(self):
        return cv2.equalizeHist(self.gray())

def img_display(img):
    cv2.imshow('image',img)
    

def draw_lines_cart(img,lines):
    cimgP=img    
    for i in range(np.shape(lines)[0]):
        for x1,y1,x2,y2 in lines[i]:
            cimgP=cv2.line(cimgP,(x1,y1),(x2,y2),(0,255,0),2)
    return cimgP
    

def draw_lines_polar(img,lines):
    cimg=img    
    for i in range(np.shape(lines)[0]):
        for rho,theta in lines[i]:
            if(line_center(tm,rho, theta)==1):
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))
                cimg=cv2.line(cimg,(x1,y1),(x2,y2),(0,0,255),2)
    return cimg

def image_cluster(img,K):
    Z = img.reshape((-1,3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    return res2
    
def line_center(tm,rho, theta):
    if (theta==0):
        return 0
    lower=(rho-tm.height*np.sin(theta)/3)/(np.cos(theta))
    upper=(rho-2*tm.height*np.sin(theta)/3)/(np.cos(theta))
    print (lower,upper)    
    if(upper<lower):
            lower,upper=upper,lower
    lower_c=tm.width/3
    upper_c=tm.width*2/3
    print (lower_c,upper_c)  
    if(lower<upper_c and lower_c<upper):
        return 1
    else:
        return 0
    
filename='./test_images/test_ear_segmented.png'
filename2='./test_images/download.jpg' 
filename3='./ear_images/normalTympanic3.jpg'   
tm=Image(cv2.imread(filename2))
#img_display(tm.edges())
thresholds=[]
nol=[]
for i in range(400):    
    lines = cv2.HoughLines(tm.edges(i),1,np.pi/180,100)
    thresholds.append(i+1)
    try:    
        nol.append(np.shape(lines)[0])
    except IndexError:
        nol.append('0')
plt.figure()
plt.plot(thresholds,nol)
plt.show()
cimg=draw_lines_polar(tm.img,lines)
cv2.imwrite('houghlines.jpg',cimg)

#img_display(tm.equal())

#img_display(image_cluster(tm.img,6))
#minLineLength = 100
#maxLineGap = 10
#linesP = cv2.HoughLinesP(tm.edges(),1,np.pi/180,20,minLineLength,maxLineGap)
#print (np.shape(linesP)[0])
#cimgP=draw_lines_cart(tm.img,linesP)
#cv2.imwrite('houghlinesP.jpg',cimgP)

cv2.waitKey(0)
cv2.destroyAllWindows()

    
        