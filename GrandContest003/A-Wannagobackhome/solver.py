import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    trip  = input()
    logging.info("Hello!")

    if (not (("S" in trip) ^  ("N" in trip))) and (not (("E" in trip) ^  ("W" in trip))):
        print("Yes")
    else:
        print("No")
        
if __name__ == "__main__":
    main()
