import Tkinter as tk
from hearing_test import *
#from camera import *


class Panel:

	def __init__(self):
		self.tk = master = tk.Tk()

		w = tk.Label(master, text="EAR DIAGNOSTICS", font=("Helvetica", 25), highlightbackground='#0f0684')
		w.pack()

		x = tk.Label(master, text="Welcome to our GUI.", font=("Helvetica", 20))
		x.pack()

		frame = tk.Frame(master)
		frame.pack()

		self.hearing_test = tk.Button(frame, text="Hearing Test", highlightbackground='#0f0684', command=lambda: hearing_test())
		#self.hearing_test.pack(side=tk.LEFT)
		self.hearing_test.pack(pady=8)

		self.temp = tk.Button(frame, text="Ear Temperature", highlightbackground='#174854', command=lambda: self.enter_temperature())
		#self.hi_there.pack(side=tk.LEFT)
		self.temp.pack(pady=8)

		self.camera = tk.Button(frame, text="Image Capture", highlightbackground='#2981ce', command=lambda: self.print_capture())
		#self.hi_there.pack(side=tk.LEFT)
		self.camera.pack(pady=8)

		self.quit = tk.Button(frame, text="QUIT", highlightbackground='#3E4149', command=frame.quit)
		#self.button.pack(side=tk.LEFT)
		self.quit.pack(pady=8)

		y = tk.Label(master, text="GM1 2017", font=("Helvetica", 15))
		y.pack()

	# Run -- never returns
	def run(self):
		self.tk.mainloop() # Hang around...

	def print_capture(self):
		print "Image captured."
		#return

	def print_hearing(self):
		print "Adminstering hearing test."
		#return

	def enter_temperature(self):
		temp = float(input("Enter the patient ear temperature in C:"))
		return temp


def main():
	panel = Panel()
	panel.run()


if __name__ == '__main__':
	main()
