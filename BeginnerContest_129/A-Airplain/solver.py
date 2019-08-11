import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.disable(logging.CRITICAL)

P, Q, R = (int(x) for x in input().split())
l_time =[P + Q, P + R, Q + R]

print(min(l_time))
