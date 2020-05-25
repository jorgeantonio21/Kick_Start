import numpy as np
T = int(input())
for turn in range(T):
    a=[int(x) for x in input().split()]
    W=a[1]
    H=a[0]
    L=a[2]-1
    U=a[3]-1
    R=a[4]-1
    D=a[5]-1
    vec=np.zeros((2, W+1))
    if(H>R+1):
        for col in range(D+1):
            vec[(R+1)%2, col]=1
    for row in range(R, L-1, -1):
        if W>D+1:
            vec[row%2, D+1]=1
        for col in range(D, U-1, -1):
            vec[row%2, col]=0
        for col in range(U-1, -1, -1):
            vec[row%2, col]=(vec[(row+1)%2, col]+vec[row%2, col+1])/2 
    
    
    for row in range(L-1, -1, -1):
        vec[row%2, D+1]=vec[(row+1)%2, D+1]
        for col in range(D, -1, -1):
            vec[row%2, col]=(vec[(row+1)%2, col]+vec[row%2, col+1])/2 #A, B, C
            
    print("Case #{}: {}".format(turn+1, vec[0, 0]))
    
    
    
import numpy as np
T = int(input())
for turn in range(T):
    a=[int(x) for x in input().split()]
    W=a[1]
    H=a[0]
    L=a[2]-1
    U=a[3]-1
    R=a[4]-1
    D=a[5]-1
    vec=np.zeros((2, W+1))
    if(H>R+1):
        for col in range(D+1):
            vec[(R+1)%2, col]=1
    for row in range(R, L-1, -1):
        if W>D+1:vec[row%2, D+1]=1 
        else: vec[row%2, D+1]=0
        for col in range(D, U-1, -1):
            vec[row%2, col]=0 #X
        for col in range(U-1, -1, -1):
            vec[row%2, col]=(vec[(row+1)%2, col]+vec[row%2, col+1])/2 #D
        
        #for col in range(W): vec[1, col]=vec[0, col]
    
    
    for row in range(L-1, -1, -1):
        vec[row%2, D+1]=vec[(row+1)%2, D+1]
        for col in range(D, -1, -1):
            vec[row%2, col]=(vec[(row+1)%2, col]+vec[row%2, col+1])/2 #A, B, C
        #for col in range(W):
            #vec[1, col]=vec[0, col]
    print("Case #{}: {}".format(turn+1, vec[0, 0]))