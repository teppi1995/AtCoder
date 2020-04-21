import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)



def main():
    X, Y = map(int, input().split())
        
    dp = [[0 for i in range(X + Y)] for j in range(X + Y)]
    logging.info("reset 0")
    dp[0][0] = 0
    dp[1][2] = 1
    dp[2][1] = 1
    
    for i in range(2, X + 1):
        for j in range(2, Y + 1):
            if (i + j) % 3 == 0:
                dp[i][j] = dp[i - 2][j - 1] + dp[i - 1][j - 2] 
                

    print(dp[X][Y] % (10 ** 9 + 7))
    
    
if __name__ == "__main__":
    main()
