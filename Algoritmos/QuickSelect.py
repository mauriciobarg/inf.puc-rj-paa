from random import randint
V = [randint(-10, 10) for x in range(10)]

def QuickSelect(A, k):
    n = len(A)
    if k <= n:
        p = randint(0, n - 1)
        l = []
        r = []
        for i in range(n):
            if i != p:
                if A[i] <= A[p]:
                    l.append(A[i])
                elif A[i] > A[p]:
                    r.append(A[i])
        if len(l) == k - 1:
            return A[p]
        elif len(l) > k - 1:
            return QuickSelect(l, k)
        else:
            return QuickSelect(r, k - len(l) - 1)
    else: return None
