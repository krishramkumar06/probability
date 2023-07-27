import random
import numpy as np
import matplotlib.pyplot as plt

# Modify the program HTSimulation so that 
# it keeps track of the maximum of Peter’s 
# winnings in each game of 40 tosses. 
# Have your program print out the proportion 
# of times that your total winnings take on 
# values 0, 2, 4, . . . , 40. 


def CoinFlip():
        num = random.random()
        if num >= 0.5:
            return 1
        else:
            return -1
        
def game(n):
    winnings = 0
    for i in range (n):
         winnings += CoinFlip()
    return winnings

numSimulations = 5000
numTosses = 40
totalWinnings = 0
array = np.zeros(numTosses+1)

for i in range(numSimulations):
     gamewin = game(numTosses)
    #  only works for even numbers
     array[int((gamewin + numTosses)/2)] = array[int((gamewin + numTosses)/2)] + 1
     totalWinnings += gamewin
     print(gamewin)

print("numSimulations: ", numSimulations)
print("numTosses: ", numTosses)
print("totalWinnings: ", totalWinnings)
print("avgWinnings: ", totalWinnings/numSimulations)
print("array: ", array)
print("arrayProportion: ", array/numSimulations)
# okay about to use some big brain arraylists here.
# we take on values from -40, -38, ... -2, 0 , 2, ..., 38, 40
# list of size 41
#  if winnings = num add one to list[num/2 + 20]
# then we divide out the entire list by numSimulations

# Calculate the 
# corresponding exact probabilities for games 
# of two tosses and four tosses.

# two tosses means -2, 0, 2 -> [0.25, 0.5, 0.25]
# fours tosses means -4, -2, 0, 2, 4 -> (1/2^4)[1, 4, 6, 4, 1]
# its just binomial