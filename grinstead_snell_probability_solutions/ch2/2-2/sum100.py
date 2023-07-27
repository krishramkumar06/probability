import random
import numpy as np
import matplotlib.pyplot as plt

def sumhundred(n):
    list = []
    for i in range(n):
        sum = 0
        for j in range(100):
            sum += random.random()
        list.append(sum)
    return list

Sumthousand = sumhundred(10000)
print(Sumthousand)

N_points = 10000
n_bins = 50

# Generate two normal distributions
plt.hist(Sumthousand,density=1, bins=20) 
# plt.axis([50, 110, 0, 0.06]) 
#axis([xmin,xmax,ymin,ymax])
plt.xlabel('Weight')
plt.ylabel('Probability')
plt.show()