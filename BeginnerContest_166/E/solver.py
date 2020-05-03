import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    A_1 = list(map(int, input().split()))
    B_l = [1 - A_1[0]]

    sum = 0
    
    for i in range(1, N):
        if A_1[i] in B_l:
            sum += 1

        B_l = list(map(lambda x: x+1, B_l))
        B_l.append(0 - A_1[i])

        
    print(sum)
    
if __name__ == "__main__":
    main()
