import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    A_ = [int(input()) for _ in range(N)]

    max_A = max(A_)
    if A_.count(max_A) > 1:
        for i in range(N):
            print(max_A)
            
    else:
        for i in range(N):
            if A_[i] == max_A:
                L = A_[0:i]
                L.extend(A_[i+1:])
                print(max(L))
            else:
                print(max_A)

                
if __name__ == "__main__":
    main()
