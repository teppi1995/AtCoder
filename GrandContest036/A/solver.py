import logging
import math

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def trial_division(S):
    factor = []
    starts_div = S // (10 ** 9)
    
    for num in range(starts_div,  10 ** 9):
        logging.info(num)
        while  S % num == 0:
            S //= num
            factor.append(num)
            logging.info(S)

        if S <= 10 ** 9:
            break

    return S, factor[-1]
        
    
def main():
    S = int(input())
    logging.info("Hello!")

    if S < 10 ** 9:
        print("0 0 1 0 1 " + str(S))
    else:
        width, height = trial_division(S)
        print("0 0 " + str(width) + " 0 " + str(width) + " " + str(height))

        
if __name__ == "__main__":
    main()
