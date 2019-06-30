import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.disable(logging.CRITICAL)

N, K = (int(x) for x in input().split())
L = list(int(x) for x in input().split())

logging.info(L)

counter = 0

for i in range(0, N):
    sum = 0
    while True:
        sum += L[i]
        if sum >= K:
            counter += (N - i)
            break
        i += 1
    
print(counter)
            
