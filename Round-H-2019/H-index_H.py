# This code was done in collaboration between Jorge Antonio and Raul Penaguiao
# This code pertains a problem set in KickStart Google Competition, see https://codingcompetitions.withgoogle.com/kickstart/archive
# This code runs in python 3.7.6.

import heapq
T = int(input())

for z in range(T):
    h_index = 1
    N = int(input())
    cits = [int(x) for x in input().split()]
    queue = [cits[0]]
    ans = ' 1'
    for i in range(1, N):
        if cits[i] > h_index and queue[0] >= h_index + 1:
            heapq.heappush(queue, cits[i])
            h_index += 1
        elif cits[i] > h_index and queue[0] < h_index + 1:
            heapq.heappushpop(queue, cits[i])
        ans += ' {}'.format(h_index)
    print('Case #{}:{}'.format(z + 1, ans))