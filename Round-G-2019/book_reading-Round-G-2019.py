import numpy as np

T = int(input())

for z in range(T):
    N_M_Q = [int(x) for x in input().split()]
    N = N_M_Q[0]
    torn_pages = [int(x) for x in input().split()] # length M number of torn apart pages
    reader_multiples = [int(x) for x in input().split()] # length Q number of readers
    soma_pages = 0
    vistas = np.zeros(N+1)
    values_of_f = np.zeros(N+1)
    array = np.zeros(N+1)
    for Pi in torn_pages:
        array[Pi] = 1
    for x in reader_multiples:
        floor = N // x
        count = 0
        if vistas[x] == 0:
            vistas[x] = 1
            for i in range(floor+1):
                if array[i * x] == 1:
                    count += 1
            values_of_f[x] = N // x - count
            soma_pages += values_of_f[x]
        else:
            soma_pages += values_of_f[x]
    print('Case #{}: {}'.format(z+1, int(soma_pages)))