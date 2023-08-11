import random
import math

def b(n,p,j):
    return (math.comb(n, j)) * (p**j) * ((1-p)**(n-j))

sum = 0

for i in range (2,5):
    val = b(4, 0.99, i)
    print(val)
    sum += val
    
print(sum)