def pascal(n):
    """
    Yield up to row ``n`` of Pascal's triangle, one row at a time.

    The first row is row 0.
    """
    def newrow(row):
        "Calculate a row of Pascal's triangle given the previous one."
        prev = 0
        for x in row:
            yield prev + x
            prev = x
        yield 1

    prevrow = [1]
    yield prevrow
    for x in range(n):
        prevrow = list(newrow(prevrow))
        yield prevrow

TwentyRows = list(pascal(20))
print(TwentyRows)

def reduceModn(n,l):
    return [i % n for i in l]

for m in range(2,8):
    print()
    Solution = [reduceModn(m,l) for l in TwentyRows]
    print(Solution)

mod2 = [reduceModn(2,l) for l in TwentyRows]

for i in range(len(mod2)):
    print(mod2[i])

# [[1], [1, 1], [1, 0, 1], [1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 1, 1], [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]]
# i learned so much about lists in this exercise oml