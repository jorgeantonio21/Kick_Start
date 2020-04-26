import numpy as np
T = int(input())
for turn in range(T):
    a=[int(x) for x in input().split()]
    N=a[0]
    K=a[1]
    P=a[2]
    partial_sum = np.zeros((N+1, K+1), dtype=int)
    for a in range(1, N+1):
        l = [int(x) for x in input().split()]
        for b in range(K):
            partial_sum[a, b+1]=partial_sum[a, b]+l[b]
    f = np.zeros((N+1, P+1), dtype=int)
    for a in range (1, N+1):
        for b in range(1, P+1):
            m = f[a-1, b] #j=0 case
            for j in range(1, min(b, K) + 1): 
                m=max(f[a-1, b-j] + partial_sum[a, j], m)
            f[a, b]=m
    print("Case #{}: {}".format(turn+1, f[N, P]))