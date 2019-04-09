from random import randint

V = [randint(0, 100) for x in range(10)]

def BubbleSort(A):
    n = len(A) - 1
    for i in range(n) :
        for j in range(n - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A

def SelectionSort(A):
    n = len(A) - 1
    for i in range(n):
        minVal = A[i]
        minIndex = i
        for j in range(i + 1, n):
            if A[j] < minVal:
                minVal = A[j]
                minIndex = j
        A[i], A[minIndex] = A[minIndex], A[i]
    return A

def InsertionSort(A):
    n = len(A)
    for i in range(1, n):
        current = A[i]
        j = i - 1
        while j >= 0 and current < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = current
    return A

def MergeSort(A):
    pass

print(V)
print(InsertionSort(V))

