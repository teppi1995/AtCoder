import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    N, K = map(int, input().split())
    L_1 = list(map(int, input().split()))
    L_2 = [list(map(int, input().split())) for _ in range(N)]
    logging.info("Hello!")

    
if __name__ == "__main__":
    main()
