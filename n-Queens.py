global cnt

def n_queens(i, col): # i번째 행
    global cnt
    n = len(col)-1 # 마지막 열의 인덱스(번호)
    if promising(i, col): # i행에 놓을 수 있으면
        if i == n: # 마지막 행까지 다 돌았으면 현재 배치를 출력
            print(col[1: n+1])
            cnt +=1
        else:
            for j in range(1, n+1): # 1, 2, ... , n # i행의 모든 열(j열)에 놓을 경우의 수 탐색
                col[i+1] = j # 다음 행에 하나씩 놔 보기
                n_queens(i+1, col) # 다음 행 실행

def promising(i, col):
    # i번째 행
    # 값 초기화
    k = 1
    flag = True
    while k < i and flag: # i번 미만(앞 행까지 체크) 반복했고 놓을 수 있는 자리일 때(flag)
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)): # 놓을 수 없는 자리면
            flag = False
        k += 1
    return flag # 놓을 수 있는지 없는지 리턴

cnt = 0
col = [None] * 15
# print(col)
n_queens(0, col)
print(cnt)