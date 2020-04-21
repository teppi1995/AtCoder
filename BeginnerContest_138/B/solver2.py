import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    A_1 = list(map(int, input().split()))
    logging.info("Hello!")

    sum = 0
    for i in A_1:
        sum += (1 / i)


    print(1 / sum)
    
    
    
if __name__ == "__main__":
    main()
