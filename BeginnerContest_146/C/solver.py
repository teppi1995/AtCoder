import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)


def main():
    A, B, X = map(int, input().split())
    logging.info("Hello!")
    
    N = X // A
    ans = A * N + B * len(str(N))
    max_ans = A * (10 ** 9) + B * 10
    
    before_N = N

    if X > max_ans:
        print(10 ** 9)
        exit()
    
    if ans > X:
        while (ans > X) and (N > 0):
            before_N = N
            N = 10 ** (len(str(N)) - 2)
            ans = A * N + B * len(str(N))

    N = before_N
    ans = A * N + B * len(str(N))
    
    if ans > X:
        while (ans > X) and (N > 0):
            
            N = N - 1
            ans = A * N + B * len(str(N))


    if N > 10 ** 9:
        print(10 ** 9)
    else:
        print(N)
            
    
if __name__ == "__main__":
    main()
