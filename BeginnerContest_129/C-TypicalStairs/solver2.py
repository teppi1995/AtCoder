import logging
from math import factorial

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

steps_memo =[0 for _ in range(1000000x)]
def cal_steps(num):
    steps_memo[0] = 1
    steps_memo[1] = 1

    for i in range(2, num):
        steps_memo[i] = steps_memo[i - 1] + steps_memo[i - 2]

    return steps_memo[num - 1]
    
def main():
    N, M = (int(x) for x in input().split())
    a_s = [int(input()) for _ in range(M)]

    logging.info(a_s)
    
    a_s.append(N + 1)
    a_s.insert(0, -1)
    diff_a = [a_s[i + 1] - a_s[i] - 1 for i in range(M + 1)]

    if diff_a[0] == 0:
        diff_a[0] = 1
    
    logging.info(diff_a)

    
    answer = 1
    for i in diff_a:
        answer *= int(cal_steps(i))

    print(answer % (10 ** 9 + 7))
        

if __name__ == "__main__":
    main()
