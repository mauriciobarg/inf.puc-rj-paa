from random import randint
from Sorting import MergeSort

V = MergeSort([randint(0, 100) for x in range(10)])

def BinarySearch(i, A):
    n = len(A)
    mid = n // 2
    if len(A) == 0:
        return False
    if A[mid] != i and n > 1:
        if A[mid] < i:
            return BinarySearch(i, A[(mid + 1):])
        elif A[mid] > i:
            return BinarySearch(i, A[:mid])
    elif A[mid] == i:
        return True
    else:
        return False