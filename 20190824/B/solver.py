import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def count_inversion(sequence):
    return sum(sum(m<n for m in sequence[i+1:]) for i,n in enumerate(sequence))

def main():
    N, K = map(int, input().split())
    A_1 = list(map(int, input().split()))
    MODI = 10 ** 9 + 7
    logging.info("Hello!")

    A_counter = count_inversion(A_1)
    k_counter = int((1 + K) * K / 2)
    K_ = int((K) * (K - 1) / 2)
    
    print(k_counter)
    if A_1[-1] > A_1[0]:
        print((A_counter * k_counter + (K_ - 1)) % MODI)
    else:
        print((A_counter * k_counter) % MODI) 
        
    
if __name__ == "__main__":
    main()
