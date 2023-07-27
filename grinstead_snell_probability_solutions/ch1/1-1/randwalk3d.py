import random
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def randomWalk3D(n):
    position = [0, 0, 0]
    def step():
        array.append(position.copy())
        num = random.randint(1, 6)
        if num == 1:
            position[0] += 1
        if num == 2:
            position[0] -= 1
        if num == 3:
            position[1] += 1
        if num == 4:
            position[1] -= 1
        if num == 5:
            position[2] += 1
        if num == 6:
            position[2] -= 1

    array = []
    for i in range(n):
        step()
    return array

lengthWalk = 200
specificWalk = randomWalk3D(lengthWalk)

# Extract x, y, and z coordinates from specificWalk
x_coords = [step[0] for step in specificWalk]
y_coords = [step[1] for step in specificWalk]
z_coords = [step[2] for step in specificWalk]

# Set up the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
line, = ax.plot([], [], [], marker='o', linestyle='-', color='blue')
scat = ax.scatter([], [], [], c=[], cmap='viridis', marker='o', s=50)

# Highlight the origin point in red
ax.scatter(0, 0, 0, color='red', s=100)

# Set axis limits to show the entire random walk path
ax.set_xlim(min(x_coords) - 1, max(x_coords) + 1)
ax.set_ylim(min(y_coords) - 1, max(y_coords) + 1)
ax.set_zlim(min(z_coords) - 1, max(z_coords) + 1)

# Function to initialize the animation
def init():
    line.set_data([], [])
    scat._offsets3d = (np.empty(0), np.empty(0), np.empty(0))
    return line, scat

# Function to update the animation at each frame
def update(frame):
    x = x_coords[max(0, frame-5):frame+1]
    y = y_coords[max(0, frame-5):frame+1]
    z = z_coords[max(0, frame-5):frame+1]
    line.set_data(x[-1], y[-1])
    line.set_3d_properties(z[-1])
    scat._offsets3d = (x, y, z)
    colors = np.arange(len(x))
    scat.set_array(colors)
    return line, scat

# Animate the random walk in 3D
ani = FuncAnimation(fig, update, frames=len(x_coords), init_func=init, interval=100)

# Save the animation as an mp4 file
ani.save('random_walk_animation.mp4', writer='ffmpeg')

# Display the 3D plot in the interactive environment (e.g., Jupyter Notebook)
plt.show()
