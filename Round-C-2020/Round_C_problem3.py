import numpy as np
import math

def perf_sqr(n):
    if math.modf(math.sqrt(n))[0] == 0.0:
        return True
    else:
        return False

T = int(input())
for turn in range(T):
    N = int(input())
    a=[int(x) for x in input().split()]
    part_sum=np.zeros(N+1, dtype='int')
    #perfsq={}
    #for i in range(3500):
    #    perfsq[i*i]=True
    part_sum[0]=0
    part_dic_sum={ 0: [0] }
    max_ps=0
    min_ps=0
    for i in range(1, N+1):
        part_sum[i]=part_sum[i-1] + a[i-1]
        max_ps=max(max_ps, part_sum[i])
        min_ps=min(min_ps, part_sum[i])
        if part_sum[i] in part_dic_sum:
            part_dic_sum[part_sum[i]].append(i)
        else: part_dic_sum[part_sum[i]] = [i]
    t=math.floor(math.sqrt(max_ps - min_ps))
    pf_list=[x*x for x in range(t+1)]
    count = 0
    for i in range(N+1):
        for ps in pf_list:
            if part_sum[i]-ps in part_dic_sum:
                count += np.sum([1 for j in part_dic_sum[part_sum[i] - ps] if j < i ])
    print("Case #{}: {}".format(turn+1, int(count)))