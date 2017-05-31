import numpy as np
import redness as rd

red_calibrated=[]
red_camera=[]

for i in range(6):
	print('Please provide path of {}% redness image'.format(20*i))
	red_calibrated.append(20*i)
	path=input()
	red_camera.append(rd.redness(path))

red_calibrated=np.asarray(red_calibrated)
red_camera=np.asarray(red_camera)

m,b=np.polyfit(red_calibrated,red_camera,1)

print (m,b)
	
