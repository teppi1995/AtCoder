import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

def main():
    M, D = map(int, input().split())
    
    counter = 0
    for i in range(10, D + 1):
        d1 = i % 10
        d2 = int(i // 10)
        
        
        if d1 >= 2 and d2 >= 2 and d1 * d2 <= M:
            logging.info(str(d1) + " " + str(d2))
            counter += 1
            

    
    print(counter)
    
    logging.info("Hello!")

    
    
    
if __name__ == "__main__":
    main()
