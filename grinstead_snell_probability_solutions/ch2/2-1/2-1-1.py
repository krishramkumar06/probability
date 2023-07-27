import random
import numpy as np
import matplotlib.pyplot as plt

def spinner(n):
    list = []
    distrib = []
    sum = 0
    onehalf = 0
    onethird = 0
    onesixth = 0
    for i in range(n):
        k = random.random();
        if k <= 1/2:
           onehalf += 1
        elif k > 5/6:
            onesixth += 1
        else:
            onethird += 1
        list.append(k)
    distrib = [onehalf/n,onethird/n,onesixth/n]
    weighteddistrib = [onehalf/(0.5*n),onethird/(1/3*n),onesixth/(1/6*n)]
    print(distrib)
    print(weighteddistrib)
    print
    return list

ThousandSpinner = spinner(100000)

# Now plot a bar graph whose bars have width 1/2, 1/3, and 1/6, and areas equal to the corresponding fractions as determined by your simulation. 
# Show that the heights of the bars are all nearly the same.

# instead of doing all that, i will just divide the areas by their width. woahh everythings close to 1!

# print(ThousandSpinner)

# N_points = 10000
# n_bins = 50

# # Generate two normal distributions
# plt.hist(Sumthousand,density=1, bins=20) 
# # plt.axis([50, 110, 0, 0.06]) 
# #axis([xmin,xmax,ymin,ymax])
# plt.xlabel('Weight')
# plt.ylabel('Probability')
# plt.show()