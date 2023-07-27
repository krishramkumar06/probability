import random
import numpy as np
import matplotlib.pyplot as plt

# A gambler plays a game in which on each play he wins one dollar with prob- ability p and loses one dollar with probability q = 1 − p.
# finding the probability wx of winning an amount T before losing everything, starting with state x. 
# Show that this problem may be considered to be an absorbing Markov chain with states 0, 1, 2, . . . , T with 0 and T absorbing states. 
# Suppose that a gambler has probability p = .48 of winning on each play. 
# Suppose, in addition, that the gambler starts with 50 dollars and that T = 100 dollars. 
# Simulate this game 100 times and see how often the gambler is ruined. 
# This estimates w50.

dollars = 50

T = 1000
p = 0.51

wincount = 0

def gamble():
    num = random.random()
    global dollars
    if num >= p:
        dollars -= 1
    else:
        dollars += 1
    print(dollars)
    # if dollars == 0:
    #     print("I lost! :(")
    #     global dollars
    #     dollars = 50
    # elif dollars == 100:
    #     print("I won! :)")
    #     global wincount
    #     global dollars
    #     wincount += 1
    #     dollars = 50

def round():
    global dollars
    global wincount
    while not (dollars == 0 or dollars == T):
        gamble()
    if dollars == 0:
        print("I lost! :(")
        dollars = 50
    elif dollars == T:
        print("I won! :)")
        wincount += 1
        dollars = 50

numRounds = 1
for i in range(numRounds):
    round()

print(wincount/numRounds)
print(wincount*1000 - 50*numRounds)

# we want to see how many times he takes a dub, how many times he loses
# the proportion
