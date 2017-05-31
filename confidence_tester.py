import classifier as cf
import redness as rd
import os
import os.path
import sys 
orig_out=sys.stdout
prob_AOM=[]
red=[]

for i in range(6):
    f = open('/home/madhielango/norm.txt', 'a')
    sys.stdout = f
    imagePath='./ear_normal/NORMAL{}.jpg'.format(i+79)
    print(imagePath)
    print(cf.run_inference_on_image(imagePath))
    print(rd.redness(imagePath))
    sys.stdout=orig_out
    f.close()
