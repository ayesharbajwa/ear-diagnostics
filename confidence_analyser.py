import numpy as np
import matplotlib as matplotlib
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import log
import cv2

matplotlib.rcParams.update({'font.size': 13})
prob=[]
red=[]
size=[]
IMG_SIZE=200

for i in range(78):
	a=input()
	img=cv2.imread(a,0)
	img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
	evals, evecs = np.linalg.eig(img)
	size.append(evals[0])
	prob.append(float(input()))
	red.append(float(input()))

prob=np.asarray(prob)
red=np.asarray(red)
fig,ax=plt.subplots()
ax.scatter(size,log(1-prob))
size=np.asarray(size)
print(size)
ax.annotate('Anomaly due to red patch',(0.51,-1.6))
m,b=np.polyfit(size,np.log(prob),1)
#plt.plot(red,m*red+b)
plt.title('Correlation between Redness and CNN Cross-Entropy')
plt.plot((0.5,0.5),(-2,0.5),'k-',label='Apparent Redness Threshold')
plt.legend()
plt.ylabel('Cross-Entropy of AOM image')
plt.ylim([-2,0.5])
plt.xlabel('Redness')
plt.show()
