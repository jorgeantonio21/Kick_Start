import numpy as np
import queue

T = int(input())
stars=np.zeros((2000, 4), dtype=int)

for turn in range(T):
    N = int(input())
    R_max=0
    for star in range(N):
        stars[star]=[int(x) for x in input().split()]
        R_max=max(R_max, stars[star, 3])
#    """For N <= 16 we can simply split the set of stars into two sets and find the minimal cube containing all the stars on each side
#    Minimal cube of a set S is computed as min(min_x(S), min_y(S), min_z(S))
#    min_x(S) is computed by min_{i< j in S} abs(X_i-R_i-X_j+R_j) analogous for the other coordinates
#    Precomputations can be done for abs(X_i-R_i-X_j+R_j), which is quadratic
#    By computing max(abs(X_i-R_i-X_j+R_j), abs(Y_i-R_i-Y_j+R_j), abs(Z_i-R_i-Z_j+R_j)) for each pair of stars i, j, we get a weighted complete graph. 
#    The goal is to find the biggest integer K such that, if all edges with weight >K are removed, we get a graph that is covered by two complete graphs.
#    Equivalently, we want to find the biggest K such that, if all edges with weight <=K are removed, obtaining the graph G_K, we get a graph with at most two connected components.
#    We can thus do binary search on K:
#        - For each K, we check if G_K is bipartite.
#        - Search binarily on K so that we get O(N^2 log 10^8) complexity."""
    dist = np.zeros((N, N), dtype=int)
    #Do some precomputation
    for i in range(N):
        for j in range(i):
            dis = np.max(np.array([np.abs(stars[i, a] - stars[i, 3] - stars[j, a] - stars[j, 3]) for a in range(3)]))
            dis = max(dis, np.max(np.array([np.abs(stars[j, a] - stars[j, 3] - stars[i, a] - stars[i, 3]) for a in range(3)])))
            dist[i, j] = dis
            dist[j, i] = dis
    K_min = 2 * R_max - 1 #There is no two cubes of this size that fit all the stars
    K_max = 4 * 10 ** 8+10 # There is always two cubes of this size that fit all the stars
    #connections = np.zeros(N, dtype=int)
    visited = np.zeros(N, dtype=int)
    while(K_max-K_min>1):
        K = (K_max+K_min)//2
        bipartite=True
        #Compute number of connected components of G_K
        # there is edge i - j iff dist[i, j] > K
        qu=queue.Queue()
        qu.put(0)
        for i in range(1,N):
            visited[i]=0
        visited[0]=1
        visited_vertices=0
        while bipartite and not(qu.empty()):
            new_v=qu.get()
            visited_vertices+=1
            #add all the neighbours
            j=0
            while j < N and bipartite:
                if dist[new_v, j]> K:
                    if visited[j] == 0:
                        visited[j]=visited[new_v]%2+1
                        qu.put(j)
                    elif visited[j]==visited[new_v]:
                        bipartite=False
                j+=1
            if qu.empty() and visited_vertices < N and bipartite:
                new_v = 1
                while visited[new_v] > 0:
                    new_v += 1
                qu.put(new_v)
                visited[new_v]=1
        if bipartite:
            K_max = K
        else:
            K_min = K
    print("Case #{}: {}".format(turn+1, K_max))