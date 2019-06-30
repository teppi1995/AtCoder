import logging
import itertools
import numpy as np

logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.INFO, format = " %(message)s")

def costs_counter(N, diffs):
    num = []
    for i in diffs:
        num.append(diffs.count(i))

    max_num = max(num)
    
    return N - max_num
        
def main():
    N = int(input())

    if N == 1:
        print(1)
    else:
        balls = []
        for i in range(0, N):
            balls.append([int(x) for x in input().split()])
            
            ball_array = np.array(balls)    
        logging.info(ball_array)
        
        costs = []
        for seq in itertools.permutations(ball_array, 2):
            katamuki = seq[1] - 

            
        logging.info(costs)
        print(min(costs))
          
if __name__ == "__main__":
    main()
