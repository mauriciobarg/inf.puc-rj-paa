T = "the quick brown fox jumps over the lazy dog"
S = "fox"

## O(mn)
def FindStringInText(s, t):
    n = len(t)
    m = len(s)
    k = 0
    for i in range(n - m):
        if k == m:
            print(i - 1)
        k = 0
        for j in range(m):
            if s[j] != t[i + j]:
                break
            else:
                k += 1

FindStringInText(S, T)