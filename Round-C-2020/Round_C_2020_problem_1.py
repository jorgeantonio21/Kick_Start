import numpy as np
T = int(input())
for turn in range(T):
    N_K=[int(x) for x in input().split()]
    N=N_K[0]
    K=N_K[1]
    a=[int(x) for x in input().split()]
    count = 0
    i=0
    j=K
    while i < N:
        if a[i] == j:
            if j==1: 
                count+=1
                j = K
            else: j-=1
        elif a[i]==K:
             j = K-1
        else:
            j = K
        i+=1
    print("Case #{}: {}".format(turn+1, count))