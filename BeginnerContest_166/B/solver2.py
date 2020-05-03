import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N, K = map(int, input().split())
    N_list = [1 for x in range(N)]
    s_list = [x for x in range(1, N)] 
    
    for i in range(K):
        di = int(input())
        A_i = list(map(int, input().split()))
        for j in A_i:
            N_list[j - 1] = 0

    print(N_list.count(1))
    
if __name__ == "__main__":
    main()
