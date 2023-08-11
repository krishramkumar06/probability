import random
import math
import numpy as np
import matplotlib.pyplot as plt

cond1 = 0
cond2 = 0
cond3 = 0
cond4 = 0
n = 1000
for i in range(n):
    rand = random.random()
    if rand > 1/3 and rand < 2/3:
        cond1 += 1
    if abs(rand - 1/2) < 1/4:
        cond2 += 1
    if rand < 1/4 or 1 - rand < 1/4:
        cond3 += 1
    if 3*rand*rand< rand:
        cond4 += 1


print("Fraction that cond1: ", cond1/n)
print("Fraction that cond2: ", cond2/n)
print("Fraction that cond3: ", cond3/n)
print("Fraction that cond4: ", cond4/n)


var1 = cond1/n - 1/3
var2 = cond2/n - 1/2
var3 = cond3/n - 1/2
var4 = cond4/n - 1/3
print("var1: ", var1)
print("var2: ", var2)
print("var3: ", var3)
print("var4: ", var4)


# Fraction that cond1:  0.324
# Fraction that cond2:  0.487
# Fraction that cond3:  0.513
# Fraction that cond4:  0.343
# var1:  -0.009333333333333305
# var2:  -0.013000000000000012
# var3:  0.013000000000000012
# var4:  0.009666666666666712