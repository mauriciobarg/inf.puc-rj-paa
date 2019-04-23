V = sorted([1, 1, 1, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 10, 10, 10])

def FindMostFrequent(A):
    n = len(A)
    current = A[0]
    biggest = 0
    count = 1
    current_max = 0
    for i in range(1, n):
        if current == A[i]:
            count += 1
        else:
            if count > current_max:
                current_max = count
                biggest = current
            count = 1
            current = A[i]
    return(biggest, current_max)

print(FindMostFrequent(V))