try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from hearing_test import *
#from camera import *


class Panel:

	def __init__(self):
		self.tk = master = tk.Tk()

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

		self.seg = tk.Button(frame3, text="Segment", font=("Helvetica", 15), highlightbackground='#174854', command=lambda: self.print_bulge())
		self.seg.pack(pady=8, padx=15)



	# Run -- never returns
	def run(self):
		self.tk.mainloop() # Hang around...

	def print_hearing(self):
		print "Adminstering hearing test."
		hearing_test()
		#return

	def enter_temperature(self):
		temp = float(input("Enter the patient ear temperature in C:"))
		return temp

	def print_feed(self):
		print "Rolling live feed."
		#return

	def print_capture(self):
		print "Image captured."
		#return

	def print_read(self):
		print "Reading data file."
		#return

	def print_plot(self):
		print "Creating plot."
		#return

	def enter_path(self):
		path = input("Enter the file path:")
		return path

	def print_redness(self):
		print "Calculating redness."
		#return

	def print_bulge(self):
		print "Calculating bulging."
		#return

def main():
	panel = Panel()
	panel.run()


if __name__ == '__main__':
	main()
