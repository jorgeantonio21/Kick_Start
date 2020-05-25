import numpy as np
T = int(input())
for turn in range(T):
    N_M_K=[int(x) for x in input().split()]
    N=N_M_K[0]
    M=N_M_K[1]
    K=N_M_K[2]
    grid=[]
    for i in range(N):
        grid.append(str(input()))
    Tfunc=np.zeros((N, M), dtype='int')
    ans=0
    for i in range(N):
        if grid[i][0]=='#':
            Tfunc[i, 0]=1
            ans=1
        if grid[i][M-1]=='#':
            Tfunc[i, M-1]=1
            ans=1
    for i in range(M):
        if grid[N-1][i]=='#':
            Tfunc[N-1, i]=1
            ans=1
    for i in range(N-2, -1, -1):
        for j in range(1, M-1):
            if grid[i][j]=='#':
                Tfunc[i, j]=1 + min(Tfunc[i+1, j-1], Tfunc[i+1, j], Tfunc[i+1, j+1])
                ans=max(ans, Tfunc[i, j])
    
    print("Case #{}: {}".format(turn+1, ans))