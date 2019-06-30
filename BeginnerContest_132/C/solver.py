import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.disable(logging.CRITICAL)

K = int(input())
L = list(int(x) for x in input().split())

Ld = sorted(L)

if Ld[int(K / 2) - 1] == Ld[int(K / 2)]:
    print(0)
else:
    print(Ld[int(K / 2)] - Ld[int(K / 2) - 1])
