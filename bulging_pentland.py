import numpy as np
import cv2
import matplotlib.pylab as plt
import math
import cmath
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import Axes3D

eps = np.finfo(float).eps
i=cmath.sqrt(-1)

def moments():
	mu=np.sum(img)/np.size(img)
	sigma=np.sum(img**2)/np.size(img)
	return mu,sigma

def albedo_calc():
	return (np.sqrt(6*math.pi**2*sigma-48*mu**2)/math.pi)

def slant_calc():
	try:	
		return math.acos(4*mu/(np.sqrt(6*math.pi**2*sigma-48*mu**2)))
	except ValueError:
		return 0
	

def tilt_calc():
	grady,gradx=np.gradient(img)
	grad=np.sqrt(grady**2+gradx**2)
	ngrady=grady/(grad+eps)
	ngradx=gradx/(grad+eps)
	#plt.imshow(gradx,interpolation='nearest')
	#plt.show()
	avx=np.sum(ngradx)/np.size(ngradx)
	avy=np.sum(ngrady)/np.size(ngrady)
	return math.atan(avy/avx)
	
	
	
img=cv2.imread('tm.jpg',0)
img = img.astype(np.float32, copy=False)
img=img/np.amax(img)
height=np.shape(img)[1]
width=np.shape(img)[0]
print(img)
mu,sigma=moments()
print(mu,sigma)

albedo=albedo_calc()
slant=slant_calc()

print (albedo,slant)
tilt=tilt_calc()
Fimg=np.fft.fft2(img)

[x,y]=np.meshgrid(range(1,1+height),range(1,1+width))
wx=2*math.pi*x/width
wy=2*math.pi*y/height
Fz=Fimg/(-i*wx*math.cos(tilt)*math.sin(slant)-i*wy*math.sin(tilt)*math.sin(slant)+eps)
z=abs(np.fft.ifft2(Fz))
z=z/np.amax(z)
#plt.imshow(z,interpolation='nearest')
#plt.show()


x = range(width)
y = range(height)
X, Y = np.meshgrid(x, y)
hf1 = plt.figure(1)
ax = hf1.add_subplot(111, projection='3d')
ax.plot_surface(X,Y, np.transpose(z),cmap=cm.coolwarm)
hf2=plt.figure(2)
ay = hf2.add_subplot(111, projection='3d')
ay.plot_surface(X,Y, np.transpose(img),cmap=cm.coolwarm)
plt.show()


#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
