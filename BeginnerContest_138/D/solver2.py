import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)



def main():
    N, Q = map(int, input().split())
    a_b = [list(map(int, input().split())) for _ in range(N - 1)]
    p_x = [list(map(int, input().split())) for _ in range(Q)]
    score = [0 for _ in range(N)]
    
    tree_dict = {}
    
    for i in a_b:        
        tree_dict.setdefault(i[0], []).append(i[1])
        
        for key, values in tree_dict.items():
            for i in values:
                if i in tree_dict:
                    tree_dict[key].extend(tree_dict[i])



    logging.info(tree_dict)

    for task in p_x:
        try:
            child = tree_dict[task[0]]
            for i in set(child):
                score[i - 1] += task[1]
            score[task[0] - 1] += task[1]
            
        except:
            score[task[0] - 1] += task[1]
                    
    
        

        
    answer = ""
    for i in score:
        answer += str(i)
        answer += " "

    print(answer)
    
    
if __name__ == "__main__":
    main()
