import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    A, B = map(int, input().split())
    logging.info("Hello!")

    if (abs(A) + abs(B)) % 2 == 0:
        print(int((A + B) / 2))
    else:
        print("IMPOSSIBLE")
        
    
if __name__ == "__main__":
    main()
