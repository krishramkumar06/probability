import random
import math
import numpy as np
import matplotlib.pyplot as plt

def lambda1Generator():
    rand = random.random()
    if rand > 0.1:
        return 1/3
    else:
        return 1/73

list = []
while len(list)<100:
    lambda1 =lambda1Generator()
    randVar = (-1/lambda1)*math.log(random.random())
    if randVar > 100:
        print(1/lambda1)
        list.append(randVar)

list = [x - 100 for x in list]

print("Wait Time after 100: ", sum(list)/len(list))

# Wait Time after 100:  72.87715443485199
# barely ever possible for the wait time with 3 to get to over 100