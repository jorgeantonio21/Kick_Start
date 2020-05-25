import numpy as np
import queue
T = int(input())
for turn in range(T):
    R_C = [int(x) for x in input().split()]
    R = R_C[0]
    C = R_C[1]
    poly = []
    for i in range(R):
        poly+= [input()]
        #print(poly[i])
    vis=np.zeros(26, dtype='int')#counts the number of squares of each piece
    edges_out=[{} for x in range(26)] #a entrada j descreve todos os vertices para onde o vertice j aponta
    edges_in=[{} for x in range(26)] #a entrada j descreve todos os vertices que apontam para j
    for i in range(R-1):
        for j in range(C):
            vis[ord(poly[i][j]) - 65]+=1
            #print("The character ", poly[i][j] , "was visited")
            #print("i = ", i)
            #print(" j = ", j)
            if poly[i][j] !=  poly[i+1][j]:
                edges_out[ord(poly[i][j]) - 65][ord(poly[i+1][j]) - 65] = True #add edge 
                edges_in[ord(poly[i+1][j]) - 65][ord(poly[i][j]) - 65] = True #add edge 
                #print("At step ", i, " - ", j)
                #print("edge from ", poly[i][j], " and ", poly[i+1][j], "added")
    for j in range(C):
        vis[ord(poly[R-1][j]) - 65]+=1
    list_of_chars=[]
    for i in range(26):
        if vis[i]>0:
            list_of_chars.append(i)
    #print("list_of_chars ", list_of_chars)
    #print("vis = ", vis)
    qu=queue.Queue()
    order_poly=[]
    for i in list_of_chars:#find all sources
        #print("edges_in = ", edges_in[i])
        if not(bool(edges_in[i])):#If there are no edges coming in
            qu.put(i)
    while not(qu.empty()):
        i=qu.get()
        #print("Starting queue in ", i)
        order_poly.append(i)
        for t in edges_out[i]:
            del edges_in[t][i]  #When finding a source remove all its edges from the neighbor lists
            if not(bool(edges_in[t])):#If there are no edges coming in put in queue
                qu.put(t)
    #print("order_poly = ", order_poly)
    #print("list_of_chars = ", list_of_chars)
    if len(order_poly)==len(list_of_chars):
        ans=""
        order_poly.reverse()
        for x in order_poly:
            ans+=chr(65 + x)
    else: ans = -1
    print("Case #{}: {}".format(turn+1, ans))