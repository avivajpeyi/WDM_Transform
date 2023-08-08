import numpy as np

DAT_FILE = '../fastAP_time.dat'

def read_data():
    """Read the data from the DAT_FILE and return as a typed numpy array.
    Columns: t, AA, fA, fdA
    """
    with open(DAT_FILE, 'r') as f:
        data = f.readlines()
    data = [d.strip().split() for d in data]
    data = np.array(data, dtype=float)
    return data

def plot_data(data):
    """Plot the data from the DAT_FILE."""
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1,1, figsize=(5, 5))
    ax.plot(data[:, 0], data[:, 1], label='AA')
    ax.plot(data[:, 0], data[:, 2], label='fA')
    ax.plot(data[:, 0], data[:, 3], label='fdA')
    plt.legend()
    plt.show()

data = read_data()
plot_data(data)