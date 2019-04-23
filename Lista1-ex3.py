from random import randint
from math import inf

V = [randint(-100, 100) for x in range(100)]
# V = [-5, -1, -4, -2, -3]
# V = [-1, 0, 1, -10, -10]
## O(n^3)
def On3(A):
    n = len(A)
    i_max, j_max = 0, 0
    soma_max = -inf
    for i in range(n):
        for j in range(i, n):
            soma_aux = 0
            for k in range(i, j + 1):
                soma_aux += A[k]
            if soma_aux > soma_max:
                soma_max = soma_aux
                i_max = i
                j_max = j
    return(soma_max, i_max, j_max)

## O(n^2)
def On2(A):
    soma_max = -inf
    n = len(A)
    B = [0]*(n + 1)
    B[0] = 0
    B[1] = A[0]
    for k in range(2, n + 1):
        B[k] = B[k - 1] + A[k - 1]

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            soma_aux = B[j] - B[i - 1]
            if soma_aux > soma_max:
                soma_max = soma_aux
                i_max = i - 1
                j_max = j - 1
    return(soma_max, i_max, j_max)

## O(n)
def On(A):
    n = len(A)
    soma_max = -inf
    soma_aux = 0
    k = 0
    i = 0
    i_aux = 0
    j = 0
    while k < n:
        soma_aux += A[k]
        if soma_aux > soma_max:
            soma_max = soma_aux
            i = i_aux
            j = k
        if soma_aux < 0:
            soma_aux = 0
            i_aux = k + 1
        k += 1

    return(soma_max, i, j)








print(V)
print(On3(V))
print(On2(V))
print(On(V))
