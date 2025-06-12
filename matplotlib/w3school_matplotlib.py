import matplotlib

# Matplotlib Pyplot
import matplotlib.pyplot as plt

import numpy as np


# Checking Matplotlib Version
print(matplotlib.__version__)


# Draw a line in a diagram from position (0,0) to position (6,250):
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)      # plot()
plt.show()                      # show()


# Draw a line in a diagram from position (1, 3) to position (8, 10):
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()