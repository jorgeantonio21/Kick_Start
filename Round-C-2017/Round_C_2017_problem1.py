import numpy as np
T = int(input())
for turn in range(T):
    W = str(input())
    len_word=len(W)
    if len_word%2:
        print("Case #{}: AMBIGUOUS".format(turn+1))
    else:
        i=2
        ans=[ch for ch in W]
        ans[1]=W[0]
        while i<len_word:
            ans[i+1]=chr(65 + ( ord(W[i]) - ord(W[i-2]) - 1 )%26)
            i+=2
        ans[len_word - 2]=W[len_word - 1]
        i=len_word-3
        while i > 0:
            ans[i-1]=chr(65 + ( ord(W[i]) - ord(W[i-2]) - 1 )%26)
            i-=2
        ans=''.join(ans)
        print("Case #{}: {}".format(turn+1, ans))