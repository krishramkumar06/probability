import random
import numpy as np
import matplotlib.pyplot as plt

# Assuming that a player has a fifty-fifty chance of making a shot and makes 20 shots a game,
#  estimate by simulation the proportion of the games in which the player will have a streak of 5 or more hits.

# win if ColdStreak breaches 5 or HotStreak breaches 5
# how am i going to do streaks?

def CoinFlip():
        num = random.random()
        if num >= 0.5:
            return 1
        else:
            return 0

def nShotGame(n):
    array = np.zeros(n)
    for i in range(n):
        array[i] = CoinFlip()
    return array

# print(nShotGame(20))
# okay so this is working how i want, now i need to count trailing 1s and 0s
# This is clever counting.
# make a list with the number of streaks? append it to the end every time it fails
# if list[i+1] = list[i-1] add one to streak
# if the streak BREAKS, append this to our list of streaks
# if the max of this array > 5, count this as a win

# do you do this recursively? how do i even look this up lol

numShots = 20
def game():
    array = nShotGame(numShots)
    # array = np.array([1, 1, 1, 0, 0, 1, 0, 1, 1, 1])
    # should print hot max of 3, cold max of 2
    # print(array)
    coldStreak = 1
    hotStreak = 1
    listCold = []
    listHot = []
    for i in range(1, numShots):
        if array[i] == 0 and array[i-1] ==0:
            coldStreak += 1
            hotStreak = 0
        elif array[i] == 0 and array[i-1] ==1:
            # print("I am about to append ", hotStreak, " to hotStreak")
            listHot.append(hotStreak)
            hotStreak = 0
            coldStreak = 1
        elif array[i] == 1 and array[i-1] ==0:
            # print("I am about to append ", coldStreak, " to coldStreak")
            listCold.append(coldStreak)
            coldStreak = 0
            hotStreak = 1
        elif array[i] == 1 and array[i-1] == 1:
            hotStreak += 1
            coldStreak = 0
        # print("i: ", i)
        # print("coldstreak: ", coldStreak, ", hotstreak: ", hotStreak)
        # print()
    listCold.append(coldStreak)
    listHot.append(hotStreak)
    # print("cold list: ", listCold)
    # print("hot list: ", listHot)
    # print("cold max streak: ", max(listCold))
    # print("hot max streak: ", max(listHot))      
    if max(listCold) >= 5 or max(listHot) >= 5:
        # print("Winner!!!!")
        return 1
    else:
        return 0

gamecount = 100000
wins = 0

for i in range(gamecount):
    wins += game()
# print("wins: ", wins)
print("proportion of wins: ", wins/gamecount)

# proportion of wins:  0.45779