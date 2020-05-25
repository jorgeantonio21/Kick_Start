import numpy as np

T = int(input())

for z in range(T):
    N_M = [int(x) for x in input().split()]
    Ais = np.array([np.int64(x) for x in input().split()])
    l = len(Ais)
    N = np.int64(N_M[0])
    M = np.int64(N_M[1])
    total_exps = [bin(a).split('b')[1] for a in Ais]
    bin_lengths = [len(x) for x in total_exps]
    m = max(bin_lengths)
    count_zeros = np.zeros(m)
    for i in range(len(total_exps)):
        while len(total_exps[i]) < m:
            total_exps[i] = '0' + total_exps[i]
        for q in range(m):
            if total_exps[i][q] == '0':
                count_zeros[q] += 1
    count_ones = N - count_zeros
    soma_xor = np.int64(np.array([(2 ** (m - i - 1)) * count_zeros[i] if count_zeros[i] == min(count_zeros[i], count_ones[i])
                          else (2 ** (m - i - 1)) * (count_ones[i]) for i in range(m)]).sum())
    k = np.int64(np.array([2 ** (m - i - 1) for i in range(m) if count_zeros[i] == min(count_zeros[1], count_ones[1])]).sum())
    k_bin = bin(k).split('b')[1]
    while len(k_bin) < m:
        k_bin = '0' + k_bin
    count = 1 
    if soma_xor > M:
        print('Case #{}: {}'.format(z+1, -1))
    else:
        for i in range(m):
            if k_bin[i] == '0':
                if (soma_xor - (2 ** (m-i-1)) * (np.int64((count_ones[i]) - count_zeros[i] ))) <= M:
                    k = np.int64(k + 2 ** (m-i-1))
                    soma_xor = np.int64(soma_xor + np.int64((2 ** (m-i-1)) * (count_zeros[i] - (count_ones[i]))))
        print('Case #{}: {}'.format(z+1, k))