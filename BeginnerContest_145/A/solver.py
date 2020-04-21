import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    r = int(input())
    logging.info("Hello!")

    print(r * r)
    
if __name__ == "__main__":
    main()
