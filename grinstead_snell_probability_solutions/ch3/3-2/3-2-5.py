import random

def CoinFlip():
    rand = random.random()
    if rand > 0.5:
        return 1
    else:
        return 0

num35to65 = 0
num40to60 = 0
num45to55 = 0

def Trial(n):
    numheads = 0
    for i in range(n):
        numheads += CoinFlip()
    return numheads

numTrials = 10000
numFlips = 100

def boolBetween(num,lower,upper):
    return int(num) >= int(lower) and int(num) <= int(upper)

for i in range(numTrials):
    result100 = Trial(numFlips)
    print("result100: ", result100)
    if boolBetween(result100,35,65):
        num35to65 += 1
    if boolBetween(result100,40,60):
        num40to60 += 1
    if boolBetween(result100,45,55):
        num45to55 += 1

print("The probability that, in 100 tosses of a fair coin, the number of heads that turns up lies between")
print("(1) 35 and 65", num35to65/numTrials)
print("(2) 40 and 60", num40to60/numTrials)
print("(3) 45 and 55", num45to55/numTrials)

# The probability that, in 100 tosses of a fair coin, the number of heads that turns up lies between
# (1) 35 and 65 0.9987
# (2) 40 and 60 0.9653
# (3) 45 and 55 0.7387

# getting boolbetween to work was interesting. i liked my use of functions here