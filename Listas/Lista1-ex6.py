from random import randint
from math import inf

V = [randint(-10, 10) for x in range(10)]

## O(n^3)
def On3(A, x):
    n = len(A)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if A[i] + A[j] + A[k] == x:
                    return True
    return False

## O(n^2 log n)
def On2logn(A, x):
    A = sorted(A)
    n = len(A)
    aux_1, aux_2 = 0, 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            remainder = x - A[i] - A[j]
            aux_1, aux_2 = A[i], A[j]
            A[i], A[j] = inf, inf
            if remainder in A:
                return True
            A[i], A[j] = aux_1, aux_2
    return False

def On2(A, x):
    A = sorted(A)
    n = len(A)
    for i in range(n - 2):
        l = i + 1
        r = n - 1
        while l < r:
            if A[i] + A[l] + A[r] > x:
                r -= 1
            elif A[i] + A[l] + A[r] < x:
                l += 1
            else:
                return True
    return False

# V = [-7, -1, 7, 5, 7, -8, -7, 1, 2, -8]
print(V)
print(On3(V, 10))
for i in range(100000):
    if On2logn(V, 10) != On2(V, 10):
        print(On2logn(V, 10))
        print(On2(V, 10))

