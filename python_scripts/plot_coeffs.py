import matplotlib.pyplot as plt
import numpy as np
import glob

def plot_curves(fname, n):
    colors = plt.cm.viridis(np.linspace(0, 1, len(n)))
    for i, idx in enumerate(n):
        data = np.loadtxt(fname.format(idx=idx))
        plt.plot(data[:, 1], data[:, 2], lw=0.5, alpha=0.6, color=colors[i])
    return plt.gcf()


n = [i for i in np.linspace(0, 299, 100, dtype=int)]
fig = plot_curves('../coeffs/WDMcoeffs{idx}.dat', n)
fig.suptitle('WDM Time coefficients')
fig.show()

fig = plot_curves('../coeffs/WDMcoeffsf{idx}.dat', n)
fig.suptitle('WDM Freq coefficients')
fig.show()


