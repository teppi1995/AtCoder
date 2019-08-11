import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    print(N * N * 3)

    
if __name__ == "__main__":
    main()
