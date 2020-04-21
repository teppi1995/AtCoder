import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    P_1 = list(map(int, input().split()))
    logging.info("Hello!")

    min_num = 0
    counter_i = 0
    
    for p in P_1:
        if p <= min_num:
            counter_i += 1
            min_num = p

    print(counter_i)
    
if __name__ == "__main__":
    main()
