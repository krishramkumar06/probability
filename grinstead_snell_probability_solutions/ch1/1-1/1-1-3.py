import random

ninecount = 0
tencount = 0

def DiceTriple():
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = random.randint(1,6)
    # Is there a nice way to define all three variables at once?
    triple =(a,b,c)
    if random.random() <= 0.01:
     print(triple, "-->", a+b+c)
    if a+b+c == 9:
        global ninecount
        ninecount += 1
    elif a+b+c == 10: 
        global tencount
        tencount += 1

# Figure out a better way to define functions so that doing them n times is more straightforward

k = 4913
for i in range(k):
    DiceTriple()

print('ninecount: ', ninecount)
print('ninecount proportion: ', ninecount/k)

print('tencount: ', tencount)
print('tencount proportion: ', tencount/k)

print('difference: ', (ninecount-tencount)/k)

# This is nuts

# ninecount:  198154
# ninecount proportion:  0.11539568010156245
# tencount:  214734
# tencount proportion:  0.12505110152168974
# difference:  -0.009655421420127302

# DAWG IS THE PROBLEM CORRECT? 10 and 11 have the same, not 9 and 10?