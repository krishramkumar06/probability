import random

HeadsCount = 0
TailsCount = 0

def CoinFlip():
        num = random.random()
        if num >= 0.5:
            global HeadsCount
            HeadsCount += 1
        else:
            global TailsCount
            TailsCount += 1

for i in range(100017):
    CoinFlip()
    if i % 100 == 0:
        print('Tosses: ', i)
        print('The # of heads minus tosses/2: ', (HeadsCount - i/2))
        print('The proportion of heads minus 1/2:',(HeadsCount/(HeadsCount+TailsCount)-0.5))

print('Final HeadsCount:', HeadsCount)
print('Final TailsCount:', TailsCount)

# 'The number of heads minus half the number of tosses is' + 
# 'The proportion of heads minus 1/2 is' + 
# 'The total count of Heads is ' + 
# 'The total count of Tails is ' + 

# neither number seems to go to zero?? wtf????