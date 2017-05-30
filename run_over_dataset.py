import redness as rd
from scipy import stats
import matplotlib as matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size': 13})

NORMAL_DIR='ear_normal/NORMAL{}.jpg'
AOM_DIR='ear_AOM/AOM{}.jpg'

normal=[]

i=1
while(True):
	try:
		normal.append(rd.redness(NORMAL_DIR.format(i)))
		i+=1
	except:
		break

print('Normal:')
print(stats.describe(normal))
print(' ')

aom=[]
i=1


while(True):
	try:
		aom.append(rd.redness(AOM_DIR.format(i)))
		i+=1
	except:
		break

print('AOM:')
print(stats.describe(aom))

plt.hist(aom, normed=True, bins=15,alpha=0.75,label='AOM')
plt.ylabel('Number')
plt.xlabel('Redness')
plt.hist(normal, normed=True, bins=15,alpha=0.75,label='Normal')
plt.legend()
plt.show()
