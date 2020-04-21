import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)


def combination(n, r, mod = 10 ** 9 + 7):
    r = min(r, n-r)
    up, down = 1, 1

    for i in range(r):
        up = up * (n - i) % mod
        down = down * (i + 1) % mod

    return up * pow(down, mod - 2, mod) % mod
        
def main():
    X, Y = map(int, input().split())

    if (X + Y) % 3 != 0:
        print(0)
    else:
        m = (2 * Y - X) // 3
        n = (2 * X - Y) // 3
    
        print(combination(n + m, m))
    
    
if __name__ == "__main__":
    main()
