import numpy as np
T=int(input())
for turn in range(T):
    word = str(input())
    l=2*len(word)+1
    P=np.zeros(l, dtype=int)
    i=1
    R=1
    C=0
    S = '|'
    for char in word:
        S += char
        S += '|'
    while R<l:
        j = C - (i - C) # i'
        if i == R:
            P[i] = 0
            C  = i
            R += 1
            L = i-1
            while L >= 0 and R < l and S[R] == S[L]:
                R += 1
                L -= 1
                P[i] += 1
        elif P[j] == R - i - 1: #Case raio de i' = R - i - 1 -> while loop
            P[i]=P[j]
            L= 2*i - R
            if S[R] == S[2*i - R]:
                C = i
                R += 1
                P[i] += 1
                L -= 1
                while L>=0 and R<l and S[R] == S[L]:
                    R += 1
                    P[i] += 1
                    L -= 1
        elif P[j] < R - i - 1:
            P[i] = P[j]
        else: #Case raio de i' > R - i - 1 -> P[i] = R - i
            P[i] = P[j]
        i += 1
    print("Case #{} : {}".format(turn+1, max(P)))