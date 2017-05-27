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
import matplotlib.path as mplPath


eps = np.finfo(float).eps
i=cmath.sqrt(-1)

def segment_tympanic_membrane(filename):
	"""Given image input containing tympanic membrane, segments by masking
	to show only membrane and displays/saves masked image."""
	orig = read_image(filename)
	orig.shape

	#make grayscale
	img = rgb2gray(orig)

	#make histogram equalized
	img = equalize_hist(img)

	#initialize search circle in center
	height = img.shape[0]
	width = img.shape[1]
	s = np.linspace(0, 2*np.pi, height)
	#start centered and use search boundary
	x = width/2 + width/2*np.cos(s)
	y = height/2 + height/2*np.sin(s)
	init = np.array([x, y]).T


	#gaussian filter before contour fit
	snake = active_contour(gaussian(img, 3), init, alpha=0.015, beta=10, gamma=0.001)
	
	fig = plt.figure(figsize=(7, 7))
	ax = fig.add_subplot(111)
	ax.plot(init[:, 0], init[:, 1], '-k', lw=3) #initial search circle
	ax.plot(snake[:, 0], snake[:, 1], '-k', lw=3) #final contour
	
	#want to mask outside of snake
	coords = []
	return (coords)
	


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
	
	
img=cv2.imread('./ear_AOM/AOM1.jpg',0)	
#img=cv2.imread('./ear_normal/NORMAL12.jpg',0)
#img = cv2.resize(img, (300,300))

img = img.astype(np.float32, copy=False)
img=img/np.amax(img)
height=np.shape(img)[1]
width=np.shape(img)[0]
mu,sigma=moments()
print(mu,sigma)

albedo=albedo_calc()
slant=slant_calc()

print (albedo,slant)
tilt=tilt_calc()

######################copied from guide (Elbhanian)###################

p = np.zeros((width,height))
q = np.zeros((width,height))
Z = np.zeros((width,height))

Z_x = np.zeros((width,height))
Z_y = np.zeros((width,height))

maxIter = 3

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
Z=sp.signal.medfilt2d(Z,29)

Z=Z-np.mean(Z)
Z=Z/np.std(Z)
hf1 = plt.figure(1)
ax = hf1.add_subplot(111, projection='3d')
ax.plot_surface(X,Y, np.transpose(Z),cmap=cm.coolwarm)


#edge=segment_tympanic_membrane('./ear_AOM/AOM18.jpg')
edge=segment_tympanic_membrane('/home/madhielango/Documents/aom2_cut.png')
#edge=segment_tympanic_membrane('./ear_normal/NORMAL12.jpg')

edges=np.asarray(edge)
edge_path=mplPath.Path(edges)

cont=sp.interpolate.interp2d(x,y,np.transpose(Z))
heights=[]

for x in edge:
	heights.append(cont(x[0],x[1]))



edges_bias=np.concatenate((edges,np.ones([len(edge),1])),1)


#coeff= (A'*A)^-1*A'*x) by linear least squares

abc=np.matmul(np.transpose(edges_bias),edges_bias)
coeff=np.matmul(np.linalg.inv(abc),np.transpose(edges_bias))
coeff=np.matmul(coeff,heights)

print(coeff)

x = range(width)
y = range(height)
X, Y = np.meshgrid(x, y)
plane=coeff[0]*X+coeff[1]*Y+coeff[2]

hf2 = plt.figure(1)
ay = hf2.add_subplot(111, projection='3d')

corrected=np.transpose(Z)
corrected=corrected-plane

#only show contour plot of TM

total_bulge=0
total_TM=0
#corrected=corrected-np.median(corrected)
for i in y:
	for j in x:
		if(edge_path.contains_point((i,j))==False):
			corrected[i,j]=0
		else:
			total_bulge+=corrected[i,j]
			total_TM+=1

mean_bulge=total_bulge/total_TM

#ay.plot_surface(X,Y, plane,cmap=cm.bwr)
#ay.plot_surface(X,Y, np.transpose(Z),cmap=cm.bwr)
ay.plot_surface(X,Y,corrected ,cmap=cm.bwr)
plt.show()

print('Bulging:')
print(mean_bulge)

#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
