L, R = (int(x) for x in input().split())
L_ = L % 2019
R_ = R % 2019 + 2019

min = 2020

for i in range(L_, R_):
    for j in range(i + 1, R_ + 1):
        mod_ij = i * j % 2019
        if min > mod_ij:
            min = mod_ij

print(min)
