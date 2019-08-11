import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    A_ = [int(input()) for _ in range(N)]
    logging.info("Hello!")

    counter = 0
    j = 0
    for i in range(N):
        if A_[i] == 0:
            counter += (sum(A_[j :i]) // 2)
            j = i

    print(counter)
            
    
    
if __name__ == "__main__":
    main()
