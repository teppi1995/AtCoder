import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    S = input()
    logging.info("Hello!")

    i = 1
    for c in S:
        if i % 2 == 1:
            if c == "L":
                print("No")
                exit()

        if i % 2 == 0:
            if c == "R":
                print("No")
                exit()
        i += 1
            
    print("Yes")
    
if __name__ == "__main__":
    main()
