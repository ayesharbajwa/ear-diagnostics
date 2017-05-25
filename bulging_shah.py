import numpy as np
import scipy as sp
from scipy import signal
import cv2
import matplotlib.pylab as plt
import math
from math import cos,sin,tan
from numpy import sqrt
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
	
	
	
img=cv2.imread('./ear_AOM/AOM18.jpg',0)
img = cv2.resize(img, (300,300))
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

######################copied from guide###################

p = np.zeros((width,height))
q = np.zeros((width,height))
Z = np.zeros((width,height))

Z_x = np.zeros((width,height))
Z_y = np.zeros((width,height))

maxIter = 6

ix = cos(tilt) * tan(slant)
iy = sin(tilt) * tan(slant)

for k in range(maxIter):
	print(k)
	R =(cos(slant) + p * cos(tilt)*sin(slant)+ q *sin(tilt)*sin(slant))/sqrt(1 + p**2 + q**2)
	R = np.maximum(R,0)
	f = img - R
	df_dZ =(p+q)*(ix*p + iy*q + 1)/(sqrt((1 + p**2 + q**2)**3)*sqrt(1 + ix**2 + iy**2))-(ix+iy)/(sqrt(1 + p**2 + q**2)*sqrt(1 + ix**2 + iy**2))
	Z = Z - f/(df_dZ + eps)
	Z_x[2:width,:] = Z[1:width-1,:]
	Z_y[:,2:height] = Z[:,1:height-1]
	p = Z - Z_x
	q = Z - Z_y

#####################copied from guide########################

Z=np.minimum(Z,np.mean(Z)+10*np.std(Z))
Z=np.maximum(Z,np.mean(Z)-10*np.std(Z))

x = range(width)
y = range(height)
X, Y = np.meshgrid(x, y)
Z=sp.signal.medfilt2d(Z,15)
hf1 = plt.figure(1)
ax = hf1.add_subplot(111, projection='3d')
ax.plot_surface(X,Y, np.transpose(Z),cmap=cm.coolwarm)
hf2=plt.figure(2)
ay = hf2.add_subplot(111, projection='3d')
ay.plot_surface(X,Y, np.transpose(img),cmap=cm.coolwarm)
plt.show()


#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
