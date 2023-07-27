# doesn't seem too bad honestly.

import random as rnd
import math

def RandomChord(n):
    length = 0
    k=0
    overRt3 = 0
    while k <= n:
        x = 100*rnd.random() - 50
        y = x = 100*rnd.random() - 50
        theta = (math.pi)*rnd.random() - (0.5)*(math.pi)
        m = math.tan(theta)
        d = abs((y-m*x)/(math.sqrt(m*m + 1)))
        if d < 1:
            l = 2*math.sqrt(1-d*d)
            if l > math.sqrt(3):
                overRt3 += 1
            length += l
            k += 1
    print(overRt3/k)
    return(length/k)


print(math.sqrt(3))
print(RandomChord(10000))

# sqrt3 = 1.7320508075688772
# estimation =  1.623550978707335
# P(overRt3)= 0.5595440455954405
# This is somewhere in between case 2 and case 3. Its different!