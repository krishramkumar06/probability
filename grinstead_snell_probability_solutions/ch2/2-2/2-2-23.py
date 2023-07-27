import random
import math
import numpy as np
import matplotlib.pyplot as plt

logdist = []
n = 10000

def lograndgenerator(n):
    for i in range(n):
        rand = random.random()
        logrand = -math.log(rand)
        logdist.append(logrand)

lograndgenerator(n)

# Define intervals and count occurrences within each interval
intervals = np.arange(0, 10.1, 0.1)
interval_counts, _ = np.histogram(logdist, bins=intervals)

# Normalize the counts to get probabilities (density values)
total_samples = len(logdist)
bin_width = intervals[1] - intervals[0]
density_values = interval_counts / (total_samples * bin_width)

# Compute the fine-grained midpoints for the density function
fine_intervals = np.linspace(0, 10, 1000)
fine_midpoints = (fine_intervals[:-1] + fine_intervals[1:]) / 2

# Compute the density function f(x) = e^(-x) for each fine-grained midpoint
density_theoretical = np.exp(-fine_midpoints)

# Plot the normalized bar graph
plt.bar(intervals[:-1], density_values, width=0.1, align='edge', label='Normalized Density')

# Plot the density function f(x) = e^(-x)
plt.plot(fine_midpoints, density_theoretical, 'r', label='Theoretical Density (e^(-x))')

plt.xlabel('x')
plt.ylabel('Density')
plt.title('Observed vs Theoretical Density')
plt.legend()
plt.grid(True)
plt.show()
