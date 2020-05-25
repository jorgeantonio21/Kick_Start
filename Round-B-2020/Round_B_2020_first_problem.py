import numpy as np
T = int(input())
for turn in range(T):
    N = int(input())
    H=[int(x) for x in input().split()]
    ans=0
    for x in range(1, N-1):
        if (H[x-1]<H[x] and H[x] > H[x+1]): ans +=1
    print("Case #{}: {}".format(turn+1, ans))