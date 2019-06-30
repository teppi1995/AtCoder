import logging
import math

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.disable(logging.CRITICAL)

def P(n, r):
    return math.factorial(n) // math.factorial(n - r)

def C(n, r):
    return P(n, r) // math.factorial(r)

N, K = (int(x) for x in input().split())
red_N = N -K


for i in range(1, K + 1):
    div_red_c = 0
    div_blue_c = C(K - 1, i - 1)
    print("blue" + str(div_blue_c))
    if red_N < i:
        print(0)
    elif red_N == i - 1:
        div_red_c = 1
    else :
        div_red_c = C(red_N, i - 1)
        if div_red_c >= i:
            div_red_c += C(red_N, i) * 2
        if div_red_c >= i + 1:
            div_red_c += C(red_N, i + 1)

    ans = (div_blue_c * div_red_c) % (10 ^ 9 + 7)
    print(ans)
