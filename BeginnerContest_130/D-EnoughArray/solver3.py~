import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.disable(logging.CRITICAL)

N, K = (int(x) for x in input().split())
L = list(int(x) for x in input().split())

logging.info(L)

counter = 0

for i in range(0, N):
    for j in range(i + 1, N):
        if sum(L[i:j + 1]) >= K:
            counter += (N - j)
            break

print(counter)
            
