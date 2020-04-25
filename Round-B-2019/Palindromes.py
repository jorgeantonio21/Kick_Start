import numpy as np

def is_2_power(n):
    if n == 0:
        return True
    else:
        return n & (n-1) == 0
    
T = int(input())

for case in range(T):
    N_Q = [int(x) for x in input().split()]
    N = N_Q[0]
    Q = N_Q[1]
    letters = input()
    vec = np.zeros(N+1)
    vec[0] = 0
    charA = ord('A')
    for x in range(1, N+1):
        vec[x] = int(vec[x-1]) ^ (2 ** (ord(letters[x-1]) - charA)) 
    ans = 0
    for k in range(Q):
        b = [int(x) for x in input().split()]
        if is_2_power(int(vec[b[0] - 1])^int(vec[b[1]])):
            ans += 1
    print('Case #{}: {}'.format(case + 1, ans))