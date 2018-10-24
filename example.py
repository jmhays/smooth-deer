from smooth_deer.smooth_multi_pair import smooth
import json
import matplotlib.pyplot as plt

"""
I'll use the same sigma and bins for all pairs
"""
sigma = 1.
bins = [i * 0.1 for i in range(80)]

metadata = {
    '052_210': {
        'deer_filename': '/home/jennifer/gdrive-desktop/Syx52_210.txt',
        'sigma': sigma,
        'bins': bins
    },
    '105_216': {
        'deer_filename': '/home/jennifer/gdrive-desktop/Syx105_216.txt',
        'sigma': sigma,
        'bins': bins
    },
    '196_228': {
        'deer_filename': '/home/jennifer/gdrive-desktop/Syx196_228.txt',
        'sigma': sigma,
        'bins': bins
    }
}

if __name__ == '__main__':

    my_result = smooth(metadata)
    json.dump(my_result, open('/home/jennifer/gdrive-desktop/syx_DEER.json', 'w'), indent=2)

    names = list(my_result.keys())

    # Plotting, just for fun
    i = 1
    for name in names:
        plt.subplot(1, len(names), i)
        plt.plot(bins, my_result[name])
        plt.title(name)
        i += 1
    plt.show()
