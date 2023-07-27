import random
import numpy as np
import matplotlib.pyplot as plt

# simulating this feels very annoying.
list = [1,2,3,4]

def roulette1():
    numgames = 0
    winnings1 = 0

    games = [0]
    timedwinnings = [0]

    while len(list) > 0:
        change = 0
        if len(list) == 1:
            change = list[0]
        else:
            change = list[0] + list[len(list) - 1]

        num = random.randint(1,38)
        if num <= 18:
            numgames += 1
            winnings1 += change
            del list[-1]
            if len(list) == 0:
                break
            del list[0]
        else:
            numgames += 1
            winnings1 += -change
            list.append(change)
        games.append(numgames)
        timedwinnings.append(winnings1)

    return [games, timedwinnings]

Roulette1 = roulette1()
plt.plot(Roulette1[0], Roulette1[1], 'r-', label = "Roulette1")
plt.title("Roulette of Type 1 Winnings")
plt.show()

# simulation works for the most part
# sometimes you can go deeep in the negatives, the reason why it doesnt work as a foolproof is that we do not have infinite money to go into debt for
