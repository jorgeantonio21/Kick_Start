T = int(input())

def counting_sort(array, maxval):
    m = maxval + 1
    count = [0] * m
    for a in array:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array[i] = a
            i += 1
    return (array, count)
    

for case in range(T):
    N_B = [int(x) for x in input().split()]
    N = N_B[0]
    B = N_B[1]
    cost_houses = [int(x) for x in input().split()]
    maxval = max(cost_houses)
    cost_houses_sort = counting_sort(cost_houses, maxval)[0]
    max_houses = 0
    money_left = B
    for m in cost_houses_sort:
        if money_left - m >= 0:
            max_houses += 1
            money_left -= m
        else:
            break
    print('Case #{}: {}'.format(case + 1, max_houses))