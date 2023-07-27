import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def randomWalk2D(n):
    position = [0, 0]
    def step():
        array.append(position.copy())
        num = random.randint(1, 4)
        if num == 1:
            position[1] += 1
        if num == 2:
            position[0] += 1
        if num == 3:
            position[1] -= 1
        if num == 4:
            position[0] -= 1

    array = []
    for i in range(n):
        step()
    return array

lengthWalk = 200
specificWalk = randomWalk2D(lengthWalk)

# Extract x and y coordinates from specificWalk
x_coords = [step[0] for step in specificWalk]
y_coords = [step[1] for step in specificWalk]

# Set up the plot
fig, ax = plt.subplots()
line, = ax.plot([], [], marker='o', linestyle='-', color='blue')
scat = ax.scatter([], [], c=[], cmap='viridis', marker='o', s=50)

# Set the aspect ratio to be equal
ax.set_aspect('equal')

# Set axis limits to show the entire random walk path
ax.set_xlim(min(x_coords) - 1, max(x_coords) + 1)
ax.set_ylim(min(y_coords) - 1, max(y_coords) + 1)

# Function to initialize the animation
def init():
    line.set_data([], [])
    scat.set_offsets(np.empty((0, 2)))
    return line, scat

# Function to update the animation at each frame
def update(frame):
    if frame >= 5:
        x = x_coords[frame-4:frame+1]
        y = y_coords[frame-4:frame+1]
    else:
        x = x_coords[:frame+1]
        y = y_coords[:frame+1]
    line.set_data(x[-1], y[-1])  # Set the current position for line plot
    scat.set_offsets(np.column_stack((x, y)))  # Set all positions for scatter plot
    colors = np.arange(len(x))  # Color map based on the number of positions
    scat.set_array(colors)  # Assign colors to scatter plot points
    return line, scat

# Animate the random walk
ani = FuncAnimation(fig, update, frames=len(x_coords), init_func=init, interval=100)

# Display the plot in the interactive environment (e.g., Jupyter Notebook)
plt.show()
