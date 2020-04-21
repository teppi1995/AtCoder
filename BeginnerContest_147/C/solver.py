import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())

    list_N = [[-10 for i in range(N)] for j in range(N)]

    logging.info(list_N)
    
    for i in range(N):
        A_1 = int(input())
        x_y = [list(map(int, input().split())) for _ in range(A_1)]
        logging.info(x_y)
        for x_ in x_y:
            list_N[i][x_[0] - 1] = x_[1]

    logging.info(list_N)
        
    logging.info("Hello!")

    
    
    
if __name__ == "__main__":
    main()
