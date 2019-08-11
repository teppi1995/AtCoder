import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.disable(logging.CRITICAL)


def gcd(m, n):
    x = max(m, n)
    y = min(m, n)
    if x % y == 0:
        return y
    else:
        while x % y != 0:
            z = x % y
            x = y
            y = z
        else:
            return z

def main():
    A, B, C_, D_ = (int(x) for x in input().split())

    if C_ > D_:
        C, D = D_, C_
    else:
        C, D = C_, D_
        

    lcm_CD = int(C * D / gcd(C, D))
    
    div_C = int(B // C) - int((A - 1) // C)
    div_D = int(B // D) - int((A - 1) // D)
    div_lcm_CD = int(B // lcm_CD) - int((A - 1) // lcm_CD)
    
    answer = B - A + 1 - div_C - div_D + div_lcm_CD

    if A == 0:
        print(answer - 1)
    else:
        print(answer)

if __name__ == "__main__":
    main()
