import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N, Q = map(int, input().split())
    a_b = [list(map(int, input().split())) for _ in range(N - 1)]
    p_x = [list(map(int, input().split())) for _ in range(Q)]
    score = [0 for _ in range(N)]
    
    logging.info("Hello!")

    
    for task in p_x:
        for i in a_b:
            if i[0] != task[0]:
                continue
            else:
                score[i[1] - 1] += task[1]

        score[task[0] - 1] += task[1]

    answer = ""
    for i in score:
        answer += str(i)
        answer += " "

    print(answer)
    
    
if __name__ == "__main__":
    main()
