import numpy as np
T = int(input())
pow2=np.zeros(10000, dtype=int)
pow2[0]=1
MOD=10**9 + 7
for i in range(1, 10000):
    pow2[i]=(pow2[i-1]*2)%MOD
for turn in range(T):
    N = int(input())
    K=np.array([int(x) for x in input().split()])
    ans = np.sum(np.array([(pow2[i] - pow2[N-i-1]) * K[i] for i in range(N)]))
    print("Case #{}: {}".format(turn+1, ans%MOD))



    