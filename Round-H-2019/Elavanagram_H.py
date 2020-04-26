# This code was done in collaboration between Jorge Antonio and Raul Penaguiao
# This code pertains a problem set in KickStart Google Competition, see https://codingcompetitions.withgoogle.com/kickstart/archive
# This code runs in python 3.7.6.


import numpy as np

T = int(input())

for z in range(T):
    num_digits = np.array([int(x) for x in input().split(' ')]) 
    for i in range(9):
        if num_digits[i] == max(num_digits):
            max_index = i
    if (num_digits >= 10).sum() >= 2:
        print('Case #{}: YES'.format(z + 1))
    else:
        soma_num_digitos = num_digits.sum()
        matriz_coeff = np.zeros(((soma_num_digitos // 2) + 1, 10, 11))
        if soma_num_digitos >= 85:
            var = (- soma_num_digitos + 2 * max(num_digits)) // 2
            soma_num_digitos -= 2 * var
            num_digits[max_index] -= 2 * var 
        soma_digitos = np.array([i * j for i, j in zip(range(1, 10), num_digits)]).sum()
        matriz_coeff[0, 0, 0] = 1 # initial value, 1 vacuously
        for j in range(1, 10):
            matriz_coeff[0, j, 0] = 1
            for i in range(1, soma_num_digitos // 2 + 1):
                for k in range(11):
                    matriz_coeff[i, j, k] = np.array([matriz_coeff[i-l, j-1, (k - l*j) % 11]
                                            for l in range(1 + min(num_digits[j-1], i))]).max()
        index_i = soma_num_digitos // 2
        index_k = (soma_digitos * 6) % 11
        if matriz_coeff[index_i, 9, index_k] > 0:
            print('Case #{}: YES'.format(z + 1))
        else:
            print('Case #{}: NO'.format(z + 1))