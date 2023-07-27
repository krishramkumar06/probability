import random
import numpy as np
import matplotlib.pyplot as plt

# A certain town is served by two hospitals. In the larger hospital about 45 
# babies are born each day, and in the smaller hospital 15 babies are born each 
# day. Although the overall proportion of boys is about 50 percent, the actual 
# proportion at either hospital may be more or less than 50 percent on any day.

# At the end of a year, which hospital will have the greater number of days on
# which more than 60 percent of the babies born were boys?

def CoinFlip():
        num = random.random()
        if num >= 0.5:
            return 1
        else:
            return 0
        
def game(n):
    winnings = 0
    for i in range (n):
         winnings += CoinFlip()
    return winnings

numSimulations = 10000
windaysmall = 0
windaybig = 0
smallSize = 15
bigSize = 60
for i in range(numSimulations):
    small = game(smallSize)
    if small/smallSize >= 0.6:
        windaysmall += 1
    big = game(bigSize)
    if big/bigSize >= 0.6:
        windaybig += 1

print("Proportion Small: ", windaysmall/numSimulations)
print("Proportion Big: ", windaybig/numSimulations)
print("Difference: ", (windaybig-windaysmall)/numSimulations)

# n = 60 big hospital, n = 15 small hospital

# # Proportion Small:  0.3012
# Proportion Big:  0.0804
# Difference:  -0.2208

# why is this?
# B. The smaller hospital. The intuitive Law of Large Numbers says 
# that with more observations the experimental average tends to get closer to the true proportion. A big hospital has more observations, so their number will be less likely to stray from 50%, or have less variance.
