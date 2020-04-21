import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def binary_search(A, B, X, N, counter):
    low = 0
    high = 10 * N
    mid = (low + high) // 2
    
    ans = A * N + B * len(str(N))
    mid_ans = A * mid + B * len(str(mid))
    
    
    while (counter > 0):
        mid = (low + high) // 2
        mid_ans = A * mid + B * len(str(mid))

        if mid_ans < ans:
            low = mid + 1
        else:
            high = mid - 1

        counter -= 1

            
    return mid, mid_ans

    
def main():
    A, B, X = map(int, input().split())
    logging.info("Hello!")
    
    N, ans = binary_search(A, B, X, X // A, 100)

    if ans > X:
        while (ans > X) and (N > 0):
            
            N = N - 1
            ans = A * N + B * len(str(N))
    else:
        while (ans < X):
            N = N + 1
            ans = A * N + B * len(str(N))

        N = N - 1
            

    if N > 10 ** 9:
        print(10 ** 9)
    elif N < 0:
        print(0)
    else:
        print(N)
        
            
    
if __name__ == "__main__":
    main()
