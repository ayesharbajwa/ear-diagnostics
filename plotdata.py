import datetime as dt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
from matplotlib.widgets import CheckButtons, Slider
import numpy as np
import csv

datafile='timedata.txt'

def plotting(datafile):
	f=open(datafile,'r')
	a=csv.reader(f,delimiter=',')
	datelist,redness,bulging,temp=zip(*a)
	t=[dt.datetime.strptime(x,'%Y-%m-%d').date() for x in datelist]
	s0=[float(x) for x in redness]
	s1=[float(x) for x in bulging]
	s2=[float(x) for x in temp]


	fig, ax = plt.subplots()
	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
	plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
	l0, = ax.plot(t, s0, lw=2, color='red')
	l1, = ax.plot(t, s1, lw=2, color='green')
	l2, = ax.plot(t, s2, lw=2, color='blue')
	plt.subplots_adjust(left=0.2)
	plt.xlabel('Time',fontsize=18)
	ax.set_ylim([0,1.2])
	
	rax = plt.axes([0.02, 0.4, 0.13, 0.15])
	check = CheckButtons(rax, ('Redness', 'Bulging', 'Temp'), (True, True, True))
	
	#Define colours for rectangles and set them
	c = ['r', 'g', 'b']    
	[rec.set_facecolor(c[i]) for i, rec in enumerate(check.rectangles)]
	
	def func(label):
		if label == 'Redness': l0.set_visible(not l0.get_visible())
		elif label == 'Bulging': l1.set_visible(not l1.get_visible())
		elif label == 'Other': l2.set_visible(not l2.get_visible())
		plt.draw()
		
	check.on_clicked(func)
	plt.show()
	plt.gcf().autofmt_xdate()
	
	
if __name__ == "__main__":
	plotting(datafile)

