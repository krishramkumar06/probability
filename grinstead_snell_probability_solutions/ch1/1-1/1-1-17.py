import random
import numpy as np
import matplotlib.pyplot as plt

# random walk on 1-d

def CoinFlip():
        num = random.random()
        if num >= 0.5:
            return 1
        else:
            return -1

def randomWalk1D(n):
    timesAtZero = []
    winnings = 0
    list = [0]
    for i in range(n):
        winnings += CoinFlip()
        list.append(winnings)
        if list[i] == 0:
             timesAtZero.append(i)
    print("timesAtZero: ", timesAtZero)
    timeDifferences = []
    for i in range(1, len(timesAtZero)):
        timeDifferences.append(timesAtZero[i] - timesAtZero[i-1])
    print("timeDifferences: ", timeDifferences)
    return list

# lengthWalk = 1000
# specificWalk = randomWalk1D(lengthWalk)
# print(specificWalk)

import random
import matplotlib.pyplot as plt

def randomWalk2D(n):
    position = [0, 0]
    def step():
        array.append(position.copy())  # Append a copy of the position list
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

lengthWalk = 14
specificWalk = randomWalk2D(lengthWalk)

# Extract x and y coordinates from specificWalk
x_coords = [step[0] for step in specificWalk]
y_coords = [step[1] for step in specificWalk]

# Center the random walk at the origin (0, 0)
final_x, final_y = specificWalk[-1]
x_coords = [x - final_x for x in x_coords]
y_coords = [y - final_y for y in y_coords]

# Plot the centered random walk
plt.plot(x_coords, y_coords, marker='o', linestyle='-')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Centered 2D Random Walk')
plt.grid(True)
plt.show()


# plt.plot(specificWalk)
# plt.show()

# timesAtZero:  [0, 6, 8, 16, 18, 28, 870, 894]
# timeDifferences:  [6, 2, 8, 2, 10, 842, 24]

# i don't know why this would indicate that the walker would always return