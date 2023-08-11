from itertools import permutations

def countOccurances(lst, n):
    numOccurrences = 0
    for i in lst:
        if i == n:
            numOccurrences += 1
    return numOccurrences

for n in range(2,10):
    l = list(permutations(range(1, n + 1)))
    numFixed = []

    for i in range(len(l)):
        fixed = 0
        list1 = l[i]
        for j in range(len(list1)):
            if list1[j] == j + 1:
                fixed += 1
        numFixed.append(fixed)

    # print("Permutations:", l)
    # print("Num Fixed:", numFixed)

    for i in range(n + 1):
        print(i, "fixed points:", countOccurances(numFixed, i))
    print()
    print("% Derangements: ", countOccurances(numFixed, 0)/len(l))
    print("% 1 fix: ", countOccurances(numFixed, 1)/len(l))
    print()


