import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.disable(logging.CRITICAL)

N = int(input())
L = list(int(x) for x in input().split())

counter = 0

for i in range(1, N - 1):
    if L[i - 1] > L[i] and L[i] > L[i + 1]:
        counter += 1
    elif L[i - 1] < L[i] and L[i] < L[i + 1]:
        counter += 1

print(counter)
