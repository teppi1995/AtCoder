import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N, M = map(int, input().split())
    N_list = [1 for x in range(N)]
    H_i = list(map(int, input().split()))

    for i in range(M):
        A, B = map(int, input().split())
        if H_i[A - 1] < H_i[B - 1]:
            N_list[A - 1] = 0
        elif H_i[A - 1] > H_i[B - 1]:
            N_list[B - 1] = 0
        else:
            N_list[A - 1] = 0
            N_list[B - 1] = 0
            
    print(N_list.count(1))

    logging.info("Hello!")

    
if __name__ == "__main__":
    main()
