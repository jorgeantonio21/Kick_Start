# This code was done in collaboration between Jorge Antonio and Raul Penaguiao
# This code pertains a problem set in KickStart Google Competition, see https://codingcompetitions.withgoogle.com/kickstart/archive
# This code runs in python 3.7.6.

import numpy as np

def symbols_to_F2(input):
    row = np.zeros(len(input))
    for i in range(len(input)):
        if input[i] == '#':
            row[i] = 0
        else:
            row[i] = 1
    return row
        
def transition_matrix(N, input):
    matrix = np.zeros(N)
    for i in range(N):
        row = symbols_to_F2(input[i, :])
        matrix[i, :] = row
    return matrix
    
def minimum_moves(N, matriz, case):
    """Computes the minimal number of moves in order to get a board whose
    cases are all black. Our strategy consists in partitioning the board into positive,
    negative, black and white diagonals (as a chessboard). Using this partition we compute
    the sum of 1's (white cases) in main positive and negative diagonals. This introduces
    a partition of 'orthogonal' basis of diagonals. The minimal number of moves is thus the
    minimum of the sums of cases with 1's or 0's (white or black) cases"""
    sum_positive_b = 0 # black negative diagonals (black as a chessboard)
    sum_negative_b = 0 # black positive diagonals (black as a chessboard)
    sum_positive_w = 0 # white positive diagonals (white as a chessboard)
    sum_negative_w = 0 # white negative diagonals (white as a chessboard)
    if N % 2 == 1:  # odd case
        for i in range(N):
            sum_positive_b += matriz[i, i] # sums the 1's in the main black positive diagonal
            sum_negative_b += matriz[i, N-i-1] # sums the 0's in the main black negative diagonal
        if matriz[N //2, N // 2] == 1: # intersection of the black positive and black negative main diagonals == 1
            b = N - sum_positive_b + sum_negative_b # number of diagonals in the connected component of orthogonal basis of the black negative main diagonal
        else:
            b = sum_positive_b + sum_negative_b # number of diagonals in the connected component opposite to the orthogonal basis of the black negative main diagonal
        for i in range(N-1): # dealing with white diagonals. The procedure is similar to the previously one
            sum_positive_w += matriz[i+1, i] 
            sum_negative_w += matriz[i, N-i-2]
        if matriz[N // 2, N // 2 - 1] == 1:
            w = N - 1 - sum_positive_w + sum_negative_w
        else:
            w = sum_positive_w + sum_negative_w
        b = min(b, 2 * N - b)
        w = min(w, 2 * N- w - 2)
    else: # even case: The procedure is similar to the odd case
        for i in range(N):
            sum_positive_b += matriz[i, i]
        for i in range(N-1):
            sum_negative_b += matriz[i, N-i-2]
        if matriz[N // 2 - 1, N // 2 - 1] == 1:
            b = N - sum_positive_b + sum_negative_b
        else:
            b = sum_positive_b + sum_negative_b
        for i in range(N):
            sum_negative_w += matriz[i, N-i-1]
        for i in range(N-1):
            sum_positive_w += matriz[i+1, i]
        if matriz[N // 2, N // 2 - 1]:
            w = N - sum_negative_w + sum_positive_w
        else:
            w = sum_positive_w + sum_negative_w
        b = min(b, 2 * N - 1 - b) # minimum move of black diagonal moves to perform (recall, black here means black diagonals in a chessboard of NxN)
        w = min(w, 2 * N - 1 - w) # minimum move of white diagonal moves to perform (recall, white here means white diagonals in a chessboard of NxN)
    print('Case #{}: {}'.format(case + 1, int(b + w)))

T = int(input())

for z in range(T):
    N = int(input())
    matriz = np.zeros((N, N))
    for i in range(N):
        row = input()
        for j in range(N):
            if row[j] == '#': # black
                matriz[i, j] = 0
            else: # white
                matriz[i, j] = 1
    minimum_moves(N, matriz, z)