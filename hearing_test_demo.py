#test procedure
import pyaudio
import time
import numpy as np
from hearing_test import play_sound

def hearing_test_demo():
	"""Takes user input and turns it into a boolean matrix"""
	freq=[250]#[250,500,1000,2000,4000,8000]      #frequencies tested
	vol_tests=5
	startvol=0.5
	delaytime=2
	canhear=np.zeros((1,len(freq)))
	
	print("This is a demo. Please put one earbud in the ear you want to test")
	ready=input("Press enter when you want to begin")

	for f in range(len(freq)):
		canhearvol=1
		vol=startvol
		for v in range(vol_tests):
			#sound of frequency freq(f), level v
			print("Listen for the tone")
			time.sleep(delaytime) #wait for 'delaytime' seconds before sound is played
			play_sound(freq[f],vol)
			hear=float(input("input 1 if you heard the noise, 0 otherwise, and then enter"))
			delta=pow(2,(-(v+2)))
			if hear>0.5:
				print("You heard 250Hz at volume=",vol)
				canhearvol=vol
				vol=vol-delta
			else:
				print("You didn't hear 250Hz at volume=",vol)
				vol=vol+delta
		canhear[0,f]=canhearvol
	if canhear[0,0]==0:
		print("You did not hear any sound")
	else:
		print("The lowest volume you heard was ",canhear[0,0])
		
if __name__ == "__main__":
	hearing_test_demo()
