# 행렬 제곱
"""거듭제곱식으로, 곱할 횟수를 반씩 나눠서 곱하고 리턴"""

import sys
input = sys.stdin.readline

def mat_mul(mat1, mat2):
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                temp[i][j] += mat1[i][k] * mat2[k][j]
            temp[i][j] %= 1000 # 1000의 배수는 곱해서 더하더라도 나중에 나눗셈할때 사라진다
    return temp

def mat_square(mat):
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                temp[i][j] += mat[i][k] * mat[k][j]
            temp[i][j] %= 1000 # 1000의 배수는 곱해서 더하더라도 나중에 나눗셈할때 사라진다
    return temp

def mat_power(mat, power):
    if power <= 1:
        temp = [[0] * N for _ in range(N)]
        for i in range(N): 
            for j in range(N):
                temp[i][j] = mat[i][j] % 1000 # 1000의 배수는 곱해서 더하더라도 나중에 나눗셈할때 사라진다
        return temp
    elif power == 2:
        return mat_square(mat)
    
    temp = mat_power(mat, power // 2)
    if power % 2: # power is odd
        return mat_mul(mat_mul(temp, temp), mat)
    else: # power is even
        return mat_mul(temp, temp)

N, B = map(int, input().split()) # N == len(mat)
mat = [list(map(int, line.split())) for line in sys.stdin.readlines()]

# 행렬의 원소마다 하나하나 나누고 출력하 것보다, 미리 1000의 배수를 없애 놓고 그냥 줄 단위로 출력하는 게 더 좋은 출력 방법
result = mat_power(mat, B)
for row in result:
    print(*row)