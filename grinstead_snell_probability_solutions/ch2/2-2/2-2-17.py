import random
import math
import numpy as np
import matplotlib.pyplot as plt

cond1 = 0
cond2 = 0
cond3 = 0
n = 1000
for i in range(n):
    rand = random.uniform(2,10)
    if rand > 5:
        cond1 += 1
    if rand > 5 and rand < 7:
        cond2 += 1
    if rand < 5 or rand > 7:
        cond3 += 1
print("Fraction that X>5: ", cond1/n)
print("Fraction that 5<X<7: ", cond2/n)
print("Fraction that x^2 - 12x + 35 > 0 : ", cond3/n)

var1 = cond1/n - 5/8
var2 = cond2/n - 2/8
var3 = cond3/n - 6/8

print("var1: ", var1)
print("var2: ", var2)
print("var3: ", var3)

# Fraction that X>5:  0.643
# Fraction that 5<X<7:  0.274
# Fraction that x^2 - 12x + 35 > 0 :  0.726
# var1:  0.018000000000000016
# var2:  0.02400000000000002
# var3:  -0.02400000000000002