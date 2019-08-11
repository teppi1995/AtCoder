import logging
import copy

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    S = input()
    S_len = len(S)
    child = [1 for _ in range(S_len)]
    logging.info("Hello!")

    R_counter = 1
    L_counter = 0
    R = [0 for _ in range(S_len)]
    L = [0 for _ in range(S_len)]
    L2R = 0
    R2L = 0
    
    for i in range(1, S_len):
        if S[i] == "R" and S[i - 1] == "R":
            R_counter += 1
        elif S[i] == "L" and S[i - 1] == "R":
            R2L = i
            R[i - 1] = R_counter
            R_counter = 0
            L_counter += 1
        elif S[i] == "L" and S[i - 1] == "L":
            L_counter += 1
        elif S[i] == "R" and S[i - 1] == "L":
            R[R2L] = L_counter
            L_counter = 0
            R_counter += 1

        if i == S_len - 1:
            R[R2L] = L_counter

    logging.info(R)
    
    for i in range(1, S_len):
        if R[i] != 0 and i % 2 == 1:
            temp1 = (R[i] + R[i + 1]) // 2
            temp2 = R[i] + R[i+1] - temp1
            R[i] = temp1
            R[i + 1] = temp2

    answer = ""
    for x in R:
        answer += str(x)
        answer += " "

    print(answer)
            
    
if __name__ == "__main__":
    main()
