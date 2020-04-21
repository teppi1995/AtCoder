import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    S = input()
    logging.info("Hello!")

    S_len = len(S)
    counter = 0
    for i in range(S_len // 2):
        if S[i] != S[S_len - 1 - i]:
            counter += 1

    print(counter)
    
    
if __name__ == "__main__":
    main()
