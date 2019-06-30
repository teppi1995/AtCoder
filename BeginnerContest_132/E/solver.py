import logging
import math

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.disable(logging.CRITICAL)


N, M = (int(x) for x in input().split())
line = []
for i in range(M):
    line.append(list(int(x) for x in input().split()))

S, T = (int(x) for x in input().split())

