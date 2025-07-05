import matplotlib

# Matplotlib Pyplot
import matplotlib.pyplot as plt

import numpy as np


# Checking Matplotlib Version
# print(matplotlib.__version__)


# # Draw a line in a diagram from position (0,0) to position (6,250):
# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)      # plot()
# plt.show()                      # show()


# # Draw a line in a diagram from position (1, 3) to position (8, 10):
# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints)
# plt.show()


# # Plotting Without Line
# # Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):
# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints, 'o')
# plt.show()


# # Multiple Points
# # Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):
# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(xpoints, ypoints)
# plt.show()


# # Default X-Points
# # Plotting without x-points:

# ypoints = np.array([3, 8, 1, 10, 5, 7])       # points: (0, 3), (1, 8), (2, 1), (3, 10), (4, 5), (5, 7)

# plt.plot(ypoints)
# plt.show()


# # Matplotlib Markers
# # Mark each point with a circle:
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = 'o')
# plt.show()


# # Mark each point with a star:
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = '*')
# plt.show()

# ## markers: 
# # 'o' 	Circle 	
# # '*' 	Star 	
# # '.' 	Point 	
# # ',' 	Pixel 	
# # 'x' 	X 	
# # 'X' 	X (filled) 	
# # '+' 	Plus 	
# # 'P' 	Plus (filled) 	
# # 's' 	Square 	
# # 'D' 	Diamond 	
# # 'd' 	Diamond (thin) 	
# # 'p' 	Pentagon 	
# # 'H' 	Hexagon 	
# # 'h' 	Hexagon 	
# # 'v' 	Triangle Down 	
# # '^' 	Triangle Up 	
# # '<' 	Triangle Left 	
# # '>' 	Triangle Right 	
# # '1' 	Tri Down 	
# # '2' 	Tri Up 	
# # '3' 	Tri Left 	
# # '4' 	Tri Right 	
# # '|' 	Vline 	
# # '_' 	Hline



# # Format Strings fmt
# # Mark each point with a circle:
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, 'o:r')
# plt.show()


# # Line Reference
# # '-' 	Solid line 	
# # ':' 	Dotted line 	
# # '--' 	Dashed line 	
# # '-.' 	Dashed/dotted line



# # Mark each point with a * and without line:
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, '*r')
# plt.show()



# # Marker Size
# # Set the size of the markers to 20:

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = 's', ms = 20)
# plt.show()


# # Marker Color
# # Set the EDGE color to red:
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
# plt.show()


# # Set the FACE color to red:
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
# plt.show()


# # Set the color of both the edge and the face to red:
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
# plt.show()


# # Hexadecimal color values:
# # Mark each point with a beautiful green color:
# plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')


# # any of the 140 supported color names.
# # Mark each point with the color named "hotpink":
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')


# Matplotlib Line
# linestyle
# Use a dotted line:

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, linestyle = 'dotted')
# plt.show()


# # Use a dashed line:
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, linestyle = 'dashed')
# plt.show()


# # Shorter Syntax
# plt.plot(ypoints, ls = ':')
# plt.show()


# # Use a none line:
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, linestyle = 'None')
# plt.show()


# # Use a none line:
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, linestyle = '')
# plt.show()


# # use a dashdot line
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, linestyle = 'dashdot')
# plt.show()


# # use a dashdot line shorter syntax
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, linestyle = 'dashdot')
# plt.show()


# Line Color

# # Set the line color to red:
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, color = 'r')
# plt.show()


# # use Hexadecimal color values:
# # Plot with a green line:
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, c = '#4CAF50')
# plt.show()


# # Plot with the color named "hotpink":
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, c = 'hotpink')
# plt.show()


# Line Width

# # Plot with a 20.5pt wide line:
# # ypoints = np.array([3, 8, 1, 10])
# # plt.plot(ypoints, linewidth = '20.5')
# # plt.show()


# # Multiple Lines
# # Draw two lines by specifying a plt.plot() function for each line:
# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(y1)
# plt.plot(y2)

# plt.show()


# # Draw two lines by specifiyng the x- and y-point values for both lines:
# x1 = np.array([0, 1, 3, 5, 7])
# y1 = np.array([0, 3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(x1, y1, x2, y2)
# plt.show()


# # Matplotlib Labels and Title

# # Create Labels for a Plot
# # xlabel() and ylabel() function

# # Add labels to the x- and y-axis:
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x, y)

# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.show()



# # Create a Title for a Plot
# # title () function

# # Add a plot title and labels for the x- and y-axis:
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x, y)

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.show()


# # Set Font Properties for Title and Labels by use the fontdict parameter

# # Set font properties for the title and labels:
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# font1 = {'family':'serif','color':'red','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}

# # plt.title("Sports Watch Data", fontdict = font1)
# # plt.xlabel("Average Pulse", fontdict = font2)
# # plt.ylabel("Calorie Burnage", fontdict = font2)

# # plt.plot(x, y)
# # plt.show()


# # Position the Title
# # Position the title to the left:
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.title("Sports Watch Data", loc = 'left')
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.plot(x, y)
# plt.show()


# Matplotlib Adding Grid Lines

