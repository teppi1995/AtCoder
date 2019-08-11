import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.disable(logging.CRITICAL)

def main():
    pass_num = input()
    for i in range(3):
        if pass_num[i] == pass_num[i + 1]:
            print("Bad")
            exit()

    print("Good")
    
if __name__ == "__main__":
    main()
