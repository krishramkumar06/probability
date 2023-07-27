# mindnumbingly hard
from numpy import random
import numpy as np

def randomArray(n): #gives random array of size n
    arr = (np.arange(1,n+1))
    random.shuffle(arr)
    return(arr)

def kFinder(arr): #finds the value of k dictated by the problem (k is the smallest integer for which (the sum from i = k to n-1 of 1/i )<= 1)
    i = 1
    sum = 0
    while sum < 1:
        sum += 1/(arr.size-i)
        i += 1
    k = n - i + 2
    return k

def leftMaxFinder(arr, k): #finds the maximum of the first k-1 members of our random arrray
    subarray = np.zeros((n,), dtype=int)

    for i in range((k-1)):
        subarray[i] = arr[i]
        arr[i] = 0

    return subarray.max()

wincount = 0 

def rightMaxFinder(arr, leftMax): #finds the first number on the right size that is greater than leftMax
    for i in range((k-1)):
        arr[i] = 0
    # print("leftBlanked array:", arr)
    for i in range(arr.size):
        if leftMax < arr[i]:
            return arr[i]
    return 0

# print("P(winning): ", wincount/numtrials )
# we want to add 1 to wincount if rightmax = n

wincount = 0
trialcount = 10000
n = 10 #number of people

for i in range(trialcount):
    arr = randomArray(n)
    # print("Original Array: ", arr)
    k = kFinder(arr)
    # print("k: ", k)
    leftMax = leftMaxFinder(arr, k)
    # print("leftMax: ", leftMax)
    rightMax = rightMaxFinder(arr, leftMax)
    # print("rightMax", rightMax, " vs N = ", n)
    if rightMax == n:
        wincount += 1
        # print("SUCCESSS!!!!!!")

print("final ratio: ", wincount/trialcount)
