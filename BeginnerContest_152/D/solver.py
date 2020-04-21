import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    #keta = len(str(N))
    logging.info("Hello!")

    dp = [0] * (N + 1)

    for i in range(1, (N + 1)):
        keta = len(str(i))
        logging.info("[+]dp[" + str(i) + "] = " + str(dp[i - 1]))
        if i < 10:
            dp[i] = i
        else:
            if str(i)[0] == str(i)[-1]:
                dp[i] = dp[i - 1] + 3
                for j in range(keta - 2):
                    dp[i] += 10 ** j * 2
            elif str(i)[0] < str(i)[-1]:
                dp[i] = dp[i - 1]
                for j in range(keta - 2):
                    dp[i] += 10 ** j * 2
            else:
                if int(str(i)[-1]) != 0:
                    logging.info("[+]" + str(i))
                    dp[i] = dp[i - 1]
                    for j in range(keta - 1):
                        dp[i] += 10 ** j * 2
                    logging.info("[*]" + str(dp[i]))
                else:
                    dp[i] = dp[i - 1]
                
    print(dp[N])
    
                
if __name__ == "__main__":
    main()
