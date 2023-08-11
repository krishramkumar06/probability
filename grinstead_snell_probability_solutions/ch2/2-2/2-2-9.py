import random
import math
import numpy as np
import matplotlib.pyplot as plt

lambda1 = 1/10
numSimulations = 10000
list = []
while len(list)<1000:
    randVar = (-1/lambda1)*math.log(random.random())
    if randVar > 100:
        list.append(randVar)

list = [x - 100 for x in list]

print("Wait Time after 100: ", sum(list)/len(list))

# Wait Time after 100:  9.653784764376365