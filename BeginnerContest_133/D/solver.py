import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

N = int(input())
a_ = list(int(x) for x in input().split())
X_ = [0 for _ in range(N)]

X_sum = sum(a_)
logging.info("sum = " + str(X_sum))

X_[0] = X_sum - 2 * sum(a_[1::2])
logging.info("X_1 = " + str(X_[0]))

for i in range(1, N):
    X_[i] = 2 * a_[i - 1] - X_[i - 1]

answer = ""
for i in X_:
    answer += str(i)
    answer += " "

print(answer)
