import logging
import heapq

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def calc_(s):
    return int(s) * (-1)

def main():
    N, M = map(int, input().split())
    L_1 = list(map(calc_, input().split()))
    logging.info("Hello!")

    heapq.heapify(L_1)
    print(L_1)
    
    for i in range(M):
        temp = heapq.heappop(L_1) * (-1)
        temp = temp // 2
        heapq.heappush(L_1, temp * (-1))

    print(sum(list(L_1)) * (-1))
        
if __name__ == "__main__":
    main()

    
