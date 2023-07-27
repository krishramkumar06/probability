# implement buffon's needle
# now include vertical lines? dude.
# im just going to try to remove it from its geometric context

import random
import math

def LaplaceNeedle(n):
    dub = 0
    for i in range(n):
        d1 = (0.5)*random.random()
        d2 = (0.5)*random.random()
        theta = (0.5)*(math.pi)*random.random()
        if d1 <= (0.5) * math.sin(theta) or d1 <= (0.5) * math.cos(theta):
            dub += 1
    return(dub/n)

a = LaplaceNeedle(100)
b = LaplaceNeedle(1000)
c = LaplaceNeedle(10000)
print('proprtion: ', a , ' pi estimate: ', 3/a )
print('proprtion: ', b , ' pi estimate: ', 3/b )
print('proprtion: ', c , ' pi estimate: ', 3/c )

# i didn't do bufoon's problem (exercise 6) but this doesn't seem too good of a pi estimation

# proprtion:  0.9  pi estimate:  3.333333333333333
# proprtion:  0.885  pi estimate:  3.389830508474576
# proprtion:  0.9013  pi estimate:  3.3285254632197936