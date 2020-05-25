import numpy as np
T = int(input())
for turn in range(T):
    N_D = [int(x) for x in input().split()]
    N = N_D[0]
    D = N_D[1]
    buses = [int(x) for x in input().split()]
    for i in range(N-1, -1, -1):
        D -= D % buses[i]
    print("Case #{}: {}".format(turn+1, D))