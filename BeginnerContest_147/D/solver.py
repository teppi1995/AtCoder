import logging
import numpy as np


logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

Mod = 10 ** 9 + 7

def main():
    N = int(input())
    arr_1 = np.array(list(map(int, input().split())))
    logging.info("Hello!")

    ans = 0

    for i in range(64):
        num_of_1 = np.count_nonzero(arr_1 & 1)
        ans += (2 ** i) * (num_of_1 * (N - num_of_1))
        arr_1 >>= 1
        
    print(ans % Mod)
    
    
if __name__ == "__main__":
    main()
