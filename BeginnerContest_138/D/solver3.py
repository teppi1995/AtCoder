import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)



def main():
    N, Q = map(int, input().split())
    a_b = sorted([list(map(int, input().split())) for _ in range(N - 1)])
    p_x = sorted([list(map(int, input().split())) for _ in range(Q)])
    score = [0 for _ in range(N)]

    for task in p_x:
        score[task[0] - 1] += task[1]

    
    for leef in a_b:
        score[leef[1] - 1] += score[leef[0] - 1]   

        
    answer = ""
    for i in score:
        answer += str(i)
        answer += " "

    print(answer)
    
    
if __name__ == "__main__":
    main()
