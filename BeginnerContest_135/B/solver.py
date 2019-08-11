import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    L = list(map(int, input().split()))
    logging.info("Hello!")

    L_sorted = sorted(L)

    counter = 0
    diff = []
    for i in range(N):
        if L[i] != L_sorted[i]:
            counter += 1
            if counter == 3:
                print("NO")
                exit()
            else:
                diff.append(L[i])

    print("YES")

            
if __name__ == "__main__":
    main()
