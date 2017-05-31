try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk


import hearing_test_demo as htd
import plotdata as pd
# import image_processing_funcs as ipf
# import camera as cam 						#UNCOMMENT
# import bulging_shah
# import redness 							#UNCOMMENT
# import classifier as cf 					#UNCOMMENT


class Panel:

	def __init__(self):
		self.tk = master = tk.Tk()
		self.temp = 0.0
		self.path = 'timedata.txt'

		w = tk.Label(master, text="EAR DIAGNOSTICS", font=("Helvetica", 25), highlightbackground='#0f0684')
		w.pack()

		x = tk.Label(master, text="Welcome to our GUI.", font=("Helvetica", 20))
		x.pack()
		self.quit = tk.Button(master, text="QUIT", font=("Helvetica", 15), highlightbackground='#3E4149', command=master.quit)
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

		#self.path = tk.Button(frame3, text="Enter Image File Path", font=("Helvetica", 15), highlightbackground='#174854', command=lambda: self.enter_path())
		#self.path.pack(pady=8, padx=15)

		self.red = tk.Button(frame3, text="Analyse Redness", font=("Helvetica", 15), highlightbackground='#174854', command=lambda: self.print_redness())
		self.red.pack(pady=8, padx=15)

		#self.bulge = tk.Button(frame3, text="Analyse Bulging", font=("Helvetica", 15), highlightbackground='#174854', command=lambda: self.print_bulge())
		#self.bulge.pack(pady=8, padx=15)

		self.cf = tk.Button(frame3, text="Classify", font=("Helvetica", 15), highlightbackground='#174854', command=lambda: self.print_classify())
		self.cf.pack(pady=8, padx=15)



	# Run -- never returns
	def run(self):
		self.tk.mainloop() # Hang around...

	def print_hearing(self):
		print("Adminstering hearing test.")
		htd.hearing_test_demo()
		print("Done.")
		return

	def enter_temperature(self):
		temp = float(input("Enter the patient ear temperature in C:"))
		self.temp = temp
		print("Temperature recorded.")
		return temp

	def print_feed(self):
		print("Rolling live feed.")
		# cam.main() 				#UNCOMMENT
		print("Done.")
		return

	def print_read(self):
		print("Reading data file.")
		self.path = input("Enter the file path:")
		print("Done.")
		return

	def print_plot(self):
		print("Creating plot.")
		pd.plotting(self.path)
		print("Done.")
		return

	def print_redness(self):
		print("Calculating redness.")
		path = './saved_images/image.jpg'
		#red = redness.redness(path) 		#UNCOMMENT
		#print(red) 						#UNCOMMENT
		print("Done.")
		#return red 						#UNCOMMENT

	def print_bulge(self):
		print("Calculating bulging.")
		# TODO: call bulging function, display explicitly if not incl.
		print("Done.")
		return

	def print_classify(self):
		print("Classiying...")
		path = './saved_images/image.jpg'
		#cf.run_inference_on_image(path)	#UNCOMMENT
		print("Done.")
		return



def main():
	panel = Panel()
	panel.run()


if __name__ == '__main__':
	main()
