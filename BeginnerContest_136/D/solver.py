import logging
import copy

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    S = input()
    S_len = len(S)
    child = [1 for _ in range(S_len)]
    logging.info("Hello!")

    for i in range(100):
        diff_child = [0 for _ in range(S_len)]
        for j in range(S_len):
            if S[j] == "R":
                diff_child[j + 1] += child[j]
                child[j] = 0
            elif S[j] == "L":
                diff_child[j - 1] += child[j]
                child[j] = 0

        child = copy.copy(diff_child)
               

    answer = ""
    for x in child:
        answer += str(x)
        answer += " "

    print(answer)
        
    
if __name__ == "__main__":
    main()
