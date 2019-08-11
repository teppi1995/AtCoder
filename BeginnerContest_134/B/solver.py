import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N, D = map(int, input().split())
    logging.info("Hello!")

    print(-1 * ((-1 * N) // (D * 2 + 1)))
    
    
if __name__ == "__main__":
    main()
