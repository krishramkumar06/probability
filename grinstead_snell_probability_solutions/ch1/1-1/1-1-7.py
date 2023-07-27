import random
import numpy as np
import matplotlib.pyplot as plt
# a roulette wheel has 38 slots numbered 0, 00, 1, 2, . . . , 36. 
# The 0 and 00 slots are green and half of the remaining 36 slots are red and half are black.
# If you bet 1 dollar on red, you win 1 dollar if the ball stops in a red slot and otherwise you lose 1 dollar.
# Another form of bet for roulette is to bet that a specific number (say 17) will turn up.
# If the ball stops on your number, you get your dollar back plus 35 dollars. If not, you lose your dollar.


# betting on red
def roulette1(n):
    numgames = 0
    winnings1 = 0

    games = [0]
    timedwinnings = [0]

    for i in range(n):
        num = random.randint(1,38)

        if num <= 18:
            numgames += 1
            winnings1 += 1
        else:
            numgames += 1
            winnings1 += -1
        
        games.append(numgames)
        timedwinnings.append(winnings1)
    return [games, timedwinnings]

Roulette1 = roulette1(500)
plt.scatter(Roulette1[0], Roulette1[1], 'r-', label = "Roulette1")
plt.title("Roulette of Type 1 Winnings")
plt.show()

# if value is greater than zero, plot it with a different color?

# 


# bro what is global really??
# betting on 17

def roulette2(n):
    numgames = 0
    winnings2 = 0

    games = [0]
    timedwinnings = [0]

    for i in range(n):
        num = random.randint(1,38)

        if num == 17:
            numgames += 1
            winnings2 += 36
        else:
            numgames += 1
            winnings2 += -1
        
        games.append(numgames)
        timedwinnings.append(winnings2)
    return [games, timedwinnings]

Roulette1 = roulette1(500)
plt.plot(Roulette1[0], Roulette1[1], 'r-', label = "Roulette1")
plt.title("Roulette of Type 1 Winnings")
plt.show()


Roulette2 = roulette2(500)
plt.plot(Roulette2[0], Roulette2[1], 'b-', label = "Roulette2")
plt.title("Roulette of Type 2 Winnings")
plt.show()

# conquering the graphing beast will be no easy task