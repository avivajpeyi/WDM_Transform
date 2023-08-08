import numpy as np
import matplotlib.pyplot as plt

DATA = np.loadtxt('../BinaryTaylorT.dat')

# data column 1 is the row number
# data column 2 is the column number
# data column 3 is the value

# reshape the data into a 2D array based on the row and column numbers
xvals = np.unique(DATA[:, 0])
yvals = np.unique(DATA[:, 1])
shape = (len(xvals), len(yvals))
print(f"Reshaping from {DATA.shape} to {shape}")
DATA = DATA[:, 2].reshape(shape)


# plot the data using the row and column numbers as the x and y axes
plt.imshow(DATA, origin='lower', aspect='auto', extent=[xvals[0], xvals[-1], yvals[0], yvals[-1]])
plt.xlabel('Column number')
plt.ylabel('Row number')
plt.colorbar(label='Value')
plt.show()

