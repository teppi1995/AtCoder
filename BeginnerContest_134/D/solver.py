import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    N = int(input())
    a_ = list(map(int, input().split()))
    box = [0 for _ in range(N)]

    logging.info("Hello!")

    for i in range(N):
        box_num = N - i

        sum = 0
        for j in range((N // (box_num)) - 1):
            sum += a_[(box_num) * (j + 2) - 1]
            
        box[box_num - 1] = abs(a_[box_num - 1] + (sum % 2))

    logging.info(box)

    
    print(box.count(1))
    answer = ""
    for i in range(N):
        if box[i] == 1:
            answer += str(i + 1)
            answer += " "

    print(answer)
    
if __name__ == "__main__":
    main()
