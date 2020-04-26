# This code was done in collaboration between Jorge Antonio and Raul Penaguiao
# This code pertains a problem set in KickStart Google Competition, see https://codingcompetitions.withgoogle.com/kickstart/archive
# This code runs in python 3.7.6.

import numpy as np
T = int(input())

for case in range(T):
    N_P = [int(x) for x in input().split()]
    N = N_P[0] # number of students
    P = N_P[1] # number of students you need to pick
    skills = [int(x) for x in input().split()] # skills of each student
    skills.sort()
    sum_ind = np.array([(skills[P-1] - skills[j]) for j in range(P)]).sum()
    sums = [sum_ind]
    for i in range(1, N - P + 1):
        sum_ind += - P *  skills[i + P - 2] + (P-1) * skills[i + P - 1] + skills[i-1] 
        sums.append(sum_ind)
    print('Case #{}: {}'.format(case + 1, min(sums)))