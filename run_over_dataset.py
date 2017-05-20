import redness as rd
from scipy import stats

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

