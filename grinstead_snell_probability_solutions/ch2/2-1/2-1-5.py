import random

def MonteCarlo(n):
    dub = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if y <= 1/(x+1):
            dub += 1
    return(dub/n)

print(MonteCarlo(10000))

# ln(2) = 0.69314718
# 0.6961, off by .003