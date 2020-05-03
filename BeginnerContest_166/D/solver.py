import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    X = int(input())

    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            if (a ** 5 - b ** 5) == X:
                print("{} {}".format(a, b))
                exit()

    logging.info("error")
        
            
if __name__ == "__main__":
    main()
