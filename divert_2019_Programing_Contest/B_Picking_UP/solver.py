import logging
import numpy as np

logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.INFO, format = " %(message)s")

def max_counter(diffs):
    num = []
    for i in diffs:
        num.append(diffs.count(i))

    max_num = max(num)
    
    return max_num
        
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
        
        p_q = []
        for i in range(0, N - 1):
            diff = list(ball_array[i] - ball_array[i + 1])
            if diff[0] != 0 or diff[1] != 0:
                p_q.append(diff)

                logging.info(p_q)

        print(N - max_counter(p_q))

          
if __name__ == "__main__":
    main()
