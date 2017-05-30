import classifier as cf
import redness as rd

prob_AOM=[]
red=[]

for i in range(36):
    file='./ear_AOM/AOM{}.jpg'.format(i+1)
    prob_AOM.append(cf.run_inference_on_image(file))
    red.append(rd.redness(file))
    
print (red)
print (prob_AOM)
print('hello')
