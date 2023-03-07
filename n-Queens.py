def n_queens(i, col):
    # i번째 행의 col열 == col 열의 i번째 행
    n = len(col)-1 # 마지막 열의 인덱스(번호)
    if promising(i, col):
        if i == n:
            print(col[1: n+1])
        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queens(i+1, col)

def promising(i, col):
    # i번째 행의 col 열
    k = 1
    flag = True
    while k < i and flag:
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
            flag = False
        k += 1
    return flag