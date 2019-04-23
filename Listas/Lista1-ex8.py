from random import randint
V = sorted([1, 1, 1, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 10, 10, 10])
m = 3
Y = [m**2 + x for x in [randint(0, m) for y in range(m)]]

## A
def FindMostFrequent(A):
    n = len(A)
    current = A[0]
    biggest = 0
    count = 1
    current_max = 0
    for i in range(1, n):
        if current == A[i]:
            count += 1
            if count > current_max:
                current_max = count
                biggest = current
        else:
            if count > current_max:
                current_max = count
                biggest = current
            count = 1
            current = A[i]
    return(biggest, current_max)

## B
def FindMostFrequentSquared(A):
    n = len(A)
    B = [0]*(n + 1)
    for i in range(n):
        B[A[i] - n**2] += 1
    
    return(B.index(max(B)) + n**2, max(B))

print(Y)
print(FindMostFrequent(sorted(Y)))
print(FindMostFrequentSquared(Y))

