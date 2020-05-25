import numpy as np
T = int(input())

for turn in range(T):
    N_M = [int(x) for x in input().split()]
    N = N_M[0]
    M = N_M[1]
    neigh_dic = {}
    for i in range(M):
        aux_list = [int(x) for x in input().split()]
        if aux_list[0]-1 in neigh_dic:
            neigh_dic[aux_list[0]-1] += [aux_list[1]-1]
        else:
            neigh_dic[aux_list[0]-1] = [aux_list[1]-1]
        if aux_list[1]-1 in neigh_dic:
            neigh_dic[aux_list[1]-1] += [aux_list[0]-1]
        else:
            neigh_dic[aux_list[1]-1] = [aux_list[0]-1]
    array=np.zeros(N, dtype=bool)
    count = 0
    for i in range(N):
        if array[i]:
            continue
        elif i in neigh_dic:
            count+=1
            queue_vis = [i]
            while queue_vis!=[]:
                vertex=queue_vis.pop()
                for neigh in neigh_dic[vertex]:
                    if not(array[neigh]):
                        queue_vis.append(neigh)
                        array[neigh]=True
        else:
            count+=1
    print("Case #{}: {}".format(turn+1, N+count-2))