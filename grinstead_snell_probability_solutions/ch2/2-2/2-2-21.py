import random

def makeTriangle():
    pointA = 0
    pointB = random.random()
    pointC = random.random()
    if (pointB < 0.5 and pointC < 0.5) or (pointB > 0.5 and pointC > 0.5):
        return 1
    else:
        return 0

n = 10000
wins = 0

for i in range(n):
    wins += makeTriangle()

print("probTriangle: ", wins/n)

# probTriangle:  0.4992