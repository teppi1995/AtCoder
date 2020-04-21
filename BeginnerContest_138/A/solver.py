import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    a = int(input())
    S = input()

    if a >= 3200:
        print(S)
    else:
        print("red")
    
if __name__ == "__main__":
    main()
