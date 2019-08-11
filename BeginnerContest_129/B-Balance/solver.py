N = int(input())
W_ = list(int(x) for x in input().split())

S = sum(W_)

s = 0
counter = 0
for num in W_:
    s += num
    counter += 1
    if s > S / 2:
        kouho1 = abs(sum(W_[0:counter - 1]) - sum(W_[counter - 1:N]))
        kouho2 = abs(sum(W_[0:counter]) - sum(W_[counter:N]))
        print(kouho1)
        print(kouho2)
        if kouho1 > kouho2:
            print(kouho2)
        else:
            print(kouho1)

        exit()
