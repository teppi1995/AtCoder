import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    V_1 = sorted(list(map(int, input().split())))
    logging.info("Hello!")

    total = V_1[0]
    
    for i in range(1, len(V_1)):
        total = (total + V_1[i]) / 2

    print(total)
    
    
if __name__ == "__main__":
    main()
