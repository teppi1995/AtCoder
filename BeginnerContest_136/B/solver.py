import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    logging.info("Hello!")

    answer = 0

    if N < 10:
        answer = N
    elif N >= 10 and N < 100:
        answer = 9
    elif N >= 100 and N < 1000:
        answer = 9 + N % 100 + 1 + int(N // 100 - 1) * 100
    elif N >= 1000 and N < 10000:
        answer = 909
    elif N >= 10000 and N < 100000:
        answer = 909 + N % 10000 + 1 + int(N // 10000 - 1) * 10000
    else:
        answer = 90909

    print(answer)
        
if __name__ == "__main__":
    main()
