import numpy as np
import numpy as np
T = int(input())
def sort_diag_plus(point):
    return point[1] - point[0]
def sort_diag_neg(point):
    return point[0] + point[1]
for turn in range(T):
    N = int(input())
    points_pos, points_neg = [], []
    tot_weight=0
    for i in range(N):
        points_pos.append([float(x) for x in input().split()])
        tot_weight += points_pos[-1][2]
    points_neg = [point for point in points_pos]
    points_pos.sort(key=sort_diag_plus)
    points_neg.sort(key=sort_diag_neg)
    i=0
    partial_weight=points_pos[0][2]
    while(partial_weight*2 <= tot_weight):
        i += 1
        partial_weight += points_pos[i][2]
    j=0
    partial_weight = points_neg[0][2]
    while(partial_weight*2 <= tot_weight):
        j += 1
        partial_weight += points_neg[j][2]
    x = (points_pos[i][0] - points_pos[i][1] + points_neg[j][0] + points_neg[j][1])/2
    y = (points_pos[i][1] - points_pos[i][0] + points_neg[j][0] + points_neg[j][1])/2
    ans = 0
    for point in points_pos:
        ans += max(abs(point[0]-x), abs(point[1]-y)) * point[2]
    print("Case #{}: {}".format(turn+1, ans))