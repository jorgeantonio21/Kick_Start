T = int(input())

for turn in range(T):
    D_S = [int(x) for x in input().split()]
    D = D_S[0]
    S = D_S[1]
    code_eat_sat = []
    for i in range(S):
        code_eat_sat.append([int(x) for x in input().split()])
    days = []
    for i in range(D):
        days.append([int(x) for x in input().split()])
    str_ans = ''
    # ordenar a eficienca das slots
    ordered_slots = list(range(S))
    ordered_slots = sorted(ordered_slots, key=lambda x, y: code_eat_sat[x][0]*code_eat_sat[y][1]>code_eat_sat[x][1]*code_eat_sat[y][0])  
    for day in range(D):
        aux_eat=0
        aux_cod=0
        boolean=True
        for i in range(1, S):
            aux_eat +=code_eat_sat[ordered_slots[i]][1]
        # x  \geq (A_day -  aux_cod)/C_i
        # (1-x) \geq ( B_day - aux_eat )/E_i
        for i in range(S): #test F(1, ..1, x, 0, ..., 0)
            if boolean: #actualizar os valores de aux eat e aux cod
                aux_cod+= code_eat_sat[ordered_slots[i-1]][0]
                aux_eat-= code_eat_sat[ordered_slots[i]][1]
                if ((days[day][0] - aux_cod )/code_eat_sat[ordered_slots[i]][0] + (days[day][1] - aux_eat)/code_eat_sat[ordered_slots[i]][1] > 1): # (A_day -  aux_cod)/C_i + ( B_day - aux_eat )/E_i
                    str_ans+='Y'
                    boolean=False
        if boolean:
            str_ans+='N'
    print("Case {}#: {}".format(turn+1, str_ans))