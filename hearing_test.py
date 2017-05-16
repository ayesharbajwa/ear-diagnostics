#test procedure
import pyaudio
import time
import numpy as np

def play_sound(f,v):
	"""Plays a sound at given frequency f(Hz) and volume v (range 0-1)"""
	p = pyaudio.PyAudio()
	fs = 44100       # sampling rate, Hz, must be integer
	duration = 3.0   # in seconds, may be float
	# generate samples, note conversion to float32 array
	samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
	# for paFloat32 sample values must be in range [-1.0, 1.0]
	stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)
	# play. May repeat with different volume values (if done interactively) 
	stream.write(v*samples)
	stream.stop_stream()
	stream.close()
	p.terminate()

def hearing_test():
	"""Takes user input and turns it into a boolean matrix"""
	freq=[2000,10000]      #frequencies tested
	vol=[1,0.5]                            #num of levels
	delaytime=2
	canhear=np.zeros((len(vol),len(freq)))

	ready=input('Press enter when you want to begin, and whenever you hear a sound')

	for f in range(len(freq)):
		for v in range(len(vol)):
			#sound of frequency freq(f), level v
			print("Listen for the tone")
			time.sleep(delaytime) #wait for 'delaytime' seconds before sound is played
			play_sound(freq[f],vol[v])
			canhear[v,f]=input("Press 1 if you heard a tone, 0 otherwise, and then enter")
	print("canhear=",canhear)

hearing_test()
