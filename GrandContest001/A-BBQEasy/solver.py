import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    L_1 = list(map(int, input().split()))

    L_1.sort()

    logging.info(L_1)

    print(sum(L_1[::2]))
    
if __name__ == "__main__":
    main()
