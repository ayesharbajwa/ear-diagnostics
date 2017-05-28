import Tkinter as tk
#import hearing_test as ht

class App:

    def __init__(self, master):
    	w = tk.Label(root, text="EAR DIAGNOSTICS!")
    	w.pack()

    	x = tk.Label(root, text="Welcome to our GUI.")
    	x.pack()

        frame = tk.Frame(master)
        frame.pack()

        self.button = tk.Button(frame, text="QUIT", fg="red", bg="blue", command=frame.quit)
        self.button.pack(side=tk.LEFT)

        self.hearing_test = tk.Button(frame, text="Hearing Test", command=self.print_hearing())
        self.hearing_test.pack(side=tk.LEFT)

        self.hi_there = tk.Button(frame, text="Image Capture", command=self.print_hello())
        self.hi_there.pack(side=tk.LEFT)

        y = tk.Label(root, text="GM1 2017.")
    	y.pack()

    def print_hello(self):
    	print "Hello World!"
    	return

    def print_hearing(self):
        print "Adminstering hearing test."
        return


root = tk.Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below