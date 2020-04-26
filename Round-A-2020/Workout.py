import numpy as np
import math
T = int(input())
for turn in range(T):
    ans=0
    a=[int(x) for x in input().split()]
    N=a[0]
    K=a[1]
    M=[int(x) for x in input().split()]
    diff=list(range(N-1))
    for k in range(N-1):
        diff[k]=M[k+1]-M[k]
    diff.sort(reverse=True)
    #kappa ( D )  = menor  K tal que podemos adicionar K exercicios cuja dificuldade resultante e no maximo D
    #Pode ser calculada com complexidade N
    # Correr por todos os intervalos, sum_{i=0}^N-2 math.ceil(diff[i]/D) - 1       D=3 , diff= 18 diff-1 //D
    lower_bound=1
    upper_bound=diff[0]
    while upper_bound - lower_bound > 1:
        new_bound=(upper_bound+lower_bound)//2
        kappa = np.sum([(math.ceil(diff[i] / new_bound) - 1) for i in range(N-1)])
        if kappa > K:
            #quer dizer que a dificuldade e muito baixa
            lower_bound=new_bound
        else:
            #quer dizer que ainda podemos diminuir a dificuldade
            upper_bound=new_bound
    if np.sum([(math.ceil(diff[i] / lower_bound) - 1) for i in range(N-1)]) <= K:
        ans = lower_bound
    else:
        ans=upper_bound
    print("Case #{}: {}".format(turn+1, ans))