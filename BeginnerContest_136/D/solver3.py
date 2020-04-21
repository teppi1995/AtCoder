import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    S = input()
    S_len = len(S)
    child = [0 for _ in range(S_len)]

    R = [i for i in S.split("L") if i != ""]
    L = [i for i in S.split("R") if i != ""]

    logging.info(R)
    logging.info(L)
    
if __name__ == "__main__":
    main()
