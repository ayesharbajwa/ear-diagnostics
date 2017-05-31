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

def hearing_test_one_ear():
	"""Takes user input and turns it into a list of hearing thresholds"""
	freq=[250,500,1000,2000,4000,8000]#[250,500,1000,2000,4000,8000]      #frequencies tested
	vol_tests=5
	startvol=0.5
	delaytime=2
	canhear=np.zeros((1,len(freq)))

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
				canhearvol=vol
				vol=vol-delta
			else:
				vol=vol+delta
		canhear[0,f]=canhearvol
	print("Your thresholds for frequencies ",freq," were, respectively, ",canhear)

def hearing_test():
	print("Testing your left ear. Please use the earbud only in this ear")
	hearing_test_one_ear()
	print("Testing your right ear. Please use the earbud only in this ear")
	hearing_test_one_ear()
	
if __name__ == "__main__":
	hearing_test()
