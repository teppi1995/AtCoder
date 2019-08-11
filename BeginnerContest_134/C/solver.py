import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    A_ = [int(input()) for _ in range(N)]

    for i in range(N):
        L = A_[0:i]
        L.extend(A_[i + 1:])
        print(max(L))
        
    
if __name__ == "__main__":
    main()
