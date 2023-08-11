import random
import math

def b(n,p,j):
    return (math.comb(n, j)) * (p**j) * ((1-p)**(n-j))

# we need to pick an n large enough such that there exists an m for which
# alpha(0.5) <= .05
# alpha(0.75) >= .95

def alpha(p, m, n ):
    sum = 0
    for k in range(m, n):
        sum += b(n, p, k)
    return sum

numParticipants = 100

# print(alpha(0.5, numParticipants-50,numParticipants))
for m in range(numParticipants):
    alpha1 = alpha(0.5, m, numParticipants+1)
    alpha2 = alpha(0.75, m, numParticipants+1)
    if(alpha1 <= 0.05 and alpha2 >= 0.95):
        print()
        print("WE HAVE A WINNER WHEN m = ", m)
        print()
        print("alpha(0.5) when m = ", m )
        print(alpha1)
        print()
        print("alpha(0.5) when m = ", m )
        print(1 - alpha2)
        print()

# the critical value can be any between 59 and 68