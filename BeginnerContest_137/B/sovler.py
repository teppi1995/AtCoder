import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    K, X = map(int, input().split())
    logging.info("Hello!")

    min_x = X - K + 1
    max_x = X + K - 1

    ans = ""
    for i in range(min_x, max_x + 1):
        if i < -1000000:
            continue
        elif i > 1000000:
            break

        ans += str(i)
        ans += " "

    print(ans)
    
if __name__ == "__main__":
    main()
