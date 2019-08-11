import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    A, B, C = map(int, input().split())

    answer = B + C - A

    if answer < 0:
        answer = 0

    print(answer)
    
    
if __name__ == "__main__":
    main()
