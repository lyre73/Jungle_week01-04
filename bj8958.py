for i in range(int(input())):
    result = input().split('X')

    score = 0
    for ele in result:
        if ele != '':        
            for j in range(len(ele)):
                score = score + j + 1
    print(score)