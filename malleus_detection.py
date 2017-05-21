import numpy as np
import cv2
import matplotlib.pylab as plt
from tqdm import tqdm

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
                cimg=cv2.line(cimg,(x1,y1),(x2,y2),(0,0,255),8)
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
    #print (lower,upper)    
    if(upper<lower):
            lower,upper=upper,lower
    lower_c=tm.width/3
    upper_c=tm.width*2/3
    #print (lower_c,upper_c)  
    if(lower<upper_c and lower_c<upper):
        return 1
    else:
        return 0
        
def valid_line_counter(edge_limit,line_limit,tm):
    lines = cv2.HoughLines(tm.edges(edge_limit),1,np.pi/180,line_limit)
    ans=0
    try:
        for i in range(np.shape(lines)[0]):
            for rho,theta in lines[i]:
                if(line_center(tm,rho, theta)==1):
                    ans+=1
    except IndexError:
        return 0
    return ans

def malleus_presence(img_number):
	
	tm=Image(cv2.imread('./ear_normal/NORMAL{}.jpg'.format(img_number)))

	minimum=5000

	min_tuples=[]
	i=30
	while(True):
		b=valid_line_counter(i,i,tm)
		#print(b)
		i+=1
		if(b<100):
			break
	    
	#print(b)
	min_e=i-2
	min_l=i
	minimum=100
	for e in np.arange(i,i+50,2):
		#print(e)
		if(min_e!=e-2):
			break
		for l in np.arange(i,i+30):
			a=valid_line_counter(e,l,tm)
			if(a<=minimum and a>0):
				minimum=a
				#print(minimum)
				min_e=e
				min_l=l
				min_tuples.append((e,l))

	#img_display(tm.edges(min_e))            
		
	lines = cv2.HoughLines(tm.edges(min_e),1,np.pi/180,min_l)
	cimg=draw_lines_polar(tm.img,lines)
	savename='./saved_images/AOM{}_malleus.png'.format(img_number)
	cv2.imwrite(savename,cimg)
	return min_e,min_l


	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
for i in tqdm(np.arange(34,38)):
	img_number=i
	tm=Image(cv2.imread('./ear_AOM/AOM{}.jpg'.format(img_number)))
	print(i,':',malleus_presence(i+1))
        
