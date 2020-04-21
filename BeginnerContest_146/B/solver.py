import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    S = input()
    logging.info("Hello!")

    answer = ""
    for c in S:
        num = ord(c) + N
        if num <= 90:
            answer += chr(num)
        else:
            num = num - 90 + 64
            answer += chr(num)

    print(answer)
            
if __name__ == "__main__":
    main()
