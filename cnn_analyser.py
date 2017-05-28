import numpy as np
from scipy import stats
tp=0
tn=0
fp=0
fn=0
accuracy=[]
print('tn,fp,tp,fn')
while(True):
	try:
		accuracy.append(float(input()))
		x=[]
		for i in input().split(' '):
			x.append(int(i))
		tp+=x[0]
		fp+=x[1]
		tn+=x[2]
		fn+=x[3]
		print(tn,fp,tp,fn)
	except:
		break

print(stats.describe(accuracy))
print('sen: {}'.format(tp/(tp+fn)))
print('spe: {}'.format(tn/(tn+fp)))
print('npv: {}'.format(tn/(tn+fn)))
print('ppv: {}'.format(tp/(tp+fp)))
	
