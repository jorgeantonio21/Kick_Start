import numpy as np
import queue
T = int(input())
BIGN=10**9
for turn in range(T):
    instructions = str(input())
    aux_list = queue.LifoQueue()
    prod_list = 1
    x_coord=1
    y_coord=1
    for i in range(len(instructions)):
        if instructions[i].isnumeric():
            if i==0 or not(instructions[i-1].isnumeric()):
                j=i+1
                while instructions[j].isnumeric():
                    j+=1
                new_num=int(instructions[i:j])
                aux_list.put(new_num)
                prod_list*=int(new_num)
        elif instructions[i] == ')':
            prod_list//=aux_list.get()
        elif instructions[i] =='N':y_coord-=prod_list
        elif instructions[i] =='E':x_coord+=prod_list
        elif instructions[i] =='W':x_coord-=prod_list
        elif instructions[i] =='S':y_coord+=prod_list
    print("Case #{}: {} {}".format(turn+1, (x_coord-1)%BIGN+1, (y_coord-1)%BIGN+1))