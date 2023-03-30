# 정수 삼각형
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dp = [[0] * i for i in range(1, n+1)]
dp[0] = data[0]
for floor in range(1, n):
    dp[floor][0] = dp[floor - 1][0] + data[floor][0]
    dp[floor][-1] = dp[floor - 1][-1] + data[floor][-1]
    for i in range(1, len(data[floor]) - 1):
        dp[floor][i] = max(dp[floor-1][i - 1], dp[floor-1][i]) + data[floor][i]
# print(*dp, sep='\n')
print(max(dp[-1]))