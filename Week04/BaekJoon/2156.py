# 포도주 시식
# ??왜지
import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(input(), end='')
elif n == 2:
    print(sum(map(int, sys.stdin.readlines())))
else:
    wine = []
    for _ in range(n):
        wine.append(int(input()))

    dp = [0 for _ in range(n)]
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(dp[1], wine[0] + wine[2], wine[1] + wine[2]) # why?

    for i in range(3, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i])
    print(max(dp))
    # print(wine)
    # print(dp)