import logging
import math

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    L_2 = [list(map(int, input().split())) for _ in range(N)]
    logging.info("Hello!")

    logging.info(L_2)

    sum = 0
    for i in range(N):
        for j in range(i + 1, N):
           sum += math.sqrt((L_2[i][0] - L_2[j][0]) ** 2 + (L_2[i][1] - L_2[j][1]) ** 2)

    print('{:.10f}'.format(sum * 2 / N))
    
    
if __name__ == "__main__":
    main()
