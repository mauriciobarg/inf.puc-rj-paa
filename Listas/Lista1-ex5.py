from random import randint
from math import inf

V = sorted([randint(0, 10) for x in range(10)])
T = sorted([0, 1, 3, 4, 5, 6, 6, 8, 9, 10])

def FindKNearest(A, j, k):
    n = len(A)
    a = 1
    b = 1
    i = 0
    while i < k:
        if j - a >= 0:
            l = A[j - a]
        else:
            l = inf
        if j + b < n:
            r = A[j + b]
        else:
            r = inf
        if abs(A[j] - l) < abs(A[j] - r):
            print(l)
            a += 1
        elif abs(A[j] - l) > abs(A[j] - r):
            print(r)
            b += 1
        else:
            print(l, r)
            a += 1
            b += 1
            k -= 1
        i += 1
    
print(V)
FindKNearest(V, 4, 3)

