import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    a, b = map(int, input().split())
    logging.info("Hello!")

    if a * b < 0:
        print("Zero")
    elif a > 0:
        print("Positive")
    else:
        if (b - a + 1) % 2 == 1:
            print("Negative")
        else:
            print("Positive")
            

    
    
if __name__ == "__main__":
    main()
