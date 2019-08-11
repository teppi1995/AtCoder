import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.disable(logging.CRITICAL)

def main():
    N, L = (int(x) for x in input().split())

    logging.info("Hello!")

    apples = [L - 1 + i for i in range(1, N + 1)]
    apples_abs = [abs(x) for x in apples]
    
    apple_pie_answer = sum(apples) - apples[apples_abs.index(min(apples_abs))]
    
    print(apple_pie_answer)
    
    
if __name__ == "__main__":
    main()
