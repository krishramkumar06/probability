import random
# lets actually solve the problem before coding it
# Calculate f(n), the probability of at least one triple-six when three dice are rolled n times
# Is this even a simulation problem???? Ig i can simulate the 150 case a bunch of times and see if it matches estimation

sucsesses = 0
triplesixcount = 0

def DiceTriple(n):

    for i in range(n):
        global triplesixcount
        a = random.randint(1,6)
        b = random.randint(1,6)
        c = random.randint(1,6)
        # Is there a nice way to define all three variables at once?
        triple =(a,b,c)
        if random.random() <= 0.0000001:
            print(triple, "-->", a+b+c)
        if a == 6 and b == 6 and c == 6:
            triplesixcount += 1

k = 5001
for i in range(k):
    DiceTriple(150)
    if triplesixcount >= 1:
        sucsesses += 1
    triplesixcount = 0

print(sucsesses/k)