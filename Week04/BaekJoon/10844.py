# 쉬운 계단 수
import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(9)
else:
    dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for _ in range(1, N):
        temp = [0 for _ in range(10)]
        temp[0] = dp[1]
        temp[9] = dp[8]
        for i in range(1, 9):
            temp[i] = (dp[i - 1] + dp[i + 1]) % 1000000000
        dp = temp
    print(sum(dp) % 1000000000)