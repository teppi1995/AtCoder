import logging
import heapq

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)


def main():
    N, M = map(int, input().split())
    A_B = [list(map(int, input().split())) for _ in range(N)]
    logging.info("Hello!")

    A_B.sort()
    logging.info(A_B)


    heap_Q = []
    curr = 0
    total = 0
    for i in range(1, M + 1):
        while curr < N and  A_B[curr][0] <= i:
            heapq.heappush(heap_Q, A_B[curr][1] * (-1))
            curr += 1

        if heap_Q:
            total += (-1) * heapq.heappop(heap_Q)

    print(total)
    
if __name__ == "__main__":
    main()
