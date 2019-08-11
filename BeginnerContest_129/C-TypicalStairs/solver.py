import logging
from math import factorial

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def cal_steps(num):
    steps = 0

    if num == 0:
        return 0

    for i in range(int(num / 2) + 1):
        steps += (factorial(num - i) / factorial(i) / factorial(num - 2 * i))

    return steps

def main():
    N, M = (int(x) for x in input().split())
    a_s = [int(input()) for _ in range(M)]

    logging.info(a_s)
    
    a_s.append(N)
    a_s.insert(0, 0)
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
