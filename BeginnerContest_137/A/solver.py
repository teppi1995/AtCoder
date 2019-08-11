import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    A, B = map(int, input().split())
    logging.info("Hello!")

    print(max([A + B, A - B, A * B]))
    
if __name__ == "__main__":
    main()
