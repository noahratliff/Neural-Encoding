from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pickle
from compute_sta import compute_sta
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

FILENAME = dir_path+'\data.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

stim = data['stim']
rho = data['rho']

# Fill in these values
sampling_period = 2  # in ms
num_timesteps = 150


sta = compute_sta(stim, rho, num_timesteps)

time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')

plt.show()
plt.pause(20)
plt.close()
