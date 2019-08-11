import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)


def main():
    N, M = map(int, input().split())
    A_B = [list(map(int, input().split()))[::-1] for _ in range(N)]
    logging.info("Hello!")

    sorted_A_B = sorted(A_B, reverse=True)
    logging.info(sorted_A_B)


    total = 0
    for i in range(N):
        if i >= M:
            break
        
        if sorted_A_B[i][1] + i <= M and sorted_A_B[i][0] != -1:
            total += sorted_A_B[i][0]
            sorted_A_B[i][0] = -1


    print(total)
    
if __name__ == "__main__":
    main()
