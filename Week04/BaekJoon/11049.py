# 행렬 곱셈 순서
"""시작~끝 인덱스 사이 k번째 인덱스를 잘라서 비교, bottom-up"""
import sys
input = sys.stdin.readline

N = int(input())
size = list(map(int, input().split())) # i(0~N-1)번째 행렬의 크기: (i, i+1)
for _ in range(N - 1):
    _, a = map(int, input().split())
    size.append(a)

dp = [[float('inf')] * (N) for _ in range(N)] # dp[i][j] = i번 행렬부터 j번 행렬까지의 최적해, i, j는 각각 0부터 N-1까지
for i in range(N):
    dp[i][i] = 0

for L in range(2, N + 1): # <행렬>의 길이 L = j - i + 1
    for i in range(N - L + 1): # 왼쪽 행렬의 번호(인덱스), 0 ~ N - L번
        j = i + L - 1 # 오른쪽 행렬의 번호(인덱스)
        if L == 2:
            dp[i][j] = size[i] * size[i + 1] * size[i + 2]
        else:
            for k in range(i + 1, j + 1):
                # print('k:', k)
                dp[i][j] = min(dp[i][j], dp[i][k-1] + dp[k][j] + size[i] * size[k] * size[j+1])
                # print(dp)
print(dp[0][N - 1])
# print(dp)