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
	
	
	
img=cv2.imread('sphere.png',0)
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

#surface normals
p = np.zeros((width,height))
q = np.zeros((width,height))

# the surface
Z = np.zeros((width,height))

# surface derivatives in x and y directions
Z_x = np.zeros((width,height))
Z_y = np.zeros((width,height))

# maximum number of iterations
maxIter = 10

# the normalized illumination direction
ix = math.cos(tilt) * math.tan(slant)
iy = math.sin(tilt) * math.tan(slant)

for k in range(maxIter):
	print(k)
	# using the illumination direction and the currently estimate
	# surface normals, compute the corresponding reflectance map.    
	R =(math.cos(slant) + p* math.cos(tilt)*math.sin(slant)+ q*math.sin(tilt)*math.sin(slant))/np.sqrt(1 + p**2 + q**2)
	# at each iteration, make sure that the reflectance map is positive at
	# each pixel, set negative values to zero.
	
	for x in np.nditer(R, op_flags=['readwrite']):
		x[...]=max(0,x)
	# compute our function f which is the deviation of the computed
	# reflectance map from the original image ...
	f = img - R
	print(f)
	# compute the derivative of f with respect to our surface Z ... refer to (62)
	df_dZ =(p+q)*(ix*p + iy*q + 1)/(np.sqrt((1 + p**2+ q**2)**3)*np.sqrt(1 + ix**2 + iy**2))-(ix+iy)/(np.sqrt(1 + p**2 + q**2)*np.sqrt(1 + ix**2 + iy**2))
	# update our surface ... refer to (61)
	Z = Z - f/(df_dZ + eps)	
	# compute the surface derivatives with respect to x and y
	Z_x[2:width,:] = Z[1:width-1,:]
	Z_y[:,2:height] = Z[:,1:height-1]
	# using the updated surface, compute new surface normals, refer to (58) and (59)
	p = Z - Z_x
	q = Z - Z_y

#####################copied from guide########################

#plt.imshow(z,interpolation='nearest')
#plt.show()


x = range(width)
y = range(height)
X, Y = np.meshgrid(x, y)
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
