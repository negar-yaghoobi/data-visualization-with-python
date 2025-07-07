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


# # Matplotlib Adding Grid Lines
# # Add Grid Lines to a Plot

# # Add grid lines to the plot:

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.plot(x, y)

# plt.grid()

# plt.show()

# # Specify Which Grid Lines to Display

# # Display only grid lines for the x-axis:

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.plot(x, y)

# plt.grid(axis = 'x')

# plt.show()


# # Display only grid lines for the y-axis:

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.plot(x, y)

# plt.grid(axis = 'y')

# plt.show()


# # Set Line Properties for the Grid

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.plot(x, y)

# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

# plt.show()


# # Matplotlib Subplot

# # Display Multiple Plots
# # Draw 2 plots:
# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)
# plt.plot(x,y)

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.show()

# # Draw 2 plots on top of each other:
# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 1, 1)
# plt.plot(x,y)

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 1, 2)
# plt.plot(x,y)

# plt.show()


# # Draw 6 plots:

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 1)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 2)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 3)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 4)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 5)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 6)
# plt.plot(x,y)

# plt.show()


# # Title
# # 2 plots, with titles:
# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# plt.title("SALES")

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.title("INCOME")

# plt.show()


# # Super Title
# # Add a title for the entire figure:

# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# plt.title("SALES")

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.title("INCOME")

# plt.suptitle("MY SHOP")
# plt.show()


# # Matplotlib Scatter
# # Creating Scatter Plots

# # A simple scatter plot:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# plt.scatter(x, y)
# plt.show()

# # Compare Plots
# # Draw two plots on the same figure:

# #day one, the age and speed of 13 cars:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y)

# #day two, the age and speed of 15 cars:
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y)

# plt.show()


# # Set your own color of the markers:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y, color = 'hotpink')

# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y, color = '#88c999')

# plt.show()


# # Set your own color of the Each Dot of plot:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

# plt.scatter(x, y, c=colors)

# plt.show()


# # colormap

# # Create a color array, and specify a colormap in the scatter plot:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

# plt.scatter(x, y, c=colors, cmap='viridis')

# plt.show()


# # Include the actual colormap:

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

# plt.scatter(x, y, c=colors, cmap='viridis')

# plt.colorbar()

# plt.show()


# # Size
# # Set your own size for the markers:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

# plt.scatter(x, y, s=sizes)

# plt.show()


# # alpha argument

# # adjust the transparency of the dots with the alpha argument.
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

# plt.scatter(x, y, s=sizes, alpha=0.5)

# plt.show()


# # Combine Color Size and Alpha

# # Create random arrays with 100 values for x-points, y-points, colors and sizes:
# x = np.random.randint(100, size=(100))
# y = np.random.randint(100, size=(100))
# colors = np.random.randint(100, size=(100))
# sizes = 10 * np.random.randint(100, size=(100))

# plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

# plt.colorbar()

# plt.show()


# # matplotlib bars
# # Creating Bars

# # Draw 4 bars:
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x,y)
# plt.show()


# # example2
# x = ["APPLES", "BANANAS"]
# y = [400, 350]
# plt.bar(x, y)
# plt.show()


# # Horizontal Bars
# # Draw 4 horizontal bars:
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.barh(x, y)
# plt.show()


# # Bar Color
# # Draw 4 red bars:
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x, y, color = "red")
# plt.show()


# # example2
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.barh(x, y, color = "red")
# plt.show()

# # example3
# # Draw 4 "hot pink" bars:
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x, y, color = "hotpink")
# plt.show()

# # Color Hex
# # Draw 4 bars with a beautiful green color:
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x, y, color = "#4CAF50")
# plt.show()


# # Bar Width
# # Draw 4 very thin bars:
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x, y, width = 0.1)
# plt.show()


# # Bar Height
# # Draw 4 very thin bars:
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.barh(x, y, height = 0.1)
# plt.show()



# # matplotlib histograms
# # creating a Normal Data Distribution by NumPy:
# x = np.random.normal(170, 10, 250)

# print(x)

# # A simple histogram:
# x = np.random.normal(170, 10, 250)
# plt.hist(x)
# plt.show()



# Matplotlib Pie Charts
# Creating Pie Charts
# A simple pie chart:

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()

# Labels
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show()

# Start Angle

# Start the first wedge at 90 degrees:
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show()


# Explode
# Pull the "Apples" wedge 0.2 from the center of the pie:
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()

# Shadow
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()

# Colors
# Specify a new color for each wedge:
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()

# Legend
# add a legend

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 