"""
Created by : Team Unique Tech for ITSP, IIT Bombay

The below code is for storing the signal data coming from the electrical circuit through the RaspberryPi. 
The code creates arrays for data collected from the RaspberryPi. 

"""

import numpy as np
import time
from math import pi
from adc_read import read_val

# some fundamental definitions and variables

# T = time interval (in s) for which the input is taken
n = 400000 # number of samples or number of data points (will represent sound intensity in 10-bits)
# dt = T/n time interval (in s) between two readings
# df = 1/T fundamental frequency of the fft
# dw = 2*pi*df fundamental angular frequency of the fft
# ny = df*n/2 nyquist frequency (or the top frequency)
freq = 2000 # frequency of the sound-source 

def data():
	mic_data_0 = np.array([]) # used to store data from mic1 for 'n' sample points
	mic_data_1 = np.array([]) # ----------""----------- mic2 ---------""----------
	mic_data_2 = np.array([]) # ----------""----------- mic3 ---------""----------
	mic_data_3 = np.array([]) # ----------""----------- mic4 ---------""----------

	t_axis = np.array([]) # used to create the time axis for data obtained through mic

	temp = n
	t_start = time.time()

	while(temp>0):

		temp -= 1
		# take the input from the mics through read_val and store it in the array
		t_now = time.time()
		t_delay = t_now - t_start # calculating the delay from the start of loop (/the point after which readings were taken)
		t_axis = np.append(t_axis, t_delay) # update the t_axis array
		
	
	return mic_data_0, mic_data_1, mic_data_2, mic_data_3
