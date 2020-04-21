import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())

    A = []
    x = []
    y = []

    for i in range(N):
        Ai = int(input())
        xi = []
        yi = []
        A.append(Ai)
        x.append(xi)
        y.append(yi)

        for j in range(Ai):
            xij, yij = map(int, input().split(' '))
            xi.append(xij)
            yi.append(yij)

    logging.info(A)
    logging.info(x)
    logging.info(y)

    ok_list = []
    for bits in range(2 ** N):
        ok_flag = True
        for i in range(N):
            if (bits >> i) & 1 == 0:
                continue

            for j in range(A[i]):
                if (bits >> (x[i][j] - 1) & 1) != y[i][j]:
                    ok_flag = False

        if ok_flag:
            ok_list.append(bin(bits).count('1'))

    print(max(ok_list))

    
if __name__ == "__main__":
    main()
