import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def count_inversion(sequence):
    return sum(sum(m<n for m in sequence[i+1:]) for i,n in enumerate(sequence))

def count_ponpon(sequence):
    counter = 0
    split_count = 0
    splited = 0
    num = len(sequence)
    for i in set(sequence):
        split_count = sequence.count(i)
        counter += (num - split_count) * split_count
        
    logging.info(counter)
    return counter
        

def main():
    N, K = map(int, input().split())
    A_1 = list(map(int, input().split()))
    MODI = 10 ** 9 + 7
    logging.info("Hello!")

    A_counter = count_inversion(A_1)
    k_counter = int((K) * (K - 1) / 2)
    
    A_ = count_ponpon(A_1)
    
    print((A_counter * K + k_counter * A_) % MODI)
        
    
if __name__ == "__main__":
    main()
