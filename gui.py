try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk

#UNCOMMENT THESE
import hearing_test as ht
#import image_processing_funcs as ipf
#import camera as cam
# TODO: import bulging
# TODO import redness
# TODO import other?


#LEAVE THESE - all have own main()
#from hearing_test import *
#from image_processing_funcs import segment_tympanic_membrane
#from camera import *


class Panel:

	def __init__(self):
		self.tk = master = tk.Tk()
		self.images = [] #initialize to empty array. Add paths of each capture?
		self.temp = 0.0

		w = tk.Label(master, text="EAR DIAGNOSTICS", font=("Helvetica", 25), highlightbackground='#0f0684')
		w.pack()

		x = tk.Label(master, text="Welcome to our GUI.", font=("Helvetica", 20))
		x.pack()
		self.quit = tk.Button(master, text="QUIT", font=("Helvetica", 15), highlightbackground='#3E4149', command=master.quit)
		#self.button.pack(side=tk.LEFT)
		self.quit.pack(pady=8, padx=15)



		frame = tk.Frame(master)
		frame.pack(side=tk.LEFT)

		a = tk.Label(frame, text="Basic Functions", font=("Helvetica", 18))
		a.pack()

		self.hearing_test = tk.Button(frame, text="Hearing Test", font=("Helvetica", 15), highlightbackground='#2981ce', command=lambda: self.print_hearing())
		self.hearing_test.pack(pady=8, padx=15)

		self.temp = tk.Button(frame, text="Ear Temperature", font=("Helvetica", 15), highlightbackground='#2981ce', command=lambda: self.enter_temperature())
		self.temp.pack(pady=8, padx=15)

		self.feed = tk.Button(frame, text="Display Live Feed", font=("Helvetica", 15), highlightbackground='#2981ce', command=lambda: self.print_feed())
		self.feed.pack(pady=8, padx=15)

		self.capture = tk.Button(frame, text="Capture Image", font=("Helvetica", 15), highlightbackground='#2981ce', command=lambda: self.print_capture())
		self.capture.pack(pady=8, padx=15)



		frame2 = tk.Frame(master)
		frame2.pack(side=tk.RIGHT)

		b = tk.Label(frame2, text="Plotting", font=("Helvetica", 18))
		b.pack()

		self.read = tk.Button(frame2, text="Read Data File", font=("Helvetica", 15), highlightbackground='#0f0684', command=lambda: self.print_read())
		self.read.pack(pady=8, padx=15)

		self.plot = tk.Button(frame2, text="Display Plot", font=("Helvetica", 15), highlightbackground='#0f0684', command=lambda: self.print_plot())
		self.plot.pack(pady=8, padx=15)




		frame3 = tk.Frame(master)
		frame3.pack(side=tk.RIGHT)

		c = tk.Label(frame3, text="Image Processing", font=("Helvetica", 18))
		c.pack()

		self.path = tk.Button(frame3, text="Enter Image File Path", font=("Helvetica", 15), highlightbackground='#174854', command=lambda: self.enter_path())
		self.path.pack(pady=8, padx=15)

		self.red = tk.Button(frame3, text="Analyse Redness", font=("Helvetica", 15), highlightbackground='#174854', command=lambda: self.print_redness())
		self.red.pack(pady=8, padx=15)

		self.bulge = tk.Button(frame3, text="Analyse Bulging", font=("Helvetica", 15), highlightbackground='#174854', command=lambda: self.print_bulge())
		self.bulge.pack(pady=8, padx=15)

		self.seg = tk.Button(frame3, text="Segment", font=("Helvetica", 15), highlightbackground='#174854', command=lambda: self.print_seg())
		self.seg.pack(pady=8, padx=15)



	# Run -- never returns
	def run(self):
		self.tk.mainloop() # Hang around...

	def print_hearing(self):
		print "Adminstering hearing test."
		ht.hearing_test()
		#return

	def enter_temperature(self):
		temp = float(input("Enter the patient ear temperature in C:"))
		self.temp = temp
		return temp

	def print_feed(self):
		print "Rolling live feed."
		# TODO: call feed function as cam.func
		# cam.main()
		#return

	def print_capture(self):
		print "Image captured."
		# TODO: call capture function as cam.func
		#return

	def print_read(self):
		print "Reading data file."
		# TODO: import dath from file with correct typing for plotting
		#return some value?

	def print_plot(self):
		print "Creating plot."
		# TODO: call plotting function
		#return

	def enter_path(self):
		path = input("Enter the file path:")
		return path

	def print_redness(self):
		print "Calculating redness."
		path = input("Enter the file path:")
		# red = redness.main(path)
		#return red

	def print_bulge(self):
		print "Calculating bulging."
		# TODO: call bulging function, display explicitly if not incl.
		#return

	def print_seg(self):
		print "Segmenting..."
		# TODO: test import on Pi
		#return ipf.segment_tympanic_membrane('./saved_images/image2017_05_18_15_22_31.png')

def main():
	panel = Panel()
	panel.run()


if __name__ == '__main__':
	main()
