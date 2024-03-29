from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def compute_sta(stim, rho, num_timesteps):
    """Compute the spike-triggered average from a stimulus and spike-train.

    Args:
        stim: stimulus time-series
        rho: spike-train time-series
        num_timesteps: how many timesteps to use in STA

    Returns:
        spike-triggered average for specified number of timesteps before spike"""

    sta = np.zeros((num_timesteps,))

    # This command finds the indices of all of the spikes that occur
    # after 300 ms into the recording.
    spike_times = rho[num_timesteps:].nonzero()[0] + num_timesteps
    # Fill in this value. Note that you should not count spikes that occur
    # before 300 ms into the recording.
    num_spikes = len(spike_times)
    print(num_spikes)


    for i in range(num_spikes):
        sta = sta + stim[spike_times[i]-num_timesteps+1:spike_times[i]+1]

    sta = sta/num_spikes

    return(sta)
