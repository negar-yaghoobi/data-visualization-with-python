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


# Plotting Without Line
# Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()


# Multiple Points
# Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()


# Default X-Points
# Plotting without x-points:

ypoints = np.array([3, 8, 1, 10, 5, 7])       # points: (0, 3), (1, 8), (2, 1), (3, 10), (4, 5), (5, 7)

plt.plot(ypoints)
plt.show()


# Matplotlib Markers
# Mark each point with a circle:
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()


# Mark each point with a star:
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = '*')
plt.show()

## markers: 
# 'o' 	Circle 	
# '*' 	Star 	
# '.' 	Point 	
# ',' 	Pixel 	
# 'x' 	X 	
# 'X' 	X (filled) 	
# '+' 	Plus 	
# 'P' 	Plus (filled) 	
# 's' 	Square 	
# 'D' 	Diamond 	
# 'd' 	Diamond (thin) 	
# 'p' 	Pentagon 	
# 'H' 	Hexagon 	
# 'h' 	Hexagon 	
# 'v' 	Triangle Down 	
# '^' 	Triangle Up 	
# '<' 	Triangle Left 	
# '>' 	Triangle Right 	
# '1' 	Tri Down 	
# '2' 	Tri Up 	
# '3' 	Tri Left 	
# '4' 	Tri Right 	
# '|' 	Vline 	
# '_' 	Hline



# Format Strings fmt
# Mark each point with a circle:
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()


# Line Reference
# '-' 	Solid line 	
# ':' 	Dotted line 	
# '--' 	Dashed line 	
# '-.' 	Dashed/dotted line



# Mark each point with a * and without line:
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, '*r')
plt.show()



# Marker Size
# Set the size of the markers to 20:

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 's', ms = 20)
plt.show()