import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    S = input()
    logging.info("Hello!")

    if N % 2 == 1:
        print("No")
    else:
        half_S_1 = S[0:N // 2]
        half_S_2 = S[N // 2:N]

        if half_S_1 == half_S_2:
            print("Yes")
        else:
            print("No")
            
if __name__ == "__main__":
    main()
