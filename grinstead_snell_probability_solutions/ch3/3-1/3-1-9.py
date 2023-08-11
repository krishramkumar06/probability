import math

def inequality(n):
    lower = math.sqrt(2 * math.pi * n) * (n / math.e) ** n * math.e ** (1 / (12 * n + 1))
    middle = math.factorial(n)
    upper = math.sqrt(2 * math.pi * n) * (n / math.e) ** n * math.e ** (1 / (12 * n))
    print("lower:", lower)
    print("middle:", middle)
    print("upper:", upper)
    if (lower < middle) and (middle <= upper):
        print("Inequality holds for n =", n)
    else:
        print("INEQUALITY IS A LIE")

num = 9

for i in range(1, num):
    inequality(i)
