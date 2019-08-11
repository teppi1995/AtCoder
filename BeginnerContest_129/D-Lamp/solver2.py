import logging
import numpy as np

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

H, W = (int(x) for x in input().split())

fields = []
fields.extend([list(input()) for _ in range(H)])

    L = np.zeros((H,W), dtype=int)
    R = np.zeros((H,W), dtype=int)
    U = np.zeros((H,W), dtype=int)
    D = np.zeros((H,W), dtype=int)

logging.info(fields)
logging.info(L[0][1])

for i in range(H):
    for j in range(W):
        if fields[i][j] == '#':
            L[i][j] = 0
            U[i][j] = 0

        elif fields[i][j] == ".":
            if j == 0:
                L[i][j] = 1
            elif j > 0 :
                L[i][j] = L[i][j - 1] + 1

            if i == 0:
                U[i][j] = 1
            elif i > 0:
                U[i][j] = U[i - 1][j] + 1
        
            
        if fields[i][W - j - 1] == "#":
            R[i][W - j - 1] = 0
        elif fields[i][W - j - 1] == ".":
            if j == 0:
                R[i][W - j - 1] = 1
            elif j > 0:
                R[i][W - j - 1] = R[i][W - j] + 1
                
        
        if fields[H - i - 1][j] == "#":
            D[H - i - 1][j] = 0
            
        elif fields[H - i - 1][j] == ".":
            if i == 0:
                D[H - i - 1][j] = 1
            elif i > 0:
                D[H - i - 1][j] = D[H - i][j] + 1


max_count = 0
for i in range(H):
    for j in range(W):
        sum = L[i][j] + R[i][j] + D[i][j] + U[i][j] - 3
        if max_count < sum:
            max_count = sum


print(max_count)
