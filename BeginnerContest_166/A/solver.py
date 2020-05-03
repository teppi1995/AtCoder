import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    S = input()
    if S == "ABC":
        print("ARC")
    else:
        print("ABC")
        
if __name__ == "__main__":
    main()
