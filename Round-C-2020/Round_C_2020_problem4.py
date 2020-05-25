import numpy as np
T = int(input())
for turn in range(T):
    N_Q=[int(x) for x in input().split()]
    N=N_Q[0]
    Q=N_Q[1]
    sum=0
    a=[int(x) for x in input().split()]
    for j in range(Q):
        a_b_c = [x for x in input().split()]
        b=int(a_b_c[1])-1
        c=int(a_b_c[2])
        if a_b_c[0] == 'U':#This is an update, change the array a
            a[b]=c
        else: #This is a query, update sum
            c-=1
            for t in range(c  - b + 1):
                if t%2:
                    sum-=a[t + b]* (t+1)
                else:
                    sum+=a[t + b]* (t+1)
    print("Case #{}: {}".format(turn+1, sum))