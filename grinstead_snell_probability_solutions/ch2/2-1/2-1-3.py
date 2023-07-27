import random

def MonteCarlo(n):
    dub = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if (x-.5)*(x-.5) + (y-.5)*(y-.5) <= 1/4:
            dub += 1
    return(dub/n)

print(4*MonteCarlo(1000))

# getting values like 3.144, 3.016, 3.212, 3.112, 3.228, 3.118. Around pi pm 0.15