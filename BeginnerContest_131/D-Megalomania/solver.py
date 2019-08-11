import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    items = []

    for i in range(N):
        value, limit = map(int, input().split())
        items.append((limit, value))

    logging.info(items)

    items.sort()

    logging.info(items)

    total_time = 0
    for lim, val in items:
        total_time += val
        if total_time > lim:
            print("No")
            exit()

    print("Yes")

    
if __name__ == "__main__":
    main()
