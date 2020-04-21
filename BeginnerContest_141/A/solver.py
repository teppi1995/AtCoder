import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    S_s = ["Sunny", "Cloudy", "Rainy"]
    S = input()
    logging.info("Hello!")

    if S == S_s[0]:
        print(S_s[1])
    elif S == S_s[1]:
        print(S_s[2])
    elif S == S_s[2]:
        print(S_s[0])
        
    
if __name__ == "__main__":
    main()
