import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N, K = map(int, input().split())
    s_list = [x for x in range(1, N)] 
    
    for i in range(K):
        di = int(input())
        A_i = list(map(int, input().split()))
        for j in A_i:
            try:
                s_list.remove(j)
            except:
                continue

    logging.info(s_list)
    print(len(s_list))
    
if __name__ == "__main__":
    main()
