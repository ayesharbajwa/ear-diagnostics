import numpy as np
import matplotlib.pyplot as plt

x = [250.0,500.0,1000.0,2000.0,4000.0,8000.0];
right = [0.8,0.9,0.7,0.7,0.5,0.7];
left = [0.7,0.85,0.73,0.65,0.7,0.6];
baseline=[0.8,0.8,0.8,0.8,0.8,0.8]

fig = plt.figure()
plt.plot(x, right,'b--',marker='o',label="Right Ear")
plt.plot(x, left,'g--',marker='^',label="Left Ear")
plt.plot(x,baseline,'r-.')
fig.suptitle('Audiogram')
plt.xlabel('Frequency/Hz')
plt.ylabel('Hearing Threshold Volume')
plt.text(7700,0.81,'Baseline',horizontalalignment='right',color='red'
            )

plt.legend(loc='lower left')#upper/lower right/left
ax = fig.add_subplot(1,1,1)
ax.set_xscale('log')
plt.xticks(x,['250','500','1000','2000','4000','8000'],color='black')
ax.set_xlim([250,8000])
ax.set_ylim([0,1.0])
plt.show()

fig.savefig('audiogram.png')


