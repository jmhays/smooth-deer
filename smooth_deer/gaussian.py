"""
Gaussian smoothing method
"""

import numpy as np


def gaussian_filter(dists, probs, sigma, bins):
    """Simple method for smoothing DEER distributions using Gaussian filter.

    Parameters
    ----------
    dists : list
        Distances measured in DEER experiment. This is simply the list of distances
        for which we have probability measurements.
    probs: list
        DEER-derived probability distribution (from Fourier-transformed raw data).
        These are the probabilities that are associated with each distance of the
        parameter `dist`
    sigma : float
        Width of the Gaussian filter.
    bins : list
        A list of final distances for which the user wants probabilities.

    Returns
    -------
    hist : list
        smoothed pdf of DEER data

    Examples

    If we were to set bins as follows

        >>> bins = [i*0.1 for i in range(100)]

    We would get back a distribution of probabilities with bin width of 1 Angstrom

    """
    num_bins = len(bins)
    num_samples = len(dists)

    hist = np.zeros(shape=num_bins)

    for i in range(num_bins):
        for j in range(num_samples):
            arg_exp = -(bins[i] - dists[j])**2 / (2 * sigma**2)
            hist[i] += probs[j] * np.exp(arg_exp)

    # Normalization: sum of bin_width*prob should be 1.
    norm = np.sum(hist) * (bins[1] - bins[0])
    hist /= norm

    return hist.tolist()
