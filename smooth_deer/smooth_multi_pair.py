"""
Applies Gaussian smoothing to multiple pairs.
"""

from smooth_deer.gaussian import gaussian_filter
import numpy as np


def smooth(pair_metadata):
    """

    Parameters
    ----------
    pair_metadata : dict
        a hierachical dictionary containing these required keys:

        1. "pair_name". The key/name of the pair.
            This will be used as the key when returning the dictionary of smoothed distributions.
        2. "deer_filename". The path to the file that contains the DEER-derived distributions
            for that pair.
        3. "sigma". The Gaussian smoothing parameter
        4. "bins". The distance bins for the final histogram.


    Returns
    -------
    smoothed_pairs : dict
        A dictionary of the form {"pair name": [smoothed distribution]}

    Examples

    """
    required_params = ["deer_filename", "sigma", "bins"]
    names = list(pair_metadata.keys())
    for pair_name in names:
        for param in required_params:
            if param not in pair_metadata[pair_name]:
                raise KeyError("Please define {} for pair {}".format(param, pair_name))

    smoothed_pairs = {}

    for pair_name in names:
        deer_filename = pair_metadata[pair_name]['deer_filename']
        sigma = pair_metadata[pair_name]['sigma']
        bins = pair_metadata[pair_name]['bins']

        deer_data = np.loadtxt(deer_filename)
        dists = deer_data[:, 0]
        probs = deer_data[:, 1]

        smoothed_pairs[pair_name] = gaussian_filter(dists=dists, probs=probs, bins=bins, sigma=sigma)

    return smoothed_pairs