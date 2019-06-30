import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.disable(logging.CRITICAL)

N, X  = (int(x) for x in input().split())
L = list(int(x) for x in input().split())

logging.info(L)

length = 0
counter = 1

for i in L:
    length += i
    if length <= X:
        counter++
    
print(counter)
