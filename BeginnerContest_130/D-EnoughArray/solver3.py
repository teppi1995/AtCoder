import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.disable(logging.CRITICAL)

N, K = (int(x) for x in input().split())
L = list(int(x) for x in input().split())

logging.info(L)

counter = 0

for i in range(0, N):
    total = sum(L[i:N])
    l = N
    while total >= K:
        counter += 1
        total - L[l]
        l -= 1

    
print(counter)
            
