import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    A_ = [int(input()) for _ in range(N)]
    logging.info("Hello!")

    A_.append(0)
    counter = 0
    for i in range(0, N):
        if A_[i] == 0:
            continue
        else:
            if A_[i] > A_[i + 1]:
                counter += (A_[i + 1] + (A_[i] - A_[i + 1]) // 2)
                A_[i + 1] = 0
            else:
                counter += (A_[i])
                A_[i + 1] -= A_[i] 

    print(counter)
    
    
if __name__ == "__main__":
    main()
